import sys
import json
import datetime

if __name__ == '__main__':
	with open(sys.argv[1],'r') as fi:
		data = json.load(fi)
		stations = data['stationBeanList']
		for s in stations:
			if s['statusKey'] == 3:
				stationName = s['stationName']
				stationLat = s['latitude']
				stationLon = s['longitude']
				print '%-50s : %s, %s' % (stationName,stationLat, stationLon)