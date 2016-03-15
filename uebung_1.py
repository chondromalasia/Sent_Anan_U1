#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Sentiment Analyse und Media Monitoring
#### Heath Gordon ####
### 16 March 2016 #####

"""
Some thoughts in retrospect:
probably should have make a 'get all words' function
There are some nested fors that could have been those list maker things
"""

################
import random, string
from nltk.corpus import movie_reviews, stopwords
from nltk.util import ngrams
import nltk
from sklearn import cross_validation

def get_stopwords():
    # long story short, the NLTK's stopword list doesn't include punctuation
    the_stopwords = stopwords.words('english')
    the_stopwords.extend(list(set(string.punctuation)))

    return the_stopwords

def get_documents():
    """
    Retrieve shuffled movie reviews from the nltk
    """
    print("Retrieving Movie Reviews\n")

    reviews = [(list(movie_reviews.words(fileid)), category)
               for category in movie_reviews.categories()
               for fileid in movie_reviews.fileids(category)]
    # so I have no idea why, but shuffle() gives me a none type
    return random.sample(reviews, len(reviews))

def get_features(documents):
    """
    Extract unigrams from the training set
    """
    unigrams = {}
    print("\tExtracting Unigram features\n")

    # get stopwords
    my_stopwords = get_stopwords()

    test_words = []
    # not proud of this, but make a list of every word, not in stopword list
    for document in documents:
        for word in document[0]:
            if word not in my_stopwords:
                test_words.append(word)

    # top 200 from a freqdist
    test_words = nltk.FreqDist(test_words)
    top_words = [i[0] for i in list(test_words.most_common(200))]
    
    return top_words
    
def get_more_features(documents):
    """
    Get bigrams
    """
    print ("\tExtracting Bigram features\n")

    my_stopwords = get_stopwords()

    # get list of all the words
    all_words = []
    for document in documents:
        for word in document[0]:
            if word not in my_stopwords:
                all_words.append(word)

    # list of bigrams
    bigrams = list(ngrams(all_words, 2))

    # get top 200
    freq_dist_bi = list(nltk.FreqDist(bigrams).most_common(200))

    return [i[0] for i in freq_dist_bi]


def featuresets(features, documents):
    """
    filters the training documents for the features
    the 'pos or negative' is the last element of each review
    review[x][1] should retrieve it
    """
    feature_set = []

    print("\tCreating Feature Set\n")

    for review in documents:
        review_hash = {}
        bigrams = list(ngrams(review[0], 2))

        for feature in features:
            # bigrams, god this is inelegant
            if type(feature) == tuple:
                if feature in bigrams:
                    review_hash[feature] = True;

            # unigrams
            else:
                if feature in review[0]:
                    review_hash[feature] = True;

        # build the list
        feature_set.append((review_hash, review[1]))
                    

    return feature_set


def train_test(train, test):
    """
    I amended this a bit because I didn't really get it
    but now it just runs the classifier and returns the accuracy
    """

    print "\tTraining and Testing Classifier\n"

    classifier = nltk.NaiveBayesClassifier.train(train)

    # un-comment the next line if you want to see the most informative feats

    classifier.show_most_informative_features(10)
    
    return nltk.classify.util.accuracy(classifier, test)
	
    
def main():

    # homebrew cross_fold
    folds = 10

    accuracy = 0
    
    # get the review
    reviews_list = get_documents()

    fold_size = len(reviews_list)/folds

    for i in range(folds):
        print "Round ", i+1

        # split up set
        test_set = reviews_list[i*fold_size:][:fold_size]
        train_set = reviews_list[:i*fold_size] + reviews_list[(i+1)*fold_size:]

        # get unigram features
        unigram_feats = get_features(train_set)

        # get bigram features
        bigram_feats = get_more_features(train_set)

        all_feats = unigram_feats + bigram_feats
        train_set = featuresets(all_feats, train_set)
        test_set = featuresets(all_feats, test_set)

        accuracy += train_test(train_set, test_set)


    print "Final Accuracy: ", (accuracy/folds)
	
	
if __name__ == '__main__':
    main()

