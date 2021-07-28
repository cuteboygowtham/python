"""

dict = {"Name": "Gowtham Kumar", "Age": 21, "Graduation": "B.tech"}
print("My Name : ", dict["Name"])
print("My Age : ", dict["Age"])
print("My Graduation : ", dict["Graduation"])

"""
"""
num = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}
print(
    "Number in words : ", num[1],
    "\nNumber in words : ", num[2],
    "\nNumber in words : ", num[3],
    "\nNumber in words : ", num[4],
    "\nNumber in words : ", num[5]
)
print(num.get(5,"Key is not found"))

"""
"""
product = {"Mobile": 10000, "Laptop": 50000, "Earphones": 1000, "Charger": 700, "Hotspot": 1000}
print("Mobile Price : ", product["Mobile"],
      "\nLaptop Price : ", product["Laptop"],
      "\nEarphones Price : ", product["Earphones"],
      "\nCharger Price : ", product["Charger"],
      "\nHotspot Price : ", product["Hotspot"])
"""
products = {"Mobile": 10000, "Laptop": 50000, "Earphones": 1000, "Charger": 700, "Hotspot": 1000}
newproducts = input("Enter a product")
if(newproducts in products):
    print(products.get(newproducts))
else:
    print("Product Not found")