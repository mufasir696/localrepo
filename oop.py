class Car:
    def __init__(self,brand,color,speed):
        self.brand=brand
        self.color=color
        self.speed=speed
    def display_info(self):
        # print("Brand",self.brand+"\n"+"Color",self.color+"\n","Speed",self.speed)
        print("Brand:", self.brand)
        print("Color:", self.color)
        print("Speed:", self.speed)
c1=Car("Honda","black",900)
c2=Car(None,None,None)
print(c1.display_info())
print(c2.display_info())
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("Name",self.name)
        print("Age",self.age)
class student(person):
    def __init__(self, name, age,course):
        super().__init__(name, age)
        self.course=course
    def stdinfo(self):
        super().info()
        print("Course",self.course)
c1=student("Sheikh Mufasir",20,"BSCS")
c1.stdinfo()
f1=open(r"C:\Users\Sup\Desktop\sheikh.txt","w")
f1.write("Hello sheikh mufasir iam learning python")
f1.close()
cont=f1.read(r"C:\Users\Sup\Desktop\sheikh.txt","r")
print(cont)
f1.close()