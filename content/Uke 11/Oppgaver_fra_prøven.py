# Med elif - altså ellers hvis
# Oppgave: Hva blir printet ut? (linje 13)
tall = 10

if tall <= 0:
    svar = "ingen"
elif tall <= 5:
    svar = "noen"
elif tall <= 10:
    svar = "flere"
elif tall <= 100:
    svar = "mange"
print(svar)

# Uten elif - altså uten ellers hvis
# Oppgave: Hva blir printet ut? (linje 27)
tall = 10

if tall <= 0:
    svar = "ingen"
if tall <= 5:
    svar = "noen"
if tall <= 10:
    svar = "flere"
if tall <= 100:
    svar = "mange"
print(svar)

# Oppgave: Forklar hva denne koden gjør
alder = int(input("Hvor gammel er du?"))

if alder < 18:
    print("Du er ikke myndig")
else:
    print("Du er myndig")


# Koden under er en modifisert utgave av et svar på oppgaven fra https://codingbat.com/prob/p135815
# Oppgave: forklar hva koden gjør
temp = 60 
is_summer = False

if is_summer:
    if temp >= 60 and temp <=100:
        play_outside = True
    else:
        play_outside = False
        
elif temp >= 60 and temp <= 90:
    play_outside = True

else:
    play_outside = False

print(play_outside)