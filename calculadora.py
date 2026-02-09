rodando = True
pergunta_continuar = True
entrar_continuar = True



while rodando:
    entrar = input("Deseja entrar na cálculadora ? (s/n) ")

    if entrar == "n":
        print("Você saiu da calculadora.")
        break

    elif entrar == "s":
        while True:

            try:
                primeiro_numero = input("Digite o primeiro número: ")
                segundo_numero = input("Digite o segundo número: ")
                primeiro_numero_inteiro = int(primeiro_numero)
                segundo_numero_inteiro = int(segundo_numero)
            except:
                print("Erro: Por favor, digite apenas números inteiros válidos")
                continue

            enquanto_mesmos_numeros = True
            while enquanto_mesmos_numeros:
                decisao = input("Qual operação deseja realizar com esses números? " \
                "(digite soma, multiplicação ou divisão) ")

                if decisao == "soma":
                    print(f"A soma entre esses números é igual a {primeiro_numero_inteiro + segundo_numero_inteiro}.")
                elif decisao == "multiplicação":
                    print(f"A multiplicação entre esses números é igual a {primeiro_numero_inteiro * segundo_numero_inteiro}.")
                elif decisao == "divisão":
                    if segundo_numero_inteiro == 0:
                        print("Não é possível dividir por zero.")
                    else:
                        print(f"A divisão entre esses números é igual a {primeiro_numero_inteiro / segundo_numero_inteiro}.")
                else:
                    print("Comando inválido. Digite apenas 'soma', 'multiplicação' ou 'divisão'. ")
                    continue
                        
                while pergunta_continuar:
                    continuar = input("Deseja realizar outra operação com estes números? (s/n) ")
                    
                    if continuar == "s":
                        print("Você escolheu realizar outra operação com os mesmos números.")
                        break
                    elif continuar == "n":
                        while entrar_continuar == True:
                            segundo_continuar = input("Você deseja sair ou escolher novos números ? ")
                            
                            if segundo_continuar == "sair":
                                enquanto_mesmos_numeros = False
                                rodando = False
                                break
                            elif segundo_continuar == "escolher novos números":
                                enquanto_mesmos_numeros = False
                                print("Escolha seus novos números.")
                                break
                            else:
                                print("Comando inválido.")
                                continue
                        break
                    else:
                        print("Comando inválido. Digite apenas 's' ou 'n'. ")
                        continue
            
            if rodando == False:
                break
    
    else:
        print("Comando inválido. Digite apenas 's' ou 'n'. ")
