import cv2
import numpy as np
import csv
from sys import exit

DEBUG_ShowFilm = True

def record():
    #Variables
    frameNum = int(input("Number of frames?   "))
    count = 0
    out_signal = np.zeros((frameNum, 3))
    
    #Define window for film
    cv2.namedWindow("Camera")
    
    #Open camera
    vc = cv2.VideoCapture(0)
    
    #Check if open and read first frame
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        print("Camera not opened. Lol")
        exit()
    
    #Select region of intrest
    ROI = cv2.selectROI("Camera",frame)
    
    
    #Gather data
    while count < frameNum:
        #Read new frame
        rval, frame = vc.read()
        
        #Crop frame
        cframe = frame[ROI[1]:ROI[1] + ROI[3], ROI[0]:ROI[0] + ROI[2],:]

        #Display frame
        if DEBUG_ShowFilm:
            cv2.imshow("Camera", cframe)
        
        #Calculate mean
        mean = np.mean(cframe, axis=(0,1))
        
        #append to list
        out_signal[count,] = mean
        count += 1
        
        #Exit when esc is pressed
        if cv2.waitKey(20) == 27:
            break

    #Flip signal to get RGB form
    out_signal = np.flip(out_signal, 1)

    #Release VC
    vc.release()
    
    #Destroy window
    cv2.destroyWindow("Camera")

    return out_signal

def readCSVFile():

    filename = input("Name of file:    ")

    if filename[0:4] != "Data/":
        filename = "Data/" + filename

    out_signal = []

    with open(filename, newline='') as file:
      file_reader = csv.reader(file,delimiter=" ")
      for t in file_reader:

        out_signal = np.append(out_signal,t)

    return out_signal

def readVideoFile():

    filename = input("Filename:   ")

    if filename[0:4] != "Data/":
        filename = "Data/" + filename

    capture = cv2.VideoCapture(filename, cv2.CAP_FFMPEG)

    if not capture.isOpened():
        print("Video not found. Lol")

    number_of_frames = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = capture.get(cv2.CAP_PROP_FPS)

    out_signal = np.zeros((number_of_frames,3))

    n = 0

    while capture.isOpened():
        ret, frame = capture.read()
        if not ret:
            break

        if n == 0:
            ROI = cv2.selectROI("Select ROI",frame)
            cv2.destroyWindow("Select ROI")

        c_frame = frame[ROI[1]:ROI[1] + ROI[3], ROI[0]:ROI[0] + ROI[2], :]

        out_signal[n,:] = np.mean(c_frame, axis=(0,1))
        n = n + 1

    capture.release()

    out_signal = np.flip(out_signal, 1)

    return out_signal
