import epmprocessor as epr
import epmwebapi as epm


@epr.applicationMethod('GetPortalResource')
def get_portal_resource(resource_name, connection):
    """
    Get Portal resource from EPM WebServer
    """
    epmResourceManager = connection.getPortalResourcesManager()
    file = epmResourceManager.getResource(resource_name)


@epr.applicationMethod('GetProcessorResource')
def get_processor_resource(resource_name, connection):
    """ 
    Get Processor resource from EPM WebServer
    """
    
    epResourceManager = connection.getProcessorResourcesManager()
    file = epResourceManager.getResource(resource_name)
