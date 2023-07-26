import unittest

from os import path
from glob import glob

from napkin.napkin import Napkin



class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.napkin = Napkin()

		scriptLocation = path.dirname(__file__)

		cls._loadTests(cls, path.join(scriptLocation, 'pairs'))



	def _loadTests(cls, testPath):
		paths = glob(f'{testPath}/*.napkin')

		cls.tests = []

		for sourcePath in paths:    
			resultPath = sourcePath[:-7]

			with open(sourcePath, 'r') as f:
				source = f.read()

			with open(resultPath, 'r') as f:
				result = f.read()

			name = path.basename(resultPath)

			cls.tests.append((name, source, result))



	def test_sanity(self):
		result = self.napkin.parseAndCompile('a')

		self.assertRegex(result, 'a')



	def test_all(self):
		for i, (name, source, expected) in enumerate(Test.tests):
			with self.subTest(msg = name, i = i):
				result = self.napkin.parseAndCompile(source)

				self.assertRegex(result, expected)



if __name__ == '__main__':
	unittest.main()