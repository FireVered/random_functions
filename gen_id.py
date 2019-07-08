import func_gen

ids = open('ids.ids','r').read().split(';')

n=0
for st in ids:
    ids[n] = ids[n].split(',')
    n+=1


num = int(input('enter a number: '))
t = 0

while t<num:
    id_f_str = str(func_gen.gen_id()).replace('[','').replace(']','')
    id_f = id_f_str.split(',')
    if not id_f in ids:
        fc = open('ids.ids','r').read()
        open('ids.ids','w').write(fc +id_f_str+';')

    t+= 1
    
