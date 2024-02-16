tupla = ("Maneiro".upper(), "Foda".upper(), "idiota".upper(), "eduardo".upper())
for p in tupla:
    print(f"\nNa palavra {p.upper()} temos", end =" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")

    