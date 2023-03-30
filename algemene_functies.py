def mijn_functie1(x):
    return x ** x

def mijn_functie2(lst):
    resultaat = []
    for num in lst:
        nieuw_nummer = num * 3 + 1
        resultaat.append(nieuw_nummer ** 2)
    return resultaat

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer