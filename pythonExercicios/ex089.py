# Initialize an empty list to store information about students
lista = []
# Temporary list to store individual student data before appending to the main list
tempNotas = []

# Start an infinite loop to input student information
while True:
    # Input student name
    nome = input("Qual o nome do aluno: ")
    # Append student name to temporary list
    tempNotas.append(nome)

    # Use a loop to input two grades for the student
    for c in range(2):
        nota = int(input(f"Qual a {c + 1} do aluno: "))
        # Append each grade to the temporary list
        tempNotas.append(nota)

    # Append the temporary list (student information) to the main list
    lista.append(tempNotas[:])
    # Clear the temporary list for the next iteration
    tempNotas.clear()

    # Ask the user if they want to continue entering student information
    resp = ' '    
    while resp not in "NnSs":
        resp = input("Voçê deseja continuar? [S] [N]: ").upper().strip()[0]
    if resp == "N":
        # Break out of the loop if the user chooses not to continue
        break

# Loop through the main list to calculate and print the average grade for each student
for i, aluno in enumerate(lista):
    nome = aluno[0]
    notas = aluno[1:]
    # Calculate the average grade
    media = sum(notas) / len(notas)
    # Print student information and average grade
    print("{:<10} {:<10} {:<10.2f}".format(i, nome, media))

# Start another loop to allow the user to check individual student grades
while True:
    # Input the number corresponding to the student (999 to exit)
    escolha = int(input("\nDigite o número do aluno para ver suas notas (999 para sair): "))
    if escolha == 999:
        # Break out of the loop if the user chooses to exit
        break
    else:
        # Loop through the main list to find the selected student and print their grades
        for i, aluno in enumerate(lista):
            if i == escolha:
                print("As notas desse aluno são: ")
                print(f"Notas: {aluno[1:]}")


        