from Process import combineBookAndRatingDataframes
import numpy as np
from sklearn.decomposition import TruncatedSVD
import random
from Popularity_based_recommendation_system import popular_books



def collabrative_filter():
    combine_df=combineBookAndRatingDataframes()

    #create Utility Table
    utility_table=combine_df.pivot_table(index='User-ID',columns='"Book-Title"',values='Book-Rating',aggfunc=np.max,fill_value=0)
    utility_table_transpose=utility_table.values.T

    #Decomposition SVD Matrix
    SVD= TruncatedSVD(n_components=12,random_state=17)
    svd_matrix = SVD.fit_transform(utility_table_transpose)


    #Generate Coralation Matrix
    np.seterr(divide='ignore', invalid='ignore')
    correlation_matrix=np.corrcoef(svd_matrix)
    book_information=utility_table.columns
    book_information_list=list(book_information)

    #Shuffle book so we can get random book List
    random.shuffle(book_information_list)

    # Take the first 5 elements of the now randomized array
    print(" Some Books Suggestions : ")
    for i in book_information_list[0:5]:
        print(i.replace('"', ""))

    user_entered_book_name=input('\nEnter book Name\n')
    user_entered_book_name='"{}"'.format(user_entered_book_name)
    print('Entered Book name is ',user_entered_book_name)

    user_enter_book_index=book_information_list.index(user_entered_book_name)

    #Isolating ented book name from other
    user_enter_book_matrix=correlation_matrix[user_enter_book_index]

    #Recommending Highly values
    recommended_book_list=list(book_information[(user_enter_book_matrix<1)&(user_enter_book_matrix>0.85)])
    print('list count',len(recommended_book_list))

    # books_info_df['"Book-Title"'].sort_values(ascending=True).head()
    # "Beyond IBM: Leadership Marketing and Finance for the 1990s"
    # No Recommendation : The Beekeeper's Apprentice
    #output : The wild ponies of Assateague Island (Books for young explorers)
    #Premeditated Marriage


    #If book has no similarity then try to find some similar book.Show 70% Similar books and 30% popular books
    if not recommended_book_list:
        new_recommended_book_list = list(book_information[(user_enter_book_matrix < 1) & (user_enter_book_matrix > 0.50)])
        popular_book_list=popular_books()
        print("new",len(new_recommended_book_list))
        #if book is not at all similar then show popular books
        if not new_recommended_book_list:
            print("\033[1;31;40m Recommendated Books are :: \033[0;37;40m \n")
            for i in popular_book_list:
                print(i.replace('"', ""))
        else:
            print("\033[1;31;40m Recommendated Books are :: \033[0;37;40m \n")
            new_recommended_list=new_recommended_book_list[0:7]+popular_book_list[0:3]
            for i in new_recommended_list:
                print(i.replace('"', ""))
    else:
        print("\033[1;31;40m Recommendated Books are :: \033[0;37;40m \n")
        for i in recommended_book_list:
            print(i.replace('"', ""))

