list= ["AShu","ashu","paras","PARas"]
new=[]
for i in list:
    if(i.lower() not in new):
        new.append(i)
 
print(new)  
        