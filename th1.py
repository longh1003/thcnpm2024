#b1

#loop
# while True:
#     try:
#
#     # b1 ax + b = 0
#         a = int(input("a = "))
#         b = int(input("b = "))
#     except Exception as ex:
#         print(str(ex))
#     #Exclusive for Python
#     else:
#         if a == 0:
#             if b == 0:
#                 print("VO SO NGHIEM")
#             else:
#                 print("VO NGHIEM")
#         else:
#             print("x = ", -b/a)
#     finally:
#         print("DONE")

# print(("*"*5 + "\n")*5)

#b2
n = int(input("n = "))
a = []
for i in range(n):
    a.append(int(input(f"a[{i}] = ")))

print(a)