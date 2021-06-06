choice = int(input("""Entrez la valeur
1. Age Calcul Simple
2. Calcul de deux Age + Comparaison

[>] """))

if choice == 1:
    year = int(input("Entrez l'année actuelle: "))
    birth_year = int(input("Entrez votre année de naissance: "))
    age = year - birth_year
    print("Vous avez :", age, "ans")
elif choice == 2:
    year = int(input("Entrez l'année actuelle: "))
    birth_year = int(input("Entrez votre année de naissance: "))
    second_birth_year = int(input("Entrez l'année de naissance de l'autre personne: "))
    age = year - birth_year
    age_other = year - second_birth_year
    print(f"""Vous avez : {age} ans
    Il a : {age_other} ans""")
    age_comparaison = age - age_other
    print("Vous avez " + str(age_comparaison) + " ans d'écart.")
else:
    print("Erreur")
