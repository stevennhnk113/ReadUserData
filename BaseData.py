import csv

class BaseData:
	def __init__(self, range, dataName):
		self.Data = None
		self.Range = range
		self.DataName = dataName

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
			self.WriteDataToCSV()


	def WriteDataToCSV(self):
		with open('csvFiles/' + self.DataName + '.csv', 'w', newline='') as csvfile:
			csvWriter = csv.writer(csvfile, delimiter=',')
			for row in self.Data:
				csvWriter.writerow(row)
