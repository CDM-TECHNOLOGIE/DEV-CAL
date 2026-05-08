import os
import math

# ===== CONFIG =====
MOT_DE_PASSE = "Terrorcdm"

# Couleurs ANSI
VERT = "\033[92m"
ROUGE = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ===== LOGIN =====
def login():
    tentatives = 3

    while tentatives > 0:
        mdp = input(VERT + "Mot de passe CDM-TECH : " + RESET)

        if mdp == MOT_DE_PASSE:
            print(VERT + "\n[ ACCÈS AUTORISÉ ]\n" + RESET)
            return True
        else:
            tentatives -= 1
            print(ROUGE + f"Incorrect ! Tentatives restantes : {tentatives}" + RESET)

    print(ROUGE + "\n[ ACCÈS REFUSÉ ]" + RESET)
    return False

# ===== MENU =====
def menu():
    print(VERT + "\n=== CDM-TECH CALCULATOR ===" + RESET)
    print(CYAN + "[1] Addition")
    print("[2] Soustraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Racine carrée")
    print("[6] Exponentiation")
    print("[7] Log (log10)")
    print("[8] Cos (radian)")
    print("[9] Tan (radian)")
    print("[10] Cotan (radian)")
    print("[11] Combinaison nCr")
    print("[0] Quitter" + RESET)

# ===== CALCULATRICE =====
def calculatrice():
    while True:
        menu()
        choix = input(VERT + "\nChoix : " + RESET)

        try:
            # ===== SORTIE =====
            if choix == "0":
                print(ROUGE + "\n[ SYSTEM OFFLINE ]" + RESET)
                break

            # ===== OPERATIONS DE BASE =====
            elif choix in ["1", "2", "3", "4", "6"]:
                a = float(input("Nombre 1 : "))

                if choix != "5":
                    b = float(input("Nombre 2 : "))

                if choix == "1":
                    print(VERT + f"Résultat : {a + b}" + RESET)

                elif choix == "2":
                    print(VERT + f"Résultat : {a - b}" + RESET)

                elif choix == "3":
                    print(VERT + f"Résultat : {a * b}" + RESET)

                elif choix == "4":
                    if b == 0:
                        print(ROUGE + "Erreur : division par 0 !" + RESET)
                    else:
                        print(VERT + f"Résultat : {a / b}" + RESET)

                elif choix == "6":
                    print(VERT + f"Résultat : {a ** b}" + RESET)

            # ===== RACINE =====
            elif choix == "5":
                a = float(input("Nombre : "))
                if a < 0:
                    print(ROUGE + "Erreur : nombre négatif !" + RESET)
                else:
                    print(VERT + f"Résultat : {math.sqrt(a)}" + RESET)

            # ===== LOG =====
            elif choix == "7":
                a = float(input("Nombre : "))
                if a <= 0:
                    print(ROUGE + "Erreur : log invalide !" + RESET)
                else:
                    print(VERT + f"Résultat : {math.log10(a)}" + RESET)

            # ===== COS =====
            elif choix == "8":
                a = float(input("Angle (radian) : "))
                print(VERT + f"Résultat : {math.cos(a)}" + RESET)

            # ===== TAN =====
            elif choix == "9":
                a = float(input("Angle (radian) : "))
                print(VERT + f"Résultat : {math.tan(a)}" + RESET)

            # ===== COTAN =====
            elif choix == "10":
                a = float(input("Angle (radian) : "))
                tan_val = math.tan(a)
                if tan_val == 0:
                    print(ROUGE + "Erreur : cotan indéfinie !" + RESET)
                else:
                    print(VERT + f"Résultat : {1 / tan_val}" + RESET)

            # ===== COMBINAISON nCr =====
            elif choix == "11":
                n = int(input("n : "))
                r = int(input("r : "))

                if r > n:
                    print(ROUGE + "Erreur : r > n !" + RESET)
                else:
                    print(VERT + f"Résultat : {math.comb(n, r)}" + RESET)

            else:
                print(ROUGE + "Choix invalide !" + RESET)

        except:
            print(ROUGE + "Erreur de saisie !" + RESET)

        input(CYAN + "\nEntrée pour continuer..." + RESET)
        clear()

# ===== START =====
clear()

if login():
    calculatrice()
