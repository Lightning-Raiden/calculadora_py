def check_int(a):
    while True:
        try:
            a = int(a)
            break

        except ValueError:
            a = input("Valor inválido! Digite um número inteiro: ")

    return a

def calculadora(valor1, valor2, operador):
    
    if operador == "+":
        result = (valor1 + valor2)
        return print(f"A soma dos números é igual a: {result}")
    
    elif operador == "-":
        result = (valor1 - valor2)
        return print(f"A subtração dos números é igual a: {result}")
    
    elif operador == "*":
        result = (valor1 * valor2)
        return print(f"A multiplicação dos números é igual a: {result}")
    
    elif operador == "/":

        while valor2 == 0:
            valor2 = input("Digite um número diferente de zero: ")
            valor2 = check_int(valor2)
            print("")
    
        result = (valor1 / valor2)
        return print(f"A divisão dos números é igual a: {result}")
    
    else:
        print("Algo deu errado! Por favor, tente novamente.")


num1 = input("Digite o primeiro número: ")
num1 = check_int(num1)

num2 = input("Digite o segundo número: ")
num2 = check_int(num2)

print("")

print("Soma (+)")
print("Subtração (-)")
print("Multiplicação (*)")
print("Divisão (/)")

operacao = input("Digite o símbolo da operação que deseja fazer: ")

while True:
    try:
        if operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/":    
            break

        else:
            raise ValueError
        
    except ValueError:
        operacao = input("Operação inválida! Digite apenas um dos símbolos especificados acima: ")

print("")

calculadora(num1, num2, operacao)