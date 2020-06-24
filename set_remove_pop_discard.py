# n = int(input())
# s = set(map(int, input().split()))
# for i in range(int(input())):
#     s1=input()
#     l1=list(s1.split())
#     if(l1[0]=='pop'):
#         s.pop()
#
#     if(l1[0]=='discard'):
#         s.discard(int(l1[1]))
#     if(l1[0]=='remove'):
#         s.remove(int(l1[1]))
#
# print(sum(s))

# import numpy
# n1=int(input())
# m1=int(input())
# print(numpy.eye(n1,m1,k=0))

# n = int(input())
# arr = map(int, input().split())
# arr=sorted(arr)
# maximum = max(arr)
# arr.remove(maximum)
# print(max(arr))

# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])
#
# second_highest = (list(set([marks for name, marks in marksheet])))[1]
# print(second_highest)
# # print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet.append([name,score])
                scorelist.append(score)
        b=sorted(list(set(scorelist)))[1]
        #print(b)
        for a,c in sorted(marksheet):
             if c==b:
                    print(a)
                    break





