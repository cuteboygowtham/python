class Computer:
    def __init__(self, ram, processor, memory):
        self.ram = ram
        self.processor = processor
        self.memory = memory

    def getspecs(self):
        print("Enter the details")
        self.ram = input("Enter Ur ram size")
        self.processor = input("Enter ur processor")
        self.memory = input("Enter ur memory size")

    def displayspecs(self):
        print("Here are the specs of the computer")
        print("Ram size is " + self.ram, "Processor is " + self.processor, "Memory size is " + self.memory)


class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def getcasecolor(self):
        self.casecolor = input("Enter ur color")

    def viewcasecolor(self):
        print("This is ur Laptop color" +self.casecolor)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def get_details(self):
        self.weight = input("Enter ur weight")

    def view_details(self):
        print("Weight of ur laptop" + self.weight)


computer = Desktop(" ")
computer.getspecs()
computer.displayspecs()
computer.getcasecolor()
computer.viewcasecolor()