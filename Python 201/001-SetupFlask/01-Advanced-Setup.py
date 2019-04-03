    # Flask is installed using pip installer
    # First check if pip is installed or not by executing - pip --version
    # If pip is not installed, install pip first using admin mode in a linux terminal
    
    # ***In case only installing flask***
    # checking Python version 
    python -V
    which python
    whereis python
    # checking if pip installed or not 
    pip3 -V
    which pip
    whereis pip
    
    # install pip first in case it is not install
    sudo apt-get -y install python-pip
    
    # now install flask
    pip3 install flask
    which flask
    whereis flask
    
    # if needed upgrade pip
    pip3 install --upgrade pip
    
    
    # ***In case installing flask, Flask-RESTful***
    ############################################
    # ***python environment installation*** 
    # for CentOS based - install python first - yum -y install python3x python3x-pip = x is version like 3.6 or 36 - 

    # for Ubuntu based apt-get -y install python3x python3x-pip

    # for windows (finstall chocolatey first)
    # Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))


    # linux 
    sudo su 
    clear
    yum -y install python36 python36-pip  
    pip3 install virtualenv
    virtualenv python3env --python=python36
    source python3env/bin/activate
    pip install flask Flask-RESTful Flask-JWT
    pip freeze

    # windows PowerShell
    clear
    choco install python36 python36-pip  
    pip3 install virtualenv
    virtualenv python3env --python=python36
    python3env/Scripts/activate.ps1
    pip install flask Flask-RESTful Flask-JWT
    pip freeze
    ############################################