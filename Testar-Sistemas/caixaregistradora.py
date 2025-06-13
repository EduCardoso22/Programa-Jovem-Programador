print ("Olá,  bem vindo!")

while True: 
    valor = float(input("Digite o valor do produto: "))

    if valor >= 100:
        desconto = valor * 0.1
        valor_final = valor - desconto
        print(f"O valor é de {valor:.2f}, com desconto fica: {valor_final:.2f}")

    elif 50 <= valor < 100:
        desconto = valor * 0.05
        valor_final = valor - desconto
        print(f"O valor é de {valor:.2f}, com desconto fica: {valor_final:.2f}")

    else:
        valor_final = valor
        print(f"O valor é de {valor:.2f}, sem desconto fica: {valor_final:.2f}")

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Obrigado por usar a caixa registradora! Encerrando o programa.")
        break