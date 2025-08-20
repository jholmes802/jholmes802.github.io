# One Touch EVS Commissioning

The purpose of this toolkit is that it will create a deployment to be one touch commissioning on XT-VIA servers.

## Navigation

[evsWebSession.py] (/evsWebSession)

## Bounds and Limits

This tools kit will be limited to things it can do/execute over standard and "safe" methods.
This is designed for the EVS and Technology Team to commission systems, it is not intended to be used for everyday use.

We may work to expand this to cover Big shows as well, but that is unlikely.

## Timeline and Phases

1. Able to confirm the correct IP Address and Server Version
2. Able to read License Information
3. Able to read Config Lines
4. Able to build standard Config Lines
5. Able to read Live IPs
6. Able to build correct Live IPs
7. Set RDS server

## Architecture

This will operates as a server client, where the server will do the workfload and actual communciation with the XT-VIA server and the Client will monitor progress and control the system.
Using Nginx as a static file server and reverse proxy engine it will handle the front end. We will to develop a strong backend handle the processing of information and status updates.

Everything should run as a container or set of containers so that it can be deployed easily to an individuals laptop or another container orchestration software such as Kubernetes.

# Notes from Testing

I found that using the testing.py testingImportConfigLine() we could upload config files to the server.
I also found that testing.py testingSendingSingleParm() could be used to set a single parameter, how ever the biggest issue is that if the parameter changes or affects other things, it will not take the change. Potentially could work around this by sending the updated parameter and then reading the response which will update the other parameters in the config file, we just then need to send that back to the server as a commit this.

This should leave us enough abstraction to not be specific to MC 20.7.

# How to Run these

```bash
ansible-playbook -i inventory.yml playbooks/<playbook>.yml

#Example would be
ansible-playbook -i inventory.yml XT-VIA-PB.yml
```


# How does it all work

Using ansible it has a series of built in modules that are used to setup one or many servers. This is expandable to set almost any parameter on the server, as long as it can be set via the web interface we can emulate it and set it via that. 

## The Tasks - Normaly Done for Comissioning

- [] Turn Server on and run correct version
- [] Set PC LAN 1 IP Address
- [] Set PC LAN 2 IP Address
- [] Set DNS Servers
- [] Set Domain
- [] Build Config Lines 

