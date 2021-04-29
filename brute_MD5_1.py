import itertools
import MD5
import string
import time

charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()+_'

hash24 = input("Enter HASH value : ")
string=''
maxlength = int(input("Enter PASSWORD length : "))

FILE = open("wordlist.txt","w")

print ("[+] Start Time: ", time.strftime('%H:%M:%S'))
print ("Loading....")

for xs in itertools.product(charset, repeat = maxlength):
    string = ''.join(xs)
    #print(string)
    FILE.write(string+'\n')
    hash_random = MD5.calcmd5(string)
    if hash_random==hash24:
        print("\nPassword found : ")
        print(string)
        break
    string=''

print ("[+] End Time: ", time.strftime('%H:%M:%S'))
FILE.close()
print("Done")
