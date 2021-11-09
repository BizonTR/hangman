import os #terminale komut göndermek için kütüphane
import keyboard #klavyeden tuş okuyabilmek için kütüphane
import re #regex
clear = lambda: os.system('cls')
def GameStart():
    clear()
    ozel_karakterler = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    word = input("Kelime giriniz : ")
    while not word.isalpha() or len(word)<2 or not ozel_karakterler.search(word) == None:
        clear()
        print("Kelime string ,en az iki harf olmalı ve özel karakter içermemeli")   
        word = input("Kelime giriniz : ")
    hp=10
    hiddenLetters=[]
    correct=[]
    
    word=word.strip().lower()
    for i in word:
        hiddenLetters.append('_')
        correct.append(i)
    while hp>0:
        clear()
        guess=input("Harf giriniz ya da tahmin giriniz: ")
        if guess ==word:
            print("Tebrikler doğru bildiniz")
            break
        if len(guess)>1 or guess.isnumeric():
            print("Girilen harf tek karakterli ve sayı olmamalı\n")
            a=input("Devam etmek için enter") 
            continue
        for i in range(0,len(word)):
            if guess==word[i]:
                hiddenLetters[i]=guess 
        hidden="".join(hiddenLetters)                  
        print(hidden)
        if word==hidden:
            print(f"Tebrikler {word} kelimesini buldunuz")           
            break
        hp-=1
        print(f"Kalan can = {hp}")
        a=input("Devam etmek için enter") 
    if hp==0:
        print("Üzgünüm hakkınız bitti")
    score=(hp*len(word))/10
    print(f"Skorunuz : {score}")
    print("Bir kez daha oynamak ister misin ? Y/N")
    while True:
        if keyboard.read_key()=='y':      
            GameStart()
        elif keyboard.read_key()=='n':
            print("Bye Bye!!")
            quit()

print("Hangman Game".center(50))
print("Devam etmek için ENTER".center(25))
while True:
    if keyboard.read_key() == "enter":       
            break
GameStart()

        
    

