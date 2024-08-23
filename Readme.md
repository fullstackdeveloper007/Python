# 2. Python 

# Topic Python Virtual Environment and pip

* pip acronym of preferred installer programe
* pip install requests(requests pkg) -- This install the pkg globally 
* pip list -- List all the packages installed globally
* pip uninstall requests
* pip install  -U requests (Update the pkg)
* pip show requests (it will show all the details of pkg and its dependent pkges
* `pip freeze` - This will list all the python pkgs in the current env, along with the versions
* `pip freeze > requirements.txt` - This will create a file called requirment.txt and mention all the project dependencies


## Virtial Environmenment (venv)
How to create a Virtial Env?
* `py -m venv .venv` (This will create a folder inside a solution folder namely `.venv`. `.venv`is the name of virtual environment. 
* `.venv\Scripts\activate.bat` (from command prompt, from python prompt getting error Activate.ps1 is not digitally signed)
* `deactivate` This will deactivate the virtual environment
*  pip


## `.env` Environment Variable File: This file can be used for keeping environment variable, like API keys
* `from dotenv import load_dotenv` This is the command for loading the env variable and `load_dotenv()` is also required after import code

* 
