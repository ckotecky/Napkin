import unittest
import re
from os import path
from glob import glob
from parameterized import parameterized

from napkin.napkin import Napkin




class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.napkin = Napkin()

		scriptLocation = path.dirname(__file__)

		# with open(path.join(scriptLocation, 'test_pairs.json'), 'rb') as f:
		# 	cls.tests = json.load(f)

		cls.loadTests(cls, scriptLocation)


	def loadTests(cls, testPath):
	    paths = glob(f'{testPath}*.napkin')

	    cls.tests = []
	    
	    for sourcePath in paths:    
	        resultPath = sourcePath[:-7]
	        
	        with open(sourcePath, 'r') as f:
	            source = f.read()
	    
	        with open(resultPath, 'r') as f:
	            result = f.read()
	    
	        name = path.basename(resultPath)
	    
	        cls.tests.append((name, source, result))



	def test_parser(self):
		for name, source, expected in Test.tests:
			result = self.napkin.parseAndCompile(source)

			self.subTest()

			if re.fullmatch(expected, result):
				continue

			else:
				print(f'''----------------------------------------------------------------------
					\tfailed
					\t\twhen parsed: {source}
					\t\tinto: {result}
					\t\twhen expected: {expected}
					''')
				return False

		return True


	def tryInput(self, source, expected):
		result = self.napkin.parseAndCompile(source)
		
		if re.fullmatch(result, expected):
			return True

		return False


	def test_sanity(self):
		self.assertTrue(self.tryInput('a', 'a'))


	def runTests(self, tests):
		for source, pattern in tests.items():
			result = self.napkin.parseAndCompile(source)

			if re.fullmatch(pattern, result):
				continue

			else:
				print(f'''----------------------------------------------------------------------
					\tfailed
					\t\twhen parsed: {source}
					\t\tinto: {result}
					\t\twhen expected: {pattern}
					''')
				return False

		return True



	# def test_math(self):
	# 	tests = self.tests["math"]

	# 	self.assertTrue(self.runTests(tests))




if __name__ == '__main__':
	unittest.main()















































