nombre, apellido, edad, edad_2, list, tuple = 'Joan', 'Pérez', 24, 25, [1, 2, 3, 4, 5], (1, 2, 3, 4, 5)

Ewe = (edad == edad_2)
palabra = nombre + " " + str(edad)
full_name = nombre + " " + apellido
elevado = pow(2, 3)
frase = f'My name is {nombre} and my surname is {apellido}'

print(frase)
print(full_name)
print(elevado)
print(palabra)
print(*tuple[::-1])
print(*reversed(list))

a = True
b = False
resultado_and = a and b
resultado_or = a or b
resultado_not = not a
print(resultado_and)
print(resultado_or)
print(resultado_not)
print('----------------------------')
print('Operadores de asignación')
numero = 32
cadena = 'Hola'
vacio = ""

bool_numero = bool(numero)
bool_cadena = bool(cadena)
bool_vacio = bool(vacio)

print(bool_numero)
print(bool_cadena)
print(bool_vacio)
print('----------------------------')
x = 5
print(x)
x += 3  # TODO Equivale a x = x + 3,  x ahora es 8
print(x)
x *= 2  # TODO a x = x * 2, x ahora es 16
print(x)
print('----------------------------')
x = 5
y = 7

if x > y:
    print('x es mayor que y')

if x < y:
    print('y es menor que x')

if x == y:
    print('x es igual a y')

print('----------------------------')

age = 20
if age < 18 or age > 30:
    print('No estás en el rango de edad 18-30')
else:
    print("Estas en el rango de edad 18-30")

print('----------------------------')

puntos = 110

if puntos >= 85 and puntos <= 100:
    calificacion = 'A'
elif puntos <= 85 and puntos >= 65:
    calificacion = 'B'
elif puntos <= 65 and puntos >= 50:
    calificacion = 'C'
elif puntos >= 100:
    calificacion = 'No valido'
else:
    calificacion = 'F'

print("Tú calificacion es:", calificacion)
print('------------------------------------')

edad = 20
nacionalidad = 'española'

if edad >= 18:
    if nacionalidad == 'española':
        print('Tú puedes votar')
    else:
        print('Necesitas nacionalidad española')
else:
    print('Necesitas ser mayor de edad para votar')

print('------------------------------------')

# todo Bloque de código a ejecutar en cada iteración.

nombres = ['Ana', 'Evelyn', 'Juliet']
for nombre in nombres:
    print(nombre)

print('------------------------------------')

# todo Range Bucle "While"

for i in range(10, -1, -1):
    print(i);

print('----------------------')

frase = 'Пуля на вылет'

for i in frase:
    print(i)

print('----------------------')

numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
    print('The result is', sum)

print('----------------------')

contador = -1
while contador < 5:
    contador +=1
    print(contador)