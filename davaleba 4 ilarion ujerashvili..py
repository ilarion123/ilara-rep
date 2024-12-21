#მეგობრებო, ქვემოთ კომენტარის სახედ მოცემულია დავალების პირობები. ყოველი ამოცანის ქვეშ დაწერეთ თქვენი პასუხი. პითონ ფაილის ჩამოტვირთვისას დააწერეთ davaleba 4 - elena bliadze.py 
# ოღონდ elena bliadze -ს ნაცვლად თქვენი სახელი და გვარი. გისურვებთ წარმატებას ! ასევე გაითვალისწინეთ მოცემული დავალება ფოლდერით უნდა ატვირთოთ გითჰაბზე და ლინკი კომენტარში დაურთოთ თქვენს მიერ ატვირთულ დავალებას.
#გისურვებთ წარმატებას!

# დაწერე (ჩაფასთე მარჯვნივ(გასწვრივ)) გითჰაბის ლინკი, სადაც ატვირთე შენი ფაილი: 

#Tuples : 

#1. დაწერე პროგრამა , რომელიც დაითვლის მოცემული tupex = ((), (), ('',), 'a', 'b', ('a', 'b', 'c'), ('d'),1,2,3,4) სიგრძეს.

# tupex = ((), (), ('',), 'a', 'b', ('a', 'b', 'c'), ('d'), 1, 2, 3, 4)
# x=len(tupex)
# print(x)


#2. დაწერე პროგრამა, რომელიც დაასორტირებს ტაპლში არსებულ ელემენტებს ინტეჯერების მიხედვით data = [('item1', '12'), ('item2', '15'), ('item3', '24')]

# data = [('item1', '12'), ('item2', '15'), ('item3', '24')]
# for i in range(len(data)):
#     for j in range(i+1,len(data)):
#         if data[j][1]<data[i][1]:
#             temp=data[j]
#             data[j]=data[i]
#             data[i]=temp
# print(data)
        

#3. შექმენი სასურველი თაფლი, რომელშიც ჩაყრი სიტყვიერ მონაცემებს და შემდეგ დაალაგებ ანბანურად და ანბანურად დალაგების შემდგომმა უკუღმა.


# arr=("vashli","msxali","atami","banani")
# sortt=sorted(arr)
# ukugma=sortt[::-1]
# print(sortt)
# print(ukugma)

#4. გაახუთმაქ თაფლში არსებული ელემენტები, ელემენტები შენით მოიფიქრე.

# arr=("axaliweli",100,"nadzvisxe")
# print(arr*5)

#Set - ები:
#5. შექმენით სიმრავლე შემდეგი ელემენტებით : 0, 1, 2, 3, 4. დაამატეთ ნებისმიერ 3 ელემენტი სურვილისამებრ. 
# წაშალეთ ორი ელემენტი სიმრავლიდან. დაბეჭდეთ სიმრავლის ელემენტები ცალ ცალკე ხაზზე (გამოიყენეთ for ციკლი). 
# დაითვალეთ სიმრავლის ელემენტების რაოდენობა.

# simravle={0,1,2,3,4}
# damateba=[5,6,7]
# for i in damateba:
#     simravle.add(i)
# simravle.discard(3)
# simravle.discard(6)
# for i in simravle:
#     print(i)
# simravlis_raodenoba=len(simravle)
# print("elementebis raodenoba",simravlis_raodenoba)

#6. შექმენით ორი სიმრავლე: set1 სიმრავლე ელემენტებით "green”, "blue”; set2 სიმრავლე ელემენტებით
# "blue", "yellow”. იპოვეთ ამ ორი სიმრავლის გაერთიანება, თანაკვეთა, სხვაობა და სიმეტრიული
# სხვაობა (შეასრულეთ დავალება ორი გზით: არსებული მეთოდით (ფუნქციით) და შესაბამისი
# ოპერატორით.)

#funqciit

# set1={"green","blue"}
# set2={"blue","yellow"}
# gaertianeba=set1.union(set2)
# tanakveta=set1.intersection(set2)
# sxvaoba=set1.difference(set2)
# simetriuli_sxvaoba=set1.symmetric_difference(set2)
# print("gaertianeba:",gaertianeba)
# print("tanakveta:",tanakveta)
# print("sxvaoba:",sxvaoba)
# print("simetriuli_sxvaoba:",simetriuli_sxvaoba)

#operatorit

# set1={"green","blue"}
# set2={"blue","yellow"}
# union=set1|set2
# intersection=set1&set2
# difference=set1-set2
# symmetric_difference=set1^set2
# print(union)
# print(intersection)
# print(difference)
# print(symmetric_difference)




#7. დაწერეთ პროგრამა რომელიც იპოვის სიმრავლეში მაქსიმალურ და მინიმალურ მნიშვნელობას და დაბეჭდეთ შედეგი (სიმრავლე შეარჩიეთ სურვილისამებრ).

# arr={34,78,12,56,90,23,45}
# maqsimaluri=max(arr)
# minimaluri=min(arr)
# print(maqsimaluri)
# print(minimaluri)


#8. შექმენით 2 სეტი, დაარქვით სასურველი სახელები და შეასრულეთ ნასწავლი მასალიდან 5 მეთოდის მაგალითი.

# set1={1,2,3,4,5}
# set2={3,4,5}
# interseqcia=set1.intersection(set2)
# issubset=set1.issubset(set2)
# issupersett=set1.issuperset(set2)
# isdisjointt=set1.isdisjoint(set2)
# print(set1.difference_update(set2))
# print(interseqcia)
# print(issubset)
# print(issupersett)
# print(isdisjointt)

#9.მომხარებელს შეაყვანინეთ 2 სიტყვა. დაბეჭდეთ ამ ორი სიტყვის ყველა საერთო ასო.


# x=input("sheiyvane sityva1:")
# y=input("sheiyvane sityva2:")
# saerto=[]
# for i in x:
#     if i in y:
#         saerto.append(i)
# print(saerto)

