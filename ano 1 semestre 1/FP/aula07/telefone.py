def listContacts(dic):
    """Print the contents of the dictionary as a table with fixed column widths."""
    print("{:>12s} | {:^20s} | {:<30s}".format("Número", "Nome", "Morada"))
    print("-" * 65)
    for num, details in dic.items():
        print("{:>12s} | {:^20s} | {:<30s}".format(num, details['Nome'], details['Morada']))

def addContact(dic):
    """Add a new contact to the dictionary."""
    number = input('Qual é o número do contacto? ').strip()
    name = input('Qual é o nome do contacto? ').strip()
    address = input('Qual é a morada do contacto? ').strip()
    if number in dic:
        print("Este número já existe! Atualizando o contacto existente.")
    dic[number] = {"Nome": name, "Morada": address}
    print('Contacto adicionado/atualizado com sucesso!')
    return dic

def removeContact(dic):
    """Remove a contact by its number."""
    number = input('Qual é o número a eliminar? ').strip()
    if number in dic:
        dic.pop(number)
        print('Contacto removido com sucesso!')
    else:
        print('Contacto não encontrado!')
    return dic

def findNumber(dic):
    """Find and display the details of a contact by its number."""
    number = input('Qual é o número do contacto? ').strip()
    contact = dic.get(number)
    if contact:
        print(f"Nome: {contact['Nome']} | Morada: {contact['Morada']}")
    else:
        print('Número não encontrado.')

def filterPartName(contacts, partName):
    """Returns a new dictionary with contacts whose names contain the partName."""
    filtered = {}
    for num, details in contacts.items():
        if partName.lower() in details['Nome'].lower():
            filtered[num] = details
    return filtered

def menu():
    """Shows the menu and gets the user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    return input("Opção? ").strip().upper()

def main():
    """Main function with the program's main loop."""
    # Dictionary with contacts: {number: {"Nome": name, "Morada": address}}
    contactos = {
        "234370200": {"Nome": "Universidade de Aveiro", "Morada": "Santiago, Aveiro"},
        "727392822": {"Nome": "Cristiano Aveiro", "Morada": "Porto"},
        "387719992": {"Nome": "Maria Matos", "Morada": "Coimbra"},
        "887555987": {"Nome": "Marta Maia", "Morada": "Lisboa"},
        "876111333": {"Nome": "Carlos Martins", "Morada": "Faro"},
        "433162999": {"Nome": "Ana Bacalhau", "Morada": "Braga"},
        "123456789": {"Nome": "Maria Silva", "Morada": "Leiria"}
    }

    while (op := menu()) != "T":
        if op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            addContact(contactos)
        elif op == "R":
            removeContact(contactos)
        elif op == "N":
            findNumber(contactos)
        elif op == "P":
            partName = input('Qual é a parte do nome do contacto? ').strip()
            filtered_contacts = filterPartName(contactos, partName)
            if filtered_contacts:
                listContacts(filtered_contacts)
            else:
                print("Nenhum contacto encontrado com essa parte do nome.")
        else:
            print("Opção não implementada!")
    print("Fim do programa.")

# Start the program
main()
