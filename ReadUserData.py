from DataControl import DataControl

SPREADSHEET_ID = '1udHMPwkvyd92ywbE8Xi_Q9-GvrEk3AtHeZ1QLGi4MD0'
DataControlObject = DataControl('INnomotion2')

def main():
	DataControlObject.GetDataFromGoogleSheets(SPREADSHEET_ID)
	DataControlObject.UploadToGoogleDrive()


if __name__ == '__main__':
	main()
