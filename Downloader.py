from Google import Create_Service
import pandas as pd
import os
import requests
import openpyxl

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
gsheetId = '1Po0VxAMtw1dR2PcTozKHRLcDu0rWXCZIWsuV8XmB_lU'

s = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
gs = s.spreadsheets()

counter = 0

def image_fetch(url, file_path):
    """
    Parameters:
    url (string): A image url

    file_path (string): Directory name where the image will be saved.

    Output:
    url's image will be saved in the file_path directory

    """

    """
    123:-12 is a distance from the right end of the url, which gets text
    """
    image_name = url[123:-12]

    fetched_image_name = file_path + str(image_name) + '.jpg'  ## saving the image as jpg

    print(url[123:-12])

    global counter
    try:
        r = requests.get(url)

        with open(fetched_image_name, 'wb') as f:
            f.write(r.content)
            counter += 1
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException,
            requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print(str(e))
        r = None
    except Exception as e:
        raise

    return r

def main():
    """ This is the main function which open a .txt file and read the urls """
    ## Checking if the current directory has the images.txt file on pwd.
    if os.path.isfile('./Images.txt'):
        file_name = 'Images.txt'
    else:
        raise FileNotFoundError
    ## Directory name where the image file should be saved.
    directory_to_save_the_image = 'Skechers-all-images/'

    if os.path.isdir(directory_to_save_the_image):  ## Checking if the directory is present
        print("YES wait downloading images...")
    else:
        os.mkdir(directory_to_save_the_image)

    # read excel file
    book = openpyxl.load_workbook('Task 2.xlsx', data_only=True)
    sheet = book.active
    i = 0
    """
    9384 is a max number of urls, you can set your own number here according to the quantity of urls
    """
    words = [0] * 9378
    for row_cells in sheet.iter_rows(min_row=2, max_row=1564, min_col=2, max_col=7):
        for cell in row_cells:
            words[i] = cell.value
            i += 1
        with open('Images.txt', 'w') as outfile:
            # outfile.write(str(words))
            for line in words:
                outfile.write("".join(str(line)) + "\n")

    with open(file_name) as file:
        # lines = [l.strip() for l in file]  ## using list comprehension to remove the "\n"
        lines = file.read().splitlines()  ## using built in function

    for line in lines:  ## going through the url in the file
        image_fetch(line, directory_to_save_the_image)

    global counter
    print(counter)

    print("Download complete.")

if __name__ == "__main__":  ## When this module is run as a script
    main()