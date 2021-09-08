#while 1 
num=None
while num !=0:
    num = int (input('Introduce un número: '))

#while 2
while True:
    num= int(input('Introduce un digito: '))
    if num==0:
        break

#while3
n=5
while n>0:
    print(n)
    n=n-1
#se puede restar n-=1
    print('¡Despegue!')
#for 1
palabra='python'
for letra in palabra:
    print (letra)

#for 2

for i in range (1, 10, 2):
    print (i, end=",")

#for lista, se diferencia de la tupla en que si permite modificar
amigos=['Joseph', 'Glenn', 'Sally']
for amigo in amigos:
    print('Feliz año nuevo: ', amigo)
print('terminado')

#for tupla , se diferencia de la lista por que esta no permite modificar
colores=('verde', 'rojo', 'azul')
for color in colores:
    print('Feliz año nuevo: ', amigo)
print('terminado')

#contador con ciclo for ejercicio 1
contador=0
for valor in [3, 41, 12, 9, 74, 15]:
    contador=contador+1
print('num elementos: ', contador)

#Imprime un rango de 0 a 9
for i in range (10):
    print (i)

#Imprime un rango de 1 a 9
for i in range (1,10):
    print (i)

#Imprime 15 veces la palabra digitada
pal=input('Escriba una palabra: ')
for i in range (15):
    print (pal)

#contador con ciclo while
contador=0
while contador<=10:
    print(contador)
    contador+=1
print('Finalizado')