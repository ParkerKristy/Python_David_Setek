print("Vítejte na horské dráze")
height = int(input("Jaká je vaše výška v cm?\n"))
bill = 0

if height >= 87:
    print("Můžete jet na horské dráze.")
    age = int(input("Jaký je Váš věk?\n"))
    if age < 12:
        bill = 50
        print("Cena Vašeho lístku je 50 Kč.")
    elif age>= 12 and age < 18:
        bill = 100
        print("Cena Vašeho lístku je 100 Kč.")
    elif age >= 40 and age <=50: #obě podmínky musí platit současně
        print("Speciální AKCE!!")
        print(f"Vaše cena je: {bill} Kč.")
    else:
        bill = 150
        print("Cena Vašeho lístku je 150 Kč.")

    photo = input("Chcete se během jízdy vyfotit? (ano/ne)\n").lower()
    if photo == "ano":
        bill += 40
        print(f"Celková cena vstupenky s fotkou je {bill} Kč.")

    
else:
    print("Omlouváme se, ale na horské dráze jet nemůžete.")