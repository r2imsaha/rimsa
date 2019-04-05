a=[1,"Abhishek","Gaurab","Rajoshree","Sonu",10]
print(a[3:])
print(a[0,2])
print(a)
print(a+a)
print(a*3)

print(fruits)
print(fruits[1])
fruits[1]="Blackbary"
print(fruits)
for x in fruits:
    print(x)
if "apple" in fruits: ##check if Item Exists
    print("yes,'apple' is in the fruit items")
print(len(fruit))
fruits.append("orange")
print(fruits)
fruits.insert(1,"orange")
print(fruits)
fruits=["apple","banana","cherry",]
fruits.remove("banana")
print(fruits)
fruits.pop()
print(fruits)
fruits=["apple","banana","cherry"] 
del fruits
fruits=["apple","banana","cherry",]
fruits.clear()
print(fruits)
fruits=list(("apple","banana","cherry"))
print(fruits)
x=10,fruits.copy()
print(x)
print(type(x))
x=fruits.count("cherry")
print(x)
points=[1,4,2,9,7,8,9,3,1]
x=points.count(9)
print(x)
fruits=["apple","banana","cherry",]
cars=["BMW","Lamborgini","Volvo"]
cars.sort()
print(cars)
