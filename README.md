# VeeamAssignment

Intro
=====
The project uses click dependency to take user inputs from the CLI
and create a synchronisation folders on the local machine based on an interval 
and log the output to a file 

Installation
============

You need to install the package dependencies for this project to run:
```bash
cd VeeamAssignment/

# Create virtual environment 
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# or activate tox's virtual environment after running tests
source .tox/{{pyversion}}/bin/activate

(venv) pip install -r requirements.txt
```


Running test cases
====================
Using tox to run tests aganist multiple test environments. 
```bash
tox
```

Running the assignment
======================

```bash
python3 script.py --src {{src_loc}} --dest {{dest_loc}} --interval {{interval_time}} --log_file {{log_file}}
# example
# python3 script.py --src /home/legion/Desktop/src/ --dest /home/legion/Desktop/dest --interval 1 --log_file /home/legion/Desktop/file_sync.log
```
