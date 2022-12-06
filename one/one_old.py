def parse():
    with open('one-input', 'r') as f:
        lines = f.readlines()
        curElfSum = 0
        results = []
        for line in lines:
            if(line[0] == '\n'):
                results.append(curElfSum)
                curElfSum = 0
            else:
                curElfSum += int(line)
        results.append(curElfSum)
    return results


def main():
    elfs = parse()
    sortedElfs = sorted(enumerate(elfs), key=lambda x: x[1], reverse=True)
    print(f"Answer 1: {sortedElfs[0][1]}")
    print(f"Answer 2: {sum(map(lambda x: x[1], sortedElfs[:3]))}")

if __name__ == "__main__":
    main()