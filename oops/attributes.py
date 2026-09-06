# instance variable call using this we can acess using object and change it
#  using a.name ="parsa"

# class variable call using className.variable

class StudentInfo:
    college = "miet"
    Branch = "CSE"

    def __init__(self, name, year, semester):
        self.name = name
        self.year = year
        self.semester = semester

    def info(self):
        print(f"=====Student Info=====")
        print(f"student name ={self.name}")
        print(f"student year ={self.year}")
        print(f"student semester ={self.semester}")
        print(f"college name ={StudentInfo.college}")
        print(f"Branch name ={StudentInfo.Branch}")


a = StudentInfo("ashu", "4th", "7th")
a.name ="paras"
print(a.name)
# a.info()
