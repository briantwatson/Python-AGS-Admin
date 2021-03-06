import adminfunctions

#Parameters - use portal credentials for federated setup
AGSRestEndpoint = "http://myserver.mysite.com/arcgis/rest"
username = "siteadmin"
password = "siteadmin"
referer = "http://referer.mysite.com/arcgis/rest"

###Script execution - Where functions are executed.
endpoints = adminfunctions.defineEndpoints(AGSRestEndpoint)
token = adminfunctions.getToken(endpoints["TokenUrl"],username,password, referer)["token"]

services = adminfunctions.getServiceAdminEndpoints(endpoints["Admin"], token)
for service in services:
    print "Editing " + service + "..."
    ##serviceAdminUrl, token, maxWaitTime, maxStartupTime, maxIdleTime, maxUsageTime)
    result = adminfunctions.updateTimeouts(service,token,60,300,300,300)
    print result
    print ""
