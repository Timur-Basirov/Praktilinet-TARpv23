# from math import e
# from string import *
# #1
# glas= ["а","e","u","y","o","i","ü","õ","ä"]
# sogl= ["z","x","c","v","b","n","m","s","d","f","g","h","j","k","l","q","w","r","t","p","š"]
# markid=punctuation
# v=k=m=t=0
# tekst=input("Sisesta sõna või lause: ").lower() #ABCD -> abcd
# tekst_list=list(tekst) #["a","b","c","d","!"]
# for sümbol in tekst_list:
#     if sümbol in glas:
#         v+=1
#     elif sümbol in sogl:
#         k+=1
#     elif sümbol in markid:
#         m+=1
#     elif sümbol==" ":
#         t+=1
# print("Vokaal: ",v)
# print("Konsonanti; ",k)
# print("Kirjuvahemärgid:",m)
# print("Tühikud:",t)

# #2
# nimed=[]
# for i in range (5):
#     nimi=input("Sisesta nimi: ").capitalize()
#     nimed.append(nimi)

# print("Loetelu: ",nimed)
# nimed.sort()
# print("Loetelu sorteeritud: ",nimed)
# for n in range(len(nimed)): #len tipo sam opredeljaet range
#     print(n+1,".",nimed[n],sep="") #sep= chtobi ne bilo probelov
# print("Vimasena oli lisatud: ",nimi)
# uued_nimed=[]
# for nimi in nimed:
#     if nimi not in uued_nimed:
#         uued_nimed.append(nimi)
# print(uued_nimed)

# uued_nimed=list(set(nimed))

# ages=[]
# for i in range(5):
#     age=int(input("Sisesta vanus: "))
#     ages.append(age) #mi dobavljaem znachenie age v ages
# minage=min(ages)
# maxage=max(ages)
# averageage =sum(ages)/len(ages)
# print("Noorim vanus:",min(ages),"\nKõrgeim vanus:",max(ages),"\nKeskmine vanus:",sum(ages)/len(ages))
# #Kuva ekraanile nimi koos vanusega
# for i in range(5):
#     print(nimed[i],"on ", ages[i],"aastat vana")

# from random import *
# arvud=[]
# N=int(input("Mitu rida joonistame? "))
# S=input("Sisesta sümbol: ")
# #loendi täitmine
# for i in range(N):
#     arvud.append(randint(1,100))
# #diagrammi loomine
# for i in range(N):
#     print(arvud[i]*S)
    
# Linnad=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
# while True:
#     while True:
#         try:
#             indeks=int(input("Sisesta oma indeks: "))
#             indekselement=len(str(indeks))
#             if indekselement==5:
#                 print("Numbriline indeks ")
#                 break
#             else:
#                 print("Elementide arv peab olema 5")
            
#         except:
#             print("Vale andmetüüp!")
#     arv1=indeks//10000
#     print(arv1)
#     symbolid=list(str(indeks))
#     sym1=symbolid[0]
#     print(f"Sa elad piirkonnas {Linnad[arv1-1]}")
    
#Напишите программу, которая меняет местами первый и последний элементы. (второй и предпоследний и т.д.). Количество меняемых местами элементов надо спросить у пользователя. В исходном списке минимум 2 элемента.
# from random import *
# from string import *
# rida=[]
# N=randint(2,25)
# for i in range(N):
#     rida.append(choise(ascii_uppercase))
# print(rida)
# kogus=int(input("Mitu elemendi vahetame oma vahel "))
# if len(rida)//2>=kogus:
#     for i in range(kodus):
#         a=rida[i]
#         rida[i]=rida[len(rida)-i-1]
#         rida[len(rida)-1-i]=a 
# print(rida)

# arv=[]
# for i in range(5):
#     arvik=int(input("Sisetage Arv: "))
#     arv.append(arvik)
# print(arv)
# a=max(arv)
# print(f"Bolshee chislo: {a}")
# b=a/len(arv)

