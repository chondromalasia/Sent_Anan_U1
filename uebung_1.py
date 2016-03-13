#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Sentiment Analyse und Media Monitoring
#### Heath Gordon ####
### 16 March 2016 #####



################
import random, string
from nltk.corpus import movie_reviews, stopwords
from nltk.util import ngrams
import nltk

def get_stopwords():
    # long story short, the NLTK's stopword list doesn't include punctuation
    the_stopwords = stopwords.words('english')
    the_stopwords.extend(list(set(string.punctuation)))

    return the_stopwords

def get_documents():
    """
    Retrieve shuffled movie reviews from the nltk
    """

    return [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]

def get_features(documents):
    """
    Extract unigrams from the training set
    """
    unigrams = {}

    print("Creating Unigram features")

    # get stopwords
    my_stopwords = get_stopwords()

    test_words = nltk.FreqDist(w.lower() for w in movie_reviews.words() if w not in my_stopwords)
    top_words = [i[0] for i in list(test_words.most_common(200))]
    for i in top_words:
        print i
    return top_words
    
            
def get_more_features(documents):
    """
    Get bigrams
    Probably could have done stopword removal as its own thing
    """
    print ("Creating Bigram features")

    # stopwords
    my_stopwords = stopwords.words('english')
    my_stopwords.extend(list(set(string.punctuation)))
    
	

def featuresets(features, documents):
    """
    filters the training documents for the features
    """


def train_test(features_sets, documents):
    """
    Tests the training set.
    """
	
    
def main():
    # get the reviews
    reviews_list = get_documents()
    random.shuffle(reviews_list)

    # get the unigram featureset
    unigram_feats = get_features(reviews_list)
    # bigram_feats = get_more_features(reviews_list)
	
	
if __name__ == '__main__':
    main()

