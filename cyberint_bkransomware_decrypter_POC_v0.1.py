# ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███   ██▓ ███▄    █ ▄▄▄█████▓
#▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
#▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
#▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░  
#▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒░██░▒██░   ▓██░  ▒██▒ ░ 
#  ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░░▓  ░ ▒░   ▒CYBERINT.COM
#
title1 = "Black KingDom Ransomware Decrypter POC"
title2 = "Cyberint Research - 26 March 2021 v0.1"
title3 = "--------------------------------------"
#
# Provided as a simple proof-of-concept to allow Blue Teamers to 
# test data recovery in a safe environment. Decryption will make 
# use of the failover key whilst reading the IV from each encrypted
# file. Decrypted data will be written to a new file. 
#
# Code to crawl a disk and attempt the recovery of all files, as well
# as removing 0x00 padding and the encrypted file extension have been
# omitted for safety... add these at your own risk! ;)
#####
# THIS SCRIPT IS PROVIDED 'AS IS' FOR PROOF-OF-CONCEPT PURPOSES ONLY
# AND SHOULD NOT BE USED IN PRODUCTION ENVIRONMENTS OR DATA LOSS MAY
# OCCUR! ATTEMPTS TO DECRYPT DATA SHOULD BE CONDUCTED AGAINST BACKUPS
# IN A SAFE 'SECONDARY' ENVIRONMENT. NO WARRANTY EXPRESSED OR IMPLIED.
####

# Import the AES crypto module
from Crypto.Cipher import AES
# Import the sys module so we can grab the command-line arguments
import sys

# Defines the default key, as used when 'Mega' cannot be contacted...
# Those with huge computational resources may want to calculate MD5
# hashes for all permetations of [A-Z0-9]{64} to brute-force??
key = b'eebf143cf615ecbe2ede01527f8178b3'

# Decrypt function, requires the key, an IV and the encrypted data
def decrypt(key, iv, data):
    # Setup the AES object, as defined in the ransomware code
    aes = AES.new(key, AES.MODE_CBC, iv)
    # Return the decrypted data 
    return aes.decrypt(data)

if len(sys.argv) > 1:
    # We'll assume that you've supplied a valid path/filename
    encrypted_file = sys.argv[1] 
    # Open this file for 'r'eading as a 'b'inary...
    with open(encrypted_file, 'rb') as ef:
        # Read the IV from the first 16 bytes
        iv = ef.read(16)
        # Now read the encrypted data that follows the IV
        encrypted = ef.read()
    # We'll name the file "<ENCRYPTED_FILENAME>.decrypted"
    decrypted_file = '{}.decrypted'.format(sys.argv[1])
    # Open this file for 'w'riting as 'b'inary...
    with open(decrypted_file, 'wb') as df:
        # Decrypt the data
        decrypted = decrypt(key, iv, encrypted)
        # Write the (hopefully) decrypted data to a new file
        df.write(decrypted)
    # Show a preview so we can see if it worked...
    print("\n{}\n{}\n{}\nExtracted File IV : {}\nEncrypted Preview : {}\nDecrypted Preview : {}\n".format(title1, title2, title3, iv, encrypted[:16], decrypted[:16]))
else:
    # Someone forgot to supply a filename!
    print("\n{}\n{}\n{}\nUsage: python(3) <script.py> <encrypted_filename>\n".format(title1, title2, title3))