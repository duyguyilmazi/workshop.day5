import matematik 

matematik.topla(10,20)
print(matematik)

#matematitk as m dersek artık m olarak isimlendirmiş oluruz.(alias)

import random 
from matematik import topla as toplam_1
from classes import human 

print(matematik.toplam(10,20))
print(random.randint(0,100))

print(toplam_1(10,20))

print(toplam_1(10,20)) #artık import edilen alan yazılırç.

human1= human("Duygu")
human1.talk("Selam")
