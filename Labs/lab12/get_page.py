'''
File:           get_page.py
Author:         Gurjinder Singh
Date:           12/4/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    introduction to the internet

'''
import requests
if __name__ == "__main__":
    grit_page = requests.get("http://www.umbc.edu").text
    count = len(grit_page.split("</a>"))
    print(count - 1)
