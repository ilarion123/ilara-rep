<<<<<<< HEAD
#1)შექმენით სია numbsნებისმიერ 5 რიცხვითი მნიშვნელობით. იპოვეთ ამ რიცხვების ჯამი,
# მინიმალური, მაქსიმალური და საშუალო არითმეტიკული.ასევე შეასრულეთ შემდეგი
# ოპერაციები:
# •სიას დაამატეთ ბოლო ელემენტად რიცხვი 102
# •სიის მესამე ელემენტად ჩასვით რიცხვი 205
# •წაშალეთ სიის მე-4 ელემენტი
# •დაალაგეთ სია ზრდადობის მიხედვით და დაბეჭდეთ

# x=[17,98,65,21,32]
# jami=sum(x)
# minimaluri=min(x)
# maqsimaluri=max(x)
# sashualo_aritmetikuli=jami/len(x)
# x.append(102)
# x.insert(2,205)
# del x[3]
# x.sort()
# print(jami)
# print(minimaluri)
# print(maqsimaluri)
# print(sashualo_aritmetikuli)
# print(x)

#2)
# დაწერეთ პროგრამა, რომლის მეშვეობით შეიყვანთ (input-ით) 10 მონაცემს. წარმოადგინეთ და
# დაბეჭდეთ ისინი სიის ელემენტების სახის.

# x=[]
# for i in range(10):
#     y=input("sheiyvane monacemi")
#     x.append(y)
# print(x)

#3)
# შექმენით სიაfruits, რომელის ელემენტებია: Watermelon, Banana, Apple. დაალაგეთ სიის
# ელემენტები ალფაბეტის უკუ-მიმართულებით და დაბეჭდეთ ისინი.

# fruits=["Watermelon","Banana","Apple"]
# fruits.sort(reverse=True)
# print(fruits)

#4)
# შექმენით 10 ელემენტიანი სია, რომლის ელემენტებია ნებისმიერი შემთხვევითი მთელი
# რიცხვები 25-დან 110-მდე. დაბეჭდეთ სია და იპოვეთ მინიმალური ელემენტი.
# import random
# x=[random.randint(25,110)for i in range(10)]
# print(x,min(x))
#5)
# დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა 2 სია. ფუნქცია აბრუნებს მნიშვნელობა
# True-ს თუ სიებს აქვთ ერთი მაინც საერთო ელემენტი. წინააღმდეგ შემთხვევაში აბრუნებს False
# მნიშვნელობას.
# list1=[1,2,3,5]
# list2=[4,5,6,2]
# saertoar=False
# for item in list1:
#     if item in list2:
#         saertoar=True
#         break
# if saertoar:
#     print("true-saerto elementi aqvt")
# else:
#     print("False-saerto lementi ar aqvs")

#6)
# დაწერეთ ფუნქცია, რომელიც სიაში არსებულ კენტ რიცხვებს წაშლის. ფუნქცია აბრუნებს
# განახლებულ სიას.
# x= [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in x:
#     if i % 2 != 0:
#         x.remove(i)
# print(x)
#7)
# დაწერეთ პროგრამა, სადაც მომხმარებელს შეაყვანინებთ 3x4მატრიცის ელემენტებს. შეყვანილი
# ინფორმაციის მიხედვით ააგეთ სია და გამოიტანეთ შედეგად მატრიცის სახით. მაგ. შედეგად
# უნდა დაიეჭდოს მატრიცა შემდეგნაირად:

# arr=[]
# for i in range(3):
#     a=[] 
#     for j in range(4):
#         x=int(input(f"sheiyvane elementi[{i},{j}]: "))
#         a.append(x)
#     arr.append(a)
# for a in arr:
#     print(a)

#8)
# იპოვეთ სიაში [1, 5, 23, 5, 12, 2, 5, 1, 18, 5]ყველაზე ხშირად განმეორებადი
# რიცხვი. დაბეჭდეთ შედეგი. ასევე მიუთითეთ რამდენჯერ შეგხვდათ სიაში ყველაზე ხშირად
# განმეორებადი რიცხვი.

# listt=[1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
# ramdenjer=0
# xshir_iricxvi=listt[0]
# for i in listt:
#     raodenoba=listt.count(i)
#     if raodenoba>ramdenjer:
#         xshir_iricxvi=i
#         ramdenjer=raodenoba
# print(xshir_iricxvi)
# print(ramdenjer)
#9)
# სტრიქონი 'python php pascal javascript java c++' წარმოადგინეთ სიის სახით
# (სტრიქონის თითოეული სიტყვა სიის თითოეული ელემენტად). იპოვეთ სიის ყველაზე გრძელი
# ელემენტი (ანუ ყველაზე გრძელი სიტყვა).

# x='python php pascal javascript java c++'
# y=x.split()
# print(y)
# list1=[]
# for i in y:
#     a=len(i)
#     list1.append(a)
# print(list1)
# print(max(list1))
# print(sum(list1))


