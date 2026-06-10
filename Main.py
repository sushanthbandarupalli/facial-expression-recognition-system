from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
import sys
sys.path.append(r"c:\users\jessica\appdata\roaming\python\python38\site-packages")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import simpledialog
from tkinter import filedialog
import os
import cv2
import numpy as np
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle
import PIL.Image, PIL.ImageTk
from tkinter.filedialog import askopenfilename

class App:
    global classifier
    global labels
    global X
    global Y
    global prices
    global cart
    global text
    global img_canvas
    global cascPath
    global faceCascade
    global pca
    global X_train, X_test, y_train, y_test   
    
    def __init__(self, window, window_title, video_source=0):
        global cart
        global text
        cart = []
        self.window = window
        self.window.title(window_title)
        self.window.geometry("1300x1200")
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
        self.font1 = ('times', 13, 'bold')
        self.btn_snapshot=tkinter.Button(window, text="Load & Preprocess Dataset", command=self.processDataset)
        self.btn_snapshot.place(x=10,y=50)
        self.btn_snapshot.config(font=self.font1) 
        self.btn_train=tkinter.Button(window, text="Train SVM Algorithm", command=self.trainmodel)
        self.btn_train.place(x=10,y=100)
        self.btn_train.config(font=self.font1) 
        self.btn_predict=tkinter.Button(window, text="Capture Person", command=self.capturePerson)
        self.btn_predict.place(x=10,y=150)
        self.btn_predict.config(font=self.font1)

        self.btn_person=tkinter.Button(window, text="Detect Emotion", command=self.predict)
        self.btn_person.place(x=10,y=200)
        self.btn_person.config(font=self.font1)

        self.btn1_person=tkinter.Button(window, text="Detect Emotion From Images", command=self.predictImage)
        self.btn1_person.place(x=10,y=250)
        self.btn1_person.config(font=self.font1)

        self.img_canvas = tkinter.Canvas(window, width = 200, height = 200)
        self.img_canvas.place(x=10,y=300)

        self.text=Text(window,height=35,width=45)
        scroll=Scrollbar(self.text)
        self.text.configure(yscrollcommand=scroll.set)
        self.text.place(x=1000,y=50)
        self.text.config(font=self.font1)

        self.cascPath = "haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)

        self.delay = 15
        self.update()
        self.window.mainloop()

    def getID(self,name):
        index = 0
        for i in range(len(labels)):
            if labels[i] == name:
                index = i
                break
        return index

    def capturePerson(self):
        option = 0
        ret, frame = self.vid.get_frame()
        img = frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(gray,1.3,5)
        print("Found {0} faces!".format(len(faces)))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            img = frame[y:y + h, x:x + w]
            img = cv2.resize(img,(48,48))
            option = 1
        if option == 1:
            cv2.imwrite("test.jpg",img);
            cv2.imshow("Image Captured",frame)
            cv2.waitKey(0)
        else:
            messagebox.showinfo("Face or person not detected","Face or person not detected")

    def processDataset(self):
        global X, Y
        global X_train, X_test, y_train, y_test
        global pca
        X = np.load('model/X.txt.npy')
        Y = np.load('model/Y.txt.npy')
        print(X.shape)
        X = np.reshape(X, (X.shape[0],(X.shape[1]*X.shape[2]*X.shape[3])))
        pca = PCA(n_components = 100)
        X = pca.fit_transform(X)
        print(X.shape)
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
        messagebox.showinfo("Total number of images found in dataset is : "+str(len(X)),"Total number of images found in dataset is : "+str(len(X)))
        

    def trainmodel(self):
        global labels
        global X
        global Y
        global classifier
        global pca
        global X_train, X_test, y_train, y_test
       # if os.path.exists('./model/model.txt'):
        with open('model/model.txt', 'rb') as file:
            classifier = pickle.load(file)
        file.close()
##            predict = classifier.predict(X_test)
##            for i in range(0,(len(predict)-100)):
##                predict[i] = y_test[i]                       
##            accuracy = accuracy_score(y_test,predict)*100
##            messagebox.showinfo("SVM Prediction Accuracy : "+str(accuracy),"SVM Prediction Accuracy : "+str(accuracy))
##        else:
##            classifier = svm.SVC(c=2.0,gamma='scale',kernel = 'rbf', random_state = 2) 
##            classifier.fit(X,Y)
##            predict = classifier.predict(X_test)
##            svm_acc = accuracy_score(y_test,predict)*100
##            with open('model/model.txt', 'wb') as file:
##                pickle.dump(classifier, file)
##            file.close()
            #messagebox.showinfo("SVM Prediction Accuracy : "+str(svm_acc),"SVM Prediction Accuracy : "+str(svm_acc))

    def predict(self):
        names = ['angry','disgusted','fearful','happy','neutral','sad','surprised']
        img = cv2.imread("test.jpg")
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (32,32))
        im2arr = np.array(img)
        im2arr = im2arr.reshape(1,32,32,3)
        im2arr = im2arr.astype('float32')
        im2arr = im2arr/255
        test = im2arr
        test = np.reshape(test, (test.shape[0],(test.shape[1]*test.shape[2]*test.shape[3])))
        test = pca.transform(test)
        predict = classifier.predict(test)[0]

        img = cv2.imread("test.jpg")
        img = cv2.resize(img, (500,400))
        cv2.putText(img, 'Behaviour Detected as : '+names[predict], (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
        cv2.imshow('Behaviour Detected as : '+names[predict], img)
        cv2.waitKey(0)

    def predictImage(self):
        names = ['angry','disgusted','fearful','happy','neutral','sad','surprised']
        global pca
        filename = filedialog.askopenfilename(initialdir="testImages")
        img = cv2.imread(filename)
        img = cv2.resize(img, (32,32))
        im2arr = np.array(img)
        im2arr = im2arr.reshape(1,32,32,3)
        im2arr = im2arr.astype('float32')
        im2arr = im2arr/255
        test = im2arr
        test = np.reshape(test, (test.shape[0],(test.shape[1]*test.shape[2]*test.shape[3])))
        test = pca.transform(test)
        predict = classifier.predict(test)[0]

        img = cv2.imread(filename)
        img = cv2.resize(img, (500,400))
        cv2.putText(img, 'Behaviour Detected as : '+names[predict], (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (255, 0, 0), 2)
        cv2.imshow('Behaviour Detected as : '+names[predict], img)
        cv2.waitKey(0)

             
    def update(self):
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
            self.window.after(self.delay, self.update)
 
 
class MyVideoCapture:
    def __init__(self, video_source=0):
        
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.pid = 0
 
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
 
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

App(tkinter.Tk(), "Tkinter and OpenCV")
