productos = ["manzana", "arroz", "pollo", "plátano", "carne","fideos", "pera"]
for x in productos:
    print(x)
    match x:
        case "manzana"|"platano"|"pera":
            dato={"nombre":x,"categoria":"fruta"}
        case "arroz"|"fideos":
            dato={"nombre":x,"categoria":"granos"}
        case "pollo"|"carne":
            dato={"nombre":x,"categoria":"carnes"}
    print(dato)