import aoc_utils
import itertools
import re

def findStartMarker(line : str) -> int:
	for i,v in enumerate(line):
		if i < 4:
			continue
		slidingBox = line[i-4:i]
		if(len(set(slidingBox)) == 4): # marker found
			return i
	return -1
def findMessageMarker(line : str) -> int:
	for i,v in enumerate(line):
		if i < 14:
			continue
		slidingBox = line[i-(14):i]
		if(len(set(slidingBox)) == 14): # marker found
			return i
	return -1

def main():
	pre = aoc_utils.getLines("./six/six-input")[0]
	startmarker = findStartMarker(pre)
	print(f"Answer 1: {startmarker}")
	messageMarker = findMessageMarker(pre)
	print(f"Answer 2: {messageMarker}")

	
	





if __name__ == "__main__":
	main()