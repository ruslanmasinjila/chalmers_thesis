import socket

# Ports used
# 65432 is for listening to mmWave Visualizer
# 65431 is for listening to Java GUI

class Server():

    def __init__(self):
        
        self.HOST = '127.0.0.1' # Standard loopback interface address (localhost)
        self.PORT = 65432       # Port to listen on (non-privileged ports are > 1023)
        self.DIR=r"C:\chalmers_thesis\data"
        self.frameNum=1
        self.startVisualizerServer()


    def startVisualizerServer(self):
        file = open("C:\\chalmers_thesis\\data\\launched.txt",'w')
        file.write("server launched")
        file.close()
        print("Server Launched")
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Listening to port:", self.PORT)
            s.bind((self.HOST, self.PORT))
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