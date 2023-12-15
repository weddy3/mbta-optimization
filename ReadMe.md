The first thing you want to do is to create a virtual environment with our project's dependicies. cd into the directory in which you cloned this repo. Then run

`python -m venv env or python3 -m venv venv`

This will create a virtual environment folder named venv, that directory will be used to control package versions and python version. On *nix systems, run

`source venv/bin/activate`

or on windows

`.\venv\Scripts\Activate.ps1`

After this command you should see a small (venv) pop up on the terminal line indicating you are in the virtual environment. Once in the environment run the following:

`pip install -r requirements.txt`

make sure you add the path to that .txt file if need be. This will install all necessities to the virtual environemnt so the website will be good to go. 