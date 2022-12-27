from math import sqrt
a = float(input("informe o primeiro numero: "))
if a == 0:
    print("equaçao nao é de segundo grau")
else:
    b = float(input("informe o segundo numero:"))
    c = float(input("informe o terceiro numero "))
    delta = (b*b-(4*a*c))
    if delta < 0:
        print(f"delta menor que zero, raizes imaginarias")
    elif delta == 0:
        raiz = (-b/(2*a))
        print("delta = 0 a raiz é {raiz}")
    else:
        raiz = ((-b) + (sqrt(delta))) / (2*a)
        raiz2 = ((-b) - (sqrt(delta)))/ (2*a)
        print(f"Delta é:{delta}\n")
        print(f"as raizes são {raiz} e {raiz2}")
