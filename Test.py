from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from DataControl import DataControl

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1nWwh3S6_LgpYl6r3_uFSZOXZy8ZXCH_kRFM6reM9_mA'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

DataControlObject = DataControl()

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1nWwh3S6_LgpYl6r3_uFSZOXZy8ZXCH_kRFM6reM9_mA'
    RANGE_NAME = 'Locations!A8:T'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    DataControlObject.GetDataFromGoogleSheets(SPREADSHEET_ID)
        

if __name__ == '__main__':
    main()