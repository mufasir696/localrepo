data = [1, [2, [3, 4], {'a':5}], (6, {'b':[7,8]}), 'x', None]
def cal(data,s=0):
    if type(data) in [list,tuple]:
        for i in data:
          s+=cal(i)
    elif type(data)==dict:
        for k,v in data.items():
            s+=cal(v)
    else:
        if type(data)==int:
          s+=data
    return s
print(cal(data))
#program_2
data = {"name":"Ali", "info":[None, "is", ("a","student")], "age":20}
def pro(data):
   if type(data) in [list,tuple]:
      for i in data:
         pro(i)
   elif type(data)==dict:
      for k,v in data.items():
         pro(v)
   else:
      if type(data)==str:
         print(data,end=" ")
pro(data)
d={"a":5, "b":[2,{"c":10}], "d":"x"}  # → 10
def maxi(d):
   maxy=0
   if type(d)==dict:
        for k,v in d.items():
         maxy=max(maxy,maxi(v))
   elif type(d)==list:
        for i in d:
          maxy=max(maxy,maxi(i))
   else:
        if type(d)==int:
            maxy=d
   return maxy
print(maxi(d))
data = [{"id":1}, {"a":2, "b":[{"id":3}]}]
# Output: 2
def count(d,c=0):
   if type(d) in [list,tuple]:
      for i in d:
         c+=count(i)
   elif type(d)==dict:
      for k,v in d.items():
         if k=='id':
           c+=1
         c+=count(v)
   return c
print(count(data))