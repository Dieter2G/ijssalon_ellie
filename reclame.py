from algemene_functies import combinatie

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertjes ijs (1 liter) in de smaak {smaak} van 4 euro naar {nieuwe_prijs} euro"

smaak = "aardbei"
prijs = 4
korting = 0.1
resultaat = aanbieding_1(smaak, prijs, korting)
print(resultaat)

def inkomsten_totaal(inkomsten):
    return sum(inkomsten)

inkomsten_deze_week = [220, 430, 125, 160, 205, 90, 345]
totaal_inkomsten = inkomsten_totaal(inkomsten_deze_week)
print(totaal_inkomsten)

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

btw = 0.09
resultaat = inkomsten_totaal(inkomsten_deze_week, btw)
print(resultaat)

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]

resultaat = laag_en_hoog(inkomsten_deze_week)
print(resultaat)

def gemiddelde(mijn_lijst):
    return sum(mijn_lijst) / len(mijn_lijst)

gemiddelde_inkomsten = gemiddelde(inkomsten_deze_week)
print(gemiddelde_inkomsten)

def gemiddelde(mijn_lijst):
    gemiddelde_bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag} euro."

gemiddelde_inkomsten = gemiddelde(inkomsten_deze_week)
print(gemiddelde_inkomsten)

def meervoudig(invoer_lijst):
    hoogste_waarde, laagste_waarde = laag_en_hoog(invoer_lijst)
    return [hoogste_waarde, laagste_waarde]

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
resultaat = meervoudig(invoer_lijst)
print(resultaat)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)

