def family(x):
 if x in ('Artistic Gymnastics','Rhythmic Gymnastics','Trampoline Gymnastics'):return 'Gymnastics'
 if x.startswith('Cycling '):return 'Cycling'
 if x.startswith('Canoe '):return 'Canoeing'
 if x=='Marathon Swimming':return 'Swimming'
 if x=='Rugby Sevens':return 'Rugby'
 if x=='Beach Volleyball':return 'Volleyball'
 if x=='3x3 Basketball':return 'Basketball'
 return x
