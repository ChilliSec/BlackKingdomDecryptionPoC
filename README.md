# Black KingDom Ransomware Decrypter POC
## [Cyberint](https://blog.cyberint.com) Research - 26 March 2021 v0.1

Provided as a simple proof-of-concept to allow Blue Teamers to test data recovery in a safe environment. Decryption will make use of the failover key whilst reading the IV from each encrypted file. Decrypted data will be written to a new file.

Code to crawl a disk and attempt the recovery of all files, as well as removing 0x00 padding and the encrypted file extension have been omitted for safety... add these at your own risk! ;)

---

THIS SCRIPT IS PROVIDED 'AS IS' FOR PROOF-OF-CONCEPT PURPOSES ONLY AND SHOULD NOT BE USED IN PRODUCTION ENVIRONMENTS OR DATA LOSS MAY OCCUR! ATTEMPTS TO DECRYPT DATA SHOULD BE CONDUCTED AGAINST BACKUPS IN A SAFE 'SECONDARY' ENVIRONMENT. NO WARRANTY EXPRESSED OR IMPLIED.
