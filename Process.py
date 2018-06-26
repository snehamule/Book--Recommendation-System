import pandas as pd
import csv

#This method process data
# read BX-Book-Ratings.csv and clean data
books_info_df = pd.read_csv('BX-Books.csv', sep=',', low_memory=False, encoding="ISO-8859-1", skipinitialspace=True,quoting=csv.QUOTE_ALL)
books_info_df=books_info_df.drop('"Image-URL-S"', axis=1)
books_info_df=books_info_df.drop('"Image-URL-M"', axis=1)
books_info_df=books_info_df.drop('"Image-URL-L"', axis=1)
books_info_df=books_info_df.drop('Unnamed: 8', axis=1)
books_info_df=books_info_df.drop(['Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15','Unnamed: 16'], axis=1)
books_info_df=books_info_df.drop(['Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20','Unnamed: 21'], axis=1)

return book_rating_df, books_info_df


# =This method merge book_rating_df and books_info_df on ISBN column
def combineBookAndRatingDataframes():
    book_rating_df, books_info_df=processData()
    combine_df = pd.merge(book_rating_df, books_info_df, on='ISBN')
    return combine_df
