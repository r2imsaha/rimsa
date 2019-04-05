List=['p','y','t','h','o','n','f','o','r','g','a','m','e','s']
sliced_List = List[3:8]
sliced_List = List[::-1]
print(sliced_List)
x={"apple","banana","cherey"}
y={"google","microsoft","facebook"}
z=x.isdisjoint(y)
print(z)
x={'a','b','c'}
y={"f","e","d","c","b","a"}
z=x.issuperset(y)
print(z)
x={"f","e","d","c","b","a"}
y={"a","b","c"}
z=x.symmetric_difference(y)
print(z)
x={"apple","banana","cherey"}
y={"google","microsoft","facebook"}
x.symmetric_difference_update(y)
print(x)
x={"apple","banana","cherey"}
y={"google","microsoft","facebook"}
z=x.union(y)
print(z)
x={"apple","banana","cherey"}
y={"google","microsoft","facebook"}
x.update(y)
print(x)




















