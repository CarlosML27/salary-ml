import csv
import argparse
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

DEFAULT_SPLIT_RATIO = 0.66
DEFAULT_FILENAME = "../data/salary.csv"

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

def get_data(filename):
	data = pd.read_csv(filename, sep=",", header=0)
	dropcolumns = ['education']
	data.drop(dropcolumns, inplace=True, axis=1)
	numericlabels = ['age', 'final_weight', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']
	for label in numericlabels:
		data[label] = data[label].astype('int32')
	labelencoder = LabelEncoder()
	stringlabels = ['workclass', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country', 'salary']
	for label in stringlabels:
		data[label] = labelencoder.fit_transform(data[label])
	return data

def print_rows(data):
	print(data)

def main():
	args = retrieve_args()
	split_ratio = get_split_ratio(args)
	print(split_ratio)
	filename = DEFAULT_FILENAME
	data = get_data(filename)
	print_rows(data[:10])

if __name__ == '__main__':
	main()