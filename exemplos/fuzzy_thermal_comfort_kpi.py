# -*- coding: utf-8 -*-

"""Elipse Plant Manager - EPM Processor - Thermal Comfort Fuzzy KPI - video example
Copyright (C) 2019 Elipse Software.
Distributed under the MIT License.
(See accompanying file LICENSE.txt or copy at http://opensource.org/licenses/MIT)
"""

# Links úteis
# Docstring: https://www.python.org/dev/peps/pep-0257/
# Type hints: https://docs.python.org/3/library/typing.html
# reStructuredText Docstring Format: https://www.python.org/dev/peps/pep-0287/
# Fuzzy model: https://anaconda.org/mauricioposser/fuzzy_thermal_comfort_kpi/notebook

import datetime
import pickle
import numpy as np
import skfuzzy.control as ctrl
import skfuzzy as fuzz

# from typing import Tuple, List

import epmprocessor as epr
import epmwebapi as epm
from epmprocessor import ScopeSession, ScopeResult
from epmwebapi import BasicVariable, epmconnection

__author__ = "Maurício Simões Posser"
__copyright__ = "Copyright 2019, Elipse Software"
__license__ = "MIT"
__status__ = "Production"
__docformat__ = 'reStructuredText'

@epr.applicationMethod('thermal_comfort_kpi') 
def kpi_fuzzy_model(session:ScopeSession, tag_temperature: BasicVariable, tag_humidity: BasicVariable,
        tag_kpi: BasicVariable, server_repository:epmconnection, file_model: str='my_repository/models/kpi_fuzzy_model.pkl',
        person_set:str='normal') -> ScopeResult:
    """
Modelo baseado em lógica fuzzy para o cálculo de um indicador de conforto térmico.

tag_temperature: valor da temperatura medida - média ponderada do período do turno avaliado.
    """

    process_interval:datetime.timedelta = session.range
    end_time: datetime = session.timeEvent
    ini_time: datetime = end_time - process_interval

    try:
        query_period = epm.QueryPeriod(ini_time, end_time)
        agg_time_avg_details = epm.AggregateDetails(process_interval, epm.AggregateType.TimeAverage)
        temperature = tag_temperature.historyReadAggregate(agg_time_avg_details, query_period)['Value']
        humidity = tag_humidity.historyReadAggregate(agg_time_avg_details, query_period)['Value']
    except:
        raise Exception(u'oops! Erro nas consultas agregadas!')
    kpi = calculate_kpi(session, file_model, temperature[0], humidity[0], person_set, server_repository)
    try:
        if session.scopeContext == epr.ScopeContext.Test:
            print(f'Resultado: {kpi} - timestamp: {ini_time.isoformat()}')
        else:  # Production ou Simulation
            tag_kpi.write(kpi, ini_time, 0)
    except:
        raise Exception(u'oops! Erro na escrita do KPI calculado!')
    return ScopeResult(True)


def calculate_kpi(session, file_model, temperature, humidity, person_set, server_repository):
    ep_resource_manager = server_repository.getProcessorResourcesManager()
    resource = ep_resource_manager.getResource(file_model)
    io_model = resource.download(epm.DownloadType.Binary)
    io_model.seek(0)
    fm_loaded = pickle.load(io_model)
    kpi= ctrl.ControlSystemSimulation(fm_loaded)
    kpi.input['Temperature'] = temperature
    kpi.input['Humidity'] = humidity
    kpi.compute()
    return kpi.output['kpi_thermal_comfort']


