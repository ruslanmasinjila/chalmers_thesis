import os
import socket
from threading import Thread
from datetime import datetime
import subprocess
import time


# Ports used
# 65432 is for listening to mmWave Visualizer
# 65431 is for listening to Java GUI

class Server():

    def __init__(self):
        self.configFileName = r"C:\chalmers_thesis\py_node sockets\16fps.cfg"
        self.HOST = '127.0.0.1'
        self.visualizerPORT = 65432
        self.fromJavaGUIPORT = 65431
        self.rootDIR=r"C:\chalmers_thesis\data"
        self.frameNum=1
        self.launchThreads()

        # 0 means don't capture
        # 1 means capture
        self.capture = 0
        self.currentGesture = None

        # The folder containing capture frames
        # The folder name consists of gesture name and current time
        self.currentDirectory = ""


    # For launching two servers
    def launchThreads(self):
        Thread(target = self.startVisualizerServer).start()
        Thread(target = self.startFromJavaGUIServer).start()
        time.sleep(2)
        subprocess.Popen(r"C:\Users\ruslan\guicomposer\runtime\gcruntime.v7\mmWave_Demo_Visualizer\launcher.exe")



    def startVisualizerServer(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Listening to port:", self.visualizerPORT)
            s.bind((self.HOST, self.visualizerPORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    try:
                        data = conn.recv(65536)
                    except:
                        print("Crashed...")
                        break
                    if(self.capture==1):
                        file = open( self.currentDirectory + "\\frame" + str(self.frameNum) + '.txt', 'w' )
                        file.write(data.decode('utf-8'))
                        file.close()
                        self.frameNum=self.frameNum+1
                    if not data:
                        break

    def startFromJavaGUIServer(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Listening to port:", self.fromJavaGUIPORT)
            s.bind((self.HOST, self.fromJavaGUIPORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    try:
                        data = conn.recv(65536)
                        data = data.decode('utf-8')
                    except:
                        print("Crashed...")
                        break
                    
                    # Create a folder with the name and
                    # time stamp of the gesture
                    if(data == "stop_capture"):
                        self.capture = 0

                    else:
                        self.frameNum = 1
                        self.capture = 1
                        self.currentGesture = data
                        # Create new folder using gesture name and current time
                        currentTime = datetime.now()
                        currentTime =   str(currentTime.year)+\
                                        str(currentTime.month)+\
                                        str(currentTime.day)+\
                                        str(currentTime.hour)+\
                                        str(currentTime.minute)+\
                                        str(currentTime.second)
                        
                        gesture_time = (self.currentGesture).replace(" ", "") +"_" + currentTime
                        self.currentDirectory = os.path.join(self.rootDIR, gesture_time)
                        os.mkdir(self.currentDirectory)
                    if not data:
                        break
                    
if __name__ == "__main__":

    server = Server()