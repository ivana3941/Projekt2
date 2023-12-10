"""

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Ivana ROHOVÁ

email: bytypr@gmail.com

discord: Ivana #3941

"""
import os
import random


def vytvor_hadane_cislo() -> str:
    """
    Vytvoří hádané číslo o 4 číslicích, bez opakování a nezačínající nulou.

    Příklad:
    >>> vysledek = vytvor_hadane_cislo()
    >>> vysledek
    "3820"
    """
    numbers = [str(i) for i in range(0, 10)]
    while True:
        random.shuffle(numbers)
        if numbers[0] != "0":
            break
    return "".join(numbers[:4])


def kontrola_tipu(tip: str) -> bool:
    """
    Vrátí True, je-li tip číslo o 4 číslicích bez opakování a nezačínající nulou.
    """
    if not tip.isnumeric():
        print("Not a number. Try again.")
        return False
    if len(tip) != 4:
        print ("Number is too short or long. Try again.")
        return False
    if len(tip)!=len(set(tip)):
        print("You repeated numbers. Try again.")
        return False
    if tip[0] == "0":
        print("First number cannot be zero. Try again.")
        return False
    return True


def vyhodnoceni_tipu(cislice: str, tip: str) -> tuple[int, int]:
    """
    Každou číslici z parametru "tip" porovná s číslicí na stejné pozici v parametru "cislice" a
    je-li stejná, pak jde o Bull. Vyskytuje-li se tato číslice jinde v parametru "cislice", pak jde o Cow.
    Vrátí tuple s celkovým počtem Bulls a Cows.
    """
    bulls = 0
    cows = 0

    for i in range(len(cislice)):
        if cislice[i] == tip[i]:
            bulls += 1
        elif cislice[i] in tip:
            cows += 1

    return bulls, cows


def hra() -> None:
    os.system("cls")
    tipy = []

    hadane_cislo = vytvor_hadane_cislo()

    print("Hi there!")
    oddelovac = "-" * 50
    print(oddelovac)
    print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    print(oddelovac)

    while True:
        tip = input("Enter a number: ")

        if not kontrola_tipu(tip):
            continue

        tipy.append(tip)


        if tip == hadane_cislo:
            print(oddelovac)
            print(f"Correct, you've guessed the right number: {tipy[-1]}.")
            print(oddelovac)
            if len(tipy) <= 5:
                print(f"You guessed the number in {len(tipy)} guesses. That's amazing !!! \nHere are your guesses: {tipy}")
            elif 5 < len(tipy) <= 10:
                print(f"You guessed the number in {len(tipy)} guesses. That's very good! \nHere are your guesses: {tipy}")
            elif 10 < len(tipy) <= 20:
                print(f"You guessed the number in {len(tipy)} guesses. That's average...  \nHere are your guesses: {tipy}")
            elif 20 < len(tipy):
                print(f"You guessed the number in {len(tipy)} guesses. That's not good!!! :-( Try it again! \nHere are your guesses: {tipy}")
            print(oddelovac)
            break
        else:
            print(oddelovac)
            bulls, cows = vyhodnoceni_tipu(hadane_cislo, tip)
            print(f">>>  {tipy[-1]}")
            if bulls == 1 and cows != 1:
                print(f"Bull: {bulls}, Cows: {cows}")
            elif cows == 1 and bulls != 1:
                print(f"Bulls: {bulls}, Cow: {cows}")
            elif cows == 1 and bulls == 1:
                print(f"Bull: {bulls}, Cow: {cows}")
            else: 
                print (f"Bulls: {bulls}, Cows: {cows}")
            print(oddelovac)


if __name__ == "__main__":
    hra()
    