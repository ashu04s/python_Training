#empty
d1 ={}
print(type(d1))

# 1d dictionary
d2 ={"name":"ashu",
     "age":20,
     "state":"bihar",
     "skill":{
            "frontend":"html,css, js, tailwind,react,redux,gsap,three.js",
            "backend":"jdbc,servlet,spring_core,spring_boot,microserivices,docker",
            "database":"mysql"
        }
}
print(d2["skill"]["frontend"])


# 3d dictionary
college = {

    "CSE": {

        "student1": {
            "name": "Ashu",
            "age": 20
        },

        "student2": {
            "name": "Rahul",
            "age": 21
        }
    },

    "ECE": {

        "student1": {
            "name": "Aman",
            "age": 20
        }
    }
}

# for acess element from dictionary
#using keys
print(d2["name"])
#for acess all keys in the dictionary
print(d2.keys())
# for acess all values in the dictionary
print(d2.values())


# iteration all keys and values using lops
for key, value in d2.items():
        print(key, ":", value)