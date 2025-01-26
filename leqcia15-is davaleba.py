# დაწერეთ ფუნქცია, რომელიც შეამოწმებს პარამეტრად გადაცემული რიცხვი არის თუ არა კენტი.
# თუ კენტია, დააბრუნოს მნიშვნელობა True, თუ არადა - False. შეამოწმეთ რამდენიმე
# რიცხვისთვის და დაბეჭდეთ შედეგი.

# def kenti(x):
#     if x%2!=0:
#         return True
#     else:
#         return False
# print(kenti(1))
# print(kenti(2))

# დაწერეთ ფუნქცია, რომელიც დაითვლის (დააბრუნებს) პარამეტრად გადაცემული რიცხვის
# ფაქტორიალს და დაბეჭდეთ შედეგი სხვადასხვა რიცხვებისთვის. (რეკურსიით)

# def factorial(x):
#     if x==0 or x==1:
#         return 1
#     else:
#         return x * factorial(x - 1)
# ricxvebi=[5,7,10,3]
# for i in ricxvebi:
#     print(factorial(i))

# დაწერეთ უპარამეტრო ფუნქცია რომელიც ეკრანზე ბეჭდავს შემდეგ ტექსტს: “Hello
# World”.(გაითვალისწინეთ რომ ფუნქცია არ აბრუნებს მნიშვნელობას).

# def hello_world():
#     print("Hello World")
# hello_world()

# დაწერეთ ანონიმური ფუნქცია რომელიც დაითვლის რიცხვის კუბს.

# kubi=lambda x:x**3
# print(kubi(2))

# • მოიფიქრე და დაწერე *args და **kwarg-ის მაგალითები

# def my_func(*args):
#     return sum(args)
# print(my_func(98,89,27))


# def my_func1(**kwargs):
#     print(kwargs)
# my_func1(saxeli="ilarioni",asaki=15,qalaqi="tbilisi")

# მოიფიქრე დეკორატორების მაგალითი

# def decorator(func):
#     def wrapper():
#         print("gamarjoba!")
#         func()
#     return wrapper
# @decorator
# def say_hello():
#     print("rogor xar?")
# say_hello()
