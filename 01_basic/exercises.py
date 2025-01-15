###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

# Solución
print("Álvaro")
print("Madrid")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

# Solución
print(f"La variable 'a' es de tipo: {type(a)}")
print(f"La variable 'b' es de tipo: {type(b)}")
print(f"La variable 'c' es de tipo: {type(c)}")
print(f"La variable 'd' es de tipo: {type(d)}")
print(f"La variable 'e' es de tipo: {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

# Solución
numero = "12345"
entero = int(numero)
float = float(entero)
print(f"El numero convertido a entero es: '{entero}'")
print(f"El entero convertido a float es: '{float}'")

numero_float = 3.99
float_convetido = int(numero_float)
print(f"El float 3.99 convertido a entero es: '{float_convetido}'") # Al convertir un float a un entero, se trunca el valor decimal, no se redondea 🤯

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# Solución
nombre = "Álvaro"
edad = 24
altura = 1.82
print(f"¡Hola! Mi nombre es '{nombre}' y tengo '{edad}' años, mido '{altura}' metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

#? No se como hacerlo sin asignar una variable... import ??

# Solución 1
print("Solución 1")
pi = 3.14159
print(f"El número PI es: '{pi}'")
pi_redondeado = round(pi)
print(f"El número PI redondeado es: '{pi_redondeado}'")
resultado = pi_redondeado // 2 # '//' es el operador de división entera, solo con '/' se hace la división decimal
print(f"El resultado de dividir el número PI entre 2 es: '{resultado}'")

# Solución 2
print("Solución 2")
print(f"El número PI es: '{round(3.14159) // 2}'")