from datetime import datetime

nombre = input("¿Cuál es tu nombre? ")
bornDate = input("¿Cuál es tu fecha de nacimiento? (DD/MM/YYYY) ")

fecha_actual = datetime.now()

fecha_nacimiento = datetime.strptime(bornDate, "%d/%m/%Y")
edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

print(f"Hola {nombre} y tienes {edad} años.")
