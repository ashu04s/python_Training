string ="ashu "
string2 ="this is "
name ="  ashu kumar  "
#convert it into uppercase
print(string.upper())

# to covert it into lowercase
print(string.lower())

# to covert it into capitalize
print(string.capitalize())

#find give the index of the character
print(string.find("a"))

#replace
print(string2.replace("this","that"))
print(string2.replace("i","a")) 


#split (convert string into list)
text = "apple banana mango"

result = text.split(" ")

print(result)

# join() joins elements of an iterable into a string (list into string).
words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)

#startswith() a sa start ho raha 
new ="ashu2"
print(new.startswith("a"))

#isalnum
print(new.isalnum())

#is numeric
print(new.isnumeric())

#title first letter capital 
print(name.title())

#strip remove  extra  space from the spring
print(name.strip())
