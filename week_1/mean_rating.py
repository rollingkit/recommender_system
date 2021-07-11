import pandas as pd
output = pd.read_csv('output1.txt', sep='|', header=None)

output.columns = ['User ID', 'Track ID', 'Album Rating', 'Artist Rating']
output['mean rating'] = output[['Album Rating', 'Artist Rating']].mean(axis=1)

train_df = pd.read_csv('trainIdx2_matrix.txt', sep='|', header=None)
train_df.columns = ['trainUserID', 'trainItemID', 'trainRating']

mean_rating = output.copy()
#mean_rating.drop(['Album Rating', 'Artist Rating'], axis=1)

mean_rating['userid_trackid'] = mean_rating['User ID'].astype(str)+'_'+mean_rating['Track ID'].astype(str)
mean_rating.drop(['User ID', 'Track ID','Album Rating', 'Artist Rating'],axis=1)
mean_rating = mean_rating[['userid_trackid', 'mean rating']]
mean_rating['rating'] = 0

for i in range(len(mean_rating)):
    if mean_rating['mean rating'][i] > 0:
        mean_rating['rating'][i] = 1
mean_rating_answer = mean_rating[['userid_trackid', 'rating']]
mean_rating_answer = mean_rating_answer.rename(columns={'userid_trackid':'TrackID', 'rating':'Predictor'})
mean_rating_answer.to_csv('based_on_mean.csv', index=False)
