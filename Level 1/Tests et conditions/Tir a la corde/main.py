nbPersonnes = int(input())
total�quipe1 = 0
total�quipe2 = 0
for loop in range(nbPersonnes):
   poids1 = int(input())
   poids2 = int(input())
   total�quipe1 = total�quipe1 + poids1
   total�quipe2 = total�quipe2 + poids2
if total�quipe1 > total�quipe2:
   print("L'�quipe 1 a un avantage")
else:
   print("L'�quipe 2 a un avantage")
print("Poids total pour l'�quipe 1 :", total�quipe1)
print("Poids total pour l'�quipe 2 :", total�quipe2)