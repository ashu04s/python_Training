def create_list(list1,n):
    """this mehtod is used to create list"""
    n= int(input("enter the size if the list"))    
    list =[]
    for i in range(1,n+1):
        item = input((f"enter list item"))
        list.append(item)
    return list


def duplicate_remove(list2):
    "this method is used to remove duplicate from the list"
    list =[]
    for i in list2:
        if i  not in list:
            list.append(i)
          
    return list

def list_inside_list_remove(list4):
    "this method is used to remove list inside list"
    for i in list4:
        if type(i)==list:
            list4.remove(i)
    return list4

def add_zero(list5):
    "this method is used to add zero"
    list5.append(0)
    return list5

def zeropush(list6):
    "this metod push index zero at last"
    for i in list6:
        if i==0:
            list6.remove(i)
            list6.append(0)
                    
    return list6