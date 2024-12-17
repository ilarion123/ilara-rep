#1) შექმენი ტაპლი, სახელად tup. ჩაყარე შენთვის ნაცნობი მონაცემთა ტიპები. დაბეჭდე.

# tup=(465,46.5,"tuple",True,False,{1,2,3})
# print(tup)

#2) შექმენი რიცხვითი მონაცემებით სავსე ტაპლი და გამოიტანე ერთი მონაცემი ინდექსის
#მეშვეობით.

# tup=(1,2,3,4,5,6.5,6.7,3.6)
# print(tup[7])

#3) გააკეთე ნესთედ თაფლი და დაბეჭდე ინდექსის მეშვეობით შიგთავსი.

# tup=(10,1,("tapli","listi","modulebi"),7)
# print(tup[::])

#4) სიტყვა Python -ის ასოები, დამარცვლულად მოათავსე თაფლში და გააკეთე ისე რომ,
#მეთოდის მეშვეობით გამოიტანოს ტერმინალმა Python -ი.

# tup=("p","y","t","h","o","n")
# py=""
# pyt=py.join(tup)
# print(pyt)

#5) ტაპლში შეინახე სიტყვა Python დამარცვლულად და შეამოწმე p და s თუ არის შეიგნით.

# print("p" in ("python"))
# print("s" in ("python"))

#6)დაასორტირეთ ფლოატ ელემენტის მიხედვით მოცემული დატა:
#Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20’)]


#7) გამოთვლაეთ საშუალო მოცემული ტაპლისთვის:
#Tupleexmp = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))

# Tupleexmp=((10, 10, 10, 12),(30, 45, 56, 45),(81, 80, 39, 32),(1, 2, 3, 4))
# sashualo1=[sum(i)/len(i) for i in Tupleexmp]
# sashualo=sum(sashualo1)/len(sashualo1)
# print(sashualo)

#8)შექმენი lisset ლისტი და გადააქციე სეტად.

# lisset=[1,2,3,4,5,6,7]
# print(set(lisset))

#9)გაქვს ორი სეტი seta, green & blue მონაცემით და seta, blue& yellow მონაცემით. გააკეთე
# ინტერსექცია.

# a={"seta","green","blue"}
# b={"seta","blue","yellow"}
# c=a.intersection(b)
# print(c)

#10)მოიფიქრე ორი სეთი და გააერთიანე მათი მნიშვნელობები

# set1={"BMW","mercedes","rolls royce"}
# set2={"range rover","ferrari","velosipedi"}
# gaertianeba=set1.union(set2)
# print(gaertianeba)

#11)შენს მიერ შექმნილ სეთებიდან გამოიტან განსხვავებული მნიშვნელობები მხოლოდ.

# set1={"BMW","mercedes","rolls royce"}
# set2={"range rover","ferrari","BMW"}
# gansxvaveba=set1.difference(set2)
# print(gansxvaveba)

#12)ასევე გამოიყენე მეთოდი symmetric difference.

# set1={"BMW","mercedes","rolls royce","ford"}
# set2={"range rover","ferrari","BMW","nissan"}
# gansxvaveba=set1.symmetric_difference(set2)
# print(gansxvaveba)

#13)setx = set(["apple", "mango"]) sety = set(["mango", "orange"]) setz = set(["mango"]) შეამოწმე
# ქვესიმრავლეობაზე.

# setx=set(["apple", "mango"]) 
# sety=set(["mango", "orange"])
# setz=set(["mango", "orange"])
# qvesimravle=setx.issubset(sety)
# qvesimravle1=setz.issubset(sety)
# print(qvesimravle,qvesimravle1)

#14)დაწერე პროგრამა, რომელიც ამოიღებს სრულად შენს მიერ შექმნილი სეტიდან ყველა
# ელემენტს.

# sett={1,2,3,4,5,6,7,8,9,10}
# sett.clear()
# print(sett)