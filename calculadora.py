from colorama import init, Fore

# Inicializa colorama 
init(autoreset=True)


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def calculadora():
    print(Fore.CYAN + "Calculadora Básica")
    print(Fore.CYAN + "Operaciones Disponibles:")
    print(Fore.RED + "1. Suma")
    print(Fore.BLUE + "2. Resta")
    print(Fore.GREEN + "3. Multiplicación")
    print(Fore.YELLOW + "4. División")

    operacion = input(Fore.CYAN + "Selecciona una operación (1/2/3/4): ")

    if operacion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if operacion == '1':
            print(Fore.RED + f"El resultado de la suma es: {suma(num1, num2)}")
        elif operacion == '2':
            print(Fore.BLUE + f"El resultado de la resta es: {resta(num1, num2)}")
        elif operacion == '3':
            print(Fore.GREEN + f"El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
        elif operacion == '4':
            print(Fore.YELLOW + f"El resultado de la división es: {division(num1, num2)}")
    else:
        print("Operación no Válida")

if __name__ == "__main__":
    calculadora()