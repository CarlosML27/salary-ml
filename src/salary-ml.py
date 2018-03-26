import csv
import argparse

DEFAULT_SPLIT_RATIO = 0.66

def restricted_float(x):
	x = float(x)
	lower_value = 0.0
	upper_value = 1.0
	if x < lower_value or x > upper_value:
		raise argparse.ArgumentTypeError("{} is not in the range [{}, {}]".format(x, lower_value, upper_value))
	return x

def retrieve_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--ratio", help="change split ratio of the data (default={})".format(DEFAULT_SPLIT_RATIO), action="store", default=DEFAULT_SPLIT_RATIO, type=restricted_float)
	return parser.parse_args()

def get_split_ratio(args):
	return args.ratio

def main():
	args = retrieve_args()
	split_ratio = get_split_ratio(args)

if __name__ == '__main__':
	main()