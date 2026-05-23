nota1, nota2 = float(input("Digite a sua primeira nota: ")), float(input("Digite sua segunda nota: "))
media = (nota1 + nota2)/2
if media >= 7:
    print("Você está aprovado")
elif media >= 5:
    print("Você está em recuperação")
else:
    print("Você está reprovado")