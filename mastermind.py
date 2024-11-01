#mastermind
import random

def main():
	possible_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	goal = get_goal(possible_nums)
	print(goal)
	accuracy = []
	while accuracy != ['green', 'green', 'green', 'green']:
		guess = get_guess()
		print(guess)
		accuracy = get_accuracy(goal, guess)
		print(accuracy)
	print("congrats, you win!")

def get_goal(possible_nums):
	random.shuffle(possible_nums)
	_goal = possible_nums[6:]
	return(_goal)

def get_guess():
	_continue = True
	while _continue:
		_guess = input('What is your guess: ')
		if len(_guess) != 4:
			print('please enter a 4 charecter integer') 
		else:
			_continue = False
	_guess = list(_guess)
	return(_guess)

def get_accuracy(_goal, _guess):
	_accuracy = []
	for i in range(len(_goal)):
		try:
			if i == _goal.index(int(_guess[i])):
				_accuracy.append("green")
			else:
				_accuracy.append("yellow")
		except:
			pass
	
	if _accuracy == []:
		_accuracy.append('red')
	_accuracy.sort()
	return(_accuracy)
		
#-----------------------#

do_again = True

while do_again:
	main()
	while play == y or play == n:
		play = input('would you like to play again(y or n)')
		if play != y or play != n:
			print("please enter y or n")
	if play == n:
		do_again = False




