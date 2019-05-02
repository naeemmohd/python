### What is Python Django:
  * is a ***web*** application development ***framework***.
  * encourages clean and ***rapid development***
  * no need to re-invebt the wheel as many ***in-build features*** available
  * highly ***sclalable*** and flexible approach
  * encourages ***open source*** development 
  
### Python Django Setup(On Linux - Ubuntu):
  * Step 1 : Install ***Python tools***
    ```
    sudo apt-get -y update && sudo apt-get -y upgrade
    sudo apt-get -y install python3.6 python3-pip python3-virtualenv python3-setuptools python-dev build-essential
    ```
    ![Install Python Tools](../images/003-01-installpythontools.png)
  * Step 2 : Install and Configure ***Virtual Evironment***
    ```
    sudo pip install virtualenv 
    mkdir ~/work && cd ~/work
    mkdir venv && cd venv
    virtualenv -p python3.6 .
    source bin/activate
    ```
    ![Install and Configure Virtual Environment](../images/003-01-installconfigurevirtualenv.png)
  * Step 3 : Install ***Django***and Configure a Project
    ```
    pip install django==1.11.3
    mkdir src && cd src
    django-admin.py startproject ecommhome .
    python manage.py migrate
    python manage.py createsuperuser
    ```
    ![Install Django and Configure Project 1](../images/003-01-installdjangoconfigureproject1.png)
    ![Install Django and Configure Project 2](../images/003-01-installdjangoconfigureproject2.png)
  
    
    
    # ***In case installing flask, Flask-RESTful Flask-JWT***
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
    ```
  * Please see screen shot below: 
    ![Python versions](../images/003-01-InstallFlask.png)
    
### Your first Django App:
  * First To DO 
    ```
    ```
  * Please see screen shot below:
    ![The first Django app](../images/003-01-FirstDjangoApp.png)
      
    

