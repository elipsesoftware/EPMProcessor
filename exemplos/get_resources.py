import epmprocessor as epr
import epmwebapi as epm


@epr.applicationMethod('GetPortalResource')
def get_portal_resource(session, filename, connection, filetype='Binary'):
    """
    Get Portal resource from EPM WebServer
    """
    epmResourceManager = connection.getPortalResourcesManager()
    file = epResourceManager.getResource(filename)


@epr.applicationMethod('GetProcessorResource')
def get_processor_resource(session, filename, connection):
    """ 
    Get Processor resource from EPM WebServer
    """
    
    epResourceManager = connection.getProcessorResourcesManager()
    file = epResourceManager.getResource(filename)
