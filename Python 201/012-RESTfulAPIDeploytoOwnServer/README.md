### How to deploy RESTful APIs on your own Servers:
  * ***Issue***: 
    * The Heroku deployment was quite seam less, but also restricted too. There were multiple reasons-
      * no complte control on the deployment servers
      * handling scalability by spawning more processes and threads not in our control
      * Setting up the caching was also not in our control
  * ***Solution***
    * Deploy the RESTful API on your own server in cloud- AWS, Azure, Google, DigitalOcean cloud etc
    * We will deploy the RESTful API on a newly provisioned Linux Server - Ubuntu 16.04  - where will install and configure the following:
      * Setting up the server with ***users, security, firewall*** settings
      * Install and configure ***Postgres*** SQL Database:
      * Install and configure ***Nginx Proxy*** server( a web server, reverse proxy, load balancer, HTTP cache handler etc)
      * Install and configure ***uWSGI***(Web Service Gateway Interface)


### Setting up the server with ***users, security, firewall*** settings
  * Provisioning a server -
    * I am setting up a server on my labserver account in LinuxAcademy, but you can use AWS, Azure, Google, DigitalOcean clouds or any other public cloud provider.
    * You can setup a Ubuntu server with a ***EC2 instance*** in ***AWS***, a ***VM instance*** in ***Azure or Cloud*** or a ***Droplet*** in ***Digital oceans***
    * Basically these are nothing but a Virtual Machine server on the specific cloud services provider
    * Also you can setup your RESTful API on any LINux server ( any ***Ubuntu based system*** e.g. Ubuntu, Mint, LinuxLite etc or ***CentOS based systems*** like CentOS, RHEL etc)
    * I am using a medium sized server - ***2 Virtual CPUs with 4GB memory and 8 GB hard disk space*** - you can use even a small sized server for testing - ***1 Virtual CPUs with 1GB memory and 4 GB hard disk space***
    * Please follow the steps below for provisioning the server:

    * Step 1: ***Setup thes server***
      * Once the server is provisioned then - 
        * ***SSH to the server***,  
        * ***set privileges to root user***,  
        * ***update the server***, ***install git tree nano curl nginx python3 python3-pip python3-dev libpq-dev packages*** 
        ```
        # ssh <user_name>@<the server ip> - for me the server is 'mnaeemsiddiqui1c.mylabserver.com' and the user is 'cloud_user'
        ssh cloud_user@mnaeemsiddiqui1c.mylabserver.com   # This line will prompt you for entering password and login you to the server as 'cloud_user'
        sudo su  # This line will set root privileges
        apt-get -y update   # this updates the server with latest packages - in Ubuntu based system you  may use apt-get -y update 
        apt-get -y install git tree nano curl nginx wget python3 python3-pip python3-dev libpq-dev # installs packages 
        * Reboot after installation and then verify 
        ```
        python -V
        pip -V
        ```
        * Here is the snapshot:
        ![Update and Insatll packages](../images/002-012-updateandinstallpackages.png)
        ![Update and Insatll packages](../images/002-012-updateandinstallpackages02.png)

    * Step 2: ***Create a new Linux user other that root***
      * Root user(***root***) is the admin level super user and if hacked can create havoc.
      * So its better to create a ***new linux user** which can be used to manage running applications
      * Use the following command to create a new user - ***adduser mnaeem*** - I am however using the linux user ***cloud_user*** as my user for running the applications
      * Also to change the password user - ***passwd mnaeem***
      * Here is the snapshot:
        ![Create new Linux User](../images/002-012-createnewlinuxuser.png)

    * Step 3: ***Grant the user Elevated permissions***
      * Since your new user(in my case "cloud_user") needs to install required software, setup and configure Postgres, NGinx, uWSGI, Firewall etc., we need to assign it ***root level permissions***.
      * Execute the code - ***visudo*** - this will open the sudoers file - change the lines from 
        ```
        # User privilege specification
        root ALL=(ALL:ALL) ALL
        ```
        to
        ```
        # User privilege specification
        root ALL=(ALL:ALL) ALL
        cloud_user ALL=(ALL:ALL) ALL  # add this line for elavating your user for root level permission
        ```
      * Since default text editor is "vi" you have to click ***"i"*** key to start editing,  ***"Esc"*** key to stop editing  and ***":wq"*** to save and quit the file.
      * Here is the snapshot:
        ![Assign Root permissions to the Linux User](../images/002-012-rootpermissionforlinuxuser.png)  
    
    * Step 4: ***Enabling SSH permissions for the Linux user***
      * Execute the code - ***nano /etc/ssh/sshd_config*** - this will open the sudoers file - add the line below at the end of the file
        ```
        AllowUsers cloud_user
        ```
      * Here is the snapshot:
        ![Enable SSH permission to the Linux User](../images/002-012-enablesshpermissionforlinuxuser.png)  
      * Reload the SSH service due to this new change - execute - ***systemctl sshd reload*** 



### Install and configure ***Postgres*** SQL Database:
  * Please follow the steps below for setting up the database:

    * Step 1: ***Install Postgres***
      * Please use the following command - (for Ubuntu based system , use apt-get instead of apt-get)
        ```
        apt-get -y install postgresql  postgresql-contrib
        systemctl start postgresql
        systemctl enable postgresql
        systemctl status postgresql
        ```
      * Here is the snapshot:
        ![Installing Postgres](../images/002-012-installpostgres.png)
        ![Initialize Postgres](../images/002-012-initializepostgres.png)
    
    * Step 2: ***Create a Postgres user and a database by the same name as user name***
      * In Postgres - ***postgress*** user and ***postgres*** database are the default user and database - this user and database is created when we install Postgres by default
      * You can directly connect to ***postgres*** database by executing a command ***pqsl*** with ***postgres*** user logged in by using command ***sudo -i -u postgres***
      * Similarly if you create a ***mnaeem*** user and ***mnaeem*** database then you can directly connect to ***mnaeem*** database by executing a command ***pqsl*** with ***mnaeem*** user logged in by using command ***sudo -i -u mnaeem***
      * Similarly if you create a ***cloud_user*** user and ***cloud_user*** database then you can directly connect to ***cloud_user*** database by executing a command ***pqsl*** with ***cloud_user*** user logged in by using command ***sudo -i -u cloud_user***
      * So lets create the ***cloud_user*** user and ***cloud_user*** database:
        ```
        sudo -i -u postgres  # this will let you login as Postgres user
        createuser cloud_user -P # this will create a cloud_user Postgres user , -P flag is used to prompt for password
        createdb cloud_user# creates database cloud_user in your case it will be different
        ```
      * Once ***cloud_user*** user and ***cloud_user*** database is created then exit out of the ***postgres*** user by executing - ***exit***
      * Now login as ***cloud_user***, execute the command ***psql*** once logged in and ***\conninfo*** after entering into the psql command window
        ```
        sudo -i -u cloud_user  # this will let you login as cloud_user 
        psql # this will take you to the pqsl command window
        \conninfo # to verify if its ***cloud_user*** user and ***cloud_user*** database
        ```
      * Execute ***\q*** to quit out of psql window
      * Here is the snapshot:
        ![Create a Postgres User by the name cloud_user](../images/002-012-loginandverifythenewuseranddatabase.png)

    * Step 3: ***Secure connection to Postgres***
      * Please use the following command - Please update the following line in the Postgres configuration file at location - ***sudo nano /etc/postgresql/9.5/main/pg_hba.conf** 
      * In Ubuntu based systems it might be at location -  /etc/postgresql/9.5/main/pg_hba.conf Otherwise find the file bby issuing a command - ***locate pg_hba.conf***
      * So change the line from 
        ```
        # "local" is for Unix domain socket connections only
        local   all             all          peer

        ```
        to
        ```
        # "local" is for Unix domain socket connections only
        local   all             all          md5

        ```
      * Here is the snapshot:
        ![Installing Postgres](../images/002-012-securesocketforpostgres.png)


### ***Note*** - ***Use cloud_user/or your users login with sudo to do these stepps from below***
### Install and configure ***Nginx Proxy*** server Part 1:
  * Step 1: ***Setting up nginx and starting it***
    * Execute the commands as below to install and run ***nginx***
      ```
      sudo apt-get -y install nginx  # installs nginx
      sudo systemctl start nginx # starts the nginx 
      sudo systemctl enable nginx # enables the nginx 
      sudo systemctl status nginx # status of the nginx 
      ```
  * Step 2: ***Setting up app folder***
    * Create the app folder where the flask application files will reside.
      * make a directory first - ***sudo mkdir /var/www/html/products-restful***
      * assign 'cloud_user' as owner of this folder(it can be something else in your case like mnaeem etc) - ***sudo chown cloud_user:cloud_user /var/www/html/products-restful***
      * change the folder to the app folder - cd /var/www/html/products-restful
      * clone the RESTful API reporsitory you used to setup and deploy your app in Heroku - ***sudo git clone https://github.com/naeemmohd/RESTfulAPIDeploytoHeroku.git .***
      * make a directory got logs - ***sudo mkdir log***
    * Please execute the below commands - 
      ```
      sudo mkdir /var/www/html/products-restful
      sudo chown -R cloud_user:cloud_user /var/www/html/products-restful
      sudo chmod -R ugo+rwx /var/www/html/products-restful
      cd /var/www/html/products-restful
      sudo git clone https://github.com/naeemmohd/RESTfulAPIDeploytoHeroku.git .
      mkdir log
      ```
    * Here is the snapshot:
      ![Setup app folder](../images/002-012-setupappfolder.png)
  
  * Step 3: ***Setting up virtual environment***
    * Virtual environment helps in setting up a seperate enviroment on a specific folder and installs the required software only for that environment.
    * This it can help setting up multiple environments for multiple versions of Python 
    * To install virtualenv packages - ***pip install virtualenv*** or ***pip3 install virtualenv*** if pip3 is installed
    * To create a virtual environment named 'myappenv' - ***virtualenv -p python3 <env_name>***
    * To activate the virtual environment - ***source <env_name>/bin/activate***
    * To install all the packages defines in the file requirements.txt - ***pip install -r requirements.txt***
    * To check what all got install in the virtual environment - ***pip freeze***
    * To deactivate the virtual environment - ***deactivate***
    * Please execute the below commands - 
      ```
      # apt-get groupinstall 'Development Tools' # installs development tools
      # pip install --upgrade pip # upgrades pip 
      sudo apt-get -y install epel-release
      sudo apt-get -y install python36 python36-pip python36-devel
      sudo pip3 install --upgrade pip3
      sudo pip3 install -U virtualenv
      # pip3 install virtualenv  # installs virtualenv
      virtualenv -p python3 myappenv # creates a virtual environment named 'myappenv' and install some default python and pip packages
      source myappenv/bin/activate  # activates the virtual environment
      pip install -r requirements.txt # installs all the packages defines in the file requirements.txt in the current folder
      pip freeze # check what all got install in the virtual environment
      ```
    * Here is the snapshot:
      ![Setup virtual environment](../images/002-012-setupvirtualenvironment01.png)
      ![Setup virtual environment](../images/002-012-setupvirtualenvironment02.png)
      ![Setup virtual environment](../images/002-012-setupvirtualenvironment03.png)

### Install and configure ***uWSGI***:
  * uWSGI is a web service gateway interface.
  * Please do the following to install and configure ***uWSGI**:
    * Step 1: ***Install uWSGI**:
      * execute -  ***pip install uwsgi*** or ***pip install https://projects.unbit.it/downloads/uwsgi-lts.tar.gz***

    * Step 2: ***Setup uWSGI service for our app**:
      * Create a file  -  ***sudo nano /etc/systemd/system/uwsgi_products_restful.service***   
      * This is a uWSGI configuration file which states the name and location of the Postgres databse, error logs, uWSGI conf files etc
      * The ***DATABASE_URL*** is as - ***DATABASE_URL=postgres://cloud_user:cloudpassword@localhost:5432/cloud_user***
        * ***postgres://*** - specifies that its a Postgres database
        * ***cloud_user:cloudpassword*** - specifies the Postgres user name and password
        * ***@localhost:5432/cloud_user*** - specifies the server as ***localhost***, port as default ***5432*** and ***cloud_user*** as the databse name
      * Copy the following content in the file and save -
        ```
        [Unit]
        Description=uWSGI products restful
        [Service]
        Environment=DATABASE_URL=postgres://cloud_user:cloudpassword@localhost:5432/cloud_user
        ExecStart=/var/www/html/products-restful/myappenv/bin/uwsgi --master --emperor /var/www/html/products-restful/uwsgi.ini --die-on-term --uid cloud_user --gid cloud_user --logto /var/www/html/products-restful/log/emperor.log
        Restart=always
        KillSignal=SIGQUIT
        Type=notify
        NotifyAccess=all
        [Install]
        WantedBy=multi-user.target
        ```
      * Here is the snapshot:
        ![Install and configure uWSGI](../images/002-012-InstallandconfigureuWSGI01.png)

    * Step 3: ***Setup uWSGI uswgi.ini for our app**:
      * Create/Update a file(delete all Heroku uwsgi content, if already exisiting)  -  ***sudo nano uwsgi.ini***   
      * Explanation of the commands in the file:
        * ***/var/www/html/products-restful*** - is set as base app folder
        * ***app =run*** - it means that the 'app' to run is 'run.py'
        * ***module = %(app)*** - the module variable also refrences the app variable
        * ***home = %(base)/myappenv*** - it means that the home directory for the app is the virtual environment folder - myappenv
        * ***pythonpath = %(base)*** - it means that pythonpath is same as base path
        * ***socket = %(base)/socket.sock*** - it means that socket or connector file is socket.sock in base folder
        * ***chmod-socket = 777*** - it means that uWSGI has full permission of 777
        * ***processes = 8*** - it means that 8 process will be spawned to support multi processing
        * ***threads = 8*** - it means that 8 threads per process will be created 
        * ***harakiri = 15*** - it means that in 15 secs it will kill a thread which is error prone and create another thread
        * ***callable = flaskApp*** - it means that flaskApp is the callable app
        * ***logto = /var/www/html/products-restful/log/%n.log*** - it means that the log will be written in a file nwsgi.log
      * Copy the following content in the file and save -
        ```
        [uwsgi]
        base = /var/www/html/products-restful
        app = run
        module = %(app)
        home = %(base)/myappenv
        pythonpath = %(base)
        socket = %(base)/socket.sock
        chmod-socket = 777
        processes = 8
        threads = 8
        harakiri = 15
        callable = flaskApp
        logto = /var/www/html/products-restful/log/%n.log
        ```
      * Here is the snapshot:
        ![Install and configure uWSGI.ini](../images/002-012-InstallandconfigureuWSGIini01.png)

    * Step 4: ***Start and enable uwsgi service**:
      * execute -  ***sudo systemctl start  uwsgi_products_restful*** and then ***sudo systemctl enable uwsgi_products_restful***
      * Here is the code - 
        ```
        sudo systemctl start  uwsgi_products_restful
        sudo systemctl enable  uwsgi_products_restful
        sudo systemctl status  uwsgi_products_restful
        
        ```
      * Here is the snapshot - on how to enable it:
        ![Start and enable uwsgi_products_restfu service](../images/002-012-startandenable_uwsgi_products_restful.png)
      * Here is the snapshot - on what log to expect if it is a success enabling uwsgi:
        ![sucess enabling uwsgi_products_restfu service](../images/002-012-startandenable_uwsgi_products_restful_succeeded.png)


### Install and configure ***Nginx Proxy*** server Part 2:
  * Step 1: ***Setting up firewall and open SSH and HTTP ports***
    * Execute the commands as below to install and run ***firewalld***
      ```
      sudo ufw status
      sudo ufw allow 'Nginx HTTP'
      sudo ufw allow ssh
      sudo ufw allow https
      sudo ufw enable
      sudo systemctl reload nginx
      sudo systemctl status nginx
      ```
  * Step 2: ***Setup Serverblocks in Nginx - Create sites-available and sites-enabled symlinks***
    * The ***Serverblocks*** in Nginx help you create multiple websites under the site root.
    * The ***sites-available*** directory keeps all server block files 
    * The ***sites-enabled*** directory holds symbolic links to server blocks that neeeds to be published
    * Execute the below commands:(***if these folder dont exist then only***)
      ```
      sudo mkdir /etc/nginx/sites-available
      sudo mkdir /etc/nginx/sites-enabled
      ```
    * Edit nginx.conf file using command  - "sudo nano /etc/nginx/nginx.conf" and below code the end of the http {} block:
      ```
      include /etc/nginx/sites-enabled/*.conf;
      server_names_hash_bucket_size 64;
      ```
    * Create the file - ***sudo nano /etc/nginx/sites-available/products-restful.conf***
    * Copy and save the below content to the file - 
      ```
      server {
      listen 80;
      real_ip_header X-Forwarded-For;
      set_real_ip_from 127.0.0.1;
      server_name localhost;

      location / {
      include uwsgi_params;
      uwsgi_pass unix:/var/www/html/products-restful/socket.sock;
      uwsgi_modifier1 30;
      root /var/www/html/products-restful;
      }

      error_page 404 /404.html;
      location = /404.html {
      root /var/www/html;
      }
      
      error_page 500 502 503 504 /50x.html;
      location = /50x.html {
      root /var/www/html;
      }
      }
      ```
    * Update ***/etc/nginx/nginx.conf***
      * update the folwwoing '***/var/www/html***' with '***/var/www/html/products-restful**' and save
    * Now setup the ***symlink*** between - /etc/nginx/sites-available/products-restful.conf /etc/nginx/sites-enabled/
      ```
      sudo rm /etc/nginx/sites-enabled/default # disables default configuration
      sudo ln -s /etc/nginx/sites-available/products-restful.conf /etc/nginx/sites-enabled/ # enables our config using symlink
      ```
    * Also disable the default config in the NGinx config file - 
    * Reload and restart Nginx - ***sudo systemctl reload nginx*** and ***sudo systemctl restart nginx***
    * Here is the snapshot - :
        ![create symlinks](../images/002-012-createsymlinks.png)
    * Cha...cha,,, You are done, start testing....

### Testing the project (The Own Server End Point - ec2-3-210-120-130.compute-1.amazonaws.com/):
  * Now the project is ready for testing, you can repeat all the operations you tested in previous Heroku related exercise like register, login, add a product, update a product, delete a product, get one product, get all products. 
  * Since we did not change the existing functionality and just changed the deployment server from Heroku to our own server, it should work.
  * The screenshot for register user below:
  ![Register user](../images/002-12-registeruser.png)
  ---------------------------------------------------------------------------------
  * The screenshot for login user below:
  ![Login user](../images/002-12-loginuser.png)
  ---------------------------------------------------------------------------------
  
  * Once having done all tests, login to postgres database to verify the data.
  ![Verify data](../images/002-12-verifydata.png)
    ---------------------------------------------------------------------------------