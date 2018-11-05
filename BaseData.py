class BaseData:
	def __init__(self, range):
		self.Data = None
		self.Range = range

	def Print(self):
		if self.Data is None:
			return

		for row in self.Data:
			print(row)

	def AddData(self, data):
		self.Data = data

	def GetDataFromGoogleSheet(self, service, spreadSheetID):
		self.service = service

		result = service.spreadsheets().values().get(spreadsheetId=spreadSheetID,range=self.Range).execute()
		values = result.get('values', [])

		if not values:
			self.Data = None
		else:
			self.Data = values
