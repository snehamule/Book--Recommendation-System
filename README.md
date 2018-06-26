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
Download Book-Crossing Dataset  from [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/).  

## Run program : <br />
1. Download code from git  using  git clone .
2. Place downloaded dataset files in the same folder
3. For Process the Data run command 
```
	python process_data.py
```	
4. To start a recommendation system run command 
```
	python start_page.py
```
5. Enter option 1 to display popular book 2 to book similar to your choice
6. If user select option one then popular books will display
7. If user select option 2, app ask to enter book name .
8. App will recommend some books but it is optional to user to choose books from the suggested book. Once user enter book app    will display recommended books

