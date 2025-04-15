# Ejercicio1

edad= 18
altura= 1.82
nombre= "Javier"
es_estudiante= True
print(type(edad))
print(type(altura))
print(type(nombre))
print(type(es_estudiante))

# Ejercicio2

dato1=int(input("ingresa un numero: "))
dato2=int(input("ahora ingresa otro numero para sumarlos: "))
suma= dato1+dato2
print("Este es el resultado: ",suma)

dato_a=int(input("este es un programa para multiplicar un numero entero por un numero decimal, ingresa un numero entero: "))
dato_b=float(input("ingresa un numero decimal: "))
multiplicacion= dato_a*dato_b
print("es es el resultado: ",multiplicacion)

String1=input("ingresa una letra o palabra: ")
String2=input("ahora ingresa una segunda palabra o letra: ")

print("Este es el resultado de la suma de ambos textos: ",String1+String2)

A=input("Este es un programa para comparar numeros y ver cual es mas grande, ingresa un numero: ")
B=input("Ingresa el segundo numero: ")
if A>B:
    print(A," Es mayor que ",B)
else:
    print(B," Es mayor que ",A)

# Ejercicio3

Q=int(input("ingresa un número entero para convertirlo en flotante: "))
W=float(Q)
print("Este es el número: ",W)

E=float(input("ingresa un número decimal para convertirlo a un número entero: "))
R=int(E)
print("Este es el número convertido: ",R)

T=int(input("Ingresa un numero para convertirlo a una cadena de texto: "))
Y=str(T)
print("Este es el número convertido: ",Y)

U=str(input("ingresa una cadena numerica para convertirla a un número: "))
I=int(U)
print("Este es el texto  convertido a número: ",I)

# Ejercicio4

nombre=input("Ingresa tu nombre: ")
edad=int(input("Ingresa tu edad: "))
years_10= edad+10
print("tu edad en diez años sera de: ",years_10)

# Desafio final

K=float(input("Ingresa un numero decimal: "))
L=float(input("Ingresa un segundo numero decimal: "))
O=int(K)
P=int(L)
suma=O+P
resta=O-P
multiplicacion=O*P
division=O/P
print("Los numeros ",K,"y",L,"se han convertido a: ",O,"y",P)
print("Esta es la suma de ambos numeros: ",suma)
print("Esta es la resta de ambos numeros: ",resta)
print("Esta es la multiplicación de ambos numeros: ",multiplicacion)
print("Esta es la division de ambos numeros: ",division)