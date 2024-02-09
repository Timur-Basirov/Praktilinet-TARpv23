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

#2
nimed=[]
for i in range (5):
    nimi=input("Sisesta nimi: ").capitalize()
    nimed.append(nimi)

print("Loetelu: ",nimed)
nimed.sort()
print("Loetelu sorteeritud: ",nimed)
for n in range(len(nimed)): #len tipo sam opredeljaet range
    print(n+1,".",nimed[n],sep="") #sep= chtobi ne bilo probelov
print("Vimasena oli lisatud: ",nimi)
uued_nimed=[]
for nimi in nimed:
    if nimi not in uued_nimed:
        uued_nimed.append(nimi)
print(uued_nimed)

uued_nimed=list(set(nimed))

