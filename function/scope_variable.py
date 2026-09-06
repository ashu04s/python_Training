def greet():
    x ="ashu"
    
    
# print(x)    we cannpot acess x in outside the scope

def my_function():
    global my_variable  
    my_variable = "Hello, World!"

# Call the function to initialize the variable
my_function()

# The variable is now accessible outside the function
print(my_variable)  # Output: Hello, World!


    