# Second Task 

## Getting Started 

The main goal of the project is downloading images using URLs from Google Drive into corresponded folders. After that uploading as a zip file (all images) to Google Drive. Detailed description you can read down below. 

### Step 1. Enable Google Drive API service

1. Log in to your [Google Cloud Platform](https://console.cloud.google.com/)
2. Select your project
3. Enable Google Drive API service
  
### Step 2. Install Python Library

    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    

### Authentication
Every request your application sends to the Drive API must include an authorization token. The token also identifies your application to Google.

Application must use [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) to authorize requests.

Another important thing is connecting to [GOOGLE SHEETS](https://learndataanalysis.org/getting-started-google-sheets-api-in-python-part-1/) more detail you can see here. 

#### Running a Code

1. To connect and start downloading images you need to run [Download.py](https://github.com/minbayevb/silicon_valley2/blob/master/Downloader.py) 
2. To organize images into folders [org_images.py](https://github.com/minbayevb/silicon_valley2/blob/master/org_images.py)
3. To upload as a zip file [upload.py](https://github.com/minbayevb/silicon_valley2/blob/master/upload.py) 

To start uploading a zip file to Google Drive, you need to convert it to a zip file (images folder) manually after organizing it into folders. 

##### Requirements

[requirements.txt](https://github.com/minbayevb/silicon_valley2/blob/master/requirements.txt)




