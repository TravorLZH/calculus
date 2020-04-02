#!/usr/bin/env python3
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
from keras.activations import relu,softmax
import keras
import os

mnist=np.load("mnist.npz")
x_train,y_train=mnist["x_train"],mnist["y_train"]
x_test,y_test=mnist["x_test"],mnist["y_test"]

n_train=x_train.shape[0]
n_test=x_test.shape[0]

assert(keras.backend.image_data_format()!="channels_first")

x_train=x_train.reshape(n_train,28,28,1).astype(np.float64)
x_test=x_test.reshape(n_test,28,28,1).astype(np.float64)

# Normalization
x_train/=0xFF
x_test/=0xFF

print("Found %d samples in training set and %d in testing set" \
    % (n_train,n_test))

# to_categorical helps convert type 3 to [0 0 0 1 ... 0]
y_train=keras.utils.to_categorical(y_train,10)
y_test=keras.utils.to_categorical(y_test,10)

fnn=None

if os.path.exists("mnist_fnn.h5"):
    fnn=keras.models.load_model("mnist_fnn.h5")
else:   # If no config exists, then train a new network
    fnn=Sequential()
    fnn.add(Conv2D(32,kernel_size=(3,3),activation="relu",
        input_shape=(28,28,1)))
    fnn.add(Conv2D(64,(3,3),activation="relu"))
    fnn.add(MaxPooling2D(pool_size=(2,2)))
    fnn.add(Dropout(0.25))
    fnn.add(Flatten())
    fnn.add(Dense(128,activation="relu"))
    fnn.add(Dropout(0.25))
    fnn.add(Dense(10,activation="softmax"))
    fnn.compile(loss=keras.losses.categorical_crossentropy,
        optimizer=keras.optimizers.Adadelta(),
        metrics=["accuracy"])
    fnn.fit(x_train,y_train,batch_size=128,epochs=12,verbose=1,
        validation_data=(x_test,y_test))
    fnn.save("mnist_fnn.h5")

score=fnn.evaluate(x_test,y_test,verbose=1)
print("Test result: loss=%f, accuracy=%.f" % (score[0],score[1]))
