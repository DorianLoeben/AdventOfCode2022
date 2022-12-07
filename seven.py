import aoc_utils
import itertools
import re


def main():
	pre = list(map(lambda x: x.split(), aoc_utils.getLines("./seven/seven-input")))
	folderStructure = {}
	currentFolder = ""
	line = 0
	for line in pre:
		if line[0] == '$': # command
			if line[1] == 'cd':
				if line[2] == '..':
					currentFolder = currentFolder[:currentFolder.rfind('/', 0, len(currentFolder)-1)+1]
				elif line[2] == '/':
					currentFolder = "/"
				else:
					currentFolder += f"{line[2]}/"
			elif line[1] == 'ls':
				pass
		else: # file
			filename = line[1]
			filesize = line[0]
			currentFolderSplit = currentFolder.split('/')
			currentFolderDict = folderStructure
			for f in currentFolderSplit:
				if f == '':
					continue
				currentFolderDict = currentFolderDict[f]
			currentFolderDict[filename] = {} if filesize == 'dir' else filesize
	#print(folderStructure)
	properDict = {"root": folderStructure}
	def folderSize(path):
		pathsplit = path.split('/')
		pathDict = properDict
		for p in pathsplit:
			if p == '':
				continue
			pathDict = pathDict[p]
		if type(pathDict) == str:
			return int(pathDict)
		else:
			return sum(map(lambda x: folderSize(path + "/" + x), pathDict.keys()))

	# Iterate through all directories and subdirectories
	# and find all directories with a size of at most 100000

	atMost100000 = []
	def SizeCheck(path):
		foldersize = folderSize(path)
		#print(path, foldersize)
		if foldersize <= 100000:
			atMost100000.append(path)
		pathsplit = path.split('/')
		pathDict = properDict
		for p in pathsplit:
			if p == '':
				continue
			pathDict = pathDict[p]
		pathDict = {pathsplit[-1]: pathDict} # hacky
		for k in pathDict[pathsplit[-1]].keys():
			if type(pathDict[pathsplit[-1]][k]) == str:
				continue
			SizeCheck(f"{path}/{k}")

	SizeCheck("root")
	#for path in atMost100000:
	#	print(path, folderSize(path))
	atMost100000 = list(set(atMost100000))
	print(f"Antwort 1: {sum(map(lambda x: folderSize(x), atMost100000))}")
	totalSpace = 70000000
	currentSpace = totalSpace - folderSize("root")
	spaceToFree = 30000000 - currentSpace
	
	allFolders = []
	def getAllFolders(path):
		allFolders.append(path)
		pathsplit = path.split('/')
		pathDict = properDict
		for p in pathsplit:
			if p == '':
				continue
			pathDict = pathDict[p]
		pathDict = {pathsplit[-1]: pathDict}
		for k in pathDict[pathsplit[-1]].keys():
			if type(pathDict[pathsplit[-1]][k]) == str:
				continue
			allFolders.append(f"{path}/{k}")
			getAllFolders(f"{path}/{k}")
	getAllFolders("root")
	allFolders = sorted(list(set(allFolders)), key=lambda x: folderSize(x))
	#print(allFolders)
	for f in allFolders:
		if folderSize(f) > spaceToFree:
			print(f"Antwort 2: {folderSize(f)}")
			break





	
	





if __name__ == "__main__":
	main()