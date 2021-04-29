import string
import random
import time
import MD5

charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()+_'

hash24 = '4adc03f09184857ee1370f4001219d45'

string=''

FILE = open("wordlist.txt","w")

print ("[+] Start Time: ", time.strftime('%H:%M:%S'))
print ("\nLoading ... ")

for count in range(0,10000000000):
    for x in random.sample(charset,random.randint(1,6)):
        string+=x
    FILE.write(string+'\n')
    hash_random = MD5.calcmd5(string)
    if hash_random == hash24:
        print("\nPassword found : ")
        print (string)
        break
    string=''

FILE.close()
print ("[+] End Time: ", time.strftime('%H:%M:%S'))
print ("Done")
