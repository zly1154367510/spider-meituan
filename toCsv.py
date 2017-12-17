import pandas

def to_csv(dataList,nameList,csvName):
    pd = pandas.DataFrame(dataList)
    pd.to_csv(csvName+".csv")

def read_csv(csvName):
    return pandas.read_csv(csvName+".csv")