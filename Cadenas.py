saludo='Hola Mundo'

print("LONGITUD DE CADENAS")
print("-"*30)
longitud=len(saludo)
print(saludo)
print("La longitud de la cadena es:",longitud)

print("-"*30)
print("CADENAS Y CADENAS")
print("-"*30)
cad="Esta es una 'cadena con comillas simples' dentro de comillas dobles"
cad=cad+" como ejemplo"
print(cad)
print(cad[0])
#cad[0]='e'  #Error, las cadenas son inmutables
lenguaje="Python"
descripcion="Este es un buen curso"
frase=descripcion+" de "+lenguaje
print(frase)

print("-"*30)
print("CADENAS Y NUMEROS")
print("-"*30)
total=5500
#mensaje="El total de la compra es: "+total+" pesos" se tiene que convertir el valor numerico para agregarlo a una cadena
mensaje="El total de la compra es: "+str(total)+" pesos"
print(mensaje)

mensaje=f"El total de la compra es: {total} pesos"
print(mensaje)

print("-"*30)
print("AGREGAR SALTOS DE LINEAS A CADENAS")
print("-"*30)
mensaje="Orden con 10 elementos\nCargo $5500.99\n¡Gracias por su preferencia!"
print(mensaje)

print("-"*30)
print("FUNCIONES CON CADENAS")
print("-"*30)
nombres="Ana Maria Juan Carlos Luis"
elementos="a a a b b B c c c c c aa"
print(nombres.upper()) #convierte en mayusculas
print(nombres.lower()) #convierte en minusculas
print(nombres.capitalize()) #convierte en la primer letra en mayuscula
print(nombres.title()) #convierte en mayuscula la letra inicial de cada palabra
print(nombres.replace("a","x")) #reemplaza todas las letras a por una x
print(nombres.split(" ")) #Separa las palabras con coma
print(nombres.count("a")) #Cuenta las letras minusculas en nombres
print(elementos.count("a")) #Cuenta las letras minusculas en elementos
print(nombres.split(" ")[0]) #Posicion inicial de los elementos
print(nombres.split(" ")[-1]) #Posicion final de los elementos
print(nombres.split(" ")[-2]) #Penultimo de los elementos
#print(nombres.split(",")[-6])
print(nombres.replace("Juan","Pedro")) #Reemplaza Pedro a Juan
print(nombres.replace(","," ")) #Reemplaxza los espacios de la lista por comas
print(nombres.endswith("Luis")) #Regresa si la cadena termina con Luis
print(nombres.startswith("Ana")) #Regresa si la cadena inicia con Ana
print(nombres.index("Carlos")) #Regresa la posicion en la que inicia el nombre de Carlos (Cuenta los caracteres)
print(nombres.find("Juan")) #Regresa la posicion donde encuentra a Juan (cuenta los caracteres)

print("-"*30)
print("Cadenas multilínea")
print("-"*30)
texto_multilinea="""Este es un texto 
[][]que abarca varias líneas.
**Podemos escribir lo que queramos aquí,
$$y se mantendrá el formato!!."""
#El triple asterisco convierte el texto en multilinea
print(texto_multilinea)
print()

cadena_limpia=texto_multilinea.replace("[]","")\
    .replace("**","").replace("$$","") #Reemplaza caracteres para eliminarlos
print(cadena_limpia)

print("-"*30)
print("CADENAS FORMATEADAS")
print("-"*30)
nombre="Gabriel"
edad=28
mensaje="Mi nombre es {} y tengo {} años.".format(nombre,edad)
print(mensaje)
mitote="""Para enterarlos que 
el dia de ayer me encontré con {}
que no veía desde que se graduó con {}.
y ahora resulta que ya no vive con {}
el que eras amigo de {}
porque se juntó con {}"""
mitote_completo=mitote.format(*nombres.split(" ")) #El Asterisco funciona para que le quite los corchetes y los toma como palabras individuales
print(mitote_completo)