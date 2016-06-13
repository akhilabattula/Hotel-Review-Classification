# Hotel-Review-Classification
Naive Bayes classifier to identify hotel reviews as either truthful or deceptive, 
and either positive or negative.Word tokens as features for classification.

A set of training data is also uploaded here and is in the following format:

A top-level directory with two sub-directories, one for positive reviews and another for negative reviews (plus license and readme files which you won’t need for the exercise).
Each of the subdirectories contains two sub-directories, one with truthful reviews and one with deceptive reviews.
Each of these subdirectories contains four subdirectories, called “folds”.
Each of the folds contains 80 text files with English text (one review per file).

nblearn.py will learn a naive Bayes model from the training data, and nbclassify.py will use the model to classify new data
