# AnsiDOC

Redfish + Ansible + vSphere 7 new REST API provisioning

## Team members

- [Prajwal Prakash](https://twitter.com/prajwalprakash)
- [Ariel Sanchez](https://twitter.com/arielsanchezmor)
- [Dario Dörflinger](https://twitter.com/virtual_frog)
- [Nacho Osete](https://twitter.com/ignosgt)
- [Wes Milliron](https://twitter.com/wesmilliron)

## Project Scope

We can do a very nice proof of concept demo using both redfish and the new ESXi rest api.

Apart from provisioning the initial ESXi+vCenter stack with Ansible, we also plan to set on top a SDDC NSX-T Nested Lab, and a VRA service over the top.
Helping to fulfill our best chaos engineering dreams, we joined the only two Ansible teams together for greater throughput

## What we would like to do

### Phase 1
- look up IP address of redfish enabled server from table
- look up redfish credentials from table
- retrieve and output serial number from redfish API to console and back to table as a new column

### Phase 2
- Lookup serial number in table, if found, in table, carry on with phase 2
- Set ESXi hostname (may need vSphere 7 for this, using new REST API)
- Set management IP address, mask and gateway, dns details for ESXi (may need vSphere 7 for this, using new REST API)

> this actually has never been done and both phases can be worked on separately

### Phase 3
- Build a nested SDDC NSX-T lab on top based on other existing project.
- Add a VRA service on top as a final step for a complete VCAP nested study lab.

## Recommended References

- vSphere 7 Web Services API - https://code.vmware.com/apis/968
- Redfish API - https://www.supermicro.com/manuals/other/RedfishRefGuide.pdf
- Redfish API - https://hewlettpackard.github.io/iLOAmpPack-Redfish-API-Docs

## What we have already learned so far

### ToDos and Getting Things Done

* Get some online learning and hands-on experience
* Prepare a GitHub repository with the necessary submodules

## Lessons Learned

- [Introduction to Ansible with AWS and CloudFormation](https://linuxacademy.com/cp/courses/lesson/course/7748)(A Cloud Guru, 3 hours)
- How to multitask and context-switch Ansible Learning, GitHub management, AWS lab building, VMWorld 2020 attending and Homekeeping at the same time!
