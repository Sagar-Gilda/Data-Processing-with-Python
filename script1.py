# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:42:30 2020
Topic   : Data Processing with Python
Abstract: How to use Python to batch download and extract the data files, 
          load thousands of files in Python via pandas, cleaning the data, 
          concatenating and joining data from different sources, converting
          between fields, aggregating, conditioning and many more data 
          processing operations.
FTP Connection Details: Below are the details of a dummy FTP folder which 
          can be used for hands-on practice.

          url : ftp.pyclass.com
          user: student@pyclass.com
          password: student123
"""

#import the FTP library
from ftplib import FTP

#Create a Connection
ftp = FTP("ftp.pyclass.com")
ftp.login("student@pyclass.com","student123")

#Check the list of data and folders in dir
ftp.nlst()

#change working directory
ftp.cwd("Data")

ftp.nlst()

#Go 1 directory backward
ftp.cwd("..")

ftp.nlst()

#Close the FTP connection
ftp.close()

"""Creating a basic Downloader Function"""
#Sample Function1
from ftplib import FTP

def ftpdownloader1(host,user,passwd):
    ftp = FTP(host)
    ftp.login(user,passwd)
    print(ftp.nlst())

ftpdownloader1("ftp.pyclass.com","student@pyclass.com","student123")

#Sample Function2
import os
def ftpdownloader2(host,user,passwd):
    ftp = FTP(host)
    ftp.login(user,passwd)  
    ftp.cwd("Data")
    os.chdir("C:\\Users\\intel\\Desktop\\python\\Data_processing_spyder")
    with open("isd-lite-format.pdf",'wb') as file:
        ftp.retrbinary('RETR isd-lite-format.pdf',file.write)

ftpdownloader2("ftp.pyclass.com","student@pyclass.com","student123")


"""*************************************************************************"""
"""*************************************************************************"""
"""*****************Creating an FTP File Downloader*************************"""

import os
from ftplib import FTP

def ftpdownloader(stationid,startyear,endyear,url="ftp.pyclass.com",
              user="student@pyclass.com",passwd="student123"):
    ftp = FTP(url)
    ftp.login(user,passwd)
    if not os.path.exists("C:\\Users\\intel\\Desktop\\python\\Data_processing_spyder"):
        os.makedirs("C:\\Users\\intel\\Desktop\\python\\Data_processing_spyder")
    os.chdir("C:\\Users\\intel\\Desktop\\python\\Data_processing_spyder")
    

    


