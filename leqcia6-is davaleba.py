# დაბეჭდეთ 5-ის ჯერადი რიცხვები 20-დან 125-ის ჩათვლით.

# a = 20
# while a <= 125:
#     if a % 5 == 0:
#         print(a)
#     a += 1

# დაბეჭდეთ 1500-დან 2100-ის ჩათვლით რიცხვები, რომლებიც არიან 7-ის
# და 5-ის ჯერადი ერთდროულად.

# for i in range(1500,2100):
#     if i%5==0 and i%7==0:
#         print(i)

# • დაითვალეთ 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც
# არიან 7-ის და 5-ის ჯერადი ერთდროულად. როგორც კი რიცხვების
# ჯამი გადააჭარბებს 20 000-ს, შეწყვიტეთ ციკლი. დაბეჭდეთ მიღებული
# ჯამი ეკრანზე.


# jami=0
# for i in range(1500,2100):
#     if i%5==0 and i%7==0:
#         jami+=i
#     if jami>20000:
#         break
# print(jami)
    
# დაითვალეთ 1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი და
# დაბეჭდეთ შედეგი.

# jami=0
# for i in range(2,101):
#    if i%2==0:
#        jami+=i
# print(jami)

# • შეიყვანეთ რიცხვი. დაითვალეთ ამ რიცხვის ფაქტორიალი და
# დაბეჭდეთ. მაგ. 5-ის ფაქტორიალი იგივია რაც 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5


# x=9
# faqtriali = 1
# x+=1
# for i in range(1,x):
#     faqtriali *= i

# print(faqtriali)



# შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის
# უმცირესი საერთო ჯერადი.

# x=9
# y=19
# i=1
# while True:
#     if i%x==0 and i%y==0:
#         print(i)
#         break
#     i+=1    


# • დაბეჭდეთ 2-დან 1000-მდე ყველა მარტივი რიცხვი. 

for x in range(2, 1001): 
    for i in range(2,x):
        if x % i == 0:  
            break
    else:
        print(x) 


# • შეიყვანეთ ნებისმიერი რიცხვი. იპოვეთ ამ რიცხვის ციფრთა ჯამი და
# დაბეჭდეთ.

# • დაწერეთ პროგრამა რომელიც ეკრანზე გამოიტანს შემდეგ
# გამოსახულებებს. 
# 1)
# for i in range(1,6):
#     for _ in range(i):
#         print("*",end="  ")
#     print()
    
# for i in range(4,1,-1):
#     for _ in range(i):
#         print("*", end="  ")
#     print()

# 2)

