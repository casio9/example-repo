# 1. Write in python that prints your name, and then counts up to your favourite number squared.
print("Print my name!")
myname = "Chris"
print(myname)
# favourite number is 64
print("My favourite number is 64. Let's count in squares!..")
for i in range(1,9):
    print(i*i)
## 3. Update the code to contain a class Engineers, with a fixed class attribute skill equal to "problem solver", and initial attributes name, type and years of experience. Create two different engineers (objects) and print out their attributes.
print("Now let's update the code to contain a class called ""Engineers"" with attributes")


print("\n")
class Engineers:
    def __init__(self, name, type, years):
        self.name = name
        self.type = type
        self.years = years
    def getName(self):
        print("Name is "+ self.name)
    def getType(self):
        print("Type is "+ self.type)
    def getYears(self):
        print(self.years + " years of experience \n\n")

e1 = Engineers("John Smith", "mechnical", "14")
e1.getName()
e1.getType()
e1.getYears()

e1 = Engineers("Kate Jones", "electrical", "5")
e1.getName()
e1.getType()
e1.getYears()
print("\n")
print('Now we will reverse my name Chris to sirhC...')
def NameBackwards(x):
    return x[::-1]
myNameBackwards = NameBackwards(myname)
print(myNameBackwards)
