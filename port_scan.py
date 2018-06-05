import socket
import sys
import threading
import time

def socket_scan(ip,port):
    try:
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sk.settimeout(1)
        port = int(port)
        st = sk.connect_ex((ip,port))
        if st == 0:
            print(ip+'开放端口：'+str(port)+'open')
        else:
            sk.close()
    except socket.error:
        #lock.release()
        pass
try:
    ip_start=sys.argv[1]
    ip_stop=sys.argv[2]
    port_list = ['23', '22', '80', '443', '445', '873', '3128', '3306', '1433', '4848', '4440', '6082', '6379', '7001', '7021', '7080', '7474', '7755', '7766', '7888', '8060', '8880', '8000', '8881', '8008', '8080', '8081', '8087', '8443', '8090', '8099', '8088', '8882', '8883', '8884', '8885', '8886', '8887', '8888', '9043', '9080', '9090', '9200', '10000', '15672', '18080', '11211', '27017', '50000']
    ip_1 = ip_start.split(".")
    ip_2 = ip_stop.split(".")
    cha = int(ip_2[-1])-int(ip_1[-1])
    for i in range(0,cha+1):
        ip = ip_1[0]+'.'+ip_1[1]+'.'+ip_1[2]+'.'+str(int(ip_1[-1])+i)
        for port in port_list:
            #lock = threading.Lock()
            t = threading.Thread(target=socket_scan, args=(ip,port))
            t.start()
            time.sleep(0.001)
            #t.join()
except:
    print(r"""
 ____    ___   ____   ______   _____    __   ____  ____  
|    \  /   \ |    \ |      | / ___/   /  ] /    ||    \ 
|  o  )|     ||  D  )|      |(   \_   /  / |  o  ||  _  |
|   _/ |  O  ||    / |_|  |_| \__  | /  /  |     ||  |  |
|  |   |     ||    \   |  |   /  \ |/   \_ |  _  ||  |  |
|  |   |     ||  .  \  |  |   \    |\     ||  |  ||  |  |
|__|    \___/ |__|\_|  |__|    \___| \____||__|__||__|__|
                                    by yangge
""")
    print("---------------------------------------------------")
    print("example：python portscan.py 10.10.10.1 10.10.10.254")
