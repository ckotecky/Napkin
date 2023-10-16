import unittest

from os import path, listdir
from glob import glob

from napkin import Napkin



class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.napkin = Napkin()
		cls.maxDiff = None

		scriptLocation = path.dirname(__file__)

		cls.math_tests = cls._loadTests(cls, path.join(scriptLocation, 'pairs/math'))
		cls.structure_tests = cls._loadTests(cls, path.join(scriptLocation, 'pairs/structure'))
		cls.list_tests = cls._loadTests(cls, path.join(scriptLocation, 'pairs/lists'))



	def _loadTests(self, testPath):
		paths = sorted(glob(f'{testPath}/*.napkin'))

		tests = []

		for sourcePath in paths:    
			patternPath = sourcePath[:-7] # remove .napkin suffix to get the name of the file containing the expected result
			resultPath = patternPath + '.tex'

			with open(sourcePath, 'r') as f:
				source = f.read()

			with open(resultPath, 'r') as f:
				result = f.read()

			name = path.basename(resultPath)

			tests.append((name, source, result))

		return tests



	def test_sanity(self):
		result = self.napkin.parseAndCompile('a')

		self.assertEqual(result, 'a')



	def test_lists(self):
		for i, (name, source, expected) in enumerate(Test.list_tests):
			with self.subTest(msg = name, i = i):
				result = self.napkin.parseAndCompile(source)

				self.assertEqual(result.strip(), expected.strip())



	def test_math(self):
		for i, (name, source, expected) in enumerate(Test.math_tests):
			with self.subTest(msg = name, i = i):
				result = self.napkin.parseAndCompile(source)

				self.assertEqual(result, expected)


	def test_structure(self):
		for i, (name, source, expected) in enumerate(Test.structure_tests):
			with self.subTest(msg = name, i = i):
				result = self.napkin.parseAndCompile(source)

				self.assertEqual(result, expected)




if __name__ == '__main__':
	unittest.main()