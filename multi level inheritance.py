class A:
    def a_method(self):
        print("This is from A method")


class B(A):
    def b_method(self):
        print("This is form B method")


class C(B):
    def c_method(self):
        print("This is from C method")

c = C()
c.a_method()
c.b_method()
c.c_method()