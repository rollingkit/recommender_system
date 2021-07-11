# recommender_system

# Yahoo Music Recommendation System

Abstract:
We have tried various different methods to build a recommender system for the Yahoo Music dataset on Kaggle (https://www.kaggle.com/c/ee627ws-2020fall). 
The training set consists of various ratings for each user ID. A user could have given a number of items (tracks, albums, artists, genres) a rating out of 100. 

The training set has all these ratings in the file trainItem2.txt.
The test set, has 6 items for each user. This is what we are trying to predict. For each user with 6 items, we want to predict three out of the six that
the user would like (assign a '1' rating) and three that the user may not (assign a '0' rating). These ratings would be based on the ratings the user has 
already made for various items in the training set. Based on the training and testing set, a test track hierarchy was generated. This showed for each track
in the test set (in the testItem2.txt file), the hierarchy of that item. This can mean the artist, the album, and the genres that the item may belong to. 
This way we were able to look into the training set and if we did not come across that particular item, we could try to find the user's rating for a related
field such as the artist, album or genre. Using this hierarchy, we were able to generate some submissions by first only considering the album and artist ratings
that the user may have given. After that we also extracted four genre ratings for each user. We were able to sum these ratings up for each item. 
Based on these values, we were able to make predictions for each user for three likes and three dislikes. 

We applied various classification algorithms using PySpark, including matrix factorization. A lot of these later methods were also based on the ratings we
were able to extract. 
Utlimately, we were able to achieve the best rating of 85.771% by using logistic regression on three ratings (artist, album, genre). 



Results:

| | Method | Accuracy |
|-|--------|----------|
| 1 | Album & Artist Ratings (Mean) | 0.85745 |
| 2 | Album & Artist Rating (Sum) | 0.84909 |
| 3 | Album + Artist + Genre Ratings (Sum, Album, Artist, Genres 1-4) | 0.84402 |
| 4 | Matrix Factorization | 0.67488 |
| 5 | Classifiers (Album, Artist, Genre 1) | |
| | Logistic Regression | 0.85771 |
| | Decision Tree | 0.85756 |
| | Random Forest | 0.85756 |
| | Gradient Boosted Decision Tree | 0.85753 |
| 6 | Classifiers (Album, Artist, Genres 1-4) | |
| | Logistic Regression | 0.85595 | 
| | Decision Tree | 0.85481 |
| | Random Forest | 0.85709 |
| | Gradient Boosted Decision Tree | 0.85539 |
| 7 | Ensemble (Swapped) | 0.79502 |
| 8 | Classifers (Mean & Mode, Album, Artist, Genres 1-4) | |
| | Logistic Regression | 0.82133 |
| | Decision Tree | 0.82060 |
| | Random Forest | 0.82147 |
| | Gradient Boosted Decision Tree | 0.82094 |

