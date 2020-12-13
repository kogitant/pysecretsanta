# pysecretsanta
Little script to draw secret santa gifters and recipients

# Usage
```
python3 main.py --names "Antti,Katja,Aada,Helmi" --lang=fi
```

# Proper project setup
To set up your development environment after a fresh git clone, do the following.
```
python3 -mvenv venv
source venv/bin/activate
pip install -r requirements.txt
black --check .
python3 -m pytest --cov=src --cov-fail-under=80 tests/*
python3 main.py --names "Antti,Katja,Aada,Helmi" --lang=fi
```

The steps being:
* Create project specific virtual env for python3 (python3 -mvenv venv)
* Activate the project specific virtualenv (source venv/bin/activate)
* Install libraries used by proect under the activated virtual environment (pip install -r requirements.txt)
* Verify source codes are formatted according to Black rules (black --check .)
* Run unit tests and verify coverage of all codes (python3 -m pytest --cov=src --cov-fail-under=80 tests/*)
* Use the app to do what it was intended to (python3 main.py --names "Antti,Katja,Aada,Helmi" --lang=fi) 

# How are things organized?
* main.py acts as the access point, intended to be used from command line
* src directory contains the source codes like classes used in main.py
* tests directory contains unit tests for sources
* .coveragerc is used to define how unit test code coverage is collected
* .gitignore is the standard file to specify what file and directories should never be versioned (committed to git, pushed to Github)
* requirements.txt specifies which python dependencies are used
* .travis.yaml specifies how travis is used to test the github repo (provided that it is public, not private) 

# Development
## Format sources with Black
```
black .
```

### Verify source codes match Black rules
```
black --check .
```

## Run unit tests and verify code coverage 
```
python3 -m pytest --cov=src --cov-fail-under=80 tests/*
```

## To 
