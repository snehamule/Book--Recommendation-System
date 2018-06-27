# Book Recommendation system App

This is hybrid Recommender system using Collaborative Filtering And Popularity-based recommender to recommend books.

## Technology / libraries used: <br />
Python, Scikit learn, Panda, Numpy

## Setup required:<br />
python version: 3 or greater<br />
Libraries : ScikitLearn, Panda,Numpy


## Install python <br />
If python is not installed then need to install python:<br />
<br />
**For  osx operating system (mac)**<br />
	python get-pip.py 

**For windows operating system**<br />
	refer steps from [windows python installation steps](https://docs.python.org/3/using/windows.html).
	

## Check python version:
python -version


## Install Libraries<br /> 

**For  osx operating system (mac)**<br />
* Install Numpy : pip install numpy<br />
* Install  Panada : pip install pandas<br />
* Install  Scikitlearn: pip install scipy, scikit-learn<br />

**For windows operating system**<br />
* Install numpy : pip install numpy<br />
* Install pandas : python -m pip install pandas<br />
* Install  Scikitlearn: pip install -U scikit-learn<br />


## Dataset Download :<br />
This recommendation system use  Book-Crossing Dataset.
Download Book-Crossing Dataset  from [Adult UCI dataset](https://archive.ics.uci.edu/ml/datasets/adult).  

## Run program : <br />
1. Download code from git  using  git clone .
2. Place downloaded dataset files in the same folder
3. For Process the Data run command 
```
	python process.py
```	
4. To start a recommendation system run command 
```
	python start_page.py
```
5. Application will prompt  to ask user to press 1 if user intrested in popular book and 2 to get recommendation for books of 	 user intrest.
6. If user enter 1 then application will display popular books
7. If user enter 2 then application ask user to enter intrested book as well as application will suggest some books. It is   	optional to user to select from suggested book. Once user enter book which he/she is  intrested , then application will	    	recommend similar 10 book which user might be intrested.
8. If appplication does not find so much similar book (Selected similarity using pearson correlation), then application will 	suggest 70 percentage (7 books) similar books and 30 % percentage (3 books) popular books
