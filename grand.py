user1,user=map(int,input("Enter two number").split())
print(user1+user)
print(user1-user)
print(user1*user)
print(user1/user)
print(user1%user)
user2=int(input("Enter your age"))
if user2>=18:
    print("you can vote now")
elif user2<18:
    print("you cannot vote now")
else:
    print("please give number in integer data type")
odds=filter(lambda x:x%2!=0,range(1,50))
print(odds)
for i in odds:
    print(i)
multi=map(lambda x:x*3,range(1,100))
for i in multi:
    print(i)
u=map(int,input("Enter the number").split())
for x in u:
    print(x,x%2==0)
m=map(lambda x:x*x,u)
for i in m:
  print(i)
m=int(input("Enter the number you want factorial"))
fact=1
for i in range(1,m+1):
    fact*=i
print(fact)
l=input("Enter any Sentence")
word=l.split()
print(len(word))
r=l[::-1]
print(r)

user1, user2, user3 = map(int, input("Enter three numbers: ").split())
print("Larger:", user1 if user1>user2 and user1>user3 else (user2 if user2>user3 else user3))

rad,pi=input("Enter the input of radius and pi").split()
area=int(rad)*float(pi)**2
print("Circumfernce of Circle",area)
n1,n2=map(int,input("enter two number").split())
avg=n1+n2/2
print(float(avg))
for i in range(2,20):
    isprime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            isprime=False
            break
    if isprime:
        print(i)
us=int(input("Enter the number"))
for i in range(1,11):
    print(us,"*",i,"=",us*i)
total=0
for i in range(1,4):
    it=int(input("Enter the item price"))
    total+=it
    if total>1000:
        discount=total*0.10
        print(discount)
        total-=discount
print(total)
u1=int(input("Enter the number"))
if u1%5==0 or u1%3==0:print("yes")
else: print("no")
vowels="aeiou"
c=0
txt=input("Enter the nay text")
if txt in vowels:
   c+=1
print("vowel count",c) 