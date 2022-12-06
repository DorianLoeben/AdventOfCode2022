import aoc_utils

def main():
	parsed = aoc_utils.formatToNums(aoc_utils.getSplitByEmptyLinesSplitStripped('./one/one-input'))
	summed = list(map(sum, parsed))
	sorted_elfs = sorted(summed)
	print(f"Answer 1: {sorted_elfs[-1]}")
	print(f"Answer 2: {sum(sorted_elfs[-3:])}")

if __name__ == "__main__":
    main()