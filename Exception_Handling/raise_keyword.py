
try:
     age =int(input("enter you age"))
     if age<18:
      raise ValueError ("age must greter than 18")
except ValueError as e:
    print(e)
else:
    print("you can vote ")    
    
    
    
# using raise we can generate our custum Exception
# raise ValueError ("age must greter than 18")
# except ValueError as e:    