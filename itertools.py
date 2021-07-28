# from itertools import count
# #count function
#
# for i in count(3):
#     print(i)
#     if i>=20 :
#         break

#accumulate function and takewhile
from itertools import accumulate, takewhile

num = list(accumulate(range(8)))
print(num)
print(list(takewhile(lambda x : x<=10, num)))

