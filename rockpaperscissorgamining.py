import random
print("enter your choice")
a=int(input("1-stone,2-paper,3-scissor"))
if(a>3):
    print("enter valid number")
    a=int(input("1-stone,2-paper,3-scissor"))
b=random.randint(1,3)
if(b==1):
    print("computer choice is stone")
if(b==2):
    print("computer choice is paper")
if(b==3):
    print("computer choice is scissor")
if((a==1 and b==2) or (a==2 and b==1)):
    c=2
elif((a==1 and b==3) or(a==3 and b==1)):
    c=1
elif(a==b):
    print("match draw")
else:
    c=3
if(a==c):
    print("you win")
else:
    print("computer win")
