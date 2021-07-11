import pandas as pd


df1 = read_csv('output4.txt', sep='|', header=None)
df1.columns = ['User ID', 'Track', 'Album Rating', 'Artist Rating', 'Genre1 Rating', 'Genre2 Rating', 'Genre3 Rating', 'Genre4 Rating']

df1['Sum'] = df1[['Album Rating', 'Artist Rating', 'Genre1 Rating', 'Genre2 Rating', 'Genre3 Rating', 'Genre4 Rating']].sum(axis=1)
df1_cp = df1.copy()

df1_cp['Predictor'] = 0

#test first six entries to see if max 3 are made 1 using the nlargest() function
df1_cp['Predictor'][df1_cp[0:6]['Sum'].nlargest(3).index] = 1

#loop to make predictor value 1 for maximum 3 in all sets of 6
#this will take some time
start=0
for i in range(20000):
    df1_cp['Predictor'][df1_cp[start:6*(i+1)]['Sum'].nlargest(3).index] = 1
    start = 6*(i+1)

#make new dataframe with only the required columns for csv file
df1_cp_ans = df1_cp[['User ID', 'Track', 'Predictor']]
#combine UserID and TrackID just like in sample_submission.csv
df1_cp_ans['TrackID'] = df1_cp_ans['UserID'].astype(str)+'_'+df1_cp_ans['Track'].astype(str)
df1_cp_ans = df1_cp_ans[['TrackID', 'User ID', 'Track', 'Predictor']]
df1_cp_ans.drop(columns={'User ID', 'Track'}, inplace=True)

df1_cp_ans.to_csv('4genres.csv', index=False)
