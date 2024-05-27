vinte = 0
dez = 0
um = 0
cinq = 0
print("=" * 35)
print("       BEM VINDO AO BANCO ED")
print("=" * 35)
valor = int(input("Qual será o valor sacado? "))
if valor >= 50:
    while True:
        if valor < 50:
            break
        valor -= 50
        cinq += 1
if valor >= 20 and valor < 50:
    while True:
        if valor < 20:
            break
        valor -= 20
        vinte += 1
if valor >= 10 and valor < 20:
    while True:
        if valor < 10:
            break
        valor -= 10
        dez += 1
if valor >= 1 and valor < 10:
    while True:
        if valor < 1:
            break
        valor -= 1
        um += 1
print("=" * 35)
print(f"Total de {cinq} cédulas de R$50")
print(f"Total de {vinte} cédulas de R$20")
print(f"Total de {dez} cédulas de R$10")
print(f"Total de {um} cédulas de R$1")
print("""
      
      """)
print("VOLTE SEMPRE! TENHA UM BOM DIA!")
  