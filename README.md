# cv_worker
task nodes for computer vision work, intended to be run on hardware accelerated platforms

this repository is a reference application.  It only supports the 'ping_cv_worker' operation.  To write a worker to do your own tasks, fork this project and make a new system for your needs, see 'writing your own cv_worker' below

## what does this application do?
cv_worker provides communications and data persistence layers around a system dedicated to supporting specific operations.  the cv_worker code will also include the executable code for the 'model' doing the operation of interest.  These models are typically driven by a big data file as well of course.  

The first operations it is being developed for are oriented around computer vision tasks, hence the name.  It's also imagined that this is running on a specialized machine, like something with special hardware resources to accelerate machine learning.


## The anticipated modes of operation are:
- live model inference
- model training
- training / runtime analysis
- data annotation
- system administration
- system monitoring and tuning via the dashboard


## How do clients consume this app?
- for cv_workers configured as 'accept_calls' type, upstream systems can call cv_worker via its rest interface to monitor and dispatch tasks.  cv_worker is designed to update the caller either via a persistent connection or by scheduled updates as it processes a task.
- for cv_workers configured as 'call_back' type, upstream system creates a job and waits for cv_worker to check in and pick upthe task.
- This system can also be accessed from the command line
- CV worker also has a single page javascript dashboard app, optimized for monitoring and system administration tasks


## What steps are needed to set up a system to run cv_worker?
- Initially the owner of a WORKER NODE (say a raspberry pi, packaged with an intel movidius neural compute stick, local disk storage, etc) decides he wants to set up a neural network for recognizing hieroglyphics in images.
- First a neural network is trained on this input on BUILD SYSTEM, let's say a desktop macintosh computer with an external GPU.
- WORKER NODE is provisioned at the physical and os package level, including the configuring of those special resources like GPUs.  Work is complete when install requirements are satisfied and WORKER NODE boots up to the os and all special hardware is recognized.
- cv_worker and all its dependencies are installed on WORKER_NODE
- cv_worker_config.py is run on WORKER_NODE to set the system up to receive tasks.
- WORKER NODE is put on the network and is ready to perform work
- If the user is interfacing with WORKER NODE via a third party system as an 'calls_back' worker, the user configures the call_back info, including the url of the third party system and any proxies that might be needed.

At task execution time:
- If the user is interfacing with WORKER NODE via a third party system as an 'accepts_calls' worker, the user registers WORKER NODE with that third party system. 
- if the system is set to 'call_back_upon_request', the user presses the physical button on WORKER NODE, or uses the dashboard to initiate the callback to the third party system.  Otherwise WORKER NODE will poll the third party system at regular intervals.


## Install requirements:
- python 3
- npm
- a reachable sql database, e.g. mysql
- a reachable messaging queue, e.g. rabbitmq
- memory and disk requirements are driven by the specific models / operations being supported.  running cv_worker_config at install time will help determine if resources are sufficient
- I've only installed on linux or mac, don't know/care what problems this has on windows

## Writing your own cv_worker
cv_workers are designed to work cooperatively in a network.  If you wish to develop a worker for a new task:
- adhere to the contracts that are defined with external systems
- adhere to the interfaces / json formats when talking to upstream and downstream nodes

## architecture notes
(link to cv_worker architecture illustration)
- in general, cv workers are organized as individual nodes grouped into one of many worker pools.  
- cv workers support specific operations, and when multiple workers in a worker pool support the same operation, they work cooperatively to load balance requests for that operation 
- inter-worker-pool messages and global messages are managed by dedicated queues
.
.
