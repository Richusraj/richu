# 1.oldway
# name_files=open("learning_file.txt","r+")
# print(name_files.read())
# name_files.close()

# #2. new way

# with open("learning_file.txt", "r") as f:
#     print(f.read())

with open ("learning_file.txt","r+")as f :
    print(f.read())

# with open("learning_file.txt", "w") as j:
#     j.write("hello ")


# with open("learning_file.txt", "r+") as b:
#     b.write("br")
#     b.seek(0)
#     print(b.read())


# with open("learning_file.txt","a+") as f:
#     print(f.tell())
#     f.seek(0)
#     data=f.readlines()
#     print(data)



