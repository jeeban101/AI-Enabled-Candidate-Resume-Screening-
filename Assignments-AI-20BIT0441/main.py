from PyQt5.QtWidgets import *
#import all the widgets for creating the GUI application
from PyQt5.uic import loadUiType
#.uic contains classes for handling the .ui files
import sys
#For access system-specific parameters and functions
from hashlib import *
#for hashing messages/data and password 
import base64
#for encoding the files
import random
#for implementing pseudo-random number generators for various distributions
import pyperclip
#for copy and paste clipboard functions.
import string
#for accessing to potentially useful constants
from cryptography.fernet import Fernet
#for encrypting and decrypting the data/text/messages
from PIL import Image
#for editing the images capabilities
import stepic
#for hiding arbitrary data within images
import wave
#provides a convenient interface to the WAV sound format
from pycipher import ColTrans, Caesar, Vigenere, ADFGX, ADFGVX, Affine, Autokey, Atbash, Beaufort, Bifid
from pycipher import SimpleSubstitution, Porta, Gronsfeld, M209, Playfair, Railfence, Rot13, Enigma
#contain many classical cipher algorithms
import monoalpha
#For generating code alphabets, as well as to encrypt and decrypt text
import re

ui,_ = loadUiType("Pratik (Nuclei).ui")  # This will load the main ui file


