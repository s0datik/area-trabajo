import os
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime

init(autoreset=True)

# Función para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función principal del blog de notas
def blog_de_notas():
    notas = []  # Lista para almacenar las notas

    while True:
        clear_screen()
        print(Fore.LIGHTRED_EX + "\n=== BLOG DE NOTAS ===")
        print(Fore.BLUE + "1. Agregar una nota")
        print(Fore.GREEN + "2. Ver todas las notas")
        print(Fore.YELLOW + "3. Editar una nota")
        print(Fore.MAGENTA + "4. Eliminar una nota")
        print(Fore.CYAN + "5. Salir")
        opcion = input(Style.BRIGHT + "\nSelecciona una opción: ")

        if opcion == "1":
            # Agregar una nota
            clear_screen()
            print(Fore.GREEN + "\n=== AGREGAR NOTA ===")
            titulo = input("Título de la nota: ")
            contenido = input("Contenido de la nota: ")
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            notas.append({"titulo": titulo, "contenido": contenido, "fecha": fecha})
            print(Fore.YELLOW + "\nNota agregada correctamente.")
            input(Fore.YELLOW + "\nPresiona Enter para continuar...")

        elif opcion == "2":
            # Ver todas las notas
            clear_screen()
            print(Fore.MAGENTA + "\n=== TODAS LAS NOTAS ===")
            if not notas:
                print("No hay notas disponibles.")
            else:
                for i, nota in enumerate(notas):
                    print(f"\nNota {i + 1}:")
                    print(f"Título: {nota['titulo']}")
                    print(f"Fecha: {nota['fecha']}")
                    print(f"Contenido: {nota['contenido']}")
            input(Fore.MAGENTA + "\nPresiona Enter para continuar...")

        elif opcion == "3":
            # Editar una nota
            clear_screen()
            print(Fore.BLUE + "\n=== EDITAR NOTA ===")
            if not notas:
                print(Style.BRIGHT + "No hay notas disponibles para editar.")
            else:
                print(Style.BRIGHT + "Selecciona la nota que deseas editar:")
                for i, nota in enumerate(notas):
                    print(f"{i + 1}. {nota['titulo']} ({nota['fecha']})")
                try:
                    indice = int(input("\nNúmero de la nota: ")) - 1
                    if 0 <= indice < len(notas):
                        print(f"\nNota seleccionada: {notas[indice]['titulo']}")
                        nuevo_contenido = input("Nuevo contenido: ")
                        notas[indice]["contenido"] = nuevo_contenido
                        notas[indice]["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print("\nNota actualizada correctamente.")
                    else:
                        print(Fore.BLUE + "\nÍndice inválido.")
                except ValueError:
                    print(Fore.BLUE + "\nEntrada no válida. Por favor, ingresa un número.")
            input(Fore.BLUE + "\nPresiona Enter para continuar...")

        elif opcion == "4":
            # Eliminar una nota
            clear_screen()
            print(Back.RED + "\n=== ELIMINAR NOTA ===")
            if not notas:
                print(Back.RED + "No hay notas disponibles para eliminar.")
            else:
                print(Back.RED + "Selecciona la nota que deseas eliminar:")
                for i, nota in enumerate(notas):
                    print(f"{i + 1}. {nota['titulo']} ({nota['fecha']})")
                try:
                    indice = int(input("\nNúmero de la nota: ")) - 1
                    if 0 <= indice < len(notas):
                        nota_eliminada = notas.pop(indice)
                        print(f"\nNota '{nota_eliminada['titulo']}' eliminada correctamente.")
                    else:
                        print("\nÍndice inválido.")
                except ValueError:
                    print(Fore.YELLOW + "\nEntrada no válida. Por favor, ingresa un número.")
            input(Fore.YELLOW + "\nPresiona Enter para continuar...")

        elif opcion == "5":
            # Salir del programa
            clear_screen()
            print(Fore.BLUE + "\n¡Gracias por usar el Blog de Notas!")
            break

        else:
            print(Fore.RED + "\nOpción no válida. Por favor, intenta de nuevo.")
            input(Fore.RED + "\nPresiona Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    blog_de_notas()
