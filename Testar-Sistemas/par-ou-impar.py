def par_ou_impar():
    print("Jogo de Par ou Ímpar")
    escolha_jogador1 = input("Jogador 1, escolha se você quer PAR ou ÍMPAR: ").strip().lower()
    while escolha_jogador1 not in ['par', 'impar']:
        escolha_jogador1 = input("Escolha inválida. Jogador 1, se você quer PAR ou ÍMPAR: ").strip().lower()
    escolha_jogador2 = 'impar' if escolha_jogador1 == 'par' else 'par'
    print(f"Jogador 1 escolheu {escolha_jogador1}. Jogador 2 será {escolha_jogador2}.")

    num_jogador1 = int(input("Jogador 1, digite um número: "))
    num_jogador2 = int(input("Jogador 2, digite um número: "))

    soma = num_jogador1 + num_jogador2
    print(f"A soma dos números é {soma}.")

    if (soma % 2 == 0 and escolha_jogador1 == 'par') or (soma % 2 != 0 and escolha_jogador1 == 'impar'):
        print("Jogador 1 ganhou a rodada!")
    else:
        print("Jogador 2 ganhou a rodada!")
