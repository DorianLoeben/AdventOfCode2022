

def getText(path):
	with open(path, 'r') as f:
		return f.read()
def getLines(path):
	return getText(path).splitlines()
def getSplitByEmptyLines(path):
	return getText(path).split('\n\n')
def getSplitByEmptyLinesSplitStripped(path):
	return list(map(lambda x: list(map(lambda x: x.strip(), x.split())), getSplitByEmptyLines(path)))
def formatToNums(l):
	if len(l) == 0:
		return l
	if type(l[0]) == list:
		return list(map(formatToNums, l))
	if type(l[0]) == str:
		return list(map(int, l))
def parseCommandList(path, types=None):
	if types is None:
		types = [str, int]
	lines = list(map(lambda x: x.split(), getLines(path)))
	return [tuple(types[i](v) for i,v in enumerate(l)) for l in lines]
# Empty Line before and after:
# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19
def createMatrixFromText(text, forcetype=None):
	if forcetype is None:
		return list(map(lambda x: list(x.split()), text.splitlines()))
	else:
		return list(map(lambda x: list(map(forcetype, x.split())), text.splitlines()))
def pointMapDict(text, splitChars=' -> ', inputMapFunc=None, outputMapFunc=None):
	mapped = map(lambda x: x.split(splitChars), text.splitlines())
	if inputMapFunc is not None:
		mapped = map(lambda x: [inputMapFunc(x[0]), x[1]], mapped)
	if outputMapFunc is not None:
		mapped = map(lambda x: [x[0], outputMapFunc(x[1])], mapped)
	return dict(mapped)
def pointMapList(text, splitChars=' -> ', inputMapFunc=None, outputMapFunc=None):
	mapped = map(lambda x: x.split(splitChars), text.splitlines())
	if inputMapFunc is not None:
		mapped = map(lambda x: [inputMapFunc(x[0]), x[1]], mapped)
	if outputMapFunc is not None:
		mapped = map(lambda x: [x[0], outputMapFunc(x[1])], mapped)
	return list(map(tuple, mapped))
def createPointFromString(string):
	return tuple(map(int, string.split(',')))


