sample=(2,3,4,"hello","brUhh")


# unpacking

person=("richu","rono","messi","neymar")
person=(*person,"ibra","toni")
print(person)



# delete



person=("richu","rono","messi","neymar")
del person

# print(person)  ---- delete memory 


# sclicing





# loops

# person=("richu","rono","messi","neymar")

# for i in person:
#     print(i)


    
# for i in range(len(person)):
#     print(i)


# for i in range(len(person)):
#     print(person[i])


# i=0
# while i < len(person):
#     print(person[i])
#     i+=
    



# sample_=("looo",1,(2,3,4),1.5)
# print(sample_)


set1={1,2,3,4,56,77}
set2={22,44,1,2,3,4}
# print(set1|set2)
# print(set1&set2)
# set1.intersection_update(set2)
# print(set1)

print(set1-set2)
set1.difference_update(set2)
print(set1)

