from Collabrartive_Filter import collabrative_filter
from Popularity_based_recommendation_system import popular_books
from Process import processData

def upload_files(Book-Ratings='BX-Book-Ratings.csv',Books = 'BX-Books.csv')
    processData(book_ratings,book_info)

# This is Entry Page
user_enter=int(input("Please Enter  1 for Popular Books,  2 Similar Specific Book,  any other key to Exit \n"))
print("\n")

#If user Enter 1 call Collabrative Recommendation System
if 1 == user_enter:
    collabrative_filter()
#If user Enter 2 call Popular Items Recommendation System
elif user_enter==2 :
    popular_books_list=popular_books()
    #Black: print("\033[2;37;40m Underlined text\033[0;37;40m \n")
    print("\033[1;31;40m Ten Popular Books : \033[0;37;40m \n")
    for i in popular_books_list:
        print(i.replace('"', ""))
else:
    exit()



