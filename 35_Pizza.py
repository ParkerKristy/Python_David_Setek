print("Vítejte v Pizzeria Kristy!")

bill = 0
# small = 100
# medium = 150
# large = 200
# extra_cheese = 15
# hot_pepper_s = 20
# hot_pepper_m_l = 30

size = input("Jakou velikost pizzy chcete (S/M/L):\n")
pepper = input("Chcete extra feferonky navíc? ano/ne\n")
cheese = input("Chcete extra sýr navíc? ano/ne\n")

# if size == "S":
#     bill += 100
#     if pepper == "ano":
#         bill += 20
#     if cheese == "ano":
#         bill += 15
# elif size == "M":
#     bill += 150
#     if pepper == "ano":
#         bill += 30
#     if cheese == "ano":
#         bill += 15
# elif size == "L":
#     bill += 200
#     if pepper == "ano":
#         bill += 30
#     if cheese == "ano":
#         bill += 15

if size == "S":
    bill += 100
elif size == "M":
    bill += 150
elif size == "L":
    bill += 200

if pepper == "ano":
    if size != "S":
        bill +=30
    else:
        bill +=20

if cheese == "ano":
    bill += 15

print(f"Váš účet za pizzu je {bill} Kč.")