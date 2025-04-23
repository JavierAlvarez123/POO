lunes = []
martes = []
miercoles = []
jueves = []
viernes = []

semana = [lunes,martes,miercoles,jueves,viernes]
productos = ["chocolate","chocolate","Leche","papasf","galletas","Pollo","Pescado","Chocolate"]

def AgregarComida(dina):
    for x in semana:
        total = ComprobarElementos(x)
        if total == 0:
            x.append(dina)
            break
        elif total == 1:
            if ComprobarBM(x[0]):
                x.append(dina)
                break
            else:
                continue
        elif total == 2:
            if ComprobarBM(x[0] == True and ComprobarBM(x[1] == True)):
                x.append(dina)
                break
            elif ComprobarBM(x[0] == False or ComprobarBM(x[1] == False)):
                continue
                #es comprobar que el alimento de parametro "dina" sea bueno, si es malo tiene que continuar 
                #con la siguiente iteracion, "continue"
                
        elif total == 3:
            continue

def recorrerLista(lista):
    for x in lista:
        for y in x:
            print(y)

def ComprobarElementos(lista):
    return len(lista)

def ComprobarBM(alimento):
    match (alimento):
        case "papasf" | "sugles" | "chocolate":
            print("este es un alimento malo: ", alimento)
            return False
        case _:
            print("es un alimento bueno",alimento)
            return True
#print(len(lista1))

while len(productos) != 0:
    #rint("se ha quitado el elemento")
    dina = (productos[0])
    print("Comparando elemento:", dina)
    AgregarComida(dina)
    productos.pop(0)
print(semana)
print(ComprobarElementos(lunes))