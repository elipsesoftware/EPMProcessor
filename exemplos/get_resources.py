import epmprocessor as epr
import epmwebapi as epm
from epmwebapi.downloadtype import DownloadType

@epr.applicationMethod('GetPortalResource')
def get_portal_resource(resource_name, connection):
    """
    Get Portal resource from EPM WebServer
    """
    epmResourceManager = connection.getPortalResourcesManager()
    resource = epmResourceManager.getResource(resource_name)
    file = resource.download(DownloadType.Json)

@epr.applicationMethod('GetProcessorResource')
def get_processor_resource(resource_name, connection):
    """ 
    Get Processor resource from EPM WebServer
    """
    
    epResourceManager = connection.getProcessorResourcesManager()
    resource = epResourceManager.getResource(resource_name)
    file = resource.download(DownloadType.Json)
