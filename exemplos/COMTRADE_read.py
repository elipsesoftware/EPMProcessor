#mandatory import
import epmprocessor as epr
import datetime as dt
import numpy as np
import comtrade
import glob

@epr.applicationMethod('Read COMTRADE File')
def method_name(epmConn, FileAddress = ''):
  '''
  This code was made to run into EPM Processor, read COMTRADE files from an informed path and save data to Basic Variables.
  It creates the tags if they don't exist, add an annotation to identify the start time of each COMTRADE sequence and a last value with bad quality to prevent connecting different sequences.
  Params:
    - epmConn = EPM connection
    - FileAddress = COMTRADE files path like "D:\COMTRADE\Files\"

  How to use:
    - Download this file and import to a code package in your EPM Processor.
    - Deploy your code package.
    - Create an Application to call this method "Read COMTRADE File" informing the parameters like the example.
    - Configure a solution to run the code when you want.
  '''

  comtradelist = [f for f in glob.glob(FileAddress + "*.cfg")]
  for comtrade_file in comtradelist:
    rec = comtrade.load(comtrade_file)

    desc = np.dtype([('Value', '>f8'), ('Timestamp', 'object'), ('Quality', 'object')])

    invChar = ['<','>','$','#','.',',',' ','´','@','/']

    newdate = rec.start_timestamp
    if newdate > dt.datetime(1970, 1, 1):
            
        station_name = ''
        for letter in rec.station_name:
            if letter in invChar:
                letter = '_'
            station_name += letter
        
        bvNames = []
        for var in rec.analog_channel_ids:
            newName = ''
            for letter in var:
                if letter in invChar:
                    letter = '_'
                newName += letter
            newName += '_COMTRADE'
            bvNames.append(station_name + '_' + newName)
        
        bvList = epmConn.getDataObjects(bvNames)
        id = 0
        
        for bv in bvList:
            if bvList[bv] == None:
                newBV = epmConn.createBasicVariable(name=bv, description='COMTRADE analog variable - ' + bv + ' - from equipment ' +  rec.station_name)
            else:
                newBV = bvList[bv]
            newvalues = list(rec.analog[id])
            newvalues.append(rec.analog[id][-1])
            recTimestamp = newdate
            newdates = []
            for recdate in rec.time:
                recTimestamp = newdate + dt.timedelta(seconds=recdate)
                newdates.append(recTimestamp)
            newdates.append(recTimestamp + dt.timedelta(milliseconds=1))
                
            datatemp = np.empty(len(newvalues), dtype=desc)
            datatemp['Value'] = newvalues
            datatemp['Timestamp'] = newdates
            datatemp['Quality'] = 0
            datatemp['Quality'][-1] = 2156724224
            newBV.historyUpdate(datatemp)
            
            #escrevendo anotação
            message = 'COMTRADE event ' + str(newdate)
            newBV.writeAnnotation(newdate,message)
            id += 1
        
        bvNames = []
        for var in rec.status_channel_ids:
            newName = ''
            for letter in var:
                if letter in invChar:
                    letter = '_'
                newName += letter
            newName += '_COMTRADE'
            bvNames.append(station_name + '_' + newName)
            
        bvList = epmConn.getDataObjects(bvNames)
        id = 0
        for bv in bvList:
            if bvList[bv] == None:
                newBV = epmConn.createBasicVariable(name=bv, description='COMTRADE status variable - ' + bv + ' - from equipment ' +  rec.station_name)
            else:
                newBV = bvList[bv]
            newvalues = list(rec.status[id])
            newvalues.append(rec.status[id][-1])
            recTimestamp = newdate
            newdates = []
            for recdate in rec.time:
                recTimestamp = newdate + dt.timedelta(seconds=recdate)
                newdates.append(recTimestamp)
            newdates.append(recTimestamp + dt.timedelta(milliseconds=1))
                
            datatemp = np.empty(len(newvalues), dtype=desc)
            datatemp['Value'] = newvalues
            datatemp['Timestamp'] = newdates
            datatemp['Quality'] = 0
            datatemp['Quality'][-1] = 2156724224
            newBV.historyUpdate(datatemp)

            #escrevendo anotação
            message = 'COMTRADE event ' + str(newdate)
            newBV.writeAnnotation(newdate,message)
            id += 1
