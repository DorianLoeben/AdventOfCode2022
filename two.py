import aoc_utils

def rate(choice_tuple): # ('A', 'X') if both chose rock
	scores = dict([
		('A', 1), # Rock
		('B', 2), # Paper
		('C', 3), # Scissors
		('X', 1), # Rock
		('Y', 2), # Paper
		('Z', 3), # Scissors
	])
	# We are the second player
	certain_score = scores[choice_tuple[1]]
	result = 0 # 3 = tie, 6 = win, 0 = loss/draw
	if scores[choice_tuple[0]] == scores[choice_tuple[1]]:
		result = 3
	elif choice_tuple[0] == 'A' and choice_tuple[1] in ['Y', 'B']:
		result = 6
	elif choice_tuple[0] == 'B' and choice_tuple[1] in ['Z', 'C']:
		result = 6
	elif choice_tuple[0] == 'C' and choice_tuple[1] in ['X', 'A']:
		result = 6
	return certain_score + result
def convertRates(choice_tuple):
	if(choice_tuple[1] == 'Y'):
		return (choice_tuple[0], choice_tuple[0])
	elif(choice_tuple[1] == 'Z'):
		if(choice_tuple[0] == 'A'):
			return ('A', 'B')
		elif(choice_tuple[0] == 'B'):
			return ('B', 'C')
		elif(choice_tuple[0] == 'C'):
			return ('C', 'A')
	elif(choice_tuple[1] == 'X'):
		if(choice_tuple[0] == 'A'):
			return ('A', 'C')
		elif(choice_tuple[0] == 'B'):
			return ('B', 'A')
		elif(choice_tuple[0] == 'C'):
			return ('C', 'B')
	raise(f"Invalid choice tuple: {str(choice_tuple)}")
	

def main():
	txt = aoc_utils.pointMapList(aoc_utils.getText('./two/two-input'),
		splitChars=' ')
	rates = list(map(rate, txt))
	properChoices = list(map(convertRates, txt))
	properRates = list(map(rate, properChoices))
	print(f"Answer 1: {sum(rates)}")
	#print(f"Answer 2: {properRates}")
	print(f"Answer 2: {sum(properRates)}")

if __name__ == "__main__":
    main()