from __future__ import print_function
from googleapiclient.discovery import build, MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
FILETYPE = 'application/vnd.google-apps.folder'

# Initialize google service
SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
		creds = tools.run_flow(flow, store)
service = build('drive', 'v3', http=creds.authorize(Http()))

def main():
	UploadFile('test.csv', '176EBMy11cKcYJXqOhxmQRXqBRkCNxEe_')

def UploadFile(filePath, folderID):
	file_metadata = {
		'name': 'test.csv',
		'parents': [folderID]
	}
	print('test')

	media = MediaFileUpload(filePath, mimetype='text/csv')
	dataFile = service.files().create(body=file_metadata, 
							media_body=media,
							fields='id').execute()
	print('File ID: %s' % dataFile.get('id'))

def AddFolder(folderName):
	file_metadata = {
		'name': folderName,
		'mimeType': FILETYPE
	}

	service.files().create(body=file_metadata, fields='id').execute()

# Return folder id
def SearchFolder(folderName):
	page_token = None
	while True:
		response = service.files().list(q="mimeType='" + FILETYPE + "' and parents = 'root'",
											fields='nextPageToken, files(id, name)',
											pageToken=page_token).execute()
		for eachFile in response.get('files', []):
			# Process change
			print('Found file: %s (%s)' % (eachFile.get('name'), eachFile.get('id')))
		page_token = response.get('nextPageToken', None)
		if page_token is None:
			break


if __name__ == '__main__':
	main()
