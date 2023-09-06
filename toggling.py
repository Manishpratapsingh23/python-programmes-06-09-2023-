#mobile phone toggle condition
#1 is for ON mode
#0 is for OFF mode
n=int(input("enter total number of students: "))
mode=[1]*n
for i in range(1,n+1):
    for k in range(i,n+1):
        if k%i==0:
            if mode[k-1]==1:
                mode[k-1]=0
            else:
                mode[k-1]=1
print("the students whose mobile phones are turned off:")
for i in range(1,n+1):
    if mode[i-1]==0:
      print(i,end=",")




#output:
      
#enter total number of students: 500
#the students whose mobile phones are turned off:
#1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,
