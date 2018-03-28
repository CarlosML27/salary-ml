# salary-ml

This project consists in the classification of the salary earned by a person depending of other attributes. This project is done using machine learning classification algorithms in Python.

The data set used for this project is a CSV version of the [adults.txt](https://raw.githubusercontent.com/chribsen/simple-machine-learning-examples/master/examples_using_a_real_dataset/adults.txt) data set uploaded by the user Chribsen at Github.

## Getting started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need to have installed Python 3. This version is installed by default on modern versions of Ubuntu.

To check if you have Python 3 already installed, use the following command.

	python3 --version
	
If your terminal returns the sentence "Python 3.X.Y" (being X and Y two positive numbers) or something similar, you're done!

Otherwise, you would need to install it using the following command line:

	sudo apt-get install python3

You will also need to install the following libraries:

- argparse
- pandas
- scikit-learn
- numpy

There are many ways to get this libraries into your system, for example, you can run the following command in your terminal:

	sudo apt-get install python-argparse

### Installing

Besides from the prerequisites, you won't need any other applications to run the program.

Simply download or clone the project to a folder of your local machine. 

If you want to clone the project into an empty folder, execute the following command:

	git clone git@github.com:CarlosML27/salary-ml.git

If the folder isn't empty, execute the following commands to clone the project:

	git init
	git remote add origin https://github.com/CarlosML27/salary-ml.git
	git fetch
	git checkout -t origin/master

Now you are ready to execute the project!

## Execution

To run the project, open a terminal window in "src" folder and type the following command:

	python3 salary-ml.py
	
### Optional arguments

You can use additional options in the arguments of the program. The following are the optional arguments supported:

- -r RATIO / --ratio RATIO: Changes the split ratio between the training set and the test set. This value must be between 0.0 and 1.0. Its default value is 0.66.

		python3 salary-ml.py -r 0.82
		
## Authors

- **Carlos Morente** - *Initial work* - [CarlosML27 (Github)](https://github.com/CarlosML27) 

See also the list of the [contributors](https://github.com/CarlosML27/salary-ml/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](https://github.com/CarlosML27/iris-ml/LICENSE.md) file for details.

## Acknowledgements

- **chribsen@Github** for the data and his examples
- **Siraj Raval@Youtube** for all the inspiration he gives
- **StackOverflow and its community** for all the help
- **PurpleBooth@Github** for this README.md template