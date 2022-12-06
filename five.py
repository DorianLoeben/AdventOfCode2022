import aoc_utils
import itertools
import re

			

def main():
	pre = aoc_utils.getLines("./five/five-input")
	start = next((i for i, line in enumerate(pre) if "1   2   3" in line), 0)
	#     [D]    
	# [N] [C]    
	# [Z] [M] [P]
	# 1   2   3 
	setup = list(pre[:start])
	instructions = list(pre[start+2:])
	# move 1 from 2 to 1
	# move 3 from 1 to 3
	# move 2 from 2 to 1
	# move 1 from 1 to 2
	# format to 1,2,1
	instructions = [tuple(map(int, re.findall(r'\d+', i))) for i in instructions]

	# Get Stacks
	stacks = len(setup)
	columns = []
	for i in range(stacks):
		columns.append(list(setup[i][1::4]))
	# invert
	columns = list(zip(*columns))
	# Remove spaces
	columns = [list(filter(lambda x: x != ' ', i)) for i in columns]
	def move(num : int, origin : int, destination : int): # 9000
		# Take from front of origin
		# Add to front of destination
		origin -= 1
		destination -= 1
		for i in range(num):
			columns[destination] = columns[origin][:1] + columns[destination]
			columns[origin] = columns[origin][1:]
	
	def move2(num : int, origin : int, destination : int): # 9000
		# Take from front of origin
		# Add to front of destination
		origin -= 1
		destination -= 1
		columns[destination] = columns[origin][:num] + columns[destination]
		columns[origin] = columns[origin][num:]

	columns_start_copy = [x.copy() for x in columns]

	#print(columns)
	for instruction in instructions:
		move(*instruction)
		#print(columns)
	print("Answer 1: " + "".join([i[0] for i in columns]))
	columns = columns_start_copy
	for instruction in instructions:
		move2(*instruction)
	print("Answer 2: " + "".join([i[0] for i in columns]))
	





if __name__ == "__main__":
	main()