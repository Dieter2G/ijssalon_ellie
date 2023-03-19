mijn_dictionary = { 
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
mijn_dictionary["vanille"] = 4 * 0.8
aanbieding = mijn_dictionary["vanille"]
tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € "
a = mijn_dictionary["vanille"]
reclame_tekst = tekst + "3.2" 
print(f"Vandaag in de aanbieding: vanille-ijs, 1 liter € {a}")
#Hoe kom je hier aan? 2.40000000004?
reclame_tekst2 = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € 2.4000000000000004"
print(reclame_tekst2[:62])
reclame_tekst3 = reclame_tekst.upper()
print(reclame_tekst3[:62])
reclame_tekst4 = reclame_tekst3.split(" ")
print(reclame_tekst4)
#Hier doe ik iets mis, ik weet niet precies wat, de formule gaat niet kloppen
if 3 <= len(reclame_tekst4):
    print(reclame_tekst4.lower())
else:
    print(reclame_tekst4.upper)