#checking wether entered number is divisible by entered divisior or not
n=int(input("enter  number: "))
d1=int(input("enter first divisor: "))
d2=int(input("enter second divisor: "))
t1=int(n%d1)
t2=int(n%d2)

if t1==t2==0:
    print("Yes.")
else:
    print("No.")
    


#outputs:

    
#enter  number: 99
#enter first divisor: 3
#enter second divisor: 12
#No.


#enter  number: 99
#enter first divisor: 3
#enter second divisor: 11
#Yes.
