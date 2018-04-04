import argparse
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import tree

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
	parser.add_argument("-r", "--ratio", help="change split ratio of the training data (default={})".format(DEFAULT_SPLIT_RATIO), action="store", default=DEFAULT_SPLIT_RATIO, type=restricted_float)
	return parser.parse_args()

def get_filename():
	return DEFAULT_FILENAME
	
def get_split_ratio(args):
	return args.ratio

def replace_missing_data(data):
	data.replace(["NaN"], np.nan, inplace = True)
	data = data.apply(lambda x:x.fillna(x.value_counts().index[0]))
	return data

def drop_repeated_columns(data):
	dropcolumns = ['education']
	data.drop(dropcolumns, inplace=True, axis=1)
	return data

def parse_integer_values(data):
	numericlabels = ['age', 'final_weight', 'education_num', 'capital_gain', 'capital_loss', 'hours_per_week']
	for label in numericlabels:
		data[label] = data[label].astype('int32')
	return data

def encode_string_values(data):
	labelencoder = LabelEncoder()
	stringlabels = ['workclass', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'native_country', 'salary']
	for label in stringlabels:
		data[label] = labelencoder.fit_transform(data[label])
	return data

def get_data(filename):
	data = pd.read_csv(filename, sep=",", header=0, na_values=["?"])
	data = replace_missing_data(data)
	data = drop_repeated_columns(data)
	data = parse_integer_values(data)
	data = encode_string_values(data)
	return data

def split_train_test_data(data, training_ratio):
	X = data.drop('salary', 1)
	Y = data['salary'].values.tolist()
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1-training_ratio)
	return X_train, X_test, Y_train, Y_test

def create_dtc(X, Y):
	decision_tree_classifier = tree.DecisionTreeClassifier()
	decision_tree_classifier = decision_tree_classifier.fit(X, Y)
	return decision_tree_classifier

def get_accuracy(classifier, X, Y):
	accuracy = classifier.score(X, Y)
	return accuracy

def get_prediction(classifier, X):
	prediction = classifier.predict(X)
	return prediction

def get_confusion_matrix(prediction, Y):
	confusion_matrix = confusion_matrix(prediction, Y)
	return confusion_matrix

def main():
	args = retrieve_args()
	split_ratio = get_split_ratio(args)
	filename = get_filename()
	data = get_data(filename)
	X_train, X_test, Y_train, Y_test = split_train_test_data(data, split_ratio)
	decision_tree_classifier = create_dtc(X_train, Y_train)
	dtc_accuracy = get_accuracy(decision_tree_classifier, X_test, Y_test) 
	print("Accuracy: {}%".format(round(dtc_accuracy*100, 4)))
	dtc_prediction = get_prediction(decision_tree_classifier, X_test)
	dtc_confusion_matrix = confusion_matrix(dtc_prediction, Y_test)
	print(dtc_confusion_matrix)

if __name__ == '__main__':
	main()