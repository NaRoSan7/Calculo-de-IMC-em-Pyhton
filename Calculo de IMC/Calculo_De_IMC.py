print("\n")

print("Calculo de IMC!")
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))
imc = float(peso/(altura**2))

print (str(imc))
if imc <= 16.9:
    input("Olá " + nome + ", seu IMC é: " + str(imc) + ". Você esta muito abaixo do peso!")

elif imc >= 17 and imc <= 18.4:
     input("Olá " + nome + ", seu IMC é: " + str(imc) + ". Você esta abaixo do peso!")
     
elif imc >= 18.5 and imc <= 24.9:
     input("Olá " + nome + ", seu IMC é: " + str(imc) + ". Você esta com peso ideal!")

elif imc >= 25 and imc <= 29.9:
     input("Olá " + nome + ", seu IMC é: " + str(imc) + ". Você esta acima do peso!")

elif imc >= 30 and imc <= 34.9:
     input("Olá " + nome + ", seu IMC é: " + str(imc) + ". Você esta com obesidade de 1º grau!")

elif imc >= 35 and imc <= 40:
     input("Olá " + nome + ", seu IMC é: " + str(imc) + ". Você esta com obesidade de 2º grau!")

else:
     input("Olá " + nome + ", seu IMC é: " + str(imc) + ". Você esta com obesidade de 3º grau!")