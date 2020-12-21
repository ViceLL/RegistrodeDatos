import os
import sys

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

while (True):
  menu = input("\n1. Salir\n2. Capturar\n3. Listar\n4. Busqueda\n5.Editar\n6.Eliminar")

  if (menu == "1"):
    sys.exit()

  elif (menu == "2"):

      while (True):
         cedula = input("Cedula: ")
         nombre = input("Nombre: ")
         apellido = input("Apellido: ")
         edad = input("Edad: ")

         if (cedula == "" and nombre == "" and apellido == "" and edad == ""):
             sys.exit()

         else:
             while (True):
                 print("¿Desea guardar?")
                 opcion = input("\nSi(Y), No(N)\n")

                 if (opcion == "Y"):
                     with open(sys.argv[1], "a") as writer:
                         writer.write(cedula + ";" + nombre + ";" + apellido + ";" + edad + "\n")
                     break
                 elif (opcion == "N"):
                     sys.exit()
                 else:
                     continue
  elif (menu == "3"):
        print()
        with open(sys.argv[1], "r") as reader:
          data = reader.readlines()
          for i in data:
            data = i.replace("\n", "")
            print(data)

  elif (menu == "4"):
    localizada, BuscarCedula = buscar()
    print(localizada)

  elif (menu == "5"):
    localizada, BuscarCedula = buscar()
    if(localizada == "" and BuscarCedula == ""):
        continue

    print(localizada)

    while(True):
        NuevaCedula = input("Escriba nuevos valores para cambiar los datos previos\ncedula: ")
        NuevoNombre = input("Nuevo nombre: ")
        NuevoApellido = input("Nuevo apellido: ")
        NuevaEdad = input("Nueva edad: ")
        NuevosDatos = NuevaCedula + ";" + NuevoNombre + ";" + NuevoApellido + ";" + NuevaEdad + "\n"

        if(NuevaCedula == "" and NuevoNombre == "" and NuevoApellido == "" and NuevaEdad == ""):
            break

        if(BuscarCedula == NuevaCedula):
            with open(sys.argv[1], "r+") as reader, open(sys.argv[1], "a") as writer:
                data = reader.readlines()
                reader.truncate(0)
                for linea in data:
                    if localizada in linea:
                        linea = linea.replace(localizada, NuevosDatos)
                    writer.write(linea)
            break

        elif(ExisteCedula(NuevaCedula)):
            print("Ya existe esta cedula, escriba otra\n")

        else:
            with open(sys.argv[1], "r+")as reader, open(sys.argv[1], "a")as writer:
                data = reader.readlines()
                reader.truncate(0)
                for linea in data:
                    if localizada in linea:
                        linea = linea.replace(localizada, NuevosDatos)
                    writer.write(linea)
            break

  elif(menu == "6"):
    localizada, BuscarCedula = buscar()

    if (localizada == "" and BuscarCedula == ""):
        continue

    print(localizada)

    while(True):
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
        else:
            print("Esta opcion es invalida")

    else:
        print("Esta opcion es invalida")
     




