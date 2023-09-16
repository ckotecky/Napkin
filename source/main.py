#!/usr/bin/env python3


from napkin import Napkin
import argparse
import timeit




def parse(inPath, outPath, silent):
	if inPath == '' or outPath == '':
		print('Provide input and output file paths.')
		return

	with open(inPath, 'r') as f:
		source = f.read()

	napkin = Napkin()

	if not silent:
		start = timeit.default_timer()

		print('Parsing...')

	result = napkin.parseAndCompile(source)


	if not silent:
		stop = timeit.default_timer()

		print(f'Parsed [{inPath}] in {stop - start}s.')

	with open(outPath, 'w') as f:
	    f.write(result)




def main():
	argParser = argparse.ArgumentParser(
		prog = 'Napkin compiler',
		description = 'Compiles .napkin files to .tex files.'
	)

	argParser.add_argument('-i', '--input', default='', type=str, help='Input file path')
	argParser.add_argument('-o', '--output', default='', type=str, help='Output file path')
	argParser.add_argument('-s', '--silent', default=False, type=str, help='Progress feedback.')

	args = argParser.parse_args()

	parse(args.input, args.output, args.silent == 'True')






if __name__ == '__main__':
	main()