mijn_prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
mijn_prijzen["vanille"] = 4 * 0.8
aanbieding = mijn_prijzen["vanille"]
a = "vanille"
"vanille" == 3.2
reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €"
str1 = reclame_tekst
str2 = 3.2
print(reclame_tekst, aanbieding)
reclame_tekst1 = str1 + " 3.2"
print(f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{a}")
print(reclame_tekst1)
reclame_tekst2 = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € 2.4000000000000004"
print(reclame_tekst2[:62])
reclame_tekst3 = reclame_tekst1.upper()
print(reclame_tekst3[:62])
reclame_tekst4 = reclame_tekst3.split(" ")
print(reclame_tekst4)
for c in reclame_tekst4:
    print(reclame_tekst4)
