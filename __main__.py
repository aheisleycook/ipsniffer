import sys
import socket
import logging
import ipaddress
isCOnnectable = []
notCOnnectablbler = []
"""
this sets to prt the usually hhtp otupund 80
"""
PORT = 80
if len(sys.argv) >= 1:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as t:
        ipselect  = list(sys.argv)
        
        for ip_adress in ipselect:
            try:
                a = t.connect_ex((ip_adress,PORT))
                isCOnnectable.append(a)
                ipaddress
            
            except Exception as b:
                notCOnnectablbler.append(b)
        for active in isCOnnectable:
            print(f"{active} : connected")
        for notactive in notCOnnectablbler:
            print(f"{notactive} not connected")
else:
    msg = """
    application name:ipsniffer\n
    expected input:
    192.168.1.80
    result:
    error i fthe port and ip is not connectable
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    print(msg)
    