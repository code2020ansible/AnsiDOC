# AnsiDOC

Redfish + Ansible + vSphere 7 new REST API provisioning

## Team members

- [Prajwal Prakash](https://twitter.com/prajwalprakash)
- [Ariel Sanchez](https://twitter.com/arielsanchezmor)

## Project Scope

I'm thinking, we can do a very nice prrof of concept demo using both redfish and the new esxi rest api.

### Phase 1
- look up IP address of redfish enabled server from table
- look up redfish credentials from table
- retrieve and output serial number from redfish API to console and back to table as a new column

### Phase 2
- Lookup serial number in table, if found, in table, carry on with phase 2
- Set ESXi hostname (may need vSphere 7 for this, using new REST API)
- Set management IP address, mask and gateway, dns details for ESXi (may need vSphere 7 for this, using new REST API)

> this actually has never been done and both phases can be worked on separately

## Recommended References

- vSphere 7 Web Services API - https://code.vmware.com/apis/968
- Redfish API - https://www.supermicro.com/manuals/other/RedfishRefGuide.pdf
- Redfish API - https://hewlettpackard.github.io/iLOAmpPack-Redfish-API-Docs
