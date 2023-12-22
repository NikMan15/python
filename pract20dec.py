'''from math import *
class circle:
    def __init__(self,r):
        self.r=r
    def perimeter(self):
        per=2*pi*self.r
        return per
    def area(self):
        ar=pi*(r**2)
        return ar
r=int(input("Enter the radius of the circle: "))
c=circle(r)
peri=circle.perimeter(c)
are=circle.area(c)
print("Perimeter of circle:",peri)
print("Area of circle:",are)
'''
'''class vits:
    counter=0
    def __init__(self):
        vits.counter += 1
v1=vits()
v2=vits()
print("no. of instances:",vits.counter)
'''
'''class vits:
    def __init__(self,name,age):
        self.name=name
        self.age=age
list=[]
list.append(vits("Akash",21))
list.append(vits("rahul",11))
list.append(vits("Adarsh",21))
for obj in list:
    print(obj.name,obj.age,sep=" ")
'''
class shoppingkart:
    def __int__(self):
        self.items=[]
    def add_item(self,item_name,qty):
        self.items.append(item_name,qty)
    def remove_item(self,item_name):
        from item in items:
            if item[0]==item_name:
                self.items.remove(item)
                break
    def calc_tot(
