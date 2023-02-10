# currency-converter
Döviz Hesaplama Programı

This is a simple graphical user interface (GUI) program written in Python using PyQt5 library. 
The program provides an exchange rate conversion information between three currencies (USD, EUR, GBP) and Turkish Lira (TRY).

Requirements

PyQt5
requests
os

How it works

The program first requests the exchange rate data from the API (fixer.io) by making a GET request.
Then it displays the information on the GUI.
The user can get the updated exchange rate information by clicking the "Kur Bilgisini Göster" button.
How to run the program

To run the program, type the following command in the terminal:
python doviz.py


Please note that the API key for fixer.io is not valid and you will need to get a new API key from their website to use the program. 
The API key can be added to the 'api_key' function in the 'requestapi.py' file.
