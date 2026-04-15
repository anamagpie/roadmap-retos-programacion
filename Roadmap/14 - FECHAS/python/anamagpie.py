from datetime import datetime # Para trabajar con fechas

'''
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
'''

ahora = datetime.now()
fecha_ing = datetime(2025, 10, 1, 12, 30, 0 )

print(ahora)
print(fecha_ing)

# Calcular los años

diferencia = ahora - fecha_ing
print(type(diferencia))

print(diferencia.days) # Días
print(diferencia.days // 365) # Años: Diferencia // Días de un año (entero) -> 0


'''
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
'''

# Día/Mes/Año
print(fecha_ing.strftime("%d/%m/%y")) #strftime

# Hora/Min/Sec
print(fecha_ing.strftime("%H:%M:%S")) #mayúsculas

# Día de Año
print(fecha_ing.strftime('%j'))

# Día de la Semana
print(fecha_ing.strftime('%A'))

# Nombre del Mes
print(fecha_ing.strftime('%h')) #abreviatura
print(fecha_ing.strftime('%B')) #completo

# Orden según país
print(fecha_ing.strftime('%c'))
print(fecha_ing.strftime('%x')) #solo la fecha
print(fecha_ing.strftime('%X')) #solo horas, min y sec

# AM/PM
print(fecha_ing.strftime('%H%p'))