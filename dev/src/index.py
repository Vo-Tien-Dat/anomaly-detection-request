import pandas
from typing import Text
import pandas as pd
from datetime import datetime




CONST_FILE_PATH = '../dataset/access_log_1.csv'

LIMIT_NUMBER_OF_REQUEST = 111532

# ĐỌC FILE DATA
def ReadData(fileName:Text, colNames):        
    data = pd.read_csv(fileName, header = 0 , names = colNames)    
    return data

def ConvertDateToFormat(data, oldColName, newColName, datePattern = "%Y-%m-%d"):

    data[oldColName] = pd.to_datetime(data[oldColName])

    if newColName is None: 
        newColName = oldColName

    data[newColName] = data[oldColName].dt.strftime(datePattern)
    return data; 

# GIẢI QUYẾT TẤT CẢ NHỮNG NGÀY CÓ SỐ LƯỢNG REQUEST BẤT THƯỜNG
def ListNumberOfAnomallyRequestDate(data, dateColName, maxRequestPerday = 0): 

    data = data.groupby(dateColName).size().reset_index(name = 'count')
    newData = data[data['count'] >= maxRequestPerday]
    return newData

def WriteFile(data, filename = 'normalize_date.txt'): 
    try: 
        with open(filename, "w") as file:
            print(data)
            for item in data.values.tolist(): 
                print(item)
                line = f"{item[0]}\t{item[1]}\n"
                file.write(line)
    except Exception as e: 
        print("Error: {}".format(str(e)))
        


def main():

    CONST_DATE_PATTERN = "%Y-%m-%d"
    colNames = ['time_stamp', 'sources', 'messages']
    
    data = ReadData(fileName=CONST_FILE_PATH, colNames=colNames )
    data = ConvertDateToFormat(data, 'time_stamp', 'date', CONST_DATE_PATTERN)
    lAnomallyRequestDate = ListNumberOfAnomallyRequestDate(data, ['date'], LIMIT_NUMBER_OF_REQUEST)
    WriteFile(lAnomallyRequestDate)
    
if __name__ == "__main__":
    main()