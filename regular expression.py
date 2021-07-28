import re

pattern = r"eggs"

if re.match(pattern, "eggsbacon"):
    print("Jodi Dorikindhi Rooo Match Found")
else:
    print("Edhi jodi Kadhu Match Not Found")

if re.search(pattern, "eggseggsbaconeggs"):
    print("Match Found")
else:
    print("Match Not Found")

print(re.findall(pattern, "eggseggsbaconeggs"))
