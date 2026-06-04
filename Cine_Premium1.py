import random

# ==========================================
# EJERCICIO 1: Sistema de Cine Premium
# ==========================================
print("--- BIENVENIDO AL SISTEMA DE CINE PREMIUM ---")

nombre = input("Ingresa el nombre del cliente: ")

edad = int(input("Ingresa la edad: "))
while edad < 0:
    print("Error: La edad no puede ser negativa.")
    edad = int(input("Ingresa la edad nuevamente: "))

tipo_entrada = input("Tipo de entrada (General/VIP): ").lower()
while tipo_entrada != "general" and tipo_entrada != "vip":
    print("Error: Ingresa 'General' o 'VIP'.")
    tipo_entrada = input("Tipo de entrada (General/VIP): ").lower()

dia = input("Ingresa el día de la semana: ").lower()
dias_validos = ["lunes", "martes", "miercoles", "miércoles", "jueves", "viernes", "sabado", "sábado", "domingo"]
while dia not in dias_validos:
    print("Error: Día inválido.")
    dia = input("Ingresa el día nuevamente: ").lower()

es_estudiante = input("¿El cliente es estudiante? (si/no): ").lower()
es_premium = input("¿Tiene membresía premium? (si/no): ").lower()

if tipo_entrada == "general":
    valor_base = 9000
else:
    valor_base = 15000

descuento_porcentaje = 0

if edad >= 60:
    descuento_porcentaje += 25
else:

    if es_estudiante == "si":
        if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "miércoles" or dia == "jueves":
            descuento_porcentaje += 20
        else:
            descuento_porcentaje += 10

if es_premium == "si":
    descuento_porcentaje += 5
    if tipo_entrada == "vip":
        descuento_porcentaje += 3

descuento_dinero = (valor_base * descuento_porcentaje) / 100
valor_final = valor_base - descuento_dinero

print("\n--- RESUMEN DE COMPRA ---")
print("Nombre del cliente:", nombre)
print("Tipo de entrada:", tipo_entrada.capitalize())
print("Valor base: $", valor_base)
print("Descuento total aplicado:", descuento_porcentaje, "%")
print("Valor final a pagar: $", int(valor_final))
print("------------------------------------------\n")


# ==========================================
# EJERCICIO 2: Desafío de Seguridad 
# ==========================================
print("--- SISTEMA DE CIBERSEGURIDAD ---")

# Pedir datos
usuario = input("Nombre de usuario: ")
pin = input("PIN secreto: ")
nivel = input("Nivel de acceso: ")


codigo = random.randint(1000, 9999)


if codigo % 2 != 0:  
    codigo = codigo + 1 
if codigo % 10 == 0:  
    codigo = codigo + 2
 

print("\nSe ha generado un código numérico secreto. Tienes 3 intentos para adivinarlo.")

intentos = 0
adivinado = False
intento_1 = 0
intento_2 = 0


while intentos < 3 and adivinado == False:
    intento_actual = int(input(f"\nIntento {intentos + 1}. Ingresa tu código: "))
    intentos += 1
    
    if intento_actual == codigo:
        adivinado = True
        if intentos == 1:
            print("Acceso inmediato")
        elif intentos == 2:
            print("Acceso parcial")
        else:
            print("Acceso restringido")
    else:
        if intentos == 1:
            intento_1 = intento_actual
            if intento_actual < codigo:
                print("Incorrecto. El código secreto es MAYOR.")
            else:
                print("Incorrecto. El código secreto es MENOR.")
                
        elif intentos == 2:
            intento_2 = intento_actual
            
            distancia_1 = abs(codigo - intento_1)
            distancia_2 = abs(codigo - intento_2)
            
            if distancia_2 < distancia_1:
                print("Incorrecto. Pero vas mejor, este segundo intento estuvo más cerca que el primero.")
            elif distancia_1 < distancia_2:
                print("Incorrecto. El primer intento estaba más cerca de la respuesta.")
            else:
                print("Incorrecto. Ambos intentos estuvieron igual de lejos.")
                
        elif intentos == 3:
            print("\nAcceso bloqueado")
            print("El código correcto era:", codigo)

print("--- FIN DEL PROGRAMA ---")