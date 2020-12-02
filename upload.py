from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive.file']

service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)

folder_id = '1y8J7g8zObWY0XNcwFozDzTe-nX3bKDtO'
file_name = "/Skechers-all-images.zip"
media = MediaFileUpload("C:/Users/minba/PycharmProjects/Valley2/Skechers-all-images.zip",chunksize=1024*256, mimetype='application/zip', resumable=True)
file_metadata = {
    'name': 'Skechers-all-images.zip',
    'parents': [folder_id]
}
file = service.files().create(body=file_metadata, media_body=media, fields='id')
res = None
while res is None:
    status, res = file.next_chunk()
    if status:
        print('Uploading %d%% "%s"' % (status.progress(), file_name))
print("Upload Complete!")