#v2.1
from os import system
special_chars=r'0 1 2 3 4 5 6 7 8 9 ! " # $ % & ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~ '
alphabet=list(("a b c ç d e f g ğ h ı i j k l m n o ö p r s ş t u ü v y z q w x").split(" "))
special_chars=list(special_chars.split(" "))
special_chars+=["'"]
ctrl_special_chars=0
system("cls")
word=(input("Kelimeyi giriniz: "))
def forfunction():
    global ctrl_special_chars
    for w in word:
        if w in alphabet:
            ctrl_special_chars=0
            continue
        else:
            ctrl_special_chars=1
            break
forfunction()
while ctrl_special_chars==1:
    print("Lütfen özel karakter ve rakam içermeyen bir ifade giriniz.")
    word=(input("Kelimeyi giriniz: "))
    forfunction()
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
    len_letter=len(letter)
    while len_letter>1 or letter in special_chars:
        print("Lütfen özel karakter ve rakam içermeyen tek bir harf giriniz:")
        letter=input("Harf giriniz: ")
        len_letter=len(letter)
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
    system("cls")
    print("".join(char2))
    if life==0:
        print("Üzgünüz tahmin hakkınız bitti. Bulmanız gereken ifade: " f'"{correct}"' " idi.")
        break
    print(f"Kalan tahmin hakkınız: {life}")
else:
    print("Tebrikler!",f'"{word}"',"ifadesini buldunuz.", f"Kalan tahmin hakkınız {life} idi")
