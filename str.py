
# len
a="hello"
print(len(a))
print(type(a))


"""ascci value"""

         # ord
a="A"
print(ord(a))

         # chr
a=65
print(chr(a))

#indexing

a="shahal"
print(a[0])
print(a[-1])

# slicing

b="cristiano"
print(b[0:5:2])
"""str reverse methord in slicing"""
print(b[::-1])

# str operators

#       1.str concastination
place="calicut"
place+="district"
# place+=5------error(str+int not works)
print(place)

#       2.str repeatation
place="calicut"
print(place*5)
# print(place*place)-----error(str*str not works)


#        1. str methords in python there are 8 methords

# case conversion methords

        #1 upper
name="richu s raj"
print(name.upper())

        #2 lower
name="riCHU s raj"
print(name.lower())

        #3 title
name="richu s raj"
print(name.title())

        #4 capitalize
name="richu s raj i am from calicut"
print(name.capitalize())

        #5 swap
name="richu S RAJ"
print(name.swapcase())


# 2.searching and fining

        # 1.finding

name="richu s raj"
print(name.find("c"))

name="richu s raj"
print(name.find("juh"))

        # 2.rfind
name="richu s raj"
print(name.rfind("r"))

        # 3.index
name="richu s raj"
print(name.index("s"))

name="richu s raj"
# print(name.index("sdj"))-------error

        # 4.rindex
name="richu s raj"
print(name.rindex("r"))

        # 5.count
name="richu s raj"
print(name.count("g"))


# 3.validation checking

        # i.isalpha()
name=("ronaldo")
print(name.isalpha())

name=("ronald o")
print(name.isalpha())

name=("ronaldo123")
print(name.isalpha())

name=("ronaldo😍")
print(name.isalpha())
print()

        # 2.isdigit
number="777777"
print(number.isdigit())

number="77777 7"
print(number.isdigit())

number="777777rr"
print(number.isdigit())
print()

        # 3.isalunm
a="cris7"
print(a.isalnum())

a="cris 7"
print(a.isalnum())

a="cris7😊"
print(a.isalnum())
print()

        # 4.isdecimal
num="7"
print(num.isdecimal())
 





        

        


























# End
# place="calicut"
# place+="dist"
# print(place)


# copamy="quest"
# print(dir(copamy))


# company="quest calicut"
# print(company.upper())

# s="ronald0"
# print(s.replace("0","o"))


# s= "cristiano  ronaldo       "
# print(s.strip())




# s="python"
# print(s.center(25,"*"))


# s="python"
# print(s.ljust(25,"*"))


# s="python"
# print(s.rjust(25,"*"))


# s="python"
# print(s.zfill(25))

# s="python"
# print(s.zfill(25))


# name="richu"
# age="22"
# print("my name is {} and iam {} years old".format(name,age))


# name="richu"
# age="22"
# print(f"my name is {name} i am {age} years old")


# rowstr
# name="richu"
# age="22"
# print("my name is richu \n iam 22 \t years old")


# s="welcome to the world of python"
# print(s.split())

# s="welcome-to-the-world-of-python"
# print(s.split("-"))

# s="welcome-to-the-world-of-python"
# print(s.split("l"))

# s="welcome-to-the-world-of-python"
# print(s.split("-",3))

# s="welcome-to-the-world-of-python"
# print(s.rsplit("-",3))




# s="job = python"
# print(s.partition("="))

# s="python"
# print(s.partition("python"))

# s="job = python"
# print(s.partition("python"))


# s="job = python"
# print(s.partition("x"))



# s="welcome to python world"
# print(s.rpartition(" "))

# encod/e
# h="hello bro"
# print(h.encode())
# print(h.encode(encoding="utf-8"))
# print(h.encode(encoding="utf-8",errors="strict"))


# # decord
# #       encode convertet to decode
# s="ronaldo"
# encode=s.encode()
# print(encode)
# decord=encode.decode()
# print(decord)




# print("hello\tpython".expandtabs(25))


# translate="hai sraava"
# print(translate.translate({97:"x",115:"y"}))
