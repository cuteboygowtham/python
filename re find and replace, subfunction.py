import re
string = "My name is John, Im John"
pattern = r"John"
newstring = re.sub(pattern, "Gowtham", string)
print(string)
print(newstring)