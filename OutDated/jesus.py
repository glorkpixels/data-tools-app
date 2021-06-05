

menu = []
with open('ingquantity.txt') as f:
    for line in f:
        damn = line.split(" " ,1 )
        menu.append(damn[1])
        
ingridientList = list(dict.fromkeys(menu))


f = open('ingkeys.txt', 'a')
for i in ingridientList:
    if(i != ""):
        f.write(i)
    
f.close()