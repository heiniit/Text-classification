# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 20:58:09 2018

@author: Heikki
"""

# Helper for downloading Finnish books from Gutenberg

from urllib.request import urlopen

def LoadFromGutenberg(url, file_name):
    book = urlopen(url) 
    with open(file_name, mode="w", encoding="ansi") as out:
        block = ""
        for row in book:
            str_row = str(row)
            new_str = str_row[2:-5] 
            new_str = new_str.replace("\\xc3\\xa4","ä")
            new_str = new_str.replace("\\xc3\\xb6","ö")
            new_str = new_str.replace("\\xc3\\x84","Ä")
            new_str = new_str.replace("\\xc3\\x96","Ö")
            new_str = new_str.replace("\\xc2\\xbb","")
            
            if len(new_str) == 0:
                if len(block) > 80:
                    out.write(block + "\n")
                block = ""
            else:
                block += new_str + " "
                
LoadFromGutenberg("http://www.gutenberg.org/cache/epub/11152/pg11152.txt", "Kivi1.txt") # Nummisuutarit
LoadFromGutenberg("http://www.gutenberg.org/cache/epub/12795/pg12795.txt", "Kivi2.txt") # Kihlaus
LoadFromGutenberg("http://www.gutenberg.org/cache/epub/11940/pg11940.txt", "Kivi3.txt") # Seitsemän veljestä
LoadFromGutenberg("http://www.gutenberg.org/cache/epub/11891/pg11891.txt", "Kivi4.txt") # Karkurit

LoadFromGutenberg("http://www.gutenberg.org/cache/epub/48321/pg48321.txt", "London1.txt") # Klondyken kuningas
LoadFromGutenberg("http://www.gutenberg.org/cache/epub/47983/pg47983.txt", "London2.txt") # Lumikenttien tytär
LoadFromGutenberg("http://www.gutenberg.org/cache/epub/45487/pg45487.txt", "London3.txt") # Erämaan kutsu
LoadFromGutenberg("http://www.gutenberg.org/cache/epub/48047/pg48047.txt", "London4.txt") # Kultaa ja kuntoa

LoadFromGutenberg("http://www.gutenberg.org/cache/epub/15632/pg15632.txt", "Shakespeare1.txt") # Hamlet
LoadFromGutenberg("http://www.gutenberg.org/cache/epub/15643/pg15643.txt", "Shakespeare2.txt") # Romeo ja Julia
LoadFromGutenberg("http://www.gutenberg.org/cache/epub/44831/pg44831.txt", "Shakespeare3.txt") # Kesäyön unelma
LoadFromGutenberg("http://www.gutenberg.org/cache/epub/16893/pg16893.txt", "Shakespeare4.txt") # Macbeth

