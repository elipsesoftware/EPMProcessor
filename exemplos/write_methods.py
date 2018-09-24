
import epmprocessor as epr
import epmwebapi as epm
import numpy as np
import pandas as pd


@epr.applicationMethod('HistoryUpdate')
def history_update(session, epmdataobject):
    '''Update epmdataobject with five itens'''

    #pandas generate a range of dates
    newdates = pd.date_range('1/1/2018', periods=5,freq='H' )

    #just a five itens list
    newvalues = [50,60,30,40,10]

    # epm ndarray data format.
    desc = np.dtype([('Value', '>f8'), ('Timestamp', 'object'), ('Quality', '>i4')])
    datatemp = np.empty(len(newvalues), dtype=desc)

    #loop to populate the object before send to EPM
    i=0
    while i < len(newvalues):
        datatemp['Value'][i] = newvalues[i]
        datatemp['Timestamp'][i] = newdates[i]
        datatemp['Quality'][i] = 0
        i = i+1
    try:

        if session.scopeContext == epr.ScopeContext.Test:
            print('Resultado: {valor} - {timestamp}'.format(valor=str(datatemp['Value'][-1]),
                                                                timestamp=datatemp['Timestamp'][-1].isoformat()))
        else:  # Production ou Simulation
            epmdataobject.historyUpdate(datatemp)

    except:
        raise Exception('Error in historyUpdate')


@epr.applicationMethod('Write')
def write(session, epmdataobject):
    '''Write one value in epmdataobject'''

    date = datetime.datetime.now()
    value = 100
    quality = 0 #zero is Good in OPC UA


    epmdataobject.write(value, date, quality)

