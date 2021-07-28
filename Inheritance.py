# Inheritance is the capability of one class to derive or inherit the properties from some another class.
# The benefits of inheritance are:
#
#  *   It represents real-world relationships well.
#  *  It provides reusability of a code. We don’t have to write the same code again and again. Also,
#     it allows us to add more features to a class without modifying it.
#  *   It is transitive in nature, which means that if class B inherits from another class A,
#     then all the subclasses of B would automatically inherit from class A.


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        print(self.name)
        print(self.age)


class ScienceStudent(Student):
    def student1(self):
        print("This is ME and My bio")


a = ScienceStudent("Gowtham", 21)
a.get_data()
a.student1()
