#classes

class Human:
    def talk(self):
        print("Human can talk")
    def walk(self):
        print("Human can walk")

#self --> this,fonksiyonu rezerve eder.

human1= Human()
human1.talk()
human1.walk()

class Human:
    name="Duygu" 
    def talk(self,sentence):
        name="Yılmaz"
        print(f"{self.name}: {sentence}") #1.rezerve parametreden sonra 2.degeri alarak devam eder.
    def walk(self):
        print(f"{self.name} can walk")
  
human1= Human()
human1.name="Mert" #kalıbı değiştirmek için kullandık fakat yukarıda self.name vermeliyim.
human1.talk("Merhaba")
human1.walk()
#self.name ile nesnenin içindeki diger alanlara ulasabiliriz.Başka bir fonksiyona erişmek içinde kullanabiliriz.
#name dediğimde yılmazı calıstırıcak,self.name dersek yılmazı ekarte edip duyguyu çalıştırıcak.

human2= Human()
human2.name="Cem"
human2.talk("Selam")
human2.walk()

#built-in : __init__
#__init__ ile yeni bir nesne ürettik.

class Human:
    name="Duygu" 
    def __init__(self,name):
        self.name=name
        print("Bir human instance üretildi")
        def __str__(self):
            return f"STR Fonksiyonundan dönen deger: {self.name}"
        
    def talk(self,sentence):
        print(f"{self.name}: {sentence}") #1.rezerve parametreden sonra 2.degeri alarak devam eder.
    def walk(self):
        print(f"{self.name} can walk")

human1= Human("Duygu")
human1.talk("Merhaba")
human1.walk()
print(human1) #adresi verdi.

human2= Human("Yılmaz")
human2.talk("Selam")
human2.walk()
print(human2)
