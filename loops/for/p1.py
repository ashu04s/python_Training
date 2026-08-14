import time

# for loop 1 se 9 tak chalega
for i in range(1, 10):

    # program ko 1 second ke liye rokega
    time.sleep(1)

    # i ko print karega
    # end="" → next line mein nahi jayega
    # flush=True → output ko immediately buffer se screen par bhejega
    print(i, end="", flush=True)


# -----------------------------------------
# __doc__ ka use documentation dekhne ke liye
# -----------------------------------------

# input() function ki documentation dekho
print(input.__doc__)


# kisi bhi function ki documentation dekhne ke liye
# function.__doc__ use kar sakte hain

# print() function ki documentation
print(print.__doc__)


# -----------------------------------------
# IMPORTANT NOTES
# -----------------------------------------

# time.sleep(1)
# → program ko 1 second ke liye wait karata hai

# end=""
# → print ke baad new line nahi banata

# flush=True
# → buffer ko immediately flush karta hai
# → output ko turant screen par bhejne ki koshish karta hai

# function.__doc__
# → function ki documentation/docstring dikhata hai