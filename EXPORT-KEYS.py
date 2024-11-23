#!/usr/bin/python2

import base58
import binascii
import bitcoin
import sys
import textwrap
import pyfiglet
from multiprocessing import Pool
from multiprocessing import cpu_count


banner_text = "BTC CRACK"
wrapped_text = "\n".join(textwrap.wrap(banner_text, width=50))
banner = pyfiglet.figlet_format(wrapped_text)
print(banner)

#Print message
print('Join Us --> https://t.me/+TtAIawVFhwEyMzdk')
print ("                                     \n") 

readlength = 10*1024*1024

magic = b'ckey!'
magiclen = len(magic)

def b58c(hex):
    return base58.b58encode_check(hex)

if len(sys.argv) != 2:
    print("./{0} <filename>".format(sys.argv[0]))
    exit()

def search_key(data):
    keys = []
    pos = 0
    while True:
        pos = data.find(magic, pos)
        if pos == -1:
            break
        key_offset = pos - 52
        key_data = data[key_offset:key_offset + 32]
        keys.append(bitcoin.encode_privkey(key_data, 'wif') + "")
        pos += 1
    return keys
def process_file(filename):
    keys = []
    with open(filename, "rb") as f:
        while True:
            data = f.read(readlength)
            if not data:
                break
            keys.extend(search_key(data))
    return keys

p = Pool(cpu_count())

output = p.map(process_file, [sys.argv[1]])

with open("WIF-KEYS.txt", "w") as outfile:
    for keys in output:
        for key in keys:
            outfile.write(key + '\n')
print ("                                     \n")
print ("PRIVATE KEYS from wallet.dat are saved in WIF-KEYS.txt\n")
print ("                                     \n") 
print ("!!!.DISCLAIMER, this is for educational purposes.!!!\n")
print ("                                     \n") 
