marks = int(input("enter Your marks"))
if marks>=90 and marks<=100:
    print('A Grade')
elif marks>=70 and marks<90:
    print('B Grade')
elif marks>=60 and marks<70:
    print("C Grade")
elif marks>=35 and marks<60:
    print('D Grade')
elif marks>=0 and marks<35:
    print('F Grade')
else:
    print('Invalid Marks')