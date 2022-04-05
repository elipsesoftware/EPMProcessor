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
