import aoc_utils
import itertools


			

def main():
	pairs = list(map(lambda x: x.split(','), aoc_utils.getLines('./four/four-input')))
	def reformat(pair):
		pair = (tuple(map(int,pair[0].split('-'))), tuple(map(int,pair[1].split('-'))))
		return pair
	pairs = list(map(reformat, pairs))
	def AtLeastOneIsSubset(pair):
		if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
			return True
		if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
			return True
		return False
	def AnyOverlap(pair):
		if pair[0][1] < pair[1][0] or pair[0][0] > pair[1][1]:
			return False
		return True
	full_subsets = list(filter(AtLeastOneIsSubset, pairs))
	print(f"Answer 1: {len(full_subsets)}")
	full_subsets = list(filter(AnyOverlap, pairs))
	print(f"Answer 2: {len(full_subsets)}")





if __name__ == "__main__":
	main()