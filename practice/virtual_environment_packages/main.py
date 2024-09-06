# Creating Virtual Environments - The module used to create and manage virtual environments is called venv. venv
# python -m venv tutorial-env

# tutorial-env\Scripts\activate - WINDOWS TO ACTIVATE ENV
# source tutorial-env/bin/activate - UNIX OR MACOS TO ACTIVATE ENV

# deactivate - DEACTIVATE CURRENT ACTIVE ENV

# Managing Packages with pip

# python -m pip install novas  - install latest version of package
# python -m pip install requests==2.6.0 - install specific version of package
# python -m pip install --upgrade - upgrade all package to latest version
# python -m pip install --upgrade requests - upgrade specific package  to latest version
# python -m pip uninstall requests - uninstall package
# python -m pip show requests - will display information about a particular package
# python -m pip list - will display all of the packages installed in the virtual environment
# python -m pip freeze > requirements.txt - will produce a similar list of the installed packages with the name of requirement.txt
# python -m pip install -r requirements.txt - install all the necessary packages within the requirements.txt
# python -m pip install "SomePackage>=1.0.4"  # minimum version
# pip install --user some_pkg # install packages just for the current user? | --user is currently not valid inside a virtual env's
