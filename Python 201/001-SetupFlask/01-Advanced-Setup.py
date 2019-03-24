    # Flask is installed using pip installer
    # First check if pip is installed or not by executing - pip --version
    # If pip is not installed, install pip first using admin mode in a linux terminal
    
    # checking Python version 
    python -V
    # checking if pip installed or not 
    pip3 -V
    
    # install pip first in case it is not install
    sudo apt-get -y install python-pip
    
    # now install flask
    pip3 install flask
    
    # if needed upgrade pip
    pip3 install --upgrade pip