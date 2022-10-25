#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la
#suma y la media de todos los números introducidos.

num=0
num=(int)(input("Dime un numero"))
contador=0
suma=0

while num!=0:
    suma+num
    contador+=1
    num=(int)(input("Dime otro numero"))
    suma=num

print(suma/contador) 
