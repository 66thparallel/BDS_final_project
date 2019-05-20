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
lda_knn.py
detecting_sys_window.py
fp.s
/data/
    reviewContent.txt
    metadata.txt
    stopwords.txt
    test.csv
    train.csv
    validate.csv


REQUIREMENTS
Please copy all files and folders into the working directory as shown above. The /data/ folder is in the same directory as main.py.

The following libraries are used: nltk, numpy, pandas, sklearn, matplotlib, gensim, statsmodels, and patsy (required by statsmodels). To set up the environment cd to the working directory and enter:

$ module purge
$ module load python3/intel/3.6.3
$ virtualenv venv
$ source venv/bin/activate
$ pip install -U nltk
$ pip install -U pandas     # this should automatically install numpy
$ pip install -U --no-deps statsmodels
$ pip install -U patsy      # required by statsmodels
$ pip install -U sklearn
$ pip install -U matplotlib
$ pip install -U gensim

This program was written in Python 3.6. It is unknown if it will work correctly for other versions of Python.


INSTRUCTIONS
1. There are two programs in our project. The first program runs the logistic regression and neural network models. The second program runs the LDA and kNN models.
2. To run this project as a batch file please enter "sbatch fp.s" and then enter "sbatch lda.s" (in the bash files the working directory file path needs to be updated).
3. If running from the server enter the virtual environment with "source venv/bin/activate" then enter "python main.py" and "python lda_knn.py".
4. Our program for deployment (detecting_sys_window.py) allows a user to input an unknown review and obtain a result (fake or non-fake). It does not work when the project is run as a batch process. The program can be run on a local machine with sufficient memory (simply uncomment the last two lines of code in main.py and type "python main.py").


EXPECTED RESULTS
Results for the logistic regression model is expected to have 65-70% accuracy.
Results for the neural network model is expected to have 70% accuracy.

(expected output from slurm:)

Optimization terminated successfully.
         Current function value: 0.588500
         Iterations 6
                           Logit Regression Results
==============================================================================
Dep. Variable:                  label   No. Observations:               125531
Model:                          Logit   Df Residuals:                   125515
Method:                           MLE   Df Model:                           15
Date:                Sat, 18 May 2019   Pseudo R-squ.:                  0.1510
Time:                        03:36:20   Log-Likelihood:                -73875.
converged:                       True   LL-Null:                       -87011.
                                        LLR p-value:                     0.000
====================================================================================
                       coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------------
length_of_review     7.7870      0.093     83.894      0.000       7.605       7.969
order                0.4303      0.168      2.563      0.010       0.101       0.760
thing                0.3251      0.142      2.282      0.022       0.046       0.604
good                -0.1892      0.088     -2.145      0.032      -0.362      -0.016
side                 1.3556      0.139      9.723      0.000       1.082       1.629
day                  0.8866      0.164      5.419      0.000       0.566       1.207
bit                  0.9866      0.144      6.839      0.000       0.704       1.269
flavor               1.4055      0.172      8.165      0.000       1.068       1.743
pretty               5.0092      0.165     30.420      0.000       4.687       5.332
sauce                1.3159      0.167      7.888      0.000       0.989       1.643
star                 1.4048      0.272      5.163      0.000       0.872       1.938
rating_2.0           1.4466      0.049     29.735      0.000       1.351       1.542
rating_3.0           1.9621      0.043     45.205      0.000       1.877       2.047
rating_4.0           1.7422      0.041     42.060      0.000       1.661       1.823
rating_5.0           1.0375      0.042     24.975      0.000       0.956       1.119
intercept           -2.4525      0.042    -58.597      0.000      -2.534      -2.370
====================================================================================
[[16434  4491]
 [ 8054 12864]]

              precision    recall  f1-score   support

           0       0.67      0.79      0.72     20925
           1       0.74      0.61      0.67     20918

    accuracy                           0.70     41843
   macro avg       0.71      0.70      0.70     41843
weighted avg       0.71      0.70      0.70     41843


Neural Network accuracy score: 0.7076452453217982

