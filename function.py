# def stdy(a):
#     return a**2
# print(stdy(5))

# stdy=lambda a: a**2
# print(stdy(5))

# total=lambda a,b,c:a+b+c
# print(total(2,2,3))

# even_odd=lambda x:x**2 if x%2==0 else x**3
# print(even_odd())

# grt= lambda a,b:f"greatest numbr is {a} "if a>b else f"greatest number is {b}"
# print(grt(3,4))

# grt_3=lambda x,y,z: x if x>y and x>z else(y if y>x and y>z else z)
# print(grt_3(224,223,222))

# equal=lambda x,y:f"geater is {x}" if x>y else if f"greater is {y}"   else "equal"
# print(equal(2,3))   


# from functools import reduce
# # from functool import *

# numbers=[1,2,3,4,5,6]
# result=reduce(lambda x,y:x+y,numbers)
# print(result)


# from functools import reduce

# join=["hello","","world"]
# result=reduce(lambda x,y:x+y,join)
# print(result)


# from functools import reduce

# lrg=[1,2,3,4,5,6,7]
# result=reduce(lambda x,y:x if x>y else y,lrg )
# print(result)



# from functools import reduce

# lrg=[1,2,3,4,5,6,7]
# result=reduce(lambda x,y:x if x<y else y,lrg )
# print(result)



# from functools import reduce

# strlist=["hello","brooo","cristiano ronaldo"]
 
# result=reduce(lambda x,y:x if len(x)>len(y) else y,strlist)
# print(result)

# from functools import reduce

# dupli=["hello","hello","broo","ronaldo"]
# result=reduce(lambda x,y:x+)
# print(result)


# def my_decor(func):
#     def wrapper():
#         print("function started")
#         func()
#         print("exicution stop")
#         return wrapper
    
# @my_decor
# def greet():

#     print("hello python")
# greet()


# def to_upper(richu_functions):
    



# def strings(s):
#     print(s)
# strings("my name is richu")    





# def greet(a):
#     print(a)
# greet("hello welcome")


# def greet(name):
#     print("welcome",name)
# greet("rono")

# def greet(a,b):
#     return a+b
# print(greet(10,20))


# def greet(name,age):
#     print(f"my name is {name} and my age is {age}")
#     # print("age",age)
# greet("richu",22)
# greet("shahal",24)


# def person(name,age,adress):
#     print(f"my name is {name} and my age is {age} i am from {adress}")
# person(age=21,adress="calicut",name="richu")



# def greet(a):
#     if a==2:
#         return "this is tow"
#     else:
#         return "tgis is not tow"
# print(greet(4))


# recrusive function

# a=int(input("ender your value : "))
# def greet(a):
#     if a>0:
#         return f"your value {a} is bigger thasn zero"
#     elif a==0:
#         return "your value is zero"
#     else:
#         return f"your value {a} is lessthan zero"
# print(greet(a))




# def greet(a,b):
#     return a+b
# print(greet(3,5))

# lam=lambda a,b:a+b
# print(lam(1,2))

# x=int(input("ender your value : "))
# a=lambda x:f"is positive{x}" if x>0 else f"is negative{x}"
# print(a(x))

# a=[2,3,4]

# b=list(map(lambda x:x**2,a))
# print(b)


# k=["mess,'ronoi"]

# b=list(map(str.upper,k))
# print(b)


# a=["hi"]
# b=list(map(str.upper,a))
# print(b)


# a=[1,4,55,44,66,77,11]
# b=list(filter(lambda x:x>10,a))
# print(b)

# a=[1,2,3,4,5]
# B=reduce

from functools import reduce

a=[1,2,3,4,5,6]
print(reduce(lambda a,b:a+b,))






    



           