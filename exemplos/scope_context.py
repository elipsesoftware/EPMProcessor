#O EPM Processor pode trabalhar com contextos de execução, através da propriedade scopeContext da sessão.

import epmprocessor as epr
import epmwebapi as epm

@epr.applicationMethod('ScopeContext')
def scope_context(session):
    

     if session.scopeContext == session.scopeContext.Test:
  
         #do it in test
         print('Test Context')

     if session.scopeContext == session.scopeContext.Simulation:
         #do it in simulation
         print('Simulation Context')

     if session.scopeContext == session.scopeContext.Production:
         #do it in production
         print('Production Context')
