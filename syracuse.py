def syracuse(n):
    u0 = n
    tv = 0
    am = u0
    tva = 0
    a = n
    while a != 1 :
        if a % 2 == 0 :
            a = a / 2
        else :
            a = a * 3 + 1
        tv = tv + 1
        if a > u0 :
            tva += 1
        else :
             tva = tva
        if a > am :
            am = a
        else :
            am = am
    return tv, tva, am


    # tant que la suite n'est pas terminée :
    #   - calcul du n suivant
    #   - mise à jour du temps de vol (tv)
    #   - mise à jour du temps de vol en altitude (tva) si nécessaire
    #   - mise à jour de l'altitude maximale (am)

    # retour de tv, tva, am
def main():
    # exemple d'exécution
    n = 127
    tv, tva, am = syracuse(n)
    print(n, tv, tva, am)

if __name__ == "__main__":
    main()
    résultat = syracuse (127)
    print (résultat)
