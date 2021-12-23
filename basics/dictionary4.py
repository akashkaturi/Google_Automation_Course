def fun(s):
    return s.get(1,"Not found")
k=["hello","world","we","are","here"]
j=[{2:"hello"},{1:"Bye"}]
k.sort(key=lambda x:x[:2])
j.sort(key=fun)
print(k)
print(j)