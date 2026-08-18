dict ={"ashu":{
    "age":20,
    "marks":50

}
       ,"aryan":{
           "age":21,
           "marks":59
       }}

a = input("enter name")

for key in dict:
    if a == key:
        print(dict[a])
    else:
        pass    