from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

def calculadora():
    while True:
        print(f"\n{Fore.CYAN}=== Calculadora Básica ==={Style.RESET_ALL}")
        print(f"{Fore.RED}1. Suma{Style.RESET_ALL}")
        print(f"{Fore.BLUE}2. Resta{Style.RESET_ALL}")
        print(f"{Fore.GREEN}3. Multiplicación{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4. División{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}5. Salir{Style.RESET_ALL}")

        operacion = input(f"{Fore.CYAN}Selecciona una operación (1-5): {Style.RESET_ALL}")

        if operacion == '5':
            print(f"{Fore.CYAN}¡Gracias por usar la calculadora! {Style.RESET_ALL}")
            break

        if operacion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print(f"{Fore.RED} Error: Debes ingresar números válidos.{Style.RESET_ALL}")
                continue

            try:
                if operacion == '1': res = suma(num1, num2)
                elif operacion == '2': res = resta(num1, num2)
                elif operacion == '3': res = multiplicacion(num1, num2)
                elif operacion == '4': res = division(num1, num2)

                print(f"{Fore.GREEN} Resultado: {res}{Style.RESET_ALL}")
            except ZeroDivisionError:
                print(f"{Fore.RED} Error: No se puede dividir por cero.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED} Operación no válida. Inténtalo de nuevo.{Style.RESET_ALL}")
        
        input(f"\n{Fore.CYAN}Presiona Enter para continuar...{Style.RESET_ALL}")

if __name__ == "__main__":
    calculadora()