#!/usr/bin/python3
#// SaDsEc_001/challenge_001 Solution Created By AbdulConsole
import hashlib

def tohash(hash):
    hashu = hash.encode('utf-8')
    h = hashlib.sha256(hashu)
    return h.hexdigest()

f = open("sadsecCTF", "r")
hashUsername = f.read()
f.close()

uname = 'No Match Username found for '+hashUsername

with open('usernames.txt') as names:
    for line in names:
        line = line.strip()
        if tohash(line)==hashUsername:
            uname = line
            print('found: '+line)
            print(tohash(line))
print(uname)
