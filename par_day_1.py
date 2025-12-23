try:
    a, b = map(int, input("Enter two numbers separated by space: ").split())
except ValueError:
    print("Error! Do numbers type karo, space ke saath.")
    exit()

print("Sum:", a + b)
print("Difference:", a - b)
print("Multiply:", a * b)
print("Integer Division:", a // b)
print("Float Division:", a / b)


user=int(input("Enter your age"))
if user>18:
    print("young vote de saktein ho")
else:
    print("vote nahi de saktein")
for i in range(1,10):
    print(i)
def square(lst,m):
    return [x*m**2 for x in lst]
lst=[1,2,3,4]
print(square(lst,3))
def iseven(lst):
    return[x%2==0 for x in lst]
print(iseven(lst))
user=input("Enter the senetnece")
def count(user,c=0):
    for word in user.split():
        c+=1
    return c
print(count(user))
def firstletter(user):
    return user[0]
def reverseletter(user):
    return user[::-1]
def cal(num,sum=0):
    return 0 if not num else num[0]+cal(num[1:])
def avg(num,sum=0):
    return cal(num)/len(num)
print(firstletter(user))
print(reverseletter(user))
print(cal(lst))
print("average",avg(lst))
def store(name,age,section):
    my_dict={
        "Name":name,
        "Age":age,
        "Section":section
    }
    return my_dict
i=0
allstd=[]
while(i<=3):
 name=input("Enter the name ")
 age=int(input("Enter your age"))
 section=(input("Enter your section"))[0]
 allstd.append(store(name,age,section))
 i+=1
for i in allstd:
  print(i)
tup=()
def stored(n):
    global tup
    tup+=(n,)
for i in range(5):
    user=int(input("Enter the number"))
    stored(user)
print(max(tup),sum(tup))
file=open(r"C:\Users\Sup\Desktop\hello.txt","w")
file.write("The \"best\" paragraph depends on its purpose, but a good one generally includes a "
"clear topic sentence, several supporting sentences with relevant details, and a concluding sentence. "
"For academic writing, paragraphs are often 100–200 words, while creative writing may have different"
" structures based on scene and narrative. This video explains the basic structure of a paragraph, "
"including topic, supporting, and concluding sentences")
file.close()
file = open(r"C:\Users\Sup\Desktop\hello.txt", "r")
content = file.read()
print(content)
file.close()
A={1,2,3}
B={4,5,6}
print(A&B)
print(A|B)
print(A-B)
user1,user2=map(int,input("Enter the number").split())
try:
    result=user1/user2
    print(result)
except ZeroDivisionError:
    print("not divide by other user")

class car:
    def __init__(self,brand,color,speed):
        self.brand=brand
        self.color=color
        self.speed=speed
    def display_info(self):
        print("Brand",self.brand+"\n"+"Color",self.color+"\n","Speed",self.speed)
c1=car("Honda","black",900)
c2=car()
print(c1.display_info())
print(c2.display_info())
