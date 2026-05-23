ano , salario = int(input("Digite o tempo de trabalho na empresa em anos: ")), 1621
if ano < 2:
    print("Seu novo salário é: ", salario * 1.05)
elif ano <= 5:
    print("Seu novo salário é: ", salario * 1.1)
else:
    print("Seu novo salário é: ", salario * 1.15)