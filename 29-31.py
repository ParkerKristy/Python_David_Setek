print("Vítejte na horské dráze")
height = int(input("Jaká je vaše výška v cm?\n"))
bill = 0

if height >= 87:
    print("Můžete jet na horské dráze.")
    age = int(input("Jaký je Váš věk?\n"))
    if age < 12:
        bill = 50
        print("Cena Vašeho lístku je 50 Kč.")
    elif age < 18:
        bill = 100
        print("Cena Vašeho lístku je 100 Kč.")
    else:
        bill = 150
        print("Cena Vašeho lístku je 150 Kč.")

    photo = input("Chcete se během jízdy vyfotit? (ano/ne)\n")
    if photo == "ano":
        bill += 40
        print(f"Celková cena vstupenky s fotkou je {bill} Kč.")

else:
    print("Omlouváme se, ale na horské dráze jet nemůžete.")