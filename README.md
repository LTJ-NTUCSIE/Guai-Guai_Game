# Guai-Guai_Game
A Simple Sorting Game.  

Given a randomized order of 1-9, your goal is to sort them into ascending order with following rules.
1. Choose 2 numbers to swap at a time.
2. In the first round, you can arbitually choose 2 numbers to swap.
3. Except the first round, you can choose a number to swap with the number that equals to the sum of the previous swapping numbers. For example, if you chose 3 and 4 to swap in the previous round, you will choose a number to swap with 7 in the current round.
4. If the sum of previous choices are bigger or equal to 10, then use the sum of the digits of the sum of the previous choices (My English is bad as hell). For example, if you chose 6 and 7 in the previous round, then the sum of it is 13.Therefore, you'll choose a number to swap with 1+3=4 in the current round.
5. Good Luck and Have Fun.

## How to use
Clone the Repo and cd in
```shell
$ git clone https://github.com/LTJ-NTUCSIE/Guai-Guai_Game.git
$ cd Guai-Guai_Game
```
Create a virtual environment :)
```shell 
$ python3 -m venv .venv
```
Then activate it by
```shell
$ source .venv/bin/activate
```
Then install what we need by
```shell
$ pip install -r requirement.txt
```
Then simply run the program by
```shell 
$ ./GuaiSorting.py
```
To deactive it after finishing the game, please type the below command in your shell.
```shell 
$ deactivate
```
