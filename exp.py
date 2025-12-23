def c_to_f(temp):
    return (temp*9/5)+32
lst=[0.0,10.0,20.0,30.0,40.0,50.0]
for i in lst:
    m=c_to_f(i)
    print(m)
u=map(c_to_f,lst)
for i in u:
    print(i)
total=0
for i in range(1,4):
    it=int(input("Enter the item price"))
    total+=it
if total>1000:
  discount=total*0.10
  total-=discount
  print(discount)
print(total)
vowels="aeiou"
c=0
const=0
txt=input("Enter the nay text")
for i in range(len(txt)):
 if txt[i] in vowels:
   c+=1
 else:
    const+=1
print("vowel count",c) 
print("other letter conunt",const)
u1=int(input("Enter the number"))
sum_div=0
for i in range(1,u1):
   if u1%i==0:
      sum_div+=i
if sum_div==u1:
   print(u1,"It is perfect Number")
else:
   print("not perfect number")
n1=int(input("Enter the number to calculate armStrong"))
org=n1
sum_dig=0
digits=len(str(n1))
while n1>0:
   digit=n1%10
   sum_dig+=digit**digits
   n1=n1//10
if sum_dig==org:
   print("Arm strong Number")
else:
   print("No it is Arrm Strong Number")

x=[1,2,3]
print(x*0)


