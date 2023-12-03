Program, který simuluje hru Bulls and Cows.

1)	Program pozdraví užitele a vypíše úvodní text
2)	Program vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
3)	Hráč hádá číslo
4)	Program jej upozorní pokud zadané číslo:
	a) je kratší nebo delší než 4 čísla
	b) obsahuje duplicity
	c) začíná nulou
	d) obsahuje nečíselné znaky

5)	Program vyhodnotí tip uživatele:
	    	Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění)
		cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění)
		

            

*******************
Příklad hry s číslem 3246:

Let's play a bulls and cows game! Enter a number: 1234
--------------------------------------------------
>>>  1234
Bull: 1, Cows: 2
--------------------------------------------------
Enter a number: 1345
--------------------------------------------------
>>>  1345
Bull: 1, Cow: 1
--------------------------------------------------
Enter a number: 1432
--------------------------------------------------
>>>  1432
Bulls: 0, Cows: 3
--------------------------------------------------
Enter a number: 1435
--------------------------------------------------
>>>  1435
Bulls: 0, Cows: 2
--------------------------------------------------
Enter a number: 3246
--------------------------------------------------
Correct, you've guessed the right number: 3246.
--------------------------------------------------
You guessed the number in 5 guesses. That's amazing !!!
Here are your guesses: ['1234', '1345', '1432', '1435', '3246']


****************************************

 <= 5: That's amazing !!! 

 6-10: That's very good!
11-20: That's average...
víc než 20 pokusů: That's not good!!! :-( Try it again! 

Program vypíše tipy:
Here are your guesses:


Příklad chybného tipu:

*****
Enter a number: 1123
You repeated numbers. Terminating the program...

*******
Let's play a bulls and cows game. Enter a number: ghjk
Not a number, terminating the program...