class MainApp(QMainWindow,ui):  # Class to create main window
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)# Call the inherited classes_init_method
        QMainWindow.__init__(self)
        self.setupUi(self) # Setup the UI File
        self.setWindowTitle("Pratik (Nuclei)")# Set the title as "Pratik (Nuclei)
        #calling the method
        self.UI() # window UI
        self.handle_button()
        self.handle_check()
        self.tabWidget.setCurrentIndex(0) # Set index as 0
        self.tabWidget.tabBar().setVisible(False) #Tab bar visibility False
        #Acessing the class attribute 
        self.message = ""
        self.hash_name = ""
        self.digest_type = ""
        self.file_hash_checksum_value = ""
        self.file_check = False
        self.generated_password = ""
        self.loaded_key = ""
        self.generated_key = ""
        self.browsed_image = ""
    


    # method for Pratik UI
    def UI(self):
        style = open("Pratik.css","r") #Connect to Pratik.css
        style = style.read()
        self.setStyleSheet(style)


    def handle_button(self):
        # for changing tabs
        self.pushButton.clicked.connect(self.change_tab_home)
        self.pushButton_2.clicked.connect(self.change_tab_encoding)
        self.pushButton_3.clicked.connect(self.change_tab_checksum)
        self.pushButton_4.clicked.connect(self.change_tab_hashing)
        self.pushButton_5.clicked.connect(self.change_tab_password_manager)
        self.pushButton_6.clicked.connect(self.change_tab_steagnography)
        self.pushButton_18.clicked.connect(self.change_tab_cryptography)

        # connecting buttons for encoding/decoding part
        self.pushButton_7.clicked.connect(self.encode_msg)
        self.pushButton_9.clicked.connect(self.decode_msg)
        self.pushButton_8.clicked.connect(self.browse_file_encodingDecoding)

        # connecting buttons for checksum part
        self.pushButton_12.clicked.connect(self.browse_file_checksum)
        self.pushButton_10.clicked.connect(self.generate_file_hash)
        self.pushButton_11.clicked.connect(self.hash_checksum)

        # connecting buttons for hashing
        self.pushButton_14.clicked.connect(self.generate_hash)
        self.pushButton_15.clicked.connect(self.browse_wordlist)
        self.pushButton_13.clicked.connect(self.crack_hash)

        # connecting buttons for password manager
        self.pushButton_19.clicked.connect(self.generate_password)
        self.pushButton_22.clicked.connect(self.copy_to_clipboard)
        self.pushButton_20.clicked.connect(self.generate_thekey)
        self.pushButton_23.clicked.connect(self.load_key)
        self.pushButton_21.clicked.connect(self.encrypt_message)
        self.pushButton_24.clicked.connect(self.decrypt_message)

        # connecting buttons for steagnography
        self.pushButton_25.clicked.connect(self.browse_image)
        self.pushButton_27.clicked.connect(self.generate_thekey)
        self.pushButton_26.clicked.connect(self.load_key)
        self.pushButton_16.clicked.connect(self.encode_image)
        self.pushButton_17.clicked.connect(self.decode_image)



    # methods to change tab
    def change_tab_home(self):
        self.tabWidget.setCurrentIndex(0)

    def change_tab_encoding(self):
        self.tabWidget.setCurrentIndex(1)

    def change_tab_checksum(self):
        self.tabWidget.setCurrentIndex(2)

    def change_tab_hashing(self):
        self.tabWidget.setCurrentIndex(3)

    def change_tab_password_manager(self):
        self.tabWidget.setCurrentIndex(4)

    def change_tab_steagnography(self):
        self.tabWidget.setCurrentIndex(5)

    def change_tab_cryptography(self):
        self.tabWidget.setCurrentIndex(6)

    def change_tab_caesar(self):
        self.tabWidget.setCurrentIndex(7)

    def change_tab_vigenere(self):
        self.tabWidget.setCurrentIndex(8)

    def change_tab_columar_transposition(self):
        self.tabWidget.setCurrentIndex(9)

    def change_tab_ADFGX(self):
        self.tabWidget.setCurrentIndex(10)

    def change_tab_ADFGVX(self):
        self.tabWidget.setCurrentIndex(11)

    def change_tab_affine(self):
        self.tabWidget.setCurrentIndex(12)

    def change_tab_autokey(self):
        self.tabWidget.setCurrentIndex(13)

    def change_tab_atbash(self):
        self.tabWidget.setCurrentIndex(14)

    def change_tab_beaufort(self):
        self.tabWidget.setCurrentIndex(15)

    def change_tab_bifid(self):
        self.tabWidget.setCurrentIndex(16)

    def change_tab_monoalphabetic_substitution(self):
        self.tabWidget.setCurrentIndex(17)

    def change_tab_enigma_m3(self):
        self.tabWidget.setCurrentIndex(18)

    def change_tab_multiplicative(self):
        self.tabWidget.setCurrentIndex(19)

    def change_tab_porta(self):
        self.tabWidget.setCurrentIndex(20)

    def change_tab_gronsfeld(self):
        self.tabWidget.setCurrentIndex(21)

    def change_tab_m209(self):
        self.tabWidget.setCurrentIndex(22)

    def change_tab_playfair(self):
        self.tabWidget.setCurrentIndex(23)

    def change_tab_polybius_square(self):
        self.tabWidget.setCurrentIndex(24)

    def change_tab_railfence(self):
        self.tabWidget.setCurrentIndex(25)

    def change_tab_rot13(self):
        self.tabWidget.setCurrentIndex(26)

    def change_tab_simple_substitution(self):
        self.tabWidget.setCurrentIndex(27)


    # methods for hashing and hash cracking 
    def generate_hash(self):#method for generating hash
        self.message = self.textEdit_2.toPlainText()#for entering message in textbox
        self.hash_type = self.comboBox.currentText()#for selecting hash type 
        self.digest_type = self.comboBox_2.currentText()#for selecting digest type

        # checking if the message box is not empty, Both, hash type and string type is selected
        if self.message == "" or self.hash_type == "Select HASH" or self.digest_type == "Select  digest Type":#Applying condition
            #error message
            QMessageBox.warning(self,"Data Error","Message Box Should not be Empty\nBoth Hash Type and Str Type Must be Selected")
        else:
            try:
                self.digest_hash(self.message,self.hash_type,self.digest_type)
            except:
                QMessageBox(self,"Error!","Oops looks like the encryption you choose is not supported")#error message


    def generate_file_hash(self):#Method for generating file hash
        self.message = self.textEdit_4.toPlainText()#for entering message in text box
        file_name = self.lineEdit_6.text()
        self.hash_type = self.comboBox_6.currentText()#choosing hash type
        self.digest_type = self.comboBox_5.currentText()#choosing digest type

        # checking if msg box is not empty, hash type and string type is selected
        if self.message == "" or self.hash_type == "Select HASH" or self.digest_type == "Select  digest Type":#Applying condition
            QMessageBox.warning(self,"Data Error","Message Box Should not be Empty\nBoth Hash Type and Str Type Must be Selected")
            #error message
        else:
            try:
                self.digest_file_hash(file_name,self.hash_type,self.digest_type)
            except:
                QMessageBox(self,"Error!","Oops looks like the encryption you choose is not supported")#error message


    def digest_hash(self,message,hash_name,digest_type):#method for digest_hash
        #Applying condition
        if hash_name == "NTLM":#choosing the hash name as NTLM
            if digest_type == "Hex String":#Choosing the sigest type as hex string
                hashObj = new('md4',message.encode('utf-16le')).hexdigest()
                #choosing the new hash object with md4 algorithm and encoding type utf-161e
                self.textBrowser.setText(hashObj)
            else:
                hashObj = new('md4',message.encode('utf-16le')).hexdigest()
                self.textBrowser.setText(str(hashObj))
        else:
            hashObj = new(hash_name)#returning the hash name 
            if digest_type == "Hex String":#choosing the digest type as hex string
                hashObj.update(message.encode())#encoding the message
                self.textBrowser.setText(hashObj.hexdigest())
            else:
                hashObj.update(message.encode())
                self.textBrowser.setText(str(hashObj.digest()))



    def digest_file_hash(self,file_name,hash_name,digest_type):#method for digest file hash

        if hash_name == "NTLM":#choosing the hash name NTLM
        #this function returns the md4 hash of the file passed into it 
            hashObj = new('md4')

            try:
                with open(file_name,"rb") as file:#open file for reading in the binary mode
                    chunk = 0#loop till the end of file
                    #choosing digest type as Hex string
                    if digest_type == "Hex String":#applying the condition
                        while chunk != b'':
                            chunk = file.read(2048)#read only 2048 bytes at a time
                            hashObj.update(chunk.encode('utf-16le'))#Updating in encoded format
                        #except the digest is returned as a string object of double length, containing only hexadecimal digits.
                        self.textBrowser_3.setText(hashObj.hexdigest())
                        self.file_hash_checksum_value = hashObj.hexdigest()#return checksum value containing hexadecimal digits
                    else:
                        while chunk != b'':
                            chunk = file.read(2048)#read only 2048 bytes at a time
                            hashObj.update(chunk.encode('utf-16le'))
                        self.textBrowser_3.setText(str(hashObj.digest()))
                        self.file_hash_checksum_value = str(hashObj.digest())
            except FileNotFoundError:#if the selected file is not found 
                QMessageBox.warning(self, "File Error","File Not Found!")#displaying error message
            except:
                QMessageBox.warning(self, "Error!", "File choosing operation was cancled")#displaying error message

        else:
            hashObj = new(hash_name)

            try:
                with open(file_name,"rb") as file:
                    chunk = 0
                    if digest_type == "Hex String":#if digest type is selected as hex string
                        while chunk != b'':
                            chunk = file.read(2048)#read only 2048 bytes at a time
                            hashObj.update(chunk)
                        self.textBrowser_3.setText(hashObj.hexdigest())
                        #except the digest is returned as a string object of double length, containing only hexadecimal digits.
                        self.file_hash_checksum_value = hashObj.hexdigest()#return checksum value containing hexadecimal digits
                    else:
                        while chunk != b'':
                            chunk = file.read(2048)#read only 2048 bytes at a time
                            hashObj.update(chunk)
                        self.textBrowser_3.setText(str(hashObj.digest()))
                        self.file_hash_checksum_value = str(hashObj.digest())
            except FileNotFoundError:
                QMessageBox.warning(self, "File Error","File Not Found!")#error message
            except:
                QMessageBox.warning(self, "Error!", "File choosing operation was cancled")#error message


    def browse_wordlist(self):#method for browse wordlist
        try:
            filename = QFileDialog.getOpenFileNames(self, "Select a wordlist file: ", "","Text File (*.txt)")#get method
            self.file = filename[0][0]
            self.lineEdit_3.setText(self.file)
        except:
            QMessageBox.about(self,"Pratik (Nuclei)","File Not Selected")#error message

    def crack_hash(self):
        self.message = self.textEdit_2.toPlainText()
        self.hash_type = self.comboBox.currentText()
        self.digest_type = self.comboBox_2.currentText()
        self.wordlist = self.lineEdit_3.text()

        # checking if msg box is not empty, hash type and string type is selected
        if self.message == "" or self.hash_type == "Select HASH" or self.digest_type == "Select  digest Type" or self.wordlist == "":
            QMessageBox.warning(self, "Data Error","Message Box Should not be Empty\nBoth Hash Type and Str Type Must be Selected\nWordlist is not selected")
        else:
            self.check_hash(self.message, self.hash_type, self.digest_type,self.wordlist)


    def check_hash(self,message,hash_name,digest_type,word_list):#method for checking hash

        p = ""
        m = message
        with open(word_list,"rt",errors='ignore') as wordlist:
            for pwd in wordlist:
                pwd = pwd.strip()
                if hash_name=="NTLM":#hash algorithm
                    hashObj = new('md4')
                    if digest_type == "Hex String":
                        hashObj.update(pwd.encode('utf-16le'))
                        p = hashObj.hexdigest()
                    else:
                        hashObj.update(pwd.encode('utf-16le'))
                        p = hashObj.digest()

                else:
                    hashObj = new(hash_name)
                    if digest_type == "Hex String":
                        hashObj.update(pwd.encode())
                        p = hashObj.hexdigest()
                    else:
                        hashObj.update(pwd.encode())
                        p = hashObj.digest()

                if str(p) == m:
                    self.textBrowser_2.setText(pwd)
                    QMessageBox.about(self, "Congratulations!", "Password has been cracked")
                    break
                else:
                    continue
            else:
                self.textBrowser_2.clear()
                QMessageBox.about(self,"Oops!","Password not found in wordlist")
    # methods for hashing and hash cracking ends here


    # methods for hash checksum starts here
    def browse_file_checksum(self):
        try:
            filename = QFileDialog.getOpenFileNames(self, "Select a file: ", "","All File (*.*)")
            self.file = filename[0][0]
            self.lineEdit_6.setText(self.file)
        except:
            QMessageBox.about(self,"Pratik (Nuclei)","File Not Selected")

    def hash_checksum(self):
        self.message = self.textEdit_4.toPlainText()

        if self.file_hash_checksum_value != "" and self.message != "":
            if self.message == self.file_hash_checksum_value:
                QMessageBox.about(self, "File Integrity Result", "Checksum Hash is Verified :)")
            else:
                QMessageBox.warning(self, "File Integrity Result", "Checksum Hash is Not Verified :(")
        else:
            QMessageBox.warning(self, "Data Error!", "Hash or File Hash value is missing!")
    # methods for hash checksum ends here


    # methods for encoding and decoding starts here
    def encode_msg(self):
        self.message = self.textEdit.toPlainText()
        encoding_format = self.comboBox_3.currentText()
        encoding_type = self.comboBox_4.currentText()

        try:
            if self.message != "" and encoding_format != "Select Encoding" and encoding_type!="Encoding Type":
                if encoding_type=="base16":
                    encoded_data = base64.b16encode(bytes(self.message,encoding=encoding_format))
                    encoded_data = str(encoded_data)[2:-1]
                    self.textBrowser_4.setText(encoded_data)
                if encoding_type=="base32":
                    encoded_data = base64.b32encode(bytes(self.message, encoding=encoding_format))
                    encoded_data = str(encoded_data)[2:-1]
                    self.textBrowser_4.setText(encoded_data)

                if encoding_type=="base64":
                    encoded_data = base64.b64encode(bytes(self.message, encoding=encoding_format))
                    encoded_data = str(encoded_data)[2:-1]
                    self.textBrowser_4.setText(encoded_data)

                if encoding_type=="base85":
                    encoded_data = base64.b85encode(bytes(self.message, encoding=encoding_format))
                    encoded_data = str(encoded_data)[2:-1]
                    self.textBrowser_4.setText(encoded_data)

                if encoding_type=="a85":
                    encoded_data = base64.a85encode(bytes(self.message, encoding=encoding_format))
                    encoded_data = str(encoded_data)[2:-1]
                    self.textBrowser_4.setText(encoded_data)

                if encoding_type=="standard_base64":
                    encoded_data = base64.standard_b64encode(bytes(self.message, encoding=encoding_format))
                    encoded_data = str(encoded_data)[2:-1]
                    self.textBrowser_4.setText(encoded_data)

                if encoding_type=="urlsafe_base64":
                    encoded_data = base64.urlsafe_b64encode(bytes(self.message, encoding=encoding_format))
                    encoded_data = str(encoded_data)[2:-1]
                    self.textBrowser_4.setText(encoded_data)

            else:
                if self.file_check == True:
                    file = self.lineEdit_5.text()
                    if file!="":
                        try:
                            enc_file_name = QFileDialog.getSaveFileName(self,"Save File as","encoded_file.txt","Text File (*.txt)")
                            enc_file = enc_file_name[0]
                            with open(file, 'rb') as file_input, open(enc_file, 'wb') as file_output:
                                base64.encode(file_input,file_output)
                            QMessageBox.about(self, "Hurray!","File encoded and saved successfully")

                        except:
                            QMessageBox.warning(self, "Data Error","Error While saving file please try again!")

                else:
                    QMessageBox.warning(self,"Input Error","Message box empty or Encoding and encoding type not selected")

        except:
            QMessageBox.warning(self, "Data Error","Encoding type not supported!\nRun Time Error Occured!\nTry other Encoding option")

    def decode_msg(self):
        self.message = self.textEdit.toPlainText()
        encoding_format = self.comboBox_3.currentText()
        encoding_type = self.comboBox_4.currentText()

        try:
            if self.message != "" and encoding_format != "Select Encoding" and encoding_type != "Encoding Type":
                if encoding_type == "base16":
                    decoded_data = base64.b16decode(bytes(self.message, encoding=encoding_format))
                    decoded_data = str(decoded_data)[2:-1]
                    self.textBrowser_4.setText(decoded_data)
                if encoding_type == "base32":
                    decoded_data = base64.b32decode(bytes(self.message, encoding=encoding_format))
                    decoded_data = str(decoded_data)[2:-1]
                    self.textBrowser_4.setText(decoded_data)

                if encoding_type == "base64":
                    decoded_data = base64.b64decode(bytes(self.message, encoding=encoding_format))
                    decoded_data = str(decoded_data)[2:-1]
                    self.textBrowser_4.setText(decoded_data)

                if encoding_type == "base85":
                    decoded_data = base64.b85decode(bytes(self.message, encoding=encoding_format))
                    decoded_data = str(decoded_data)[2:-1]
                    self.textBrowser_4.setText(decoded_data)

                if encoding_type == "a85":
                    decoded_data = base64.a85decode(bytes(self.message, encoding=encoding_format))
                    decoded_data = str(decoded_data)[2:-1]
                    self.textBrowser_4.setText(decoded_data)

                if encoding_type == "standard_base64":
                    decoded_data = base64.standard_b64decode(bytes(self.message, encoding=encoding_format))
                    decoded_data = str(decoded_data)[2:-1]
                    self.textBrowser_4.setText(decoded_data)

                if encoding_type == "urlsafe_base64":
                    decoded_data = base64.urlsafe_b64decode(bytes(self.message, encoding=encoding_format))
                    decoded_data = str(decoded_data)[2:-1]
                    self.textBrowser_4.setText(decoded_data)

            else:
                if self.file_check == True:
                    file = self.lineEdit_5.text()
                    if file!="":
                        try:
                            enc_file_name = QFileDialog.getSaveFileName(self,"Save File as","decoded_file.txt","All File (*.*)")
                            enc_file = enc_file_name[0]
                            with open(file, 'rb') as file_input, open(enc_file, 'wb') as file_output:
                                base64.decode(file_input,file_output)
                            QMessageBox.about(self, "Hurray!","File decoded and saved successfully")

                        except:
                            QMessageBox.warning(self, "Data Error","Error While saving file please try again!")

                else:
                    QMessageBox.warning(self,"Input Error","Message box empty or Encoding and encoding type not selected")

        except:
            QMessageBox.warning(self, "Data Error", "Encoding type not supported!\nRun Time Error Occured!\nTry other Encoding option")

    def browse_file_encodingDecoding(self):
        try:
            filename = QFileDialog.getOpenFileNames(self, "Select a text file: ", "","Text File (*.txt)")
            self.file = filename[0][0]
            self.lineEdit_5.setText(self.file)
        except:
            QMessageBox.about(self,"Pratik (Nuclei)","File Not Selected")

    def handle_check(self):
        self.checkBox.toggled.connect(self.file_on)

    def file_on(self):
        if self.checkBox.isChecked():
            self.file_check = True
        else:
            self.file_check = False
    # methods for encoding and decoding ends here


    # methods for password manager starts here
    def generate_password(self):#method for generating password
         #Characters to generate password from
        chars = string.ascii_letters + string.digits + string.punctuation
        #Spinbox() widget is used to select from a fixed number of values
        password_length = self.spinBox.value()#Entering the length of the password from spinbox
        self.generated_password = ""
        for c in range(password_length):#length of the password
            self.generated_password += random.choice(chars)#using random module for generating random password

        self.lineEdit_4.setText(self.generated_password)


    def copy_to_clipboard(self):#method for copy to clipbord
        self.generated_password = self.lineEdit_4.text()
        pyperclip.copy(self.generated_password)#Using pyprclip module for copying password
        QMessageBox.about(self, "Copied!", "Password Copied to Clipboard!")#Message gnerated as password has been copyed

    def generate_thekey(self):#method for generate key
        try:#save the key file as encryption_key.key
            key_file = QFileDialog.getSaveFileName(self, "Save Key File as", "encryption_key.key", "Key File (*.key)")
            self.generated_key = key_file[0]#generating key
            key = Fernet.generate_key()#using external module fernet for encryption
            #file is opened for writing in binary mode
            with open(self.generated_key, "wb") as key_file:
                key_file.write(key)

            if self.tabWidget.currentIndex()==4:
                self.textBrowser_6.setText(self.generated_key)

            if self.tabWidget.currentIndex()==5:
                self.textBrowser_8.setText(self.generated_key)

            QMessageBox.about(self, "Key Generated", "Key File generated and saved")#key generated and saved in the system
        except:#Error warning
            QMessageBox.warning(self, "Error!", "Opps! an error occurred during key generation\nPlease! try again once")
            #\n give us new line


    def load_key(self):#method for loading key
        try:
            #open the key file
            key_file = QFileDialog.getOpenFileNames(self, "Select Key File: ", "encryption_key.key", "Key File (*.key)")
            loaded_key_file = key_file[0][0]#loading the key file
            #opened for reading in binary mode
            with open(loaded_key_file, "rb") as f:
                self.loaded_key = f.readline()

            if self.tabWidget.currentIndex()==4:
                self.textBrowser_6.setText(loaded_key_file)

            if self.tabWidget.currentIndex()==5:
                self.textBrowser_8.setText(loaded_key_file)
             #key loaded successfully
            QMessageBox.about(self, "Key Loaded", "Key File Loaded Successfully!")
        except:
            #Error messagw
            QMessageBox.warning(self, "Error!", "Opps! an error occurred during key loading\nPlease! try again once")
            #\n give us new line


    def encrypt_message(self):#method for encrypting messae
        self.generated_password = self.lineEdit_4.text()
        #loaded key is empty
        if self.loaded_key=="" or self.generated_password=="":#Generated password is empty
        #Displaying the error message if the generated password and loaded key is empty
            QMessageBox.warning(self, "Error", "Key or Generated password is missing")
        else:
        	#Executing further process if password and key is not empty
            encoded_message = self.generated_password.encode()#encode message
            #create instance of fernet and load the key
            f = Fernet(self.loaded_key) #using the external module fernet for encryption
            encrypted_message = f.encrypt(encoded_message)#encrypt the message
            #Saving the file in .txt extension
            password_file = QFileDialog.getSaveFileName(self, "Save Password File as", "password_1.txt", "Text File (*.txt)")
            pass_file = password_file[0]
            self.lineEdit_2.setText(pass_file)
            #open the file for writing in binary mode
            with open(pass_file, "wb") as file:
                file.write(encrypted_message)
                #displaying the text as password encrypted successfully if the process is correct

            QMessageBox.about(self, "Password Encrypted", "Encrypted Password File Saved Successfully!")


    def decrypt_message(self):#method for decrypting message
    	#loaded key is not empty
        if self.loaded_key!="":
            key = self.loaded_key
            #create instance of fernet wit encryption key
            f = Fernet(key)#using the module Fernet 

            #opening the .txt file (encrypted file)
            password_file = QFileDialog.getOpenFileNames(self, "Select Password File: ", "password_1.txt", "Text File (*.txt)")
            pass_file = password_file[0][0]
            #open the file for reading in binary format
            with open(pass_file, "rb") as file:
                encrypted_message = file.readline()

            decrypted_message = f.decrypt(encrypted_message)

            password = decrypted_message.decode()

            self.textBrowser_5.setText(password)
            #Applying condition if the process is correct
            QMessageBox.about(self, "Password Decrypted", "Encrypted Password have been Decrypted!")
        else:
        	#if the process is incorrect
            QMessageBox.warning(self, "Error", "Key Not Loaded or password file missing")
    # methods for password manager ends here


    # methods for steagnography starts here
    # Note: generate_key and load_key methods will be used of Password Manager
    def browse_image(self):#method for browse_image
        try:#get method for getting file name
            image_file = QFileDialog.getOpenFileNames(self, "Select Image/Audio(wav) File: ", "Image/Audio(wav) file Only","JPG (*.jpg);;JPEG (*.jpeg);;PNG (*.png);;GIF (*.gif);;BMP (*.bmp);;ICO (*.ico);;Wave (*.wav) ")
            img_file = image_file[0][0]
            self.textBrowser_7.setText(img_file)
            self.browsed_image = img_file#browsing image file
        except:
            QMessageBox.about(self,"Pratik (Nuclei)","File Not Selected")#error message


    def encrypt_message_image(self,message):#method for encrypt message image
        key = self.loaded_key#loading key
        encoded_message = message.encode()
        f = Fernet(key)#using python external module fernet for encryption
        encrypted_message = f.encrypt(encoded_message)

        return encrypted_message#returning the encrypted message

    def decrypt_message_image(self,encrypted_message):#method for decrypting message image
        key = self.loaded_key
        f = Fernet(key)#using fernet encryption
        decrypted_message = f.decrypt(encrypted_message)#decrypting the encrypted message using fernet
        decoded_img = decrypted_message.decode()
        self.textBrowser_9.setText(decoded_img)

    def encode_image(self): #method for encode image
        self.message = self.textEdit_3.toPlainText()
        if self.message=="" or self.browsed_image=="":#applying condition
            QMessageBox.warning(self,"Error!","Message box empty or Image/Audio(wav) not browsed")#error message
        else:
            if self.loaded_key =="":#if the key is not loaded
                #Error message popup
                QMessageBox.warning(self, "Warning!", "Key is not loaded. If you proceed further,\nEncoded message will not be encrypted and will be visible easily")
                if self.browsed_image.endswith(".wav"):#.WAV format recognized as audio
                    try:#opening the audi file for reading in the binary format 
                        audio_file  = wave.open(self.browsed_image, mode='rb')
                        frame_bytes = bytearray(list(audio_file.readframes(audio_file.getnframes())))
                        self.message = self.message + int((len(frame_bytes)-(len(self.message)*8*8))/8) *'#'#applying LSB technique
                        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in self.message])))
                        for i, bit in enumerate(bits):
                            frame_bytes[i] = (frame_bytes[i] & 254) | bit#calculating the frame bytes

                        frame_modified = bytes(frame_bytes)
                          #saving the audio file
                        encoded_audio_file = QFileDialog.getSaveFileName(self, "Select Audio(wav) File: ", "encoded_audio.wav","Wave (*.wav)")
                        enc_audio_file = encoded_audio_file[0]
                         #opening the file for writing in the binary format
                        with wave.open(enc_audio_file, 'wb') as fd:
                            fd.setparams(audio_file.getparams())#get method
                            fd.writeframes(frame_modified)
                        audio_file.close()#closing the audio file after the process is completed

                        QMessageBox.about(self, "Audio Encoded", "Message encoded successfully in Audio File")#encoded sucessfully
                    except:#Error message if the process is wrong 
                        QMessageBox.warning(self, "Error", "Oops! problem occured while saving please try again!")

                if self.browsed_image.endswith(".jpg") or self.browsed_image.endswith(".jpeg") or self.browsed_image.endswith(".png") or self.browsed_image.endswith(".gif") or self.browsed_image.endswith(".bmp") or self.browsed_image.endswith(".ico"):
                    try:
                        original_image = Image.open(self.browsed_image)
                        encoded_img = stepic.encode(original_image,self.message)
                        encoded_img_file = QFileDialog.getSaveFileName(self, "Select Image File: ", "encoded_image.png","PNG (*.png);;GIF (*.gif);;BMP (*.bmp);;ICO (*.ico)")
                        enc_img_file = encoded_img_file[0]
                        encoded_img.save(enc_img_file)
                        QMessageBox.about(self, "Image Encoded", "Message encoded successfully in image")#process sucessful
                    except:
                        QMessageBox.warning(self, "Error", "Oops! problem occured while saving please try again!")#Error message

            else:
                if self.browsed_image.endswith(".wav"):#if the browse image end with .wav
                    try:
                        self.message = self.encrypt_message_image(self.message)
                        self.message = str(self.message)
                        audio_file = wave.open(self.browsed_image, mode='rb')
                        frame_bytes = bytearray(list(audio_file.readframes(audio_file.getnframes())))
                        self.message = self.message + int((len(frame_bytes)-(len(self.message)*8*8))/8) *'#'
                        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in self.message])))
                        for i, bit in enumerate(bits):
                            frame_bytes[i] = (frame_bytes[i] & 254) | bit

                        frame_modified = bytes(frame_bytes)

                        encoded_audio_file = QFileDialog.getSaveFileName(self, "Select Audio(wav) File: ", "encoded_audio.wav","Wave (*.wav)")
                        enc_audio_file = encoded_audio_file[0]

                        with wave.open(enc_audio_file, 'wb') as fd:
                            fd.setparams(audio_file.getparams())
                            fd.writeframes(frame_modified)
                        audio_file.close()

                        QMessageBox.about(self, "Audio Encoded", "Message encoded successfully in Audio File")
                    except:
                        QMessageBox.warning(self, "Error", "Oops! problem occured while saving please try again!")

                if self.browsed_image.endswith(".jpg") or self.browsed_image.endswith(".jpeg") or self.browsed_image.endswith(".png") or self.browsed_image.endswith(".gif") or self.browsed_image.endswith(".bmp") or self.browsed_image.endswith(".ico"):
                    try:
                        self.message = self.encrypt_message_image(self.message)
                        original_image = Image.open(self.browsed_image)
                        encoded_img = stepic.encode(original_image,self.message)
                        encoded_img_file = QFileDialog.getSaveFileName(self, "Select Image File: ", "encoded_image.png","PNG (*.png);;GIF (*.gif);;BMP (*.bmp);;ICO (*.ico)")
                        enc_img_file = encoded_img_file[0]
                        encoded_img.save(enc_img_file)
                        QMessageBox.about(self, "Image Encoded", "Encrypted message encoded successfully in image")
                    except:
                        QMessageBox.warning(self, "Error", "Oops! problem occured while saving please try again!")


    def decode_image(self):#method for decoding image
        if self.browsed_image == "":
            QMessageBox.warning(self, "Error!", "Image not browsed")#error message popup if the image is not selected
        else:
            if self.browsed_image.endswith(".jpg") or self.browsed_image.endswith(".jpeg"):#.jpg,.jpeg format image
                QMessageBox.warning(self, "Warning!","JPG or JPEG File is not supported for decode,\nPlease rerun the program and choose other file extension")
            else:
                if self.loaded_key == "":#key not loaded
                    QMessageBox.warning(self, "Warning!","Key is not loaded. If you proceed further,\nif encoded message is encrypted then, only encrypted message will be visible")
                    if self.browsed_image.endswith(".wav"):#.wav format
                        try:
                            audio_file = wave.open(self.browsed_image, mode='rb')#opening the file for reading in binary format 
                            frame_bytes = bytearray(list(audio_file.readframes(audio_file.getnframes())))#applying lsb
                            extracted_bytes = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
                            message = "".join(chr(int("".join(map(str,extracted_bytes[i:i+8])),2)) for i in range(0,len(extracted_bytes),8))
                            decoded_msg = message.split("###")[0]
                            self.textBrowser_9.setText(decoded_msg)
                            QMessageBox.about(self, "Audio Decoded", "Message decoded successfully from Audio File")
                        except:
                            QMessageBox.warning(self, "Error", "Oops! problem occured while decoding please try again!")

                    else:#applying condition
                        try:
                            encoded_img = Image.open(self.browsed_image)
                            decoded_img = stepic.decode(encoded_img)
                            self.textBrowser_9.setText(decoded_img)
                            QMessageBox.about(self, "Image Decoded", "Message decoded successfully from image")
                        except:
                            QMessageBox.warning(self, "Error", "Oops! problem occured while decoding please try again!")

                else:
                    if self.browsed_image.endswith(".wav"):
                        try:
                            audio_file = wave.open(self.browsed_image, mode='rb')
                            frame_bytes = bytearray(list(audio_file.readframes(audio_file.getnframes())))
                            extracted_bytes = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
                            message = "".join(chr(int("".join(map(str,extracted_bytes[i:i+8])),2)) for i in range(0,len(extracted_bytes),8))
                            decoded_msg = message.split("###")[0]

                            decoded_msg = decoded_msg[2:-1]
                            decoded_msg = bytes(decoded_msg,encoding="utf-8")
                            decoded_msg = self.decrypt_message_image(decoded_msg)

                            # self.textBrowser_9.setText(decoded_msg)
                            QMessageBox.about(self, "Audio Decoded", "Message decoded successfully from Audio File")
                        except:
                            QMessageBox.warning(self, "Error", "Oops! problem occured while decoding please try again!")

                    else:
                        try:
                            encoded_img = Image.open(self.browsed_image)
                            decoded_img = stepic.decode(encoded_img)
                            self.decrypt_message_image(bytes(decoded_img, encoding="utf-8"))
                            QMessageBox.about(self, "Image Decoded", "Message decoded successfully from image")
                        except:
                            QMessageBox.warning(self, "Error", "Oops! problem occured while decoding please try again!")

    # methods for steagnography ends here


# methods for cryptography ends here


def main():  # Main function to execute app
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
