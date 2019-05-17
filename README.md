Final Project for CSCI-GA.3033 Big Data Science
Authors: Jiajun Bao, Meng Li, Jane Liu


FILES
main.py
dataset.py
train.py
neuralnetwork.py
preprocessor.py
train.py
validate.py
test.csv
train.csv
validate.csv
fp.s
/data/
    reviewContent.txt
    metadata.txt
    stopwords.txt


REQUIREMENTS
Please copy all files and folders into the working directory like shown above.

The following libraries are used: Nltk, Numpy, Pandas, Sklearn, Statsmodels. To set up the environment cd to the working directory and enter:
$ module purge
$ module load python3/intel/3.6.3
$ virtualenv venv
$ source venv/bin/activate
$ pip install -U nltk
$ pip install -U pandas     # this should automatically install numpy
$ pip install -U --no-deps statsmodels
$ pip install -U sklearn

This program was written in Python 3.6. It is unknown if it will work correctly for other versions of Python.


INSTRUCTIONS
To run this program as a batch file please enter "sbatch fp.s" or if running from the terminal enter the virtual environment and type "python main.py".