from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

from Location import LocationData, DepartmentData, UsersData, UserRolesData, ApprovalRoutingData, AccountCodeData, BudgetsData, VendorListData, ProductCatalogData

SCOPES = 'https://www.googleapis.com/auth/drive'
FOLDER_FILE_TYPE = 'application/vnd.google-apps.folder'

class DataControl:
	def __init__(self, clientName):
		self.ClientName = clientName
		self.LocationData = LocationData()
		self.DepartmentData = DepartmentData()
		self.UsersData = UsersData()
		self.UserRolesData = UserRolesData()
		self.ApprovalRoutingData = ApprovalRoutingData()
		self.AccountCodeData = AccountCodeData()
		self.BudgetsData = BudgetsData()
		self.VendorListData = VendorListData()
		self.ProductCatalogData = ProductCatalogData()

		store = file.Storage('token.json')
		creds = store.get()
		if not creds or creds.invalid:
			flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
			creds = tools.run_flow(flow, store)
		self.googleSheetsService = build('sheets', 'v4', http=creds.authorize(Http()))
		self.driveService = build('drive', 'v3', http=creds.authorize(Http()))

	def GetDataFromGoogleSheets(self, spreadSheetID):
		self.LocationData.GetDataFromGoogleSheet(self.googleSheetsService, spreadSheetID)
		self.DepartmentData.GetDataFromGoogleSheet(self.googleSheetsService, spreadSheetID)
		self.UsersData.GetDataFromGoogleSheet(self.googleSheetsService, spreadSheetID)
		self.UserRolesData.GetDataFromGoogleSheet(self.googleSheetsService, spreadSheetID)
		self.ApprovalRoutingData.GetDataFromGoogleSheet(self.googleSheetsService, spreadSheetID)
		self.AccountCodeData.GetDataFromGoogleSheet(self.googleSheetsService, spreadSheetID)
		self.BudgetsData.GetDataFromGoogleSheet(self.googleSheetsService, spreadSheetID)
		self.VendorListData.GetDataFromGoogleSheet(self.googleSheetsService, spreadSheetID)
		self.ProductCatalogData.GetDataFromGoogleSheet(self.googleSheetsService, spreadSheetID)

	def UploadToGoogleDrive(self):
		folderID = self.SearchFolder(self.ClientName)
		
		if folderID == None:
			folderID = self.AddFolder(self.ClientName)
			print('After add, folderID:' + folderID)
		else:
			print('After search, folderID:' + folderID)

		if folderID == None:
			return

		self.LocationData.UploadCsvToGoogleDrive(self.driveService, folderID)
		self.DepartmentData.UploadCsvToGoogleDrive(self.driveService, folderID)
		self.UsersData.UploadCsvToGoogleDrive(self.driveService, folderID)
		self.UserRolesData.UploadCsvToGoogleDrive(self.driveService, folderID)
		self.ApprovalRoutingData.UploadCsvToGoogleDrive(self.driveService, folderID)
		self.AccountCodeData.UploadCsvToGoogleDrive(self.driveService, folderID)
		self.BudgetsData.UploadCsvToGoogleDrive(self.driveService, folderID)
		self.VendorListData.UploadCsvToGoogleDrive(self.driveService, folderID)
		self.ProductCatalogData.UploadCsvToGoogleDrive(self.driveService, folderID)

	# Return folder id
	def SearchFolder(self, folderName):
		page_token = None
		while True:
			response = self.driveService.files().list(q="mimeType='" + FOLDER_FILE_TYPE + "' and parents = 'root' and name = '" + folderName + "'",
												fields='nextPageToken, files(id, name)',
												pageToken=page_token).execute()
			for eachFile in response.get('files', []):
				return eachFile.get('id')
			page_token = response.get('nextPageToken', None)
			if page_token is None:
				break

	def AddFolder(self, folderName):
		file_metadata = {
			'name': folderName,
			'mimeType': FOLDER_FILE_TYPE
		}

		folderFiles = self.driveService.files().create(body=file_metadata, fields='id').execute()
		return folderFiles.get('id')