# from random import *
# nimekirja=[]
# n=int(input("Nimekirja suurus: "))
# for i in range(n):
#     arv=randint(10,100)
#     nimekirja.append(arv)
# print(nimekirja)
# maksimum=max(nimekirja)
# vajavarv=maksimum/len(nimekirja)
# nimekirja[nimekirja.index(maksimum)]=vajavarv
# print(nimekirja)

# #1v for
# lst = []
# v = int(input("Kui palju numbreid te nimekirjas soovite?"))
# for i in range(v):
#     v = int(input("Arv: "))
# lst.append(v)
# suur = 0
# for el in lst:
#     if el > suur:
#         suur = el
# lst[lst.index(suur)] = suur / ( len(lst) + 1 )
# print(f"suur {suur}, indeks on {lst.index(suur) + 1}\n{lst}")

# #11

# #2v sort
# lst = []
# v = int(input("Kui palju numbreid te nimekirjas soovite?"))
# for i in range(v):
#     v = int(input("Arv: "))
# lst.append(v)
# lst.sort()
# suur = lst[-1]

# lst[lst.index(suur)] = suur / ( len(lst) + 1 )
# print(f"suur {suur}, indeks on {lst.index(lst[-1]) + 1}\n{lst}")



# #1,#9
glas=["e", "y", "u", "i", "o", "ü", "õ", "a", "ö", "ä"]
soglas=[]
nimi=input("Sisestage nimi: ")
if nimi.isalpha():
    print("Tere!", nimi.capitalize())
else:
    print("Sisestage nimi, mitte sümbolid")
count=len(nimi)
glas4et=0
soglas4et=0
print("Kolichestvo bukv v imeni:",count)
kiri=list(nimi.lower())
for kiris in kiri:
    if kiris in glas:
        glas4et+=1
    else:
        soglas.append(kiris)
        soglas4et+=1
print("Kolichestvo:", count,"\nKolichestvo glasnih bukv:", glas4et,"\nKolichestvo soglasnih bukv:", soglas4et)
unique=sorted(set(kiri))
print("bukvi iz imeni v alfavitnom porjadke:", ''.join(unique))

#2 #12
from random import *
number=[]
for i in range(10):
    number.append(randint(1,100))
mins=number.index(min(number))
maxs=number.index(max(number))
number[mins],number[maxs]=number[maxs],number[mins]
print(number)

# #3 #15
arvud=[1,2,3,4,5,6,7,8,9]
eesti=["üks","kaks","kolm","neli","viis","kuus","seitse","kaheksa","üheksa"]
inglise=["one","two","three","four","five","six","seven","eight","nine"]
itaalia=["uno","due","tre","quattro","cinque","sei","sette","otto","nove"]
print("Arv / Eesti / Inglise / Itaalia")
for i in range(len(arvud)):
    print(f"{arvud[i]} / {eesti[i]} / {inglise[i]} / {itaalia[i]}")
    
# #4 #17
jarjend=["lahti","rekord","mõnus","tunnel","kõrvalt","kummaline"]
sona=input("Sisestage otsitav sõna: ")
for i in range(1):
    if sona in jarjend:
        print("Jaa, sisaldab sõna",jarjend)
    else:
        print("ei, pole sisaldab sõna")
        
#5 #14
linnad=["Берлин","Вена","Париж","Мадрид","Рим","Лондон","Амстердам","Осло","Лиссабон","Афины"]
linnad.sort()
print("Euroopa pealinnade praegune loetelu:")
for i in linnad:
    print(i)
for i in range(2):
    new_linn=input(f"Sisestage {i+1}. uue Euroopa pealinna nimi:")
    linnad.append(new_linn)
linnad.sort()
print("\nEuroopa pealinnade ajakohastatud tähestikuline loetelu:")
for i, linn in enumerate(linnad, 1):                    #при помощи индекса i и функции enumerate я делаю нумерованный список для вывода
    print(f"{i}. {linn}")
print(f"\nMeie järjekorras on {len(linnad)} Euroopa pealinnad.")
