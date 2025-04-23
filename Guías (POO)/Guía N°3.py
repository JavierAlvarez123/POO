nombres = ["Ana", "Luis", "Carlos", "Marta", "Pedro"]
roles = ["admin", "editor", "visitante", "editor", "admin"]
activos = [True, False, True, True, False]

for x in range(len(nombres)):
    print(nombres[x])
    print(roles[x])
    print(activos[x])
    print("Usuario mostrado")

    match activos[x]:
        case True:
            print("El usuario ",nombres[x],"esta activo")
        case False:
            print("El usuario ",nombres[x],"Esta inactivo")
    print(x)