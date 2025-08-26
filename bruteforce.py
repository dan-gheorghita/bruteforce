from pypdf import PdfReader, PdfWriter
from pathlib import Path
import os

p = Path(r'C:\Users\Dan\Downloads\Python codes\Automate_the_Boring_Stuff_2e_onlinematerials\automate_online-materials\dictionary.txt')

dictonaryFile = open(p)

reader = PdfReader("encrypted.pdf")

if reader.is_encrypted:
    lines = dictonaryFile.readlines()  
    for line in lines:
        if reader.decrypt(line.strip()) or reader.decrypt(line.strip().lower()):
            writer = PdfWriter(clone_from=reader)

            print("Decrypted with: " + line.strip())
            # Save the new PDF to a file
            with open("decrypted-pdf.pdf", "wb") as f:
                writer.write(f)
            break
        #print(line.strip())
