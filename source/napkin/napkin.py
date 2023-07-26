from lark import Lark
from napkin.lister import Lister
from napkin.compiler import Compiler

from os import path


class Napkin:
	def __init__(self):
		scriptLocation = path.dirname(__file__)

		with open(path.join(scriptLocation, 'napkin.lark'), 'r') as f:
			grammar = f.read()

		self.parser = Lark(grammar)
		self.lister = Lister()
		self.compiler = Compiler()


	def parse(self, source):
		tree = self.parser.parse(source)
		
		self.lister.transform(tree)
		self.compiler.visit(tree)

		return tree		


	def parseAndCompile(self, source):
		return self.parse(source).result
