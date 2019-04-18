### How to deploy RESTful APIs on your own Servers:
  * ***Issue***: 
    * The Heroku deployment was quite seam less, but also restricted too. There were multiple reasons-
      * no complte control on the deployment servers
      * handling scalability by spawning more processes and threads not in our control
      * Setting up the caching was also not in our control
  * ***Solution***
    * Deploy the RESTful API on your own server in cloud- AWS, Azure, Google, DigitalOcean cloud etc
    * We will deploy the RESTful API on a newly provisioned Linux Server - Red Hat Liniux - RHEL 7 - where will install and configure the following:
      * Setting up the server with ***users, security, firewall*** settings
      * Install and configure ***Postgres*** SQL Database:
      * Install and configure ***Nginx Proxy*** server( a web server, reverse proxy, load balancer, HTTP cache handler etc)
      * Install and configure ***uWSGI***(Web Service Gateway Interface)

### Setting up the server with ***users, security, firewall*** settings
  * Provisioning a server -
    * I am setting up a server on my labserver account in LinuxAcademy, but you can use AWS, Azure, Google, DigitalOcean clouds or any other public cloud provider.
    * You can setup a 'Red Hat Enterprize Linux(RHEL 7)' server with a ***EC2 instance*** in ***AWS***, a ***VM instance*** in ***Azure or Cloud*** or a ***Droplet*** in ***Digital oceans***
    * Basically these are nothing but a Virtual Machine server on the specific cloud services provider
    * Also you can setup your RESTful API on any LINux server ( any ***Ubuntu based system*** e.g. Ubuntu, Mint, LinuxLite etc or ***CentOS based systems*** like CentOS, RHEL etc)
    * I am using a medium sized server - ***2 Virtual CPUs with 4GB memory and 8 GB hard disk space*** - you can use even a small sized server for testing - ***1 Virtual CPUs with 1GB memory and 4 GB hard disk space***
    * Please follow the steps below for provisioning the server:

    * Step 1: ***Setup thes server***
      * Once the server is provisioned then ***SSH to the server***,  ***set privileges to root user***,  ***update the server***, ***install git, tree, nano packages*** - 
      ```
      # ssh <user_name>@<the server ip> - for me the server is 'mnaeemsiddiqui1c.mylabserver.com' and the user is 'cloud_user'
      ssh cloud_user@mnaeemsiddiqui1c.mylabserver.com   # This line will prompt you for entering password and login you to the server as 'cloud_user'
      sudo su  # This line will set root privileges
      yum -y update   # this updates the server with latest packages - in Ubuntu based system you  may use apt-get -y update 
      yum -y install git tree nano   # installs git, tree, nano packages
      ```

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

    * Step 3: ***Enabling SSH permissions for the Linux user***
      * Execute the code - ***nano /etc/ssh/sshd_config*** - this will open the sudoers file - add the line below at the end of the file
        ```
        AllowUsers cloud_user
        ```
      * Here is the snapshot:
        ![Enable SSH permission to the Linux User](../images/002-012-enablesshpermissionforlinuxuser.png)  
      * Reload the SSH service due to this new change - execute - ***service sshd reload*** 

### Install and configure ***Postgres*** SQL Database:
  * Please follow the steps below for setting up the database:

    * Step 1: ***Install Postgres***
      * Please use the following command - (for Ubuntu based system , use apt-get instead of yum)
        ```
        yum -y install postgresql postgresql-server postgresql-contrib
        postgresql-setup initdb
        systemctl start postgresql
        systemctl enable postgresql
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
      * Please use the following command - Please update the following line in the Postgres configuration file at location - ***/var/lib/pgsql/data/pg_hba.conf** 
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

### Install and configure ***Nginx Proxy*** server:
  * Upcoming 

### Install and configure ***uWSGI**:
  * Upcoming

### Testing the project (The Own Server End Point - http://mnaeemsiddiqui1c.mylabserver.com/):
  * Now the project is ready for testing, you can repeat all the operations you tested in previous Heroku related exercise like register, login, add a product, update a product, delete a product, get one product, get all products. 
  * Since we did not change the existing functionality and just changed the deployment server from Heroku to our own server, it should work.
  * The screenshot for register user below:
  ![Register user](../images/002-12-registeruser.png)
  ---------------------------------------------------------------------------------
  * The screenshot for login user below:
  ![Login user](../images/002-12-loginuser.png)
  ---------------------------------------------------------------------------------
  * The screenshot for POST category below:
  ![POST Category](../images/002-12-postcategory.png)
  ---------------------------------------------------------------------------------
  * The screenshot for POST product below:
  ![POST Product](../images/002-12-postproduct.png)
  ---------------------------------------------------------------------------------
  * The screenshot for PUT Category below:
  ![PUT Category](../images/002-12-putcategory.png)
  ---------------------------------------------------------------------------------
  * The screenshot for PUT Product below:
  ![PUT Product](../images/002-12-putproduct.png)
  ---------------------------------------------------------------------------------
  * The screenshot for GETCategory below:
  ![GET Category](../images/002-12-getcategory.png)
  ---------------------------------------------------------------------------------
  * The screenshot for GETProduct below:
  ![GET Product](../images/002-12-getproduct.png)
  ---------------------------------------------------------------------------------
  * The screenshot for GET All Categorys below:
  ![GET All Categorys](../images/002-12-getallcategory.png)
  ---------------------------------------------------------------------------------
  * The screenshot for GET All Products below:
  ![GET All Products](../images/002-12-getallproducts.png)
  ---------------------------------------------------------------------------------
  * The screenshot for DELETE Product below:
  ![DELETE Product](../images/002-12-deleteproduct.png)
  ---------------------------------------------------------------------------------
  * The screenshot for DELETE Category below:
  ![DELETE Category](../images/002-12-deletecategory.png)
  ---------------------------------------------------------------------------------