import socket
from threading import Thread

# Ports used
# 65432 is for listening to mmWave Visualizer
# 65431 is for listening to Java GUI

class Server():

    def __init__(self):
        
        self.HOST = '127.0.0.1'
        self.visualizerPORT = 65432
        self.fromJavaGUIPORT = 65431
        self.DIR=r"C:\chalmers_thesis\data"
        self.frameNum=1
        self.launchThreads()


    # For launching two servers
    def launchThreads(self):
        Thread(target = self.startVisualizerServer).start()
        Thread(target = self.startFromJavaGUIServer).start()


    def startVisualizerServer(self):
        file = open("C:\\chalmers_thesis\\data\\visualizerServer.txt",'w')
        file.write("server launched")
        file.close()
        print("Server Launched")
        
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
                    file = open( self.DIR + "frame" + str(self.frameNum) + '.txt', 'w' )
                    file.write(data.decode('utf-8'))
                    file.close()
                    print(data.decode('utf-8'))
                    self.frameNum=self.frameNum+1
                    if not data:
                        break

    def startFromJavaGUIServer(self):
        file = open("C:\\chalmers_thesis\\data\\fromJavaGUIServer.txt",'w')
        file.write("server launched")
        file.close()
        print("Server Launched")
        
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
                    except:
                        print("Crashed...")
                        break
                    file = open( self.DIR + "frame" + str(self.frameNum) + '.txt', 'w' )
                    file.write(data.decode('utf-8'))
                    file.close()
                    print(data.decode('utf-8'))
                    self.frameNum=self.frameNum+1
                    if not data:
                        break


if __name__ == "__main__":

    server = Server()