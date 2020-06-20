# cv_worker
task nodes for computer vision work, intended to be run on hardware accelerated platforms


## what does this application do?
cv_worker provides communications and data persistence layers around a system dedicated to supporting specific operations.  The first operations it is being developed for are oriented around computer vision tasks, hence the name.  It's also imagined that this is running on a specialized machine, like something with special hardware resources to accelerate machine learning.


## The anticipated modes of operation are:
- live model inference
- model training
- training / runtime analysis
- data annotation
- system administration


## How do clients consume this app?
Upstream systems can call cv_worker via its rest interface to monitor and dispatch tasks.  cv_worker is designed to update the caller either via a persistent connection or by scheduled updates as it processes a task.
This system can also be accessed from the command line or the django command line.


## What steps are needed to set up a system to run cv_worker?
- Initially the owner of a WORKER NODE (say a raspberry pi, packaged with an intel movidius neural compute stick, local disk storage, etc) decides he wants to set up a neural network for recognizing hieroglyphics in images.
- First a neural network is trained on this input on BUILD SYSTEM, let's say he used his desktop macintosh computer with a external GPU.
- She procures WORKER NODE and gets it to boot up to the os.
- Python, cv_worker and all  their requirements are installed on WORKER_NODE
- cv_worker_config.py is run on WORKER_NODE to set the system up to receive tasks.
- WORKER NODE is put on the network and is ready to perform work

If the user is interfacing with WORKER NODE via a third party system, the user registers the system with that third party system.  Or, a clever third party system could be designed to poll for WORKER NODE and automatically start talking with it when it comes up at its expected host/port/ip address.


## Install requirements:
python 3
I've only installed on linux or mac, don't know/care what problems this has on windows
