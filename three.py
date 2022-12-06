import aoc_utils
import itertools

def priority(string):
	prio = 0
	for i,v in enumerate(string):
		if(v.islower()):
			prio += ord(v) - ord('a') + 1
		elif(v.isupper()):
			prio += ord(v) - ord('A') + 26 + 1
	return prio
def antwort1(lines):
	def splitInHalf(string):
		return (string[:len(string)//2], string[len(string)//2:])
	rucksacks_split = list(map(splitInHalf, lines))
	def commonLetters(stringTuple):
		common = set()
		for i in range(len(stringTuple[0])):
			if stringTuple[0][i] in stringTuple[1]:
				common.add(stringTuple[0][i])
		return (stringTuple[0], stringTuple[1], "".join(common))
	rucksacks_withCommon = list(map(commonLetters, rucksacks_split))
	#print(rucksacks_withCommon)
	prios = list(map(lambda x: priority(x[2]), rucksacks_withCommon))
	print(f"Answer 1: {sum(prios)}")

def antwort2(lines):
	setified = list(map(set, lines))
	score = 0
	for i in range(0, len(setified), 3):
		groupHeader = setified[i] & setified[i+1] & setified[i+2]
		score += priority("".join(groupHeader))
	print(f"Answer 2: {score}")
			

def main():
	rucksacks = aoc_utils.getLines('./three/three-input')
	antwort1(rucksacks)
	antwort2(rucksacks)





if __name__ == "__main__":
	main()