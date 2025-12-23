data={
    "a":1,
    "b":{"c":1,"d":3}
}
def nested(data):
    for k,v in data.items():
        if type(v)==dict:
            nested(v)
        else:
            print(f"{k}:{v}")
nested(data)
data1={
    "x":{"y":5},
    "z":10
}
def mul(data):
    for k,v in data.items():
        if type(v)==dict:
            mul(v)
        else:
            mult=2*v
            print(f"{k}:{mult}")
mul(data1)
data3={
    "a":[1,2,{"b":3}],
    "b":{"d":[4,{"e":5}]}
}
def printing(data):
    if type(data)==dict:
        for k,v in data.items():
            printing(v)
    elif type(data)==list:
        for i in data:
            printing(i)
    else:
        print(data)
printing(data3)
data4={
    "info":{"name":"Ali","Skills":["Python","java"]},
    "extra":[{"age":20},{"city":"lahore"}]
}
def prints(data):
    if type(data)==dict:
        for k,v in data.items():
            print(k+"\n")
            prints(v)
    elif type(data)==list:
        for i in data:
            prints(i)
    else:
        print(data)
prints(data4)
data5={
    "a":[1,{"b":2,"c":[3,4]},5],
    "d":{"e":{"f":6}},
    "g":"ignore"
}
def sumy(data,s=0):
    if type(data)==list:
        for i in data:
           s+=sumy(i)
    elif type(data)==dict:
        for k,v in data.items():
           s+=sumy(v)
    else:
        if type(data)==int:
          s+=data
    return s
print(sumy(data5))
data=[1,2,[3,4,[5,6]],{"a":7,"b":[8,9]}]
def printnum(data):
    if type(data)==list:
        for i in data:
          printnum(i)
    elif type(data)==dict:
        for k,v in data.items():
            printnum(v)
    else:
        if type(data)==int:
            print(data)
printnum(data)
data3={"x":[1,2,{"y":3}],"z":{"p":4,"q":[5,6]}}
def sume(data2,total=0):
    if type(data2)==list:
        for i in data2:
            total+=sume(i)
    elif type(data2)==dict:
        for k,v in data2.items():
            total+=sume(v)
    else:
        if type(data2)==int:
            total+=data2
    return total
print(sume(data3))
data3=[1,{"a":2,"b":[3,{"c":4}]}]
def multi(data3,mul=1):
    if type(data3)==list:
        for i in data3:
            mul*=multi(i)
    elif type(data3)==dict:
        for k,v in data3.items():
            mul*=multi(v)
    else:
        if type(data3)==int:
            mul*=data3
    return mul
print(multi(data3))
def multi2(data3):
    if type(data3)==list:
        for i in data3:
            multi2(i)
    elif type(data3)==dict:
        for k,v in data3.items():
            multi2(v)
    else:
        if type(data3)==int:
            return 2*data3
m=multi2(data3)
print(m)
def multi3(data):
    if type(data)==int:
        return 2*data
    if type(data)==list:
        return  [multi3(i) for i in data]
    elif type(data)==dict:
        return {k:multi(v) for k,v in data.items()}
    else:
        return data
print(multi3(data3))
data0=[1,2,[3,4],{"a":5,"b":[6,{"c":7}]}]
def cal(data,s=0):
    if type(data)==int:
        s+=data
    elif type(data)==list:
        for i in data:
            s+=cal(i)
    elif type(data)==dict:
        for k,v in data.items():
            s+=cal(v)
    return s
print(cal(data0))
data1={"x":1,"y":[2,{"z":3}],"w":{"a":4}}
def multi(data):
    if type(data) == int:
        return 3 * data
    elif type(data) == list:
        return [multi(i) for i in data]
    elif type(data) == dict:
        return {k: multi(v) for k, v in data.items()}
    else:
        return data

print(multi(data1))
data40 = [10, {"a":[20, {"b":30}], "c":40}]
def rev(data3):
    if type(data3)==int:
        return int(str(data3)[::-1])
    elif type(data3)==dict:
        return{k:rev(v) for k,v in data3.items()}
    elif type(data3)==list:
        return [rev(i) for i in data3]
print(rev(data40))

def rev2(data):
    if type(data)==list:
        return [rev2(i) for i in data[::-1]]
    elif type(data)==dict:
        val=list(data.values())[::-1]
        keys=list(data.keys())
        # return {ke:rev2(data[ke]) for ke in keys}
        return{k:rev2(v) for k,v in zip(keys,val)}
    else:
        return data
print(rev2(data40))
# data3 = [10, {"a":[20, {"b":30}], "c":40}]
def rev3(data):
    if type(data)==list:
        return [rev3(i) for i in data[::-1]]
    elif type(data)==dict:
        keys=list(data.keys())[::-1]
        return {k:rev3(data[k]) for k in keys}
    else:
        return data
print(rev3(data40))
def rev4(data):
    if type(data)==list:
        return[rev4(i) for i in data]
    elif type(data)==dict:
        key=list(data.keys())
        val=list(data.values())[::-1]
        return {k:rev4(v)for k,v in zip(key,val)}
    else:
        return data
print(rev4(data40))
data4 = {"a":[1, 2, {"b":3}], "c":{"d":[4, {"e":5}]}, "f":6}
def count(data,c=0):
    if type(data)==list:
        for i in data:
            c+=count(i)
    elif type(data)==dict:
        for k,v in data.items():
            c+=count(v)
    else:
        if type(data)==int:
          c+=1
    return c
print(count(data4))
data5 = [10, {"a":2, "b":[3, {"c":4}]}]
def squs(data,s=0):
    if type(data)==list:
        return [squs(i) for i in data]
    elif type(data)==dict:
        return {k:squs(v)for k,v in data.items()}
    else:
        if type(data)==int:
            s+=data**2
    return s
print(squs(data5))
data6 = {"nums":[2, 4, {"a":6, "b":[8, 11]}], "x":12}
def muleven(data,mul=1):
    if type(data)==list:
        for i in data:
            mul*=muleven(i)
    elif type(data)==dict:
        for k,v in data.items():
            mul*=muleven(v)
    elif type(data)==int:
        if data%2==0:
            mul*=data
    return mul
print(muleven(data6))
def mulevens(data, mul=1):
    if type(data) == list:
        for i in data:
            mul *= muleven(i)
    elif type(data) == dict:
        for k, v in data.items():
            mul *= muleven(v)
    else:
        if type(data) == int:
            if data % 2 == 0:
                mul *= data
    return mul

data6 = {"nums":[2, 4, {"a":6, "b":[8, 10]}], "x":12}
print(mulevens(data6))


data7 = {"a":1, "b":"ignore", "c":[2, "skip", {"d":3}]}
def peint(data):
    if type(data)==dict:
        return {k:peint(v)for k,v in data.items()}
    elif type(data)==list:
        return [peint(i)for i in data]
    else:
        if not type(data)==str:
          print(data)
peint(data7)