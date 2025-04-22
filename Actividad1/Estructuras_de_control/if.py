Asistentes= ["Camila","Jose","Lucia","Pedro","Sofia"]
nombre=str(input("Ingresa un nombre para verificar si esta en la lista: "))

if nombre in Asistentes:
    print(nombre," si esta en la lista.")
else:
    print(nombre," no esta en la lista.")