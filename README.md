# Black KingDom Ransomware Decrypter POC
## [Cyberint](https://blog.cyberint.com) Research - 26 March 2021 v0.1

Provided as a simple proof-of-concept to allow Blue Teamers to test data recovery in a safe environment. Decryption will make use of the failover key whilst reading the IV from each encrypted file. Decrypted data will be written to a new file.

Code to crawl a disk and attempt the recovery of all files, as well as removing 0x00 padding and the encrypted file extension have been omitted for safety... add these at your own risk! ;)

* <script>.py - The decyption PoC, written in Python 3 and should be supplied a single Black KingDom encrypted file path/name as an argument.
* encrypted[123].txt - Example Black KingDom encrypted files (from the Python directory on my test VM) for testing purposes... note the IV differs per file!
* encrypted[123].txt.decrypted - Proof that the tool works when the data is encrypted using the failover key.

By all means rewrite this code or wrap it in a directory walker to decrypt everything on an impacted server BUT consider that it will create new files (disk space?) and that it won't handle files that were corrupted by the original process or encrypted multiple times. Furthermore, exercise caution if attempting to automatically remove the 0x00 padding that may have been added to files as well as automatically truncating filenames using some right-trim type method to remove the random 4-7 character file extensions!

Be on the look out for our report that features this script, it should be dropping any time soon on the blog!

---

THIS SCRIPT IS PROVIDED 'AS IS' FOR PROOF-OF-CONCEPT PURPOSES ONLY AND SHOULD NOT BE USED IN PRODUCTION ENVIRONMENTS OR DATA LOSS MAY OCCUR! ATTEMPTS TO DECRYPT DATA SHOULD BE CONDUCTED AGAINST BACKUPS IN A SAFE 'SECONDARY' ENVIRONMENT. NO WARRANTY EXPRESSED OR IMPLIED.
