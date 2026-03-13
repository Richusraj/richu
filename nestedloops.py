# length=6
# width=6
# for i in range(length):
#     for j in range(length):
#         print(width, end="")
# row=5
# for i in range(row):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# row=5
# col=5
# for i in range(row):
#     for j in range(col):
#         print("*",end=" ")
#     print()

row=5
col=4
for i in range(row,0,-1):
    for j in range(i):

        print("*",end=" ")
    print()