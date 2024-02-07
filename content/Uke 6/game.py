print("Gjett hvilket tall jeg tenker på!")

svar = int(input("Du gjetter: "))
from random import seed, randint as tilfeldig_heltall

seed(42)

print("Seed is 42")

def sjekk_svar(gjett: int, riktigt_tall: int) -> bool:
    if gjett == riktig_tall:
        print("Riktig! Du vant spillet 🥳")
        return True
    elif gjett < riktig_tall:
        print("Tallet er ⬆⬆⬆")
        return False
    elif svar > riktig_tall: 
        print("Tallet er ⬇⬇⬇")
        return False
    else:
        svar = int(input("Gjett igjen: "))
        return False

riktig_tall = tilfeldig_heltall(0,9)

sjekk_svar(svar, riktig_tall)

print("Du tapte 😝")
print(f"Tallet du skulle gjette til var {riktig_tall}")
