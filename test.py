"""
test.py: Test your code.
"""


from graph import *
from search import *
from util import *
import traceback
import argparse
import time


def testSearch():
	searchFunctions = [("Hill climbing", searchHillClimbing),
			("Best first", searchBestFirst),
			   
					   ("Beam", searchBeam),
					   
					   ("A*", searchAStar)]

					  

	for i in range(50):
		g, start, goal = randomGridSearch(30, 30)
		print('Test %d' % (i + 1))

		for (name, f) in searchFunctions:
			try:
		
				path = f(g, start, goal)
				startTime = time.time()
				if goal not in path:
					pass
					print('%s - path not found.' % name)
					print('Sart: %s, goal: %s' % (start, goal))
					#print(g)
				else:
					node = goal
					print('%s - path found with cost %d.' % (name, len(path) - 1))
				endTime = time.time()
				#print('%s executed in the time %f.' % (name, endTime - startTime))
			except:
				traceback.print_exc()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Test your code.', epilog='Runs all tests.')
	parser.parse_args()

	testSearch()
