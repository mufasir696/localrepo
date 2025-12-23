lst = [1, [2, [3, 4], 5], 6]
fal=[]
for i in lst:
    if isinstance(i,int):
     fal.append(i)
    elif isinstance(i,(list,tuple)):
        for j in i:
            if isinstance(j,int):
                fal.append(j)
            elif isinstance(j,(list,tuple)):
                for k in j:
                    if isinstance(k,int):
                        fal.append(k)
print(sum(fal))
def arbitary(lst):
    total=0
    for i in lst:
        if isinstance(i,int):
           total+=i
        elif isinstance(i,(list,tuple)):
           total+=arbitary(i)
    return total
print(arbitary(lst))

products = {
"Electronics": {"Laptop": 1200, "Phone": 800},
"Clothes": {"Shirt": 50, "Shoes": 100},
"Grocery": {"Rice": 20, "Milk": 10}
}
def highprice(pro):
    cat=max(pro,key=lambda x:max(pro[x].values()))
    item=max(pro[cat],key=lambda y:pro[cat][y])
    return item,pro[cat][item]
print(highprice(products))

lst = [1, [2, [3, 2, 4], 5, 1], 6]
count=0
def arbt(lst):
    save={}
    for i in lst:
        if isinstance(i,int):
          save[i]=save.get(i,0)+1
        elif isinstance(i,(list,tuple)):
            nested=arbt(i)
            for k,v in nested.items():
                save[k]=save.get(k,0)+v
    return save
print(arbt(lst))
def cout(lst):
    f={}
    count=0
    for i in lst:
        if isinstance(i,int):
            f[i]={count}
        elif isinstance(i,(list,tuple)):
            nested=cout(i)
            for k,v in nested.items():
                f[k]={count}
        count+=1
    return f
lst=[1,[2,[3,2,4],5,1],6]
def convert(lst):
    dct={}
    for i in lst:
        if isinstance(i,int):
            dct[i]=i
        elif isinstance(i,(list,tuple)):
            nested=convert(i)
            dct.update(nested)
    return dct
print(convert(lst))

def count(lst):
    freq={}
    for i in lst:
        if isinstance(i,int):
          freq[i]=freq.get(i,0)+1
        elif isinstance(i,(list,tuple)):
            nested=count(i)
            for k,v in nested.items():
                freq[k]=freq.get(k,0)+v
    return freq
print(count(lst))
  
