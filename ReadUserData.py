from DataControl import DataControl

SPREADSHEET_ID = '1gcnPKfM5nWNzBLB4uW0G136Hi8yoiUZFS3I_Zw0Ot_s'
DataControlObject = DataControl('TestSteven2')

def main():
	DataControlObject.GetDataFromGoogleSheets(SPREADSHEET_ID)
	DataControlObject.UploadToGoogleDrive()


if __name__ == '__main__':
	main()
