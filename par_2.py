data = [1, [2, [3, 4], {'a':5}], (6, {'b':[7,8]}), 'x', None]
def sumall(data,total=0):
    if type(data) in [list,tuple]:
        for i in data:
            total+=sumall(i)
    elif type(data)==dict:
        for k,v in data.items():
            total+=sumall(v)
    else:
        if type(data)==int:
            total+=data
    return total
print(sumall(data))

data = {"name":"Ali", "info":[None, "is", ("a","student")], "age":20}
def pri(data):
    if type(data)==dict:
        for k,v in data.items():
            pri(v)
    elif type(data)in [list,tuple]:
        for i in data:
            pri(i)
    else:
        if type(data)==str:
           print(' '.join([data]),end=' ')
pri(data)
data={"a":5, "b":[2,{"c":10}], "d":"x"}  # → 10
def maxi(data,max=0):
    if type(data)==dict:
        for k,v in data.items():
            temp=maxi(v,max)
            if temp>max:
                max=temp
    elif type(data)==list:
        for i in data:
            tem=maxi(i)
            if tem>max:
                max=tem
    else:
        if type(data)==int:
            if data>max:
                max=data
    return max
print(maxi(data))
data = [1, (2, [3, {'a': 4}], 5)]

def flat(data):
    result = []
    if type(data) in [list, tuple]:
        for i in data:
            result.extend(flat(i))
    elif type(data) == dict:
        for v in data.values():
            result.extend(flat(v))
    else:
        result.append(data)
    return result

print(flat(data))
data = [1, "a", [2.0, {"x": True, "y": None}]]
# Output: {"int":1, "str":1, "float":1, "bool":1, "NoneType":1}
def datacount(data,c=None):
     if c is None:
      c = {"int":0, "str":0, "float":0, "bool":0, "NoneType":0}     
     if type(data) in [list,tuple]:
        for i in data:
            datacount(i,c)
     elif type(data) == dict:
        for v in data.values():
            datacount(v,c)
     else:
        typename=type(data).__name__
        if typename in c:
            c[typename]+=1
     return c
print(datacount(data))