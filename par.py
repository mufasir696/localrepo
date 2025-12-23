print('helo wolrd')
age=25
isstudent=True
height=3.5
name="Mufasir"
print(name,"is",age,"year old")
file = open(r"C:\Users\Sup\Desktop\test.txt", "w")
file.write("Hello Mufasir")
file.close()
print("File successfully written on Desktop")

print("File written successfully")
file = open("C:\\Users\\Sup\\AppData\\test.txt", "r")
content = file.read()
print(content)
file.close()
def gen_numbers(n):
    for i in range(1, n+1):
        yield i

for num in gen_numbers(5):
    print(num)
