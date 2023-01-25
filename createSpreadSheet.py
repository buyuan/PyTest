
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pandas as pd
import traceback
from gspread_dataframe import set_with_dataframe

def createSpread():
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('pysheettest-375808-c7c13c9e067e.json'
                , scope)

    gc = gspread.authorize(credentials)
    
    # create and open a blank spreedsheet
    file = gc.create('BuyuanAPITest')
    # this mail is a automatically generated mail for my new google peoject that is used for this test
    file.share('pytestbuyuan@pysheettest-375808.iam.gserviceaccount.com', perm_type='user', role='writer')
    # this mail is my own mail that is used for checking if the spreadsheet created or not
    file.share('neobuyuan@gmail.com', perm_type='user', role='writer')

    sheet = file.sheet1
   

    # create DataFrame , same as create local csv file
    fileName = 'testData.json'
    data = ''
    with open(fileName,'r') as jsFile:
        data = json.load(jsFile)
    for key in data.keys():
        cur = {}
        for d in data[key]:
            cur[d]=1
        data[key] = cur
    newJs = json.dumps(data)
    newD = pd.read_json(newJs,orient='index').fillna(0).astype('int')   

    print(newD)

    # update the dataframe into sheet1
    try:
        #Insert dataframe to google sheets , the include_index = True will keep the index
        set_with_dataframe(sheet, newD, include_index=True)
    except Exception:
        print(traceback.format_exc())

    return

if __name__ == '__main__':
    createSpread()