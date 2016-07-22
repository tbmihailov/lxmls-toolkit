import numpy as np
import scipy as scipy
import lxmls.classifiers.linear_classifier as lc
import sys
from lxmls.distributions.gaussian import *


class MultinomialNaiveBayes(lc.LinearClassifier):

    def __init__(self, xtype="gaussian"):
        lc.LinearClassifier.__init__(self)
        self.trained = False
        self.likelihood = 0
        self.prior = 0
        self.smooth = False
        self.smooth_param = 1

    def train(self, x, y):
        # n_docs = no. of documents
        # n_words = no. of unique words
        n_docs, n_words = x.shape

        # classes = a list of possible classes
        classes = np.unique(y)
        # n_classes = no. of classes
        n_classes = np.unique(y).shape[0]

        # initialization of the prior and likelihood variables
        prior = np.zeros(n_classes)
        likelihood = np.zeros((n_words, n_classes))


        # TODO: This is where you have to write your code!

        # You need to compute the values of the prior and likelihood parameters
        # and place them in the variables called "prior" and "likelihood".
        # Examples:
        # prior[0] is the prior probability of a document being of class 0
        # likelihood[4, 0] is the likelihood of the fifth(*) feature being
        # active, given that the document is of class 0
        # (*) recall that Python starts indices at 0, so an index of 4
        # corresponds to the fifth feature!

        # Complete Exercise 1.1 
        raise NotImplementedError("Complete Exercise 1.1")

        params = np.zeros((n_words+1, n_classes))
        for i in xrange(n_classes):
            params[0, i] = np.log(prior[i])
            params[1:, i] = np.nan_to_num(np.log(likelihood[:, i]))
        self.likelihood = likelihood
        self.prior = prior
        self.trained = True
        return params


if __name__ == "__main__":
    # Load the data
    import lxmls.readers.sentiment_reader as srs
    scr = srs.SentimentCorpus("books")

    print scr.train_X

    exit

    import lxmls.classifiers.multinomial_naive_bayes as mnbb
    mnb = mnbb.MultinomialNaiveBayes()


    params_nb_sc = mnb.train(scr.train_X, scr.train_y)
    y_pred_train = mnb.test(scr.train_X, params_nb_sc)

    acc_train = mnb.evaluate(scr.train_y, y_pred_train)
    y_pred_test = mnb.test(scr.test_X, params_nb_sc)
    acc_test = mnb.evaluate(scr.test_y, y_pred_test)
    print "Multinomial Naive Bayes Amazon Sentiment Accuracy train: %f test: %f" % (
        acc_train, acc_test)

