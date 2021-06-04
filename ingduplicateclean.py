
menu = []
with open('ingnames.txt') as f:
    for line in f:
        menu.append(line)
        
ingridientList = list(dict.fromkeys(menu))


f = open('ingnamesnodp.txt', 'a')
for i in ingridientList:
    
    if "("  in i : 
        lol = i .split("(")
        print(lol)
        engName= lol[0] + "\n"
                
        f.write(engName)
    else:
        f.write(i)
    
f.close()
  