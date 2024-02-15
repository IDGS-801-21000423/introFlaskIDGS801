from io import open   # importar archivo 


""" 
archivo1 = open('archivo.txt', 'a')  # archivo, si no existe lo crea y permite excribir y leer
archivo1.write('\n saludo IDGS801 nuevo') # escribir en el archivo
archivo1.close()
 """

archivo1 = open('archivo.txt', 'r')   # archivo y lectura
""" 
print(archivo1.read())
archivo1.seek(0)            # comenzar desde una posicion
print(archivo1.read())      # leer todo el archivo
archivo1.close()            # cerrar archivo 
"""
#print(archivo1.readlines())
for datos in archivo1.readlines():
  print(datos.rstrip())
archivo1.close()