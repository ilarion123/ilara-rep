# დაბეჭდეთ 8-ის ჯერადი რიცხვები 200-დან 25-ის ჩათვლით კლებადობით.

# for i in range(200,25,-1):
#     if i%8==0:
#         print(i)

# დაითვალეთ 100-დან 2500-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი
#   ერთდროულად. დაბეჭდეთ მიღებული შედეგი.

# jami=0
# for i in range(100,2501):
#     if i%7==0 and i%5==0:
#         jami+=i
# print(jami)

# დაითვალეთ 1500-დან 2100-ის ჩათვლით 5-ის ჯერადი რიცხვების რაოდენობა. დაბეჭდეთ შედეგი.

# raodenoba= 0
# for i in range(1500, 2101, 5):
#     raodenoba += 1
# print(raodenoba)

# დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის, 75, 80-ისა. გამოიყენეთ continue
#ოპერატორი.

# for i in range(15,151,5):
#     if i==50 or i==75 or i==80:
#         continue
#     print(i)

# შეიყვანეთ ნებისმიერი 2 რიცხვი.
# ციკლის გამოყენებით დაბეჭდეთ შეყვანილი რიცხვების საერთო გამყოფები.
# მაგ. 15-ის და 18-ის საერთო გამყოფებია: 1, 3

# x = int(input("enter number"))
# y = int(input("enter number"))
# i = 1
# while i <= x and i<=y:
#     if x % i == 0 and y % i == 0:
#         print(i)
#     i += 1

# შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.

# x=int(input("enter a number"))
# y=int(input("enter a number"))
# i=1
# while True:
#     if i%x==0 and i%y==0:
#         print(i)
#         break
#     i+=1    

#  დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს.
# პროგრამამ შეამოწმოს, თუ შეყვანილი რიცხვი 10-ის ჯერადია, დაბეჭდოს “რიცხვი ბოლოვდება 0-ით”, 
# თუ არადა დაბეჭდოს “რიცხვი არ ბოლოვდება 0-ით”. 
# (გაითვალისწინეთ: 10-ის ჯერადი ნიშნავს რომ 10-ზე გაყოფისას ნაშთი არის 0).


# number=int(input("enter number"))
# if number %10==0:
#     print("რიცხვი ბოლობდება 0-ით")
# else:
#     print("რიცხვი არ ბოლოვდება 0-ით")


#  დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ნებისმიერ რიცხვს.
#  პროგრამამ შეამოწმოს, თუ რიცხვი დადებითია, დაბეჭდოს ეკრანზე “Number is positive”, თუ რიცხვი უარყოფითია, 
# # დაბეჭდოს “Number is negative”, თუ არადა დაბეჭდოს “Number is equal to zero”.

# number=eval(input("enter number"))
# if number > 0:
#     print("number is positive")
# elif number<0:
#     print("number is negative")
# else:
#     print("number is equal to zero")

# დაწერეთ პროგრამა, რომლის მეშვეობითაც შეიტანთ ორ ნებისმიერ რიცხვს
# პროგრამამ შეამოწმოს, თუ ორივე შეყვანილი რიცხვი 10-ზე მეტია, დაითვალეთ მათი საშუალო არითმეტიკული, 
# თუ არადა დაითვალეთ მათი ნამრავლი. დაბეჭდეთ მიღებული შედეგი.

# x=eval(input("enter a number:"))
# y=eval(input("enter a number"))
# if x>10 and y>10:
#     print((x+y)/2)
# else:
#     print(x*y)

# დაბეჭდე კალკულატორი ციკლის და პირობითი ოპერატოორების გამოყენებით,
# გამოიყენე ოპერაციებად + - მიმატება, ** - ხარისხში აყავანა, /- გაყოფა.

# x=eval(input("enter a number1:"))
# y=eval(input("enter a number2:"))
# operacia=str(input("amoirchie operacia:+,**,/ :"))
# if operacia=="+":
#     amoxsna= x+y
#     print(amoxsna)
# elif operacia=="**":
#     amoxsna=x**y
#     print(amoxsna)
# elif operacia=="/":
#     if y!=0:
#         amoxsna=x/y
#         print(amoxsna)
#     else:
#         print("0-ze gayofa ar sheileba")