alder = int(input("Hvor gammel er du?"))

if alder < 18:
    print("Du er ikke myndig")
else:
    print("Du er myndig")


# Koden under er en modifisert utgave av et svar på oppgaven fra https://codingbat.com/prob/p135815
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