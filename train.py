import numpy as np
import os
import cv2
from lib.layers import Dense
from lib.accuracy import Accuracy_Categorical
from lib.activations import SoftMax,Relu
from lib.losses import CategoricalCrossEntropy
from lib.layers import Dense
from lib import Model

def load_dataset(dataset,path):
    labels = os.listdir(os.path.join(path, dataset))
    X= []
    y = []
    for label in labels:
        for file in os.listdir(os.path.join(path, dataset, label)):
            image = cv2.imread(os.path.join(path, dataset, label, file),cv2.IMREAD_UNCHANGED)

            X.append(image)
            y.append(label)
    return np.array(X),np.array(y).astype('uint8')

def create_dataset(path):
    X,y = load_dataset('train',path)
    X_test,y_test = load_dataset('test',path)
    return X,y,X_test,y_test

X, y, X_test, y_test = create_dataset('fashion_mnist_images')
X = (X.reshape(X.shape[0], -1).astype(np.float32) - 127.5) / 127.5
X_test = (X_test.reshape(X_test.shape[0], -1).astype(np.float32) -127.5) / 127.5

model = Model()
# Add layers
model.add(Dense(X.shape[1], 64))
model.add(Relu())
model.add(Dense(64, 64))
model.add(Relu())
model.add(Dense(64, 10))
model.add(SoftMax())
model.set(loss=CategoricalCrossEntropy(),optimizer=SGD(lr=0.001),accuracy=Accuracy_Categorical())
model.finalize()
model.train(X,y,validation_data=(X_test,y_test),epochs=1,batch_size=128,print_every=100)