# Přestupý rok

year = int(input("Zadejte rok:\n"))

# if year % 4 == 0:
#     if year % 100 == 0: 
#         if year % 400 == 0:     
#             print("Tento rok je přestupný.")
#         else:
#             print("Tento rok není přestupný.")
#     else: 
#         print("Tento rok je přestupný.")    
# else:
#     print("Tento rok není přestupný.")


if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print("Tento rok je přestupný.")
else:
    print("Tento rok není přestupný.") 