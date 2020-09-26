# AnsiDOC

Redfish + Ansible + vSphere 7 new REST API provisioning

Team members:

Prajwal Parkash   
Ariel Sanchez https://twitter.com/arielsanchezmor  

I'm thinking, we can do a very nice prrof of concept demo using both redfish and the new esxi rest api. Something like this:

Phase 1  
look up IP address of redfish enabled server from table  
look up redfish credentials from table  
retrieve and output serial number from redfish API to console and back to table as a new column  

Phase 2  
lookup serial number in table, if found, in table, carry on with phase 2  
Set ESXi hostname (may need vSphere 7 for this, using new REST API)  
Set management IP address, mask and gateway, dns details for ESXi (may need vSphere 7 for this, using new REST API)  
this actually has never been done and both phases can be worked on separately  
