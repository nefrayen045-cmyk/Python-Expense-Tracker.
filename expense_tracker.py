expenses = []

def add_expense():
    description = input("Description : ")
    amount = float(input("Montant : "))
    expenses.append({"description": description, "amount": amount})
    print("Depense ajoutee !")

def show_expenses():
    if len(expenses) == 0:
        print("Aucune depense enregistree.")
    else:
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}. {expense['description']} - {expense['amount']:.2f}")

def show_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total : {total:.2f}")

def delete_expense():
    if not expenses:
        print("Aucune depense enregistree.")
        return

    show_expenses()
    try:
        number = int(input("Numero de la depense a supprimer : "))
    except ValueError:
        print("Numero invalide.")
        return

    if 1 <= number <= len(expenses):
        deleted = expenses.pop(number - 1)
        print(f"Depense supprimee : {deleted['description']}")
    else:
        print("Numero invalide.")

def main():
    while True:
        print("\n===== SUIVI DES DEPENSES =====")
        print("1. Ajouter une depense")
        print("2. Afficher les depenses")
        print("3. Afficher le total")
        print("4. Quitter")
        print("5. Supprimer une depense")

        choice = input("Votre choix : ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Au revoir !")
            break
        elif choice == "5":
            delete_expense()
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
