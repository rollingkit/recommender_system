#!/usr/bin/env python

import numpy

dataDir='/Users/Sivankit/Documents/work/stevens/ee_627/hw5/'
file_name_test=dataDir + 'testTrack_hierarchy.txt'
file_name_train=dataDir + 'trainIdx2_matrix.txt'
output_file= dataDir + 'output4.txt'

fTest= open(file_name_test, 'r')
fTrain=open(file_name_train, 'r')
Trainline= fTrain.readline()
fOut = open(output_file, 'w')

trackID_vec=[0]*6
albumID_vec=[0]*6
artistID_vec=[0]*6
genre1ID_vec=[0]*6
genre2ID_vec=[0]*6
genre3ID_vec=[0]*6
genre4ID_vec=[0]*6
#genre3ID_vec=[0]*6
lastUserID=-1

user_rating_inTrain=numpy.zeros(shape=(6,7))

for line in fTest:
	arr_test=line.strip().split('|')
	userID= arr_test[0]
	trackID= arr_test[1]
	albumID= arr_test[2]
	artistID=arr_test[3]
	genre1ID = 0
	genre2ID = 0
	genre3ID = 0
	genre4ID = 0
	if len(arr_test) > 4:
		genre1ID=arr_test[4]
	if len(arr_test) > 5:
		genre2ID=arr_test[5]
	if len(arr_test) >6:
		genre3ID=arr_test[6]
	if len(arr_test)>7:
		genre4ID=arr_test[7]



	if userID!= lastUserID:
		ii=0
		user_rating_inTrain=numpy.zeros(shape=(6,7))

	trackID_vec[ii]=trackID
	albumID_vec[ii]=albumID
	artistID_vec[ii]=artistID
	genre1ID_vec[ii]=genre1ID
	genre2ID_vec[ii]=genre2ID
	genre3ID_vec[ii]=genre3ID
	genre4ID_vec[ii]=genre4ID

	ii=ii+1
	lastUserID=userID

	if ii==6 :
		while (Trainline):
		# for Trainline in fTrain:
			arr_train = Trainline.strip().split('|')
			trainUserID=arr_train[0]
			trainItemID=arr_train[1]
			trainRating=arr_train[2]
			Trainline=fTrain.readline()

			if trainUserID< userID:
				continue
			if trainUserID== userID:
				for nn in range(0, 6):
					if trainItemID==albumID_vec[nn]:
						user_rating_inTrain[nn, 0]=trainRating
					if trainItemID==artistID_vec[nn]:
						user_rating_inTrain[nn, 1]=trainRating
					if trainItemID==genre1ID_vec[nn]:
						user_rating_inTrain[nn,3]=trainRating
					if trainItemID==genre2ID_vec[nn]:
						user_rating_inTrain[nn,4]=trainRating
					if trainItemID==genre3ID_vec[nn]:
						user_rating_inTrain[nn,5]=trainRating
					if trainItemID==genre4ID_vec[nn]:
						user_rating_inTrain[nn,6]=trainRating
			if trainUserID> userID:
				for nn in range(0, 6):
					outStr=str(userID) + '|' + str(trackID_vec[nn])+ '|' + str(user_rating_inTrain[nn,0]) + '|' + str(user_rating_inTrain[nn, 1]) + '|' +str(user_rating_inTrain[nn,3])+'|'+str(user_rating_inTrain[nn,4])+'|'+str(user_rating_inTrain[nn,5])+'|'+str(user_rating_inTrain[nn,6])
					fOut.write(outStr + '\n')
				break



fTest.close()
fTrain.close()
