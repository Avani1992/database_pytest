"""
HackerLand University has the following grading policy:

Every student receives a grade  in the inclusive range from 0 to 100 .
Any  grade less than  40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the  grade and the next multiple of 5  is less than 3 , round  grade up to the next multiple of 5 .
If the value of  grade is less than 38, no rounding occurs as the result will still be a failing grade.
For example,grade=84  will be rounded to 85 but  grade=29 will not be rounded because the rounding would result in a 
number that is less than 40.

Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.


"""

a=[38,75,70,83]

def GradingStudents(x):
  l1=[]
  for i in range(0,len(x)):
    if(x[i]<38):
      l1.append(x[i])
    elif(x[i]%10==3 or x[i]%10==8):
      l1.append((x[i])+2)
    elif(x[i]%10==4 or x[i]%10==9):
      l1.append((x[i])+1)
    else:
      l1.append(x[i])
    
  print(l1)
  
GradingStudents(a) 