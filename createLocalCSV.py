import json
import pandas as pd

def createLocal(JsonFile,csvFile):
    JsonFile = 'testData.json'
    # modify the json,  change to standard key:value dict
    data = ''
    with open(JsonFile,'r') as jsFile:
        data = json.load(jsFile)
    for key in data.keys():
        cur = {}
        for d in data[key]:
            cur[d]=1
        data[key] = cur

    # create new json object with the modified json strings
    newJs = json.dumps(data)

    # read json and create DataFrame object by {index；{column:value}} mode, and replace NaN with 0, and change float to int
    newD = pd.read_json(newJs,orient='index').fillna(0).astype('int')

    # output to csv
    newD.to_csv(csvFile)

    print(newD)

    return

if __name__ == '__main__':
    createLocal('testData.json','result.csv')