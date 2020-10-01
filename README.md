# AnsiDOC

Redfish + Ansible + vSphere 7 new REST API provisioning

## Team members

![the best teampicture ever!](https://github.com/code2020ansible/AnsiDOC/blob/master/vHackathon_Ansible_Team_Picture.jpg)

- [Prajwal Prakash](https://twitter.com/prajwalprakash)
- [Ariel Sanchez](https://twitter.com/arielsanchezmor)
- [Dario Dörflinger](https://twitter.com/virtual_frog)
- [Nacho Osete](https://twitter.com/ignosgt)
- [Wes Milliron](https://twitter.com/wesmilliron)
- [David Prows](https://twitter.com/commputethis)

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

- We had the opportunity to design a simulated redfish-server-supported environment, and then use a more robust model based on a community [RedFish Interface Emulator](https://github.com/code2020ansible/AnsiDOC/tree/master/Redfish-Lookup) with Docker, a necessary requirement for the next stage of the project (get details and setup new RedFish-supported ESXi servers)

- On the intermediate stage, we had a free hand to create some additional playbooks leveraging the newest vSphere ESXi Server 7.0 API specification, so we may configure and set up the RedFish-Interfaced servers previously detected. 

- After getting a better insight of how Ansible could deploy a [VMware SDDC Nested Lab](https://github.com/code2020ansible/AnsiDOC/tree/master/Ansible-microSDDC-Lab) we repurposed the initial deployment answer file, so it may fit in our actual physical lab on the previously configured RedFish-Ready ESXi servers. We will finally try to add an existing community Ansible VRA module for extended functionality, over the previously configured ESXi servers in the intermediate stage.

- Take some time for some e-learning with courses like [Introduction to Ansible with AWS and CloudFormation](https://linuxacademy.com/cp/courses/lesson/course/7748) among other online resources apart from the excellent VMworld 2020's [Single Touch, Production-Ready ESXi Rollouts in Minutes With Ansible session - HCP1705](https://my.vmworld.com/widget/vmware/vmworld2020/catalog/session/1587247214712001aHPB) by [Bryan Sullins](https://www.twitter.com/RussianLitGuy)

- Use extensively and discovered Wireguard, a nice OpenSource VPN service so we could connect all the members to our follow-the-sun lab plaform, based in the AMER and EMEA regions. And additionally...how to multitask and context-switch Ansible Learning, GitHub management, AWS/VMWare lab building, VMWorld 2020 attending and Family/Homekeeping at the same time!
