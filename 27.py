# age = int(input("Zadejte svůj věk:\n"))

# if age >= 18:
#     print("Jste dospělý.")
# else:
#     print("Nejste dospělý.")

adult = 150 
student = 120

status = input("Jste student? (ano/ne)\n")
if status == "ano" or "ANO" or "Ano":
    print(f"Cena vašeho lístku je {student} Kč.")
else:
    print(f"Cena Vašeho lsítku je {adult} Kč.")    