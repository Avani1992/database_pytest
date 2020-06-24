"""Given an array A of positive integers of size N, where each value represents number of chocolates in a packet.
 Each packet can have variable number of chocolates. There are M students, the task is to distribute chocolate packets such that :
1. Each student gets one packet.
2. The difference between the number of chocolates given to the students having packet with maximum chocolates and student having
packet with minimum chocolates is minimum."""

import sys
for i in range(int(input())):
    s=int(input())
    l1=list(map(int,input().strip().split()))
    k=int(input())
    l1=sorted(l1)
    size=len(l1)
    min_difference=sys.maxsize
    difference=0
    if(len(l1)==0 or k==0):
        print("0")
    if(len(l1)<k):
        print("-1")
    i=0
    while(i+(k-1)<size):
        difference=l1[i+(k-1)]-l1[i]
        if(difference<min_difference):
            min_difference=difference
        i=i+1
    print(min_difference)

