nome = input('DIGITE SEU NOME: ')

if len(nome) > 1:

    if len(nome) <= 4:
        print('SEU NOME É CURTO')

    elif len(nome) >= 5 and len(nome) <= 6:
        print('SEU NOME É NORMAL')

    else:
        print('SEU NOME É MUITO GRANDE')

else:
    print('Digite mais de um caractere')