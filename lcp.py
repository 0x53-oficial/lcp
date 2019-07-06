#   ___       ____ _____ 
#  / _ \__  _| ___|___ / 
# | | | \ \/ /___ \ |_ \ 
# | |_| |>  < ___) |__) |
#  \___//_/\_\____/____/
#
# LinuxCrackPass -> By 0x53.
# Twitter: @samueltuxx
# GitHub: https://github.com/0x53-oficial/

# Tested on: Manjaro Linux 18.0.4 in Python 3.7.3!

try:
	import crypt, string, argparse
except ImportError:
	print('Error in importing modules! Make sure they are installed (crypt, string, argparse).')
	exit()
	
parser = argparse.ArgumentParser(description='LCP by 0x53 | Script to crack linux passwords using Brute Force.')
parser.add_argument('--wordlist','-w', action='store', dest='wordlist', help='Set the Wordlist.', required=True)
parser.add_argument('-q','--quiet', action='store_true', dest='mode', default=False, help='Set quiet mode.', required=False)
parser.add_argument('--version', action='version', version='LCP Version: 1.1')
arguments = parser.parse_args()

wl = arguments.wordlist
mode = arguments.mode
hashToCrack = input("[+] Hash: ")
salt = input("[+] Salt: ")
print("")

try:
	wordlist = open(wl,'r' ,errors='ignore') # Read-Only.
	if mode == False:
		for word in wordlist.read().splitlines():
			gen = crypt.crypt(word, salt)
			print(word+" -> " + gen)
			if gen == hashToCrack:
				print("\n[+] Password Found: "+word)
				break
			else:
				continue
	else:
		for word in wordlist.read().splitlines():
			gen = crypt.crypt(word, salt)
			if gen == hashToCrack:
				print("[+] Password Found: "+word)
				break
			else:
				continue				
except KeyboardInterrupt:
	print("^C\nGoodBye ;(")
	exit()
except IOError:
	print("[-] No such file: "+wl)
