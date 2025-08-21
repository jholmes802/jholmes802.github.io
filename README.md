# Justin Holmes
## EVS XT-VIA
An ansible role that supports configuring and managing XT-VIA servers for Broadcast applications.

## What is it?
The XT-VIA is a replay server used in a large variety of broadcast events, it is the gold standard of replay. These servers are flexible with many options and methods of Input and Output configurations these servers have thousands of parameters to set. The objective here was to develop a way to make setting up servers easier and give new tools to Broadcast Engineers.

## How does it work?

This is built on [Anisble](https://docs.ansible.com/) a tool developed by [Red Hat](https://www.redhat.com/) with a hugh community behind it. Building modules, libraries, roles and collections to support the configuration of thousands of types of systems, it has accelerated out deployment into the future. 

## Code Review

Here is a code review I did at the beginning of this course. 

[Video Code Review](https://youtu.be/emOqEMgcZ6w)

# Self Assessment

Software development has been a passion of mine since high school where I learned the infinite possibilities of software development, the ability to control and do almost anything from a laptop was fascinating to me. I started with small projects like displaying data on a web page or an inventory application, nothing too complicated. Almost all of my projects have used Python to code because of its rapid development and flexibility, I have dabbled in languages like JavaScript, and C++ for more performant applications. This course has helped me develop me skills after reviewing and trying things to better understand the importance of documentation and designing for collaborative work. 

This project comes from my work where we aimed to automate the deployment of EVS XT-VIA broadcast replay servers and their deployment into facilities. These servers are what drive most of the worlds TV replay, almost every replay on major football, hockey, basketball and baseball is done with these systems. They are incredibly powerful and flexible with hundreds of possible configurations they are complex to setup and ensure they are done correctly. Utilizing ansible was a clear path for me, because of its native item potency which gave us insights into which parameters or tasks were changes vs already set or failed, as well as its complex handling of variables which would let us build large dynamic EVS setups. With a new age of ST 2110 IP Video we now have hundreds of parameters to set that are all ports and multicast addresses for each server so this tool is designed to configure these and ensure the IP addresses and multicasts are correct. 

This was written to fit into our larger company’s automation pipeline and workflow to set up our system’s easier and more efficiently. I worked with coworkers to develop not only the modules which accessed the servers but the variable and task structure around it so it would match other projects we have done. One of the biggest challenges I had was writing it abstractly enough for the server with so many parameters it was critical that I did not have to create classes for each and control them that way, I needed something more generic. We had many meeting and revisions to get to this point of the software. One of the complexities was creating a structure to handle all this data and store it in an easy fashion that was quick to debug and develop as I went so JSON structure made sense to, working and manipulating data as dictionaries was the simplest way. 

# The Code
### [evs-xt-via](evs-xt-via)
### [v0.0.1](evs-xt-via/v0.0.1/)

This iterration was the first pass, it used very little python and structured methods. It lacked support for item potency and variables. Everything was hardcoded to use specifc formulas and variables, so it would not work on the next truck system. This was a patch designed to get us through the current build and be the ground work for more to come. 

### [v0.1.0](evs-xt-via/v0.1.0/)

This system used a datastructure that where each server was a key with the value being the settings for the server. This was ok but struggled to easily scale this because of the way Ansible dealt wih vairables. Another major change was developing the evsApi which is a python library that interfaces with the actual server. This API is called from library modules that are in the role as well which are passes variables within a task to make changes. This was a huge shift becuase it centeralized the command process into something that was much easier to abstractly interact with and make the edge tasks deal with the specific parameters but the library still handles most of the edge cases within the evsApi. 

### [v0.1.2](evs-xt-via/v0.1.2/)

This version got more functionality like tasks that better handle PTP and Audio Packet timing. There is an expansion of tasks to capture even more parameters and options. It better handles Super Motion Phases for 6x times cameras. Something else this new module does is change the way the variables are handled and uses more of the native ansible variable handling which relies on host variables and each host/task has unique variables. This allows one to set variables by host/server and then have global variables like the Codec to use. This also fit into our inventory file structure and other things to better handle our truck systems. It was integrated into our automation platform so this needed a fair bit of updates to merge into it. 