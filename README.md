# bruteforce.py

**Code Analysis: Decrypting an Encrypted PDF**

This Python code uses the `pypdf` library to decrypt an encrypted PDF file using a password from a text file.

**Code Overview**

The code performs the following steps:

1. **Reads a dictionary file**: The code reads a text file (`dictionary.txt`) located at a specified path (`C:\...`). The file contains a list of passwords, one per line.
2. **Loads an encrypted PDF**: The code loads an encrypted PDF file (`encrypted.pdf`) using the `PdfReader` class from `pypdf`.
3. **Checks for encryption**: The code checks if the loaded PDF is encrypted using the `is_encrypted` method. If it is, the code proceeds to decrypt it.
4. **Tries to decrypt the PDF**: The code iterates over each line in the dictionary file. For each line, it attempts to decrypt the PDF using the `decrypt` method. The `decrypt` method