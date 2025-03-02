#მეგობრებო, ქვემოთ კომენტარის სახედ მოცემულია დავალების პირობები. ყოველი ამოცანის ქვეშ დაწერეთ თქვენი პასუხი. პითონ ფაილის ჩამოტვირთვისას დააწერეთ davaleba 7 - elena bliadze.py 
# ოღონდ elena bliadze -ს ნაცვლად თქვენი სახელი და გვარი. გისურვებთ წარმატებას ! ასევე გაითვალისწინეთ მოცემული დავალება ფოლდერით უნდა ატვირთოთ გითჰაბზე და ლინკი კომენტარში დაურთოთ თქვენს მიერ ატვირთულ დავალებას.
#გისურვებთ წარმატებას!

# დაწერე (ჩაფასთე მარჯვნივ(გასწვრივ)) გითჰაბის ლინკი, სადაც ატვირთე შენი ფაილი:  


#1. მომხმარებლის რეგისტრაცია: შექმენი პროგრამა, რომელიც გაატარებს მოხმარებელს რეგისტრაციას დაგჭირდება ფუნქცია:
#register_user (username:str,password:str) , 1 - პარამეტრის სიგრძე მინიმუმ 3, 2 - პარამეტრის მინიმუ 5  წარმატებული რეგისტრაციის გავლის შემთხვევაში დააბრუნოს 
#შესაბამისი მესიჯი. (შენიშვნა: ფუნქციის გამოძახებისას შენ ჩააწოდე ორივე პარამეტრის მნიშვნელობა და არ გამოიყენო input())

# def register_user(username:str,password:str):
#     if len(username)<3:
#         return "momxmareblis saxeli unda iyos minimum 3 simbolo"
#     if len(password)<5:
#         return "paroli unda iyos minimum 5 simbolo"
#     return "registracia warmatebit ganxorcielda"
# print(register_user("baideni","12345"))
# print(register_user("mai","1234"))

#2. კალკულალტორი: შექმენი პროგრამა, რომელიც იქნება მინი კალკულატორი , შემდეგი ოპერატორებისთვის +,-,*,/ :
#ფუნქციის დასახელება calculate(a,b,oper). ფუნქციას, როდესაც შესამოწმებელ რიცხვებს ჩააწოდებთ, ასევე შესაბამისი მესიჯი გამოჰქონდეს.

# def kalkulatori(x,y,operacia):
#     if operacia=="+":
#         result=x+y
#         return result
#     elif operacia=="-":
#         result=x-y
#         return result
#     elif operacia=="*":
#         result=x*y
#         return result
#     elif operacia=="/":
#         if y==0:
#             return "nulze gayofa ar sheileba"
#         else:
#             result=x/y
#             return result
#     else:
#         return "archeuligaq araswori operacia"
# print(kalkulatori(10,2,"+"))
# print(kalkulatori(10,2,"-"))
# print(kalkulatori(10,2,"*"))
# print(kalkulatori(10,2,"/"))

#3.გრადუსის კონვერტაცია: შექმენი ფუნქცია, რომელიც გადაგვიყვანს ჩაწოდებულ რიცხვს ფარენჰეითში ცელსიუსის შემთხვევაში და ფარენჰეითის ცელსიუსში :
#ფორმულები : (ცელსიუსი* 9/5) +32, (ფარენჰეითი-32)* (5/9) 

# def farenheitshi_gadayvana(celsiusi):
#     return (celsiusi*9/5)+32
# def celsiusshi_gadayvana(farenheiti):
#     return (farenheiti-32)*(5/9)
# print(farenheitshi_gadayvana(20))
# print(celsiusshi_gadayvana(50))

#4. ფაილის წაკითხვა: შექმენი ფუნქცია, რომელიც წაიკითხავს შენს ფაილს და წაიკითხავს შიგთავსს.
#შენიშვნა ფაილიც სავალდებულოა მოყვეს დავალება, ანუ აგდებთ მოცემულ და txt ფაილებს ფოლდერში.

# def faili(filename,teqsti):
#     with open(filename,"w",encoding="utf-8") as file:
#         file.write(teqsti)
#     with open(filename,"r",encoding="utf-8") as file:
#         return file.read()
# print(faili("example.txt","teqsti romelsac waikitxavs"))

#5. შეაჯამე ფუნქცია არგსის გამოყენებით,შემდეგი მნიშვნელობები:(100.50, 200.75, 50.25)

# def shejameba(*args):
#     return sum(args)
# jami=shejameba(100.50, 200.75, 50.25)
# print(jami)

#6. დაითვალე , მოცემული სიტყვების სიგრძე: ("Workout", "Grocery shopping", "Read", "Cook dinner")

# def func(sityvebi):
#     sigrdze=[]
#     for i in sityvebi:
#         sigrdze.append(len(i))
#     return sigrdze
# print(func(("Workout", "Grocery shopping", "Read", "Cook dinner")))

#7. მოიფიქრე ფუნქცია სადაც გამოიყენებ **kwargs

# def my_func(**kwargs):
#     print(kwargs)
# my_func(name="ilarioni",gvari="ujerashvili",asaki=15)
# my_func(x=1,y=2,z=3)

#8. გამოითვალე რიცხვების საშუალო მოცემული რიცხვებისთვის: [10, 20, 30, 40]

# def average(nums):
#     return sum(nums)/len(nums)
# print(average([10,20,30,40]))

#9.შექმენი ფუნქცია რომელიც ამოიღებს დუბლიკატებს (მსგავსებს): [1, 2, 2, 3, 4, 4, 5]

# def func(listt):
#     dublikatebi=[]
#     for i in listt:
#         if i not in dublikatebi:
#             dublikatebi.append(i)
#     return dublikatebi
# print(func([1, 2, 2, 3, 4, 4, 5]))

#10. შექმენი შენი საკუთარი მოდული და ნაცნობი მოდულების გამოყენებით, შექმენი შენთვის სასურველი პრპოგრამა.

# from moduli import *
# amorcheva=randomuli_ricxvi(1,100)
# print(amorcheva)
# a=3
# b=4
# c=pitagora(a,b)
# print(c)
