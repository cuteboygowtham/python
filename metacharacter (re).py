# import re
# pattern = r"g.wtham"
# match = "gowtham"
# if(re.match(pattern, match)):
#     print("Match Found")
# else:
#     print("Match Not Foun")
# caset and dollar meta character
# import re
# pattern = r"^go.tham$"
# if re.match(pattern, "gowtham"):
#     print("Match Found")

# character class
# import re
# pattern = r"[A-Z][0-9]"
# if re.search(pattern, "AP50300318142018"):
#     print("Match Found", )

# *character
# import re
# pattern = r"eggs(bacon)*"
# if re.match(pattern, "eggsbacon"):
#     print("Match Found")

# groups
# import re
# pattern = r"eggs(bacon)*eggs"
# if re.match(pattern, "eggsbaconbaconbaconbaconbaconbaconbaconeggs"):
#     print("match found")
import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
