

import threading
from server import runServer
from Utils import get_host_ip
import requests


def startServer():
    runServer()

def pushIp():
    _ip = '0.0.0.0'
    _ip = str(_ip)
    while True:
        ip = get_host_ip()
        if ip == None:
            ip = _ip

        ip = str(ip)

        if ip == _ip:
            print 'ip == _ip'
        else:
            print 'ip != _ip'
            _ip = ip
            _url = 'http://23.83.255.85:11000/change?ips=' + ip
            print _url
            rep = requests.get(_url)

        threading._sleep(60 * 10)



def main():

    thread_getInfoDate = threading.Thread(target=pushIp, name='PushIp')
    thread_startServer = threading.Thread(target=startServer, name='startServer')

    thread_getInfoDate.start()
    thread_startServer.start()

    thread_getInfoDate.join()
    thread_startServer.join()

main()

# pushIp()