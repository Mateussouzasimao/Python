letra = input('Digite uma letra: ')
listaLetra = ('a','e','i','o','u')

if letra.isalpha() and len(letra) == 1:
    if letra.lower() in listaLetra:
        print(f"\nA letra '{letra}' é uma vogal.")
    else:
        print(f"\nA letra '{letra}' é uma consoante.")
        
else:
    print('\nDigite somente uma letra!')
