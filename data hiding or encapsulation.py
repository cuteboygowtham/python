# Encapsulation (or) Data Hiding :
#     It allows preventing the functions of a program to access directly the internal representation of a class type.
#       We use double underscore __ before the attributes names to make those attributes private.

class Myclass :
    __hiddenvariable = 2

    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)

object1 = Myclass()
object1.add(5)
# print(object1.__hiddenvariable)

