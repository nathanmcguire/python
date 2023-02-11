Use packages and moudles to structure projects.

One Class per Module

Look at projects on github for examples of how to strucuture your projects.

Place utilities all in single location.

Organize import statements - 3rd party, built-ins, locals & relatives; all in alpha order within the groupings.

Starting a new project:
Install Ptyon Environment: "pip install pipenv"
Create and Enter Environment: "pipenv shell"

Traditional Requirements Management

Save requirements
pip freeze > requirements.txt

Install requirements
pip install -r requirements.txt 

Pipfile Requirements Management
If requirements.txt exists, runnign pipenv install will create a pipfile and pipfile.lock and a new virtual env from the requirements.txt.
To remove a previous virtual environment pipenv --rm
