
import pandas as pd
import numpy as np
import sklearn
from Process import combineBookAndRatingDataframes
from sklearn.decomposition import TruncatedSVD

def popular_books():
    combine_df=combineBookAndRatingDataframes()
    popular_books_df = combine_df.groupby('ISBN')['Book-Rating'].mean().sort_values(ascending=False).reset_index()
    popular_books_df =popular_books_df.head(10)
    p_l=list(popular_books_df ['ISBN'])
    a= combine_df[combine_df['ISBN'].isin(p_l)]
    popular_book_list=list(a['"Book-Title"'].unique())
    return popular_book_list




