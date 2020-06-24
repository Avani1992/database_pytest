""""""
#
#
# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if (year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)):
#         leap = True
#     else:
#         leap = False
#
#     return leap
#
#
# year = int(input())
# print(is_leap(year))


(_, A) = (int(input()),set(map(int, input().split())))
B = int(input())
for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)

print (sum(A))

