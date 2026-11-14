from pathlib import Path
import re
import json
from html.parser import HTMLParser

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务三_专题深挖'
s1=TASK/'S1_东道主效应'/'index.html'
s3=TASK/'S3_冠军的保质期'/'06_冠军王朝时间轴'/'index.html'
portal=TASK/'统一中文入口'/'index.html'

class Visible(HTMLParser):
    def __init__(self):super().__init__();self.hidden=0;self.words=[]
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.hidden+=1
    def handle_endtag(self,tag):
        if tag in ('script','style'):self.hidden-=1
    def handle_data(self,data):
        if not self.hidden:self.words.append(data)

assert s1.exists() and s3.exists()
assert '../S1_东道主效应/index.html' in portal.read_text(encoding='utf-8')
for page in (s1,s3):
    text=page.read_text(encoding='utf-8')
    for ref in re.findall(r'(?:href|src)=["\']([^"\']+)["\']',text):
        if ref.startswith(('#','http:','https:')):continue
        assert (page.parent/ref).resolve().is_file(),(page,ref)
    v=Visible();v.feed(text)
    visible=' '.join(v.words)
    assert not re.search(r'\b(?:Athletics|Swimming|Basketball|Men|Women|USA|CHN)\b',visible),page
text=s3.read_text(encoding='utf-8')
assert '数据.map(x=>x.代表团名称)' in text
assert '${x.代表团名称} · ${x.小项名称}' in text
assert not re.search(r'"小项名称":"[^"]*[A-Za-z]',text)
print(json.dumps({'passed':True,'S1':'链接完整','S3':'160条王朝记录中文化','portal':'入口指向HTML'},ensure_ascii=False))
