#mandatory import
import epmprocessor as epr

#necessary import
import epmwebapi as epm
import datetime
import numpy as np
import pytz

#-------------------------
#      Method Sample
#-------------------------
@epr.applicationMethod('getCurve')
def getCurve(session, ini_date, measList, interval_seconds = 3600):
  '''
    ini_date: Data inicial para cálculo da curva.
    measList: Lista de objetos que contém as propriedades "Value" e "EstimatedValue".
      - Value: propriedade a ser consultada.
      - EstimatedValue: propriedade onde será gravado o resultado da estimativa.
    interval_seconds: Valor inteiro em segundos utilizado para amostra dos dados.
  '''
  
  evento = session.timeEvent.astimezone(pytz.timezone('America/Sao_Paulo'))
  fim_date = evento
  weekday = evento.weekday()
  weekdayDiff = weekday - ini_date.weekday()
  ini_date += datetime.timedelta(days = weekdayDiff)
  
  # epm ndarray data format.
  size = 86400 / interval_seconds
  desc = np.dtype([('Value', '>f8'), ('Timestamp', 'object'), ('Quality', 'object')])
  datatemp = np.empty(int(size), dtype=desc)
  
  for meas in measList.values():
    starttime = datetime.datetime(ini_date.year, ini_date.month, ini_date.day, evento.hour, 0, 0).astimezone(pytz.timezone('America/Sao_Paulo'))
    endtime = (starttime + datetime.timedelta(days = 1)).astimezone(pytz.timezone('America/Sao_Paulo'))
    diviavg = 0
    
    measProps = meas.enumProperties()

    measType = measProps['AnalogType'].read()

    if (measType.value == 'Power'):

      datatemp['Quality'] = 0
      datatemp['Value'] = 0
      tempDate = datetime.datetime(evento.year, evento.month, evento.day, evento.hour, 0, 0).astimezone(pytz.timezone('America/Sao_Paulo'))
      
      datatemp['Timestamp'][0] = tempDate
      
      i = 1
      while i < size:
        tempDate += datetime.timedelta(seconds = interval_seconds)
        datatemp['Timestamp'][i] = tempDate
        i += 1
      
      while starttime <= fim_date:
        diviavg += 1
        queryperiod = epm.QueryPeriod(starttime, endtime)
        processInterval = datetime.timedelta(seconds = interval_seconds)

        aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)
        valuecontent = measProps['Value'].historyReadAggregate(aggregationdetails, queryperiod)
      
        datatemp['Value'] += valuecontent['Value']
        
        starttime += datetime.timedelta(days = 7)
        endtime += datetime.timedelta(days = 7)
    
      datatemp['Value'] /= diviavg
      
      measProps['EstimatedValue'].historyUpdate(datatemp)
      
  
  
  return epr.ScopeResult(True)
