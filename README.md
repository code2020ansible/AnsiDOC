# AnsiDOC
Redfish + Ansible + vSphere 7 new REST API provisioning + vRA integrations

## Winning entry to the VMware {code} Connect Hackathon 2020!
Here's the winning project of VMware {code} Connect Hackathon 2020, the result of hard work, teamwork and a lot of commitment! 

## Team members

![the best teampicture ever!](https://github.com/code2020ansible/AnsiDOC/blob/master/vHackathon_Ansible_Team_Picture.jpg)

- [Prajwal Prakash](https://twitter.com/prajwalprakash)
- [Ariel Sanchez](https://twitter.com/arielsanchezmor)
- [Dario Dörflinger](https://twitter.com/virtual_frog)
- [Nacho Osete](https://twitter.com/ignosgt)
- [Wes Milliron](https://twitter.com/wesmilliron)
- [David Prows](https://twitter.com/commputethis)
- [Carl Capozza](https://twitter.com/Carlcapozza)

## For the Hackathon presentation

### How we came about the idea

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/ansible-vmware.png width=100%>

**Originally, AnsiDOC was going to be an Ansible native translation of vDocumentation**. The vDocumentation project gets excel reports from virtual environments. The new version, vDoc, has started leveraging RedFish, a new protocol for out of band management of servers adopted by all major industry players. **Because of Ansible's popularity and RedFish functionality, a new documentation tool can be created** that works with VMware hosts as well as any other type of server out there - it is no longer dependent on OS. This became phase 1 of the project.

**We also set to use the new REST API endpoints for vSphere 7. We thought we could transition from collecting data to using the data for provisioning**. This became phase 2 of the project.

Finally, **we merged with the other EMEA based Ansible team to combine lab resources and focus on what's really amazing of the VMware Hackathons: meeting new people who are geeking out over the same things you are interested, and making friends!** The EMEA team had big sights and we collaborated to create a joint lab environment so they can work on furthering work by [Rutger Blom](https://github.com/rutgerblom/SDDC.Lab) and [VMware's own Ansible examples](https://github.com/vmware-archive/ansible-role-vra/).

### What you have learned

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/vHackathon_Ansible_Meeting.png width=720px>

First, **companionship and collaboration have no bounds**. We were able to effectively work together using VMware Code's Slack, Github and the lab environment. We made new friendships and will continue using this lab and this team in the future. For most of us **Ansible was a new tool to be explored**, so we tried our best to learn about how it works and what can be done. 

Every team member can find a way to contribute, and every team member in this case learned something.

### What challenges you faced

Standing up a collaborative lab is no small feat. This took too much time. And even then, we didn't have the right hardware, so we had to get creative in our solutions. During the joint-effort **we had to merge some changes and track advanced work so it may be pushed to the upstream branch**, but after some hours of full commitment we achieved to have all the work -up to the last byte!- of all the team members that worked in a follow-the-sun basis.

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/git-commitment.png width=720px>


### Why your chosen language was the right choice for this project

**Ansible is Agentless, OS and platform agnostic - perfect for our operational plane**, which was at the hardware and infrastructure level. Additionally, it is comfortable using open source technologies such as an Ubuntu VM jumpbox, and tracking changes in yaml with git. It was also very easy for members to pick up, and we discovered lots of functionality without spending too much time googling

And now, on to the project!

## Project Scope

We can do a very nice proof of concept demo using both Redfish and the new vSphere 7 ESXi RESTful api.

Apart from provisioning the initial ESXi+vCenter stack with Ansible, we also plan to set on top a SDDC NSX-T Nested Lab, and a VRA service over the top.
Helping to fulfill our best chaos engineering dreams, we joined the only two Ansible teams together for greater throughput

## What we would like to do

### Phase 1

- Look up IP address of redfish enabled server from table
- Look up redfish credentials from table
- Retrieve and output serial number from redfish API to console and back to table as a new column

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

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/team-lab.png width=512px>

- Thanks to Ariel we disposed of a nice Intel NUC-based Lab environment, where we could Just-In-Time-mess-with our Git repository, play with Ansible, emulate a RedFish Server-interfaced environment and the latest vSphere ESXi 7 RESTful API. **We disposed of three ESXi servers, a DNS server, a vCenter appliance and a nice jumpbox, Wireguard(ed) for better worldly availability**; coast to coast and overseas, AMER + EMEA regions together in a lab that never sleeps and never got user-emptied in the latest 24 hours ;-)

### Design, simulate, and emulate a RedFish-interfaced Server enviroment with Docker

- We had the opportunity to design a simulated redfish-server-supported environment, and then use a more robust model based on a community [RedFish Interface Emulator](https://github.com/code2020ansible/AnsiDOC/tree/master/Redfish-Lookup) with Docker, a necessary requirement for the next stage of the project (get details and setup new RedFish-supported ESXi servers).

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/docker-redshift-containers.png width=720px>

- With this Docker environment (and several containers acting as physical servers), we were able to query serial numbers with Ansible against the RedShift interfaces and populate a CSV-based tablespace, the foundation for the next stage in our project: identify certain servers and gather ESXi information (Note: we are just on the stage to provision/configure the selected servers depending on the SERIAL/State criteria of our CSV document.

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/table-csv.png width=720px>

### Use Ansible to query configuration data from the newest vSphere 7 RESTful API in our lab

- On the intermediate stage, we had a free hand to create some additional playbooks leveraging the newest [vSphere ESXi Server 7.0 Web Services API](https://code.vmware.com/apis/968) for better RESTfulness (and greater justice!), so we may configure and set up the RedFish-Interfaced servers previously detected.

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/ansible-playbook-api-test.png width=720px>

- We also learned that in order to reference information returned from an API call like the host mob-id from vcenter host api call...

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/vchosts.png width=512px>

...one can do the following:  

<img src=https://github.com/code2020ansible/AnsiDOC/blob/master/images/gathering-facts-playbook.png width=720px>

- On the other hand, we found out that the vSphere 7 esx REST API still required having vCenter to use.  It can not be used to connect directly to a host.  We used the API Explorer in Developer Center with in the vSphere Client to determine this.

![vSphere API Explorer - esx API](https://github.com/code2020ansible/AnsiDOC/blob/master/images/vSphereAPIExporer-esxAPI.png)

- Finally, with some expert help traversing the data sets by Prajwal, we managed to join the host query, REST query and redfish table created before to accomplish the proof of concept!

![Joint phase 2 efforts](https://github.com/code2020ansible/AnsiDOC/blob/master/images/phase2-for-showing.png)


### Try to build a reduced version of an existing SDDC Nested Lab Ansible deployment, and add VRA deployability to the set

- After getting a better insight of how Ansible could deploy a [VMware SDDC Nested Lab](https://github.com/code2020ansible/AnsiDOC/tree/master/Ansible-microSDDC-Lab) we repurposed the initial deployment answer file, so it may fit in our actual physical lab on the previously configured RedFish-Ready ESXi servers. We will finally try to add an existing [community Ansible VRA module](https://github.com/vmware-archive/ansible-role-vra/) for extended functionality, over the previously configured ESXi servers in the intermediate stage.

### Apart and overall, learn something new, have fun and expand our codeverse(tm)!

- Take some time for some e-learning with courses like [Introduction to Ansible with AWS and CloudFormation](https://linuxacademy.com/cp/courses/lesson/course/7748) among other online resources apart from the excellent VMworld 2020's [Single Touch, Production-Ready ESXi Rollouts in Minutes With Ansible session - HCP1705](https://my.vmworld.com/widget/vmware/vmworld2020/catalog/session/1587247214712001aHPB) by [Bryan Sullins](https://www.twitter.com/RussianLitGuy)

- Use extensively and discovered [Wireguard, a nice OpenSource VPN service](https://www.wireguard.com/quickstart/) so we could connect all the members to our follow-the-sun lab plaform, based in the AMER and EMEA regions. And additionally...how to multitask and context-switch Ansible Learning, GitHub management, AWS/VMWare lab building, VMWorld 2020 attending and Family/Homekeeping at the same time!
