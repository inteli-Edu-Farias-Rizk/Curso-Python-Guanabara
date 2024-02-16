print("=="*15)
equipes =('Red Bull Racing', 'Aston Martin', 'Mercedes F1 Team', 'Scuderia Ferrari', 'Alfa Romeo', 'Alpine F1 Team', 'Williams Racing',
        'Scuderia Alpha Tauri', 'Haas F1 Team', 'Mclaren Racing')
print("Os cinco primeiro são: ")
for c in range (0,5):
    print(equipes[c])
print("=="*15)
print("OS quatro últimos times são: ")

for c in range (1,5):
    print(equipes[-c])

print("=="*15)
print("Aqui estão todos os times em ordem alfabética")
print(sorted(equipes))