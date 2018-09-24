#EPM Processor modules
import epmprocessor as epr
import epmwebapi as epm

import datetime


@epr.applicationMethod('GetHistoryRaw')
def get_history_raw(session, epmdataobject):
    '''Get one hour historic data from epmtag '''

    endtime = session.timeEvent

    initime = endtime - datetime.timedelta(hours=1)

    queryperiod = epm.QueryPeriod(initime, endtime)

    data = epmdataobject.historyReadRaw(queryperiod)

    print("Initial Time:{} \nEnd Time:{} \nData:{}".format(initime,endtime,data))

