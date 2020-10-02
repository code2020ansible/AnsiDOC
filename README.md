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

- vSphere 7 Web Services API - <https://code.vmware.com/apis/968>
- Redfish API - <https://www.supermicro.com/manuals/other/RedfishRefGuide.pdf>
- Redfish API - <https://hewlettpackard.github.io/iLOAmpPack-Redfish-API-Docs>

## What we have already learned so far

### To collaborate altogether in a thriving JIT/GitLab/AnsiLab/SDDCLab/NestedLab

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/team-lab.png width=512px></>

- Thanks to Ariel we disposed of a nice Intel NUC-based Lab environment, where we could Just-In-Time-mess-with our Git repository, play with Ansible, emulate a RedFish Server-interfaced environment and the latest vSphere ESXi 7 RESTful API. **We disposed of three ESXi servers, a DNS server, a vCenter appliance and a nice jumpbox, Wireguard(ed) for better worldly availabity**; coast to coast and overseas, AMER + EMEA regions together in a lab that never sleeps and never got user-emptied in the latest 24 hours ;-)

### Design, simulate, and emulate a RedFish-interfaced Server enviroment with Docker

- We had the opportunity to design a simulated redfish-server-supported environment, and then use a more robust model based on a community [RedFish Interface Emulator](https://github.com/code2020ansible/AnsiDOC/tree/master/Redfish-Lookup) with Docker, a necessary requirement for the next stage of the project (get details and setup new RedFish-supported ESXi servers)

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/table-csv.png width=720px></>

### Use Ansible to query configuration data from the newest vSphere 7 RESTful API in our lab

- On the intermediate stage, we had a free hand to create some additional playbooks leveraging the newest [vSphere ESXi Server 7.0 Web Services API](https://code.vmware.com/apis/968) for better RESTfulness (and greater justice!), so we may configure and set up the RedFish-Interfaced servers previously detected.

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/gathering-facts-playbook.png width=720px></>
<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/ansible-playbook-api-test.png width=720px></>

### Try to build a reduced version of an existing SDDC Nested Lab Ansible deployment, and add VRA deployability to the set

- After getting a better insight of how Ansible could deploy a [VMware SDDC Nested Lab](https://github.com/code2020ansible/AnsiDOC/tree/master/Ansible-microSDDC-Lab) we repurposed the initial deployment answer file, so it may fit in our actual physical lab on the previously configured RedFish-Ready ESXi servers. We will finally try to add an existing [community Ansible VRA module](https://github.com/vmware-archive/ansible-role-vra/) for extended functionality, over the previously configured ESXi servers in the intermediate stage.

### Apart and overall, learn something new, have fun and expand our codeverse(tm)!

- Take some time for some e-learning with courses like [Introduction to Ansible with AWS and CloudFormation](https://linuxacademy.com/cp/courses/lesson/course/7748) among other online resources apart from the excellent VMworld 2020's [Single Touch, Production-Ready ESXi Rollouts in Minutes With Ansible session - HCP1705](https://my.vmworld.com/widget/vmware/vmworld2020/catalog/session/1587247214712001aHPB) by [Bryan Sullins](https://www.twitter.com/RussianLitGuy)

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/vHackathon_Ansible_Meeting.png width=512px></>

- Use extensively and discovered [Wireguard, a nice OpenSource VPN service](https://www.wireguard.com/quickstart/) so we could connect all the members to our follow-the-sun lab plaform, based in the AMER and EMEA regions. 

- And additionally...how to multitask and context-switch Ansible Learning, GitHub management, AWS/VMWare lab building, VMWorld 2020 attending and Family/Homekeeping at the same time!


