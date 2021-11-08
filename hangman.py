word=(input("Kelimeyi giriniz: "))
char=[]
char2=[]
char3=[]
count=0
ctrl=0
life=10
for i in word:
    if i == " ":
        char2.append("/")
    else:
        char2.append("_")
    char.append(i)
    count+=1
char3=char
correct="".join(char3)
def taking_letter():
    global ctrl
    global life
    letter=input("Harf giriniz: ")
    if letter in char:
        while ctrl!=count:
            if letter not in char:
                break
            found_index=char.index(letter)
            del char[found_index]
            char.insert(found_index,"*")
            del char2[found_index]
            char2.insert(found_index,letter)
            ctrl+=1             
    else:
        life-=1
while "_" in char2:
    taking_letter()
    print("".join(char2))
    if life==0:
        print("Üzgünüz tahmin hakkınız bitti. Bulmanız gereken ifade: " f'"{correct}"' " idi.")
        break
    print(f"Kalan tahmin hakkınız: {life}")
    
else:
    print("Tebrikler!",f'"{word}"',"ifadesini buldunuz.")
