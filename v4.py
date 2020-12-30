import os
import sys

if(len(sys.argv) == 1):
	print("\nNo se han introducido argumentos.\n")
	sys.exit()

if (os.path.exists(sys.argv[1]) == False):
	with open(sys.argv[1], "w+") as creator:
		creator.write("Cédula;Nombres;Apellidos;Edad;Ahorros\n")

def ExisteCedula(x):
	with open(sys.argv[1], "r") as reader:
		if x + ";" in reader.read():
			return True

def buscar():
	localizada = ""
	BuscarCedula = input("\nEscriba que cedula quiere buscar: ")

	if (ExisteCedula(BuscarCedula)):
		with open(sys.argv[1], "r") as reader:
			data = reader.readlines()
			for i in data:
				if BuscarCedula + ";" in i:
					localizada = i
	if localizada == "":
		print("\nNo existe esta cedula")

	return localizada, BuscarCedula

def Salir():
	sys.exit()
 
def If_Num(S):
	return any(char.isdigit() for char in S)

def Capturar():
	while (True):
		while(True):
			try:
				cedula = int(input("Cedula: "))
				break
			except ValueError:
				print("Debe ingresar un entero")

		nombre = input("Nombre: ")
		while If_Num(nombre):
			print("El nombre solo debe contener letras. Intente otra vez.")
			nombre = input("Nombre: ")

		apellido = input("apellido: ")
		while If_Num(apellido):
			print("El apellido solo debe contener letras. Intente otra vez.")
			apellido = input("apellido: ")

		while(True):
			try:
				edad = int(input("Edad: "))
				break
			except ValueError:
				print("Debe ingresar un entero")

		while(True):
			try:
				ahorros = float(input("Ahorros: "))
				break
			except ValueError:
				print("Debe ingresar un entero")

		if (str(cedula) == "" and nombre == "" and apellido == "" and str(edad) == "" and str(ahorros) == ""):
			sys.exit()

		else:
			while (True):
				print("¿Desea guardar?")
				opcion = input("\nSi(Y), No(N)\n").upper()
				if (opcion == "Y"):
					with open(sys.argv[1], "a") as writer:
						writer.write(str(cedula) + ";" + nombre + ";" + apellido + ";" + str(edad) + "," + str(ahorros)+ "\n")
					break
				elif (opcion == "N"):
					sys.exit()
				else:
					continue

def Listar():
	print()
	with open(sys.argv[1], "r") as reader:
		data = reader.readlines()
		for i in data:
			data = i.replace("\n", "")
			print(data)

def Busqueda():
	localizada, BuscarCedula = buscar()
	print(localizada)

def Editar():
	localizada, BuscarCedula = buscar()
	if (localizada == "" and BuscarCedula == ""):
		print(localizada)

	while (True):

		print("\nIngrese los nuevos datos:\n")

		while(True):
			try:
				cedula = int(input("Cedula: "))
				break
			except ValueError:
				print("Debe ingresar un entero")

		nombre = input("Nombre: ")
		while If_Num(nombre):
			print("El nombre solo debe contener letras. Intente otra vez.")
			nombre = input("Nombre: ")
		
		apellido = input("apellido: ")
		while If_Num(apellido):
			print("El apellido solo debe contener letras. Intente otra vez.")
			apellido = input("apellido: ")

		while(True):
			try:
				edad = int(input("Edad: "))
				break
			except ValueError:
				print("Debe ingresar un entero")

		while(True):
			try:
				ahorros = float(input("Ahorros: "))
				break
			except ValueError:
				print("Debe ingresar un entero")

		if (str(cedula) == "" and nombre == "" and apellido == "" and str(edad) == "" and str(ahorros) == ""):
			sys.exit()

		NuevaCedula = str(cedula) # str = string // Originally an int, needs to be converted to string to avoid errors
		NuevoNombre = nombre
		NuevoApellido = apellido
		NuevaEdad = str(edad)
		NuevoAhorro = str(ahorros)
		NuevosDatos = NuevaCedula + ";" + NuevoNombre + ";" + NuevoApellido + ";" + NuevaEdad + "," + NuevoAhorro + "\n"

		if (NuevaCedula == "" and NuevoNombre == "" and NuevoApellido == "" and NuevaEdad == "" and NuevoAhorro == ""):
			break

		if (ExisteCedula(NuevaCedula)):
			print("Ya existe esta cedula, escriba otra\n")

		else:
			with open(sys.argv[1], "r+") as reader, open(sys.argv[1], "a") as writer:
				data = reader.readlines()
				reader.truncate(0)
				for linea in data:
					if localizada in linea:
						linea = linea.replace(localizada, NuevosDatos)
					writer.write(linea)
			break

def Eliminar():
	localizada, BuscarCedula = buscar()

	if (localizada == "" and BuscarCedula == ""):
		print(localizada)

	while (True):
		confirmar = input("Quiere borrar este usuario? (Y/N)\n")

		if (confirmar == "Y"):
			with open(sys.argv[1], "r+") as reader:
				data = reader.readlines()

			os.remove(sys.argv[1])
			with open(sys.argv[1], "w+") as creator:
				for linea in data:
					if localizada in linea:
						linea = ""
					creator.write(linea)
			break

		elif (confirmar == "N"):
			break

while (True):

	menu = input("\n1. Salir\n2. Capturar\n3. Listar\n4. Busqueda\n5. Editar\n6. Eliminar\n\nOpción ---> ")

	if (menu == "1"):
		Salir()

	elif (menu == "2"):
		Capturar()

	elif (menu == "3"):
		Listar()

	elif (menu == "4"):
		Busqueda()

	elif (menu == "5"):
		Editar()

	elif(menu == "6"):
		Eliminar()

	else:
		print("Esta opcion es invalida")




