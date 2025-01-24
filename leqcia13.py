#1)
# try:
#     x=int(input("enter a number 1:"))
#     y=int(input("enter a number 2:"))
#     z=x/y
# except ValueError:
#     print("araswori inputi")
# except ZeroDivisionError:
#     print("nulze ver gaiyofa")

#2)
# try:
#     print("python"[9])
# except IndexError:
#     print("araaqvs aseti indeqsi")

#3)
# age=17
# try:
#     if age<18:
#         raise ValueError("asaki unda iyos 18 an meti")
# except ValueError:
#     print("asaki unda iyos 18 an meti")

#4)
# try:
#     x=int(input("enter a number 1:"))
#     y=int(input("enter a number 2:"))
#     z=x/y
# except ValueError:
#     print("araswori inputi")
# except ZeroDivisionError:
#     print("nulze ver gaiyofa")
# else:
#     print("shecdoma arari")
# finally:
#     print("programa morcha")

#5)
# try:
#     a=int(input("sheiyvane mteli ricxvi 1:"))
#     b=int(input("sheiyvane mteli ricxvi 2:"))
#     c=int(input("sheiyvane mteli ricxvi 3:"))
#     if a+b>c and a+c>b and b+c>a:
#         sashualo=(a+b+c)/3
#         print(sashualo)
#     else:
#         raise ValueError("ricxvebi ar akmayofileben samkutxedis wess")
# except ValueError as m:
#     print(m)
