#!/usr/bin/env python3
import numpy as np
import keras
import os

n_emotions=7
try:
    training_x=np.loadtxt("training_x.txt")
    training_y=np.loadtxt("training_y.txt")
    n=len(training_x)
    print(n)
    training_x=testing_x.reshape(n,48,48,1)
    training_y=testing_y.reshape(n,n_emotions)
except OSError:
    print("Cannot find training set or testing set")
    print("Run `./parse_dataset.py' to generate them")
    exit(-1)

cnn=None

if os.path.exists("emotion_cnn.h5"):
    testing_x=np.loadtxt("testing_x.txt")
    testing_y=np.loadtxt("testing_y.txt")
    n=len(testing_x)
    testing_x=testing_x.reshape(n,48,48,1)
    testing_y=testing_y.reshape(n,n_emotions)
    cnn=keras.models.load_model("emotion_cnn.h5")
    score=cnn.evaluate(testing_x,testing_y,verbose=1)
    print("Test result: loss=%f, accuracy=%f" % (score[0],score[1]))
    exit(0)

from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,MaxPooling2D,Dropout, \
    BatchNormalization

# Set up the Convolutional Network with Keras's Sequential model
cnn=Sequential()
cnn.add(Conv2D(1,kernel_size=(5,5),activation="relu",
    input_shape=(48,48,1)))
cnn.add(MaxPooling2D(pool_size=(2,2)))
cnn.add(BatchNormalization())
cnn.add(Conv2D(1,kernel_size=(3,3),activation="relu"))
cnn.add(MaxPooling2D(pool_size=(2,2),))
cnn.add(BatchNormalization())
cnn.add(Conv2D(1,kernel_size=(3,3),activation="relu"))
cnn.add(MaxPooling2D(pool_size=(2,2)))
cnn.add(BatchNormalization())
cnn.add(Flatten())
cnn.add(Dense(256,activation="relu"))
cnn.add(Dropout(0.5))
cnn.add(Dense(256,activation="relu"))
cnn.add(Dropout(0.5))
cnn.add(Dense(n_emotions,activation="softmax"))
cnn.compile(loss=keras.losses.categorical_crossentropy,
    optimizer="adam",
    metrics=["accuracy"])
cnn.fit(training_x,training_y,batch_size=256,epochs=20,verbose=1,
    validation_data=(testing_x,testing_y))
cnn.save("emotion_cnn.h5")
