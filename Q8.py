peso , altura = float(input("Digite seu peso em Kg: ")), float(input("Digite sua altura em m: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Você está abaixo do peso ideal")
elif imc < 25:
    print("Você está no peso normal")
else:
    print("Você está com sobrepeso")