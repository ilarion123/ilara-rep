#მეგობრებო, ქვემოთ კომენტარის სახედ მოცემულია დავალების პირობები. ყოველი ამოცანის ქვეშ დაწერეთ თქვენი პასუხი. პითონ ფაილის ჩამოტვირთვისას დააწერეთ davaleba 8 - elena bliadze.py 
# ოღონდ elena bliadze -ს ნაცვლად თქვენი სახელი და გვარი. გისურვებთ წარმატებას ! ასევე გაითვალისწინეთ მოცემული დავალება ფოლდერით უნდა ატვირთოთ გითჰაბზე და ლინკი კომენტარში დაურთოთ თქვენს მიერ ატვირთულ დავალებას.
#გისურვებთ წარმატებას!

# დაწერე (ჩაფასთე მარჯვნივ(გასწვრივ)) გითჰაბის ლინკი, სადაც ატვირთე შენი ფაილი:  

#1. შექმენი კლასი car გაუკეთე 2 დეფაულტ ატრიბუტი , დაუმატე 2 მეთოდი, str და len. ასევე დინამიურად 2 შენს მიერ მოფიქრებული ატრბუტი.
# საბოლოოდ გამოჰქონდეს შესაბამისი მესიჯი.

# class Car:
#     def __init__(self,marka,modeli):
#         self.marka=marka
#         self.modeli=modeli
#     def __str__(self):
#         return f"es manqanaa {self.marka} {self.modeli},{self.weli}wliani da aris {self.feri}"
#     def __len__(self):
#         return len(self.marka)+len(self.modeli)
# car=Car("BMW","m5")
# setattr(car,"feri","tetri")
# setattr(car,"weli","2015")
# print(car.__str__())
# print(car.__len__())

#2. დააიმპორტე მათემატიკის მოდული და იპოვე პოლიმორფიულდ ფართობები შემდეგი ფიგურებისთვის: წრე, კვადრატი, მართკუთხედი.
#გამოიტანე ყველას ფართობი, შესაბამისი მესიჯებით.

# import math
# class figura:
#     def fartobi(self):
#         pass
# class wre(figura):
#     def __init__(self,radiusi):
#         self.radiusi=radiusi
#     def fartobi(self):
#         return math.pi*(self.radiusi**2)
# class kvadrati(figura):
#     def __init__(self,gverdi):
#         self.gverdi=gverdi
#     def fartobi(self):
#         return self.gverdi**2
# class martkutxedi(figura):
#     def __init__(self,sigane,sigrdze):
#         self.sigane=sigane
#         self.sigrdze=sigrdze
#     def fartobi(self):
#         return self.sigrdze*self.sigane
# wre1=wre(15)
# kvadrati1=kvadrati(15)
# martkutxedi1=martkutxedi(15,15)
# print(wre1.fartobi())
# print(kvadrati1.fartobi())
# print(martkutxedi1.fartobi())

#3. შექმენ პერსონ აიდის კლასი, სადაც დაახასიათებ სახელით, ასაკით , სქესით და ინფო მეთოდის მეშვეობით გამოიტან მომხმარებელზე ინფოს.

# class PersonID:
#     def __init__(self,saxeli,asaki,sqesi):
#         self.saxeli=saxeli
#         self.asaki=asaki
#         self.sqesi=sqesi
#     def info(self):
#         return f"momxmareblis saxelia {self.saxeli},asakia{self.asaki} da sqesia {self.sqesi}"
# PersonID1=PersonID("lado",20,"mamrobiti")
# print(PersonID1.info())

#4. შექმენი მშობელი კლასი გუნდი და შვილობილლი ფეხბურთისგუნდი, შექმენით Team კლასი, რომელსაც აქვს ფეხბურთელების სია. შექმენით FootballTeam კლასი, რომელიც მემკვიდრეობას იღებს Team კლასიდან.
#შექმენით Team კლასი, რომელსაც აქვს ფეხბურთელების სია. შექმენით FootballTeam კლასი, რომელიც მემკვიდრეობას იღებს Team კლასიდან. გამოიყენე super() ფუნქციაც.
#განავრცე შენით, ეს მხოლოდ დასახმარებლად არის და ბევრი რამ აკლია:

