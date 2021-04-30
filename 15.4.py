
import itertools, random

karty = list(itertools.product(range(1,14),['Pik','Kier','Trefl','Karo']))

random.shuffle(karty)

print("Wylosowałeś: ")
for i in range(5):
   print(karty[i][0], karty[i][1])