#Single Inheritance 
'''class Person:
    def __init__(self,name):
        self.name=name
    def print_name(self):
        print(f"name is {self.name}")
class Emp(Person):
    def employee(self):
        super.__init__(name)
        print(self.name,"is an employee")
e=Emp("San")
e.employee()
e.print_name()'''

'''def minRepeat(s1,s2):
    repeat=s1
    count=1
    while len(repeat)<len(s2):
        repeat+=s1
        count+=1
    if s2 in repeat:
        return count
    repeat+=s1
    count+=1
    if s2 in repeat:
        return count
    return -1

result=minRepeat('ab','cab')
print(result)'''
