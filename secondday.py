def countdown(n):
    if n==0:
        return ""
    else:
        return str(n)+" "+countdown(n-1)
print(countdown(5))
def countdowns(n):
    if n==0:
        return []
    else:
        return [n]+countdowns(n-1)
print(countdowns(5))
def count(n):
    if n==0:
        return []
    else:
        return count(n-1)+[n]
print(",".join(map(str,count(5))))
def square(x):
    return (x,x * x)

numbers = [1, 2, 3, 4]
result = map(square, numbers)
print(dict(result))
def sq(n):
    return (n,n*n)
num=[1,2,3,4]
res=[]
for i in num:
    res.append(sq(i))
print(res)
def sqs(n):
    return n*n
nums=[1,2,3,4]
print(list(map(sqs,nums)))
data = [1, [2, [3, [4, 5]]]]
def recu1(data):
    for i in data:
        if type(i)==list:
            recu1(i)
        else:
            print(i)
recu1(data)
data = {
    "a": 1,
    "b": {"c": 2, "d": {"e": 3}}
}
def complex(data):
    for k,v in data.items():
        if type(v)==dict:
            complex(v)
        else:
            print(f'{k}:{v}')
complex(data)
def sqy(n):
    return n*n
num=[1,2,3,4]
for i in num:
    print(sqy(i))
