#mandatory import
import epmprocessor as epr
import pandas as pd
import datetime as dt

@epr.applicationMethod('ExportParquet')
def ExportParquet(epmConnection, dsName, saveTo = 'C:/'):
  '''
  Parameters:
    - epmConnection: EPM Connection
    - dsName: Dataset name from where data will be obtained
    - sabeTo: Path to save Parquet file (can be a OneDrive path, for example)
  '''
  dsConfig = epmConnection.loadDatasetServer(dsName)
  datavar = dsConfig.execute()
  df_list = {}
  for var in datavar:
    new_Quality = datavar[var][:]['Quality'].byteswap().newbyteorder()
    new_Timestamp = datavar[var][:]['Timestamp']
    new_Value = datavar[var][:]['Value'].byteswap().newbyteorder()

    d = {'VarName': var, 'Value':new_Value, 'Timestamp':new_Timestamp, 'Quality':new_Quality}
    df_list[var] = pd.DataFrame(d)
    
  invChar = ['<','>','$','#','.',',',' ','´','@','/','+',':']
  pFileName = ''
  for letter in 'Dataset_{}_{}'.format(dsName, dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
    if letter in invChar:
      letter = '_'
    pFileName += letter
  finalData = pd.concat(df_list).reset_index(drop=True)
  finalData.to_parquet('{}/{}.parquet'.format(saveTo, pFileName))
