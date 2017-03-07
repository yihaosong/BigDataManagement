import sys
if __name__=='__main__':
	myList = []
	for fileName in sys.argv[1:]:
		with open(fileName,'r') as fi:
			for line in fi:
				myList.append(int(line))
	myList.sort()
	print myList[len(myList)/2]