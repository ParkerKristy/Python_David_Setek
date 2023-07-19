# BMI Calculater

weight = float(input("Zajdete svou váhu v kg (x.y):\n"))
height = float(input("Zajdete svou výšku v m (x.yy):\n"))
               
bmi = weight/(height*height)
bmi = round(bmi,1)

if bmi < 18.5:
    print(f"Vaše BMI je {bmi}, což spadá do kategorie podváha.")
elif bmi <= 24.9:
    print(f"Vaše BMI je {bmi}, což spadá do kategorie norma.")
elif bmi <= 29.9:
    print(f"Vaše BMI je {bmi}, což spadá do kategorie nadváha.")
elif bmi <= 34.9:
    print(f"Vaše BMI je {bmi}, což spadá do kategorie obezita.")
else:
    print(f"Vaše BMI je {bmi}, což spadá do kategorie extrémní obezita. Vysoké riziko kardiovaskulárních chorob. ")
   

# podváha >18,5
# norma 18,5-24,9 
# nadváha 25,0-29,9
# obezita 30,0-34,9
# extrémní obezita <35