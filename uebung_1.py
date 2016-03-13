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

    reviews = [(list(movie_reviews.words(fileid)), category)
               for category in movie_reviews.categories()
               for fileid in movie_reviews.fileids(category)]
    
    return random.shuffle(reviews)

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
    return test_words
    
            
def get_more_features(documents):
    """
    Get bigrams
    """
    print ("Creating Bigram features")

    my_stopwords = get_stopwords()

    # get list of all the words
    all_words = [w.lower() for w in movie_reviews.words() if w not in my_stopwords]

    # list of bigrams
    bigrams = list(ngrams(all_words, 2))

    # get top 200
    freq_dist_bi = list(nltk.FreqDist(bigrams).most_common(200))

    return [i[0] for i in freq_dist_bi]


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

    # get the unigram featureset
    unigram_feats = get_features(reviews_list)

    # get bigrams
    bigram_feats = get_more_features(reviews_list)
	
	
if __name__ == '__main__':
    main()

