from psutil import process_iter
from signal import SIGTERM # or SIGKILL

visualizerPORT = 65432
fromJAVAGUIPORT = 65431
toJAVAGUIPORT=65430
allPorts = [visualizerPORT, fromJAVAGUIPORT,toJAVAGUIPORT]

for proc in process_iter():
    for conns in proc.connections(kind='inet'):
        for i in allPorts:
            if conns.laddr.port == i:
                try:
                    proc.send_signal(SIGTERM) # or SIGKILL
                except:
                    pass
                continue 