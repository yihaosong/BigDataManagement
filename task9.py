import sys
import json
import datetime

if __name__ == '__main__':
	with open(sys.argv[1],'r') as fi:
		meta = json.load(fi)
	print datetime.datetime.fromtimestamp(meta['createdAt'])