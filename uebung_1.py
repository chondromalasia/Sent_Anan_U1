#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Sentiment Analyse und Media Monitoring
#### Heath Gordon ####
### 16 March 2016 #####



################
import random
from nltk.corpus import movie_reviews, stopwords



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

    print("Creating Unigram features")

    # get the top 100 unigrams

		
	
	
def get_more_features(documents):
    """
    Get bigrams
    """
	

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
    print type(reviews_list)

    # get the unigram featureset
    unigram_feats = get_features(reviews_list)
	
	
if __name__ == '__main__':
    main()

