def check_int(a):
    while True:
        try:
            a = int(a)
            break

        except ValueError:
            a = input("Valor inválido! Digite um número inteiro: ")

    return a

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

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
print("")

if operacao == "+":
    print(f"A soma dos números é igual a: {soma(num1, num2)}")

elif operacao == "-":
    print(f"A subtração dos números é igual a: {sub(num1, num2)}")

elif operacao == "*":
    print(f"A multiplicação dos números é igual a: {mult(num1, num2)}")

elif operacao == "/":
    print(f"A divisão dos números é igual a: {div(num1, num2)}")

else:
    print("Algo deu errado! Por favor, tente novamente.")