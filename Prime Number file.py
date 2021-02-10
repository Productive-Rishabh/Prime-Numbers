# Prime Number not above 1000

x=int(input("Enter Your Number: "))


for i in range (2,x):
     if x%i==0 and x<1000:
        print(x,"Composite Number")
        break
if x==1:
    print("Neither Prime Nor Composite")

if x>1000:
    print("Do Not disturb")
        
if x%i!=0 and x<1000:
    print(x,"Prime Number")

    
