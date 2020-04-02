#!/usr/bin/env python3
import keras
import numpy as np
import pandas as pd

n_emotions=7

training_x=[]
training_y=[]
testing_x=[]
testing_y=[]

# Assume no errors occur
dataset=pd.read_csv("fer2013/fer2013.csv")

print("Found %d samples in dataset" % len(dataset))

for i,usage in enumerate(dataset["Usage"]):
    # Normalize the input
    x=np.array([int(a)/0xFF for a in dataset["pixels"][i].split(' ')]) \
        .reshape((48,48,1))
    y=int(dataset["emotion"][i])
    if usage=="Training":
        training_x.append(x)
        training_y.append(y)
    elif usage=="PrivateTest" or usage=="PublicTest":
        testing_x.append(x)
        testing_y.append(y)

n_trainings=len(training_x)
n_testings=len(testing_x)

print("Found %d training samples and %d testing samples" \
    % (n_trainings,n_testings))

training_x=np.array(training_x).reshape(n_trainings,48*48).astype(np.int8)
training_y=np.array(training_y).reshape(n_trainings).astype(np.int8)
testing_x=np.array(testing_x).reshape(n_testings,48*48).astype(np.int8)
testing_y=np.array(testing_y).reshape(n_testings).astype(np.int8)

training_y=keras.utils.to_categorical(training_y,n_emotions)
testing_y=keras.utils.to_categorical(testing_y,n_emotions)

np.savetxt("training_x.txt",training_x)
np.savetxt("testing_x.txt",testing_x)
np.savetxt("training_y.txt",training_y)
np.savetxt("testing_y.txt",testing_y)
