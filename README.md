# cv_worker
task nodes for computer vision work, intended to be run on hardware accelerated platforms


## what does this application do?
cv_worker provides communications and data persistence layers around a system dedicated to supporting specific operations.  the cv_worker code will also include the executable code for the 'model' doing the operation of interest.  These models are typically driven by a biiiiig data file as well of course.  

The first operations it is being developed for are oriented around computer vision tasks, hence the name.  It's also imagined that this is running on a specialized machine, like something with special hardware resources to accelerate machine learning.


## The anticipated modes of operation are:
- live model inference
- model training
- training / runtime analysis
- data annotation
- system administration
- system monitoring and tuning via the dashboard


## How do clients consume this app?
- Upstream systems can call cv_worker via its rest interface to monitor and dispatch tasks.  cv_worker is designed to update the caller either via a persistent connection or by scheduled updates as it processes a task.
- This system can also be accessed from the command line or the django command line.
- CV worker also has a single page javascript dashboard app, optimized for monitoring and system administration tasks


## What steps are needed to set up a system to run cv_worker?
- Initially the owner of a WORKER NODE (say a raspberry pi, packaged with an intel movidius neural compute stick, local disk storage, etc) decides he wants to set up a neural network for recognizing hieroglyphics in images.
- First a neural network is trained on this input on BUILD SYSTEM, let's say a desktop macintosh computer with an external GPU.
- WORKER NODE is provisioned at the physical and os package level, including the configuring of those special resources like GPUs.  Work is complete when install requirements are satisfied and WORkER NODE boots up to the os.
- cv_worker and all its dependencies are installed on WORKER_NODE
- cv_worker_config.py is run on WORKER_NODE to set the system up to receive tasks.
- WORKER NODE is put on the network and is ready to perform work

If the user is interfacing with WORKER NODE via a third party system, the user registers the system with that third party system.  Or, a clever third party system could be designed to poll for WORKER NODE and automatically start talking with it when it comes up at its expected host/port/ip address.


## Install requirements:
- python 3
- npm
- a reachable sql database, e.g. mysql
- a reachable messaging queue, e.g. rabbitmq
- memory and disk requirements are driven by the specific models / operations being supported.  running cv_worker_config at install time will help determine if resources are sufficient
- I've only installed on linux or mac, don't know/care what problems this has on windows
