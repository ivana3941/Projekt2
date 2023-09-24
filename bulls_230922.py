
import os
import random

print("Hi there!")
oddelovac = "-" * 50
print(oddelovac)
print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
print(oddelovac)


def vytvor_hadane_cislo():
    numbers = [str(i) for i in range(1, 10)]
    random.shuffle(numbers)
    return "".join(numbers[:4])

#def generate_unique_number():
 #   while True:
  #      number = random.sample(range(10), 4) 
   #     if number[0] == 0:
    #        continue  
     #   unique_number = int(''.join(map(str, number)))
      #  if 1000 <= unique_number <= 9999:
       #     return unique_number

# generated_numbers = set()
hadane_cislo = str(vytvor_hadane_cislo())

def hra():
    os.system("cls")
    hadane_cislo
    tipy = []

    while True:
        tip = input("Enter a number: ")
        
        tipy.append(tip)

        if not tip.isnumeric():
            print("Not a number, terminating the program...")
            quit()
        if len(tip) != 4:
            print ("Number is too short or long, terminating the program...")
            quit()


  #      def opakovana_cisla(number):
   #         digit_str = str(number)
    #        return len(set(digit_str)) < len(digit_str)
     #   if opakovana_cisla(tip) == True:
      #      print("You repeated numbers. Terminating the program...")
       #     quit()

 	
        if len(tip)!=len(set(tip)):
            print("You repeated numbers. Terminating the program...")
            quit()
            
        def zacina_nulou(tip):
            cislo = str(tip)
            return cislo[0] == "0"
        if zacina_nulou(tip) == True:
            print("First number cannot be zero, terminating the program...")
            quit()

        def vyhodnoceni(cislice, tip):
            bulls = 0
            cows = 0

            for i in range(len(cislice)):
                if cislice[i] == tip[i]:
                    bulls += 1
                elif cislice[i] in tip:
                    cows += 1

            return bulls, cows

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
            bulls, cows = vyhodnoceni(hadane_cislo, tip)
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
    