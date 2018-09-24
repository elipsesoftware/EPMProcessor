#EPM Processor modules
import epmprocessor as epr
import epmwebapi as epm

import datetime



@epr.applicationMethod('GetHistoryInterpolative')
def get_history_interpolative(epmdataobject, starttime, endtime, interval_seconds):

    try:
        queryperiod = epm.QueryPeriod(starttime,endtime)
        processInterval = datetime.timedelta(seconds=interval_seconds)
        aggregationdetails = epm.AggregateDetails(processInterval, epm.AggregateType.Interpolative)
        data = epmdataobject.historyReadAggregate(aggregationdetails,queryperiod)

    except:
        raise Exception('Error in read aggregation')

    print(data)

    return epr.ScopeResult(True)


