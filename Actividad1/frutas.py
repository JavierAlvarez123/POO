watermelon = int(input("ingrese la cantidad de watermelon: "))
cucumber = int(input("ingrese la cantidad cucumber:" ))
avocado = int(input("ingrese la cantidad avocado:" ))
apple = int(input("ingrese la cantidad apple:" ))

total_frutas = watermelon + cucumber + avocado + apple
print(total_frutas) 
total_rojas = watermelon+apple 
print(total_rojas)
total_verdes = avocado+cucumber

total_rojas =  watermelon+apple
print("el grupo de las frutas rojas es de" +total_rojas+ "y el grupo de las frutas verdes es de"+total_verdes)

if total_verdes > total_rojas:
    print("las frutas verdes es el grupo mas grande.")
elif total_verdes < total_rojas:
    print("las frutas rojas es el grupo mas grande.")
else :
    print("contiene la misma cantidad de frutas.")
