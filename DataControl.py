from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

from Location import LocationData

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

class DataControl:
	def __init__(self):
		self.LocationData = LocationData()

	def AddLocationData(self, data):
		self.LocationData.AddData(data)

	def SetSpreadSheetID(self, id):
		self.SpreadSheetID = id

	def GetDataFromGoogleSheets(self, spreadSheetID):
		store = file.Storage('token.json')
		creds = store.get()
		if not creds or creds.invalid:
			flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
			creds = tools.run_flow(flow, store)
		self.service = build('sheets', 'v4', http=creds.authorize(Http()))

		SPREADSHEET_ID = '1nWwh3S6_LgpYl6r3_uFSZOXZy8ZXCH_kRFM6reM9_mA'
		self.LocationData.GetDataFromGoogleSheet(self.service, spreadSheetID)
		self.LocationData.Print()

		