#10)
# შექმენით სია რიცხვითი ელემენტებით. shuffle ფუნქციის გამოყენებით (random მოდულიდან)
# მოახდინეთ სიის ელემენტების შემთხვევითად არევა და დაბეჭდეთ მიღებული სია.(მითითება:
# ფუნქცია იწერება შემდეგნაირად: random.shuffle(x) სადაც x სიის დასახელებაა)
# import random
# x=[10,20,30,40,50,60,70,80,90,100]
# random.shuffle(x)
# print(x)
=======
#1)შექმენით სია numbsნებისმიერ 5 რიცხვითი მნიშვნელობით. იპოვეთ ამ რიცხვების ჯამი,
# მინიმალური, მაქსიმალური და საშუალო არითმეტიკული.ასევე შეასრულეთ შემდეგი
# ოპერაციები:
# •სიას დაამატეთ ბოლო ელემენტად რიცხვი 102
# •სიის მესამე ელემენტად ჩასვით რიცხვი 205
# •წაშალეთ სიის მე-4 ელემენტი
# •დაალაგეთ სია ზრდადობის მიხედვით და დაბეჭდეთ

# x=[17,98,65,21,32]
# jami=sum(x)
# minimaluri=min(x)
# maqsimaluri=max(x)
# sashualo_aritmetikuli=jami/len(x)
# x.append(102)
# x.insert(2,205)
# del x[3]
# x.sort()
# print(jami)
# print(minimaluri)
# print(maqsimaluri)
# print(sashualo_aritmetikuli)
# print(x)

#2)
# დაწერეთ პროგრამა, რომლის მეშვეობით შეიყვანთ (input-ით) 10 მონაცემს. წარმოადგინეთ და
# დაბეჭდეთ ისინი სიის ელემენტების სახის.

# x=[]
# for i in range(10):
#     y=input("sheiyvane monacemi")
#     x.append(y)
# print(x)

#3)
# შექმენით სიაfruits, რომელის ელემენტებია: Watermelon, Banana, Apple. დაალაგეთ სიის
# ელემენტები ალფაბეტის უკუ-მიმართულებით და დაბეჭდეთ ისინი.

# fruits=["Watermelon","Banana","Apple"]
# fruits.sort(reverse=True)
# print(fruits)

#4)
# შექმენით 10 ელემენტიანი სია, რომლის ელემენტებია ნებისმიერი შემთხვევითი მთელი
# რიცხვები 25-დან 110-მდე. დაბეჭდეთ სია და იპოვეთ მინიმალური ელემენტი.
# import random
# x=[random.randint(25,110)for i in range(10)]
# print(x,min(x))
#5)
# დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა 2 სია. ფუნქცია აბრუნებს მნიშვნელობა
# True-ს თუ სიებს აქვთ ერთი მაინც საერთო ელემენტი. წინააღმდეგ შემთხვევაში აბრუნებს False
# მნიშვნელობას.
# list1=[1,2,3,5]
# list2=[4,5,6,2]
# saertoar=False
# for item in list1:
#     if item in list2:
#         saertoar=True
#         break
# if saertoar:
#     print("true-saerto elementi aqvt")
# else:
#     print("False-saerto lementi ar aqvs")

#6)
# დაწერეთ ფუნქცია, რომელიც სიაში არსებულ კენტ რიცხვებს წაშლის. ფუნქცია აბრუნებს
# განახლებულ სიას.
# x= [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in x[:]:
#     if i % 2 != 0:
#         x.remove(i)
# print(x)
#7)
# დაწერეთ პროგრამა, სადაც მომხმარებელს შეაყვანინებთ 3x4მატრიცის ელემენტებს. შეყვანილი
# ინფორმაციის მიხედვით ააგეთ სია და გამოიტანეთ შედეგად მატრიცის სახით. მაგ. შედეგად
# უნდა დაიეჭდოს მატრიცა შემდეგნაირად:

# arr=[]
# for i in range(3):
#     a=[] 
#     for j in range(4):
#         x=int(input(f"sheiyvane elementi[{i},{j}]: "))
#         a.append(x)
#     arr.append(a)
# for a in arr:
#     print(a)

#8)
# იპოვეთ სიაში [1, 5, 23, 5, 12, 2, 5, 1, 18, 5]ყველაზე ხშირად განმეორებადი
# რიცხვი. დაბეჭდეთ შედეგი. ასევე მიუთითეთ რამდენჯერ შეგხვდათ სიაში ყველაზე ხშირად
# განმეორებადი რიცხვი.
sia=[1,5,7,8,9,9,9,7,6,5,5]
# a=sia.count(9)
# print(a)
#9)
# სტრიქონი 'python php pascal javascript java c++' წარმოადგინეთ სიის სახით
# (სტრიქონის თითოეული სიტყვა სიის თითოეული ელემენტად). იპოვეთ სიის ყველაზე გრძელი
# ელემენტი (ანუ ყველაზე გრძელი სიტყვა).
# x='python php pascal javascript java c++'
# y=x.split()
# print(y)
# list1=[]
# for i in y:
#     a=len(i)
#     list1.append(a)
# print(list1)
# print(max(list1))
# print(sum(list1))

#10)
# შექმენით სია რიცხვითი ელემენტებით. shuffle ფუნქციის გამოყენებით (random მოდულიდან)
# მოახდინეთ სიის ელემენტების შემთხვევითად არევა და დაბეჭდეთ მიღებული სია.(მითითება:
# ფუნქცია იწერება შემდეგნაირად: random.shuffle(x) სადაც x სიის დასახელებაა)
# import random
# x=[10,20,30,40,50,60,70,80,90,100]
# random.shuffle(x)
# print(x)
>>>>>>> 86dd9464aaeca00e3966d380c4059466965308b0
