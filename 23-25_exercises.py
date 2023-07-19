# 23 video
age = int(input("Zadej svůj věk:\n"))
average_age = 90

print(f"Do konce života ti zbývá:\n{average_age-age} let,\n{(average_age-age)*12} měsíců,\n{(average_age-age)*52} týdnů,\n{(average_age-age)*365} dní.")


# 24 video
print("Vítejte v kalkulátoru na výpočet plateb")
price = int(input("Kolik máte celkem zaplatit: "))
gratuities = int(input("Kolik chcete dát spropitného (v %): "))
person = int(input("Mezi kolik lidí se má rozdělit částka: "))

price_each = (price + (price/100*gratuities))/person

print(f"Každý člověk by měl zaplatit {price_each} Kč.")


# 25 video
print("Vítejte v kalkulátoru na výpočet plateb")
price = int(input("Kolik máte celkem zaplatit: "))
gratuities = int(input("Kolik chcete dát spropitného (v %): "))
person = int(input("Mezi kolik lidí se má rozdělit částka: "))

price_each = round((price + (price/100*gratuities))/person,2)
final_price = "{:.2f}".format(price_each) # aby int měl 2 desetinná místa

print(f"Každý člověk by měl zaplatit {final_price} Kč.")