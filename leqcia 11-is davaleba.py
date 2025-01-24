#1)• დაწერეთ პროგრამა რომლის მეშვებით შეიტანთ ნებისმიერ სტრიქონს (input ბრძანების
# გამოყენებით). დაბეჭდეთ შეყვანილი სტრიქონის სიგრძე (სიმბოლოების რაოდენობა).

# striqoni=input("sheitane striqoni:")
# print(len(striqoni))

#2)• შეიყვანეთ ნებისმიერი ორი სტრიქონი. ახალ ცვლადში მოახდინეთ მათი შეერთება და დაბეჭდეთ
# შედეგი.

# striqoni1=input("sheiyvane striqoni1:")
# striqoni2=input("sheiyvne striqoni2:")
# sheerteba=striqoni1+striqoni2
# print(sheerteba)

#3)•შეიყვანეთ სტრიქონი. გადაიყვანეთ სტრიქონის ყველა სიმბოლო მაღალ რეგისტრში და დაბეჭდეთ
# შედეგი.

# striqoni=input("sheiyvane striqoni:")
# magali=striqoni.upper()
# print(magali)

#4)• text ცვლადს მიანიჭეთ სტრიქონი “სწავლის ძირი მწარე არის, კენწეროში გატკბილდების”.
# სტრიქონიდან წაიკითხეთ პირველი 20 სიმბოლო და დაბეჭდეთ შედეგი. დაითვალეთ რამდენჯერ
# არის ნახსენები სიმბოლო ‘ს’.

# text="სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
# pirveli_20_simbolo=text[:20]
# raodenoba=text.count('ს')
# print(pirveli_20_simbolo)
# print(raodenoba)

#5)შეიყვანეთ სტრიქონი. პატარა ლატინური ასოები შეცვალეთ დიდი ლათინური ასოებით, ხოლო
# დიდი-პატარათი და გამოიტანეთ შედეგი.

# text=input("შsheiyvane striqoni:")
# didi_asoebi=text.upper()
# print(didi_asoebi)
# patara_asoebi=text.lower()
# print(patara_asoebi)

#6)• დაწერეთ პროგრამა, რომელშიც მომხარებელს შეაყვანინებთ რაიმე სტრიქონს. პროგრამამ უნდა
# დაითვალოს დიდი ლათინური ასოების, პატარა ლათინური ასოების და ციფრების რაოდენობა
# ცალ-ცალკე და დაბეჭდეთ მიღებული შედეგები. ასევე დაითვალეთ სტრიქონში გამოყენებული
# სპეციალური სიმბოლოების რაოდენობა როგორიცაა !@#$%^&*()_+ 

# text=input("sheiyvane striqoni:")
# didi_asoebi=0
# patara_asoebi=0
# cifrebi=0
# specialuri_simbolo=0
# for i in text:
#     if i.isupper():
#         didi_asoebi+=1
#     elif i.islower():
#         patara_asoebi+=1
#     elif i.isdigit():
#         cifrebi+=1
#     else:
#         specialuri_simbolo+=1
# print(didi_asoebi)
# print(patara_asoebi)
# print(cifrebi)
# print(specialuri_simbolo)