# class Team:
#     def __init__(self,name):
#         self.name = name
#         self.players = []
#     def damateba(self,player):
#         self.players.append(player)
# class FootballTeam(Team):
#     def __init__(self,name,mwvrtneli):
#         super().__init__(name)
#         self.mwvrtneli=mwvrtneli
#     def damateba(self,motamashe,pozicia):
#         self.players.append(f"{motamashe} {pozicia}") 
#     def info(self):
#         return f"Team name is:{gundi.name},Coach is:{gundi.mwvrtneli},players:{gundi.players}"
# gundi=FootballTeam("Barcelona","Hansi Flick")
# gundi.damateba("Raphinha","forward")
# gundi.damateba("Lamine Yamal","forward")
# gundi.damateba("Pedri gonzalez","Midfielder")
# print(gundi.info())

#5. მოიფიქრე და შექმენი წიგნების მართვის სისტემა. (ყოველივე მოიფიქრე შენით, შეგიძლია გამოიყენო 2 კლასი/ნებისმიერი მეთოდებით.)
#განავრცე შენით, ეს მხოლოდ დასახმარებლად არის და ბევრი რამ აკლია:

# class Book:
#     def __init__(self,satauri,avtori):
#         self.satauri=satauri
#         self.avtori=avtori
#     def info(self):
#         return f"wignis satauria:{self.satauri},avtoria:{self.avtori}"
# class wignis_sacavi:
#     def __init__(self):
#         self.wignebi=[]
#     def wignisdamateba(self,book):
#         self.wignebi.append(book)
#     def info(self):
#         listt=[]
#         for i in self.wignebi:
#             listt.append(i.info())
#         return f"sacavshia wignebi: {listt}"
# wigni1=Book("vefxistyaosani","Shota rustaveli")
# wigni2=Book("karlsoni","Astrid lindgreni")
# wignis_sacavi1=wignis_sacavi()
# wignis_sacavi1.wignisdamateba(wigni1)
# wignis_sacavi1.wignisdamateba(wigni2)
# print(wigni1.info())
# print(wigni2.info())
# print(wignis_sacavi1.info())

#6. მოხმარებელთა მართვის სისტემა: შექმენით User კლასი, რომელიც მოიცავს სახელს, ასაკს და ელ.ფოსტას.
# დაამატეთ Admin კლასი, რომელიც მემკვიდრეობს User კლასიდან და აქვს მეთოდად დამატებითი უფლებები.
#განავრცე შენით, ეს მხოლოდ დასახმარებლად არის და ბევრი რამ აკლია:

# class User:
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.friends=[]
#     def info(self):
#         return f"momxmareblis saxelia {self.name},asaki {self.age},xolo emaili {self.email}"
#     def damateba(self,megobris_emaili):
#         if megobris_emaili not in self.friends:
#             self.friends.append(megobris_emaili)
#             print(f"{megobris_emaili} daemata megobrebshi")
#     def megobrebi(self):
#         if self.friends:
#             print(f"{self.name}-s megobari aris {self.friends}")
#         else:
#             print(f"{self.name} ar yavs megobrebi")
# class Admin(User):
#     def __init__(self,name,age,email):
#         super().__init__(name,age,email)
# momxmarebeli=User("luka",15,"luka15@gmail.com")
# print(momxmarebeli.info())
# momxmarebeli.damateba("giorgi16@gmail.com")
# momxmarebeli.megobrebi()
# admini=Admin("nika",16,"nika15@gmail.com")
# admini.damateba("giorgi16@gmail.com")
# admini.megobrebi()

#7. შექმენი სოც.ქსელის პლატფორმის მართვის სისტემა: კლასი მომხმარებლით დაახასიათე მომხარებელი, და ერთი ატრიბუტი წარმოადგენდეს ლისტს:
# შემდეგნაირად:
# შექმენი მეგობრის დამატების მეთოდი მოცემულ კლასსში. დაამატე კლასი SocialMediaUser. წამოიღე მომკვიდრეობითი ატრიბუტები და დაამატე ერთი ატრიბური. გამოიტანე შესაბამისი შედეგი.

# class User:
#     def __init__(self, name, age, sqesi):
#         self.name = name
#         self.age = age
#         self.sqesi=sqesi
#         self.friends = []
#     def megobris_damateba(self,friend):
#         if friend in self.friends:
#             print("megobari ukve damatebuli gyavs")
#         else:
#             self.friends.append(friend)
#             print(f"{friend.name} daemata megobrebshi")
# class SocialMediaUser(User):
#     def __init__(self,name,age,sqesi,username):
#         super().__init__(name,age,sqesi)
#         self.username=username
#     def info(self):
#         return f"momxmarebis saxelia {self.name},gvari {self.username},asaki:{self.age},sqesi {self.sqesi}"
# momxmarebeli1=SocialMediaUser("Daviti",20,"mamrobiti","Trumpi")
# momxmarebeli2=SocialMediaUser("Mariami",20,"mdedrobiti","zelenski")
# momxmarebeli1.megobris_damateba(momxmarebeli2)
# print(momxmarebeli1.info())

#8. შექმენი ბანკის ანგრიშების მართვის სისტემა:
# შექმენით BankAccount კლასი, რომელიც მოიცავს ანგარიშის ნომერს, ბალანსსა და დეპოზიტების/ამოღებების მეთოდებს. 
# ბალანსი უნდა იყოს private და უნდა შესაბამისი მეთოდებით უნდა შეგვეძლოს ანგარიშის გამოტანა, და მისი შეცვლა.

# class BankAccount:
#     def __init__(self, account_number):
#         self.__account_number = account_number  
#         self.__balance = 0  
#     def depositi(self,raodenoba):
#         if raodenoba>0:
#             self.__balance+=raodenoba
#             print(f"depoziti {raodenoba} {self.__account_number} angarishze")
#         else:
#             print("tanxa unda iyos dadebiti")
#     def amogeba(self,raodenoba):
#         if 0 <raodenoba<=self.__balance:
#             self.__balance-=raodenoba
#             print(f"amogeba {raodenoba} {self.__account_number} angarishidan")
#         else:
#             print("arasakmarisi balansi an araswori tanxa")
#     def balansi(self):
#         return self.__balance
#     def angarishis_nomeri(self):
#         return self.__account_number
# account=BankAccount("GE1867649864898")
# account.depositi(1000)
# print("balansi",account.balansi())
# account.amogeba(500)
# print("balansi",account.balansi())
# account.amogeba(600)




#9. მოიფიქრე ოოპ-ის გამოყენების მაგალითი.

# class Animal:
#     def __init__(self,name,sound):
#         self.name=name
#         self.sound=sound
# class Cat(Animal):
#     def __init__(self,name,sound):
#         super().__init__(name,sound)
#     def info(self):
#         return f"katis saxelia {cat.name} da gamoscems {cat.sound} xmas"
# class Dog(Animal):
#     def __init__(self,name,sound):
#         super().__init__(name,sound)
#     def info(self):
#         return f"dzaglis saxelia {dog.name} da gamoscems {dog.sound} xmas"
# cat=Cat("Oscar","MEOW")
# dog=Dog("Jeka","WOOf")
# print(cat.info())
# print(dog.info())

#10. მოიფიქრე და დაახასიათე ნებისმიერი ობიექტი ოოპის მემკვიდრეობის მეშვოებით. გამოიყენე იერარქიული მემკვიდრეობა.

# class figura:
#     def __init__(self,feri):
#         self.feri=feri
#     def area(self):
#         pass
# class Circle(figura):
#     def __init__(self,feri,radiusi):
#         super().__init__(feri)
#         self.radiusi=radiusi
#     def area(self):
#         return 3.14*self.radiusi**2
# class kvadrati(figura):
#     def __init__(self,feri,gverdis_sigrdze):
#         super().__init__(feri)
#         self.gverdis_sigrdze=gverdis_sigrdze
#     def area(self):
#         return self.gverdis_sigrdze**2
# circle=Circle("witeli",5)
# kvadrati1=kvadrati("lurji",5)
# print(circle.area()) 
# print(kvadrati1.area()) 
