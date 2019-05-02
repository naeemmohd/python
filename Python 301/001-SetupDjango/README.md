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
  

### Python Django Setup(On Windows - using Powershell):
  * Please wait ...
    ```
    Upcoming ...
    ```
  
    
### Your first Django App:
  * Please wait ...
    ```
    Upcoming ...
    ```
  
      
    

