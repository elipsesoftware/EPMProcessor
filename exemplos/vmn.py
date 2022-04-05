#mandatory import
import epmprocessor as epr

#necessary import
import epmwebapi as epm
import datetime

#-------------------------
#      Method Sample
#-------------------------

@epr.applicationMethod('Get_VMN')
def get_vmn(session, flowMeters):
  '''
    Este método pressupoe que será chamado a partir de um evento diário do EPM, executado depois das 6h.
    Sempre que o evento for executado, será passado automaticamente o objeto session, contendo informações do momento de execução do evento.
    O segundo parâmetro é o flowMeters, que deve ser passado como um objeto "epmobjectDict" com Type sendo "FlowMeter".
    A partir disso, percebe-se que deve existir um modelo no EPM contendo objetos do tipo FlowMeter (medidores de vazão), que contenham
    duas propriedades:
      1- Flow: medida que retorna a vazão medida no campo pelo medidor de vazão;
      2- MNF: propriedade criada para receber o valor da vazão mínima medida entre o período entre 0h e 6h do dia.
  '''
  today = session.timeEvent
  end_date = datetime.datetime(today.year,today.month,today.day,6,0)
  ini_date = datetime.datetime(today.year,today.month,today.day,0,0)
  queryperiod = epm.QueryPeriod(ini_date,end_date)
  processInterval = datetime.timedelta()
  aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Minimum)

  for meter in flowMeters.values():
    meterProps = meter.enumProperties()
    flow = meterProps['Flow'].historyReadAggregate(aggregationdetails, queryperiod)
    vmn = flow['Value']
    meterProps['MNF'].write(float(vmn),datetime.datetime(today.year,today.month,today.day,0,0))

  return epr.ScopeResult(True)
