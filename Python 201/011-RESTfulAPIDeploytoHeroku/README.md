### How to deploy RESTful APIs in the Cloud:
  * To test our Flask app locally we normally run - ***python app.py*** and test the APIs in postman
  * But this is not an efficient way of testing the APIs 
  * ***Issues***:
    * We cant test if the application is scalable to handle more load
    * The local testing is a non-prod enviroment testing
    * You can't share your APIs to the world
  * ***Solution***:
    * Deploy the application in a cloud environment
      * You have to deploy your app to a PAAS(Platform as a service) where developers can build, deploy, run, test their apps
      * ***Heroku Cloud*** - uses Dyno similar to a VM to deploy apps and does much more
      * ***AWS Cloud*** - use EC2 instances(VMs), Serverless, API Gateway, ECS(Container), EKS(Kubernetes) to deploy apps
      * ***Azure Cloud*** - uses VMs and Azure functions, Container and Kubernetes services to deploy apps
      * ***Google Cloud*** - uses VM instances, Cloud Functions, Container and Kubernetes engine to deploy apps 

### How to deploy RESTful APIs t the Heroku Cloud:
  * Heroku uses VMs called as **Dyno*** where you can build, deploy and run your apps
  * Please do the following steps to deploy your Flask app to Heroku:
  * Step 1 : ***Push your Flask app to a public respository - E.g. GitHub, BitBucket etc *** - 
    * Let us prepare our flask app to first be pushed to GitHub(you must have an account, if not register - ***https://github.com/join***) 
    * First lets copy all the files from last exercise from folder - ***010-RESTfulAPIUsingSQLAlchemywithRelationships**  to a new folder ***011-RESTfulAPIDeploytoHeroku***  
    * We will use it as our app to deploy to Heroku
    * Go to the folder 011-RESTfulAPIDeploytoHeroku in command line and execute - ***git init*** (commands git that current folder is version controlled)
    * ***Prepare*** required files for deployment purpose - follwing 4 additional files are needed 
      * ***runtime.txt*** - holds the value of the runtime application - in our case - ***python-3.5.2**
      * The code for runtime.txt:
        ```
        python-3.5.2
        ```
      * ***requirements.txt*** - holds the values for the packages needed by the  application
      * The code for requirements.txt:
        ```
        Flask
        Flask-RESTful
        Flask-JWT
        Flask-SQLAlchemy
        uwsgi
        psycopg2
        ```
      * ***uwsgi.ini*** - holds the values for the effeciently running our app
      * ***http-socket = :$(PORT)*** instructs to get the port from the app port
      * ***module = run:app** instructs ro run app app.py
      * The code for uwsgi.ini:
        ```
        [uwsgi]
        http-socket = :$(PORT)
        master = true
        die-on-term = true
        module = run:app
        memory-report = true
        ```
      * ***Procfile*** - holds the info for start point for running our app
      * ***web: uwsgi uwsgi.ini*** instructs to run the uwsgi runtime with uwsgi.ini info
      * The code for Procfile:
        ```
        web: uwsgi uwsgi.ini
        ```
      * ***.ignorefile*** - ignores any file which you dont want to push while committing
      * You are instructing git to ignore any .pyc(python compile files, __pychache__folder, and jypyter folders if you have used any and any .DS_Store folders if you are on mac)
      * The code for .ignorefile:
        ```
        __pycache__/
        .ipynb_checkpoints/
        .DS_Store
        *.pyc
        ```
    * Once your flask aspp files and these above 4 files are ready then execute - ***git add --a*** - you are instructing git to add all the files to the staging areas of the git on yr local machine
    * Now commit your changes with a nice commit message - ***git commit -m "Initial commit for Flask app and required files for Heroku deployment"***
    * Now push your changes to GitHub respository( in my case ***https://github.com/naeemmohd/python.git***)
    * if you have not created a repository then from the logged in GitHbb Dashboard 0 use "New Repository" option to create a respository 
    * Once the GitHub repository is created, execute the command
      * ***git push origin add https://github.com/naeemmohd/python.git*** - you are instructing Git to add a remote GitHub repository for your local repository 
      * ***git push -u orgin master*** - you are instructing Git to now finally push your changes in the local master branch to the upstream origin branch
    * Finally check if all your lacal changes are now pushed to GitHub repository
    * This respository is public and other developers can see and collaborate with you.
      

  * Step 2 : ***Create an account in Heroku Cloud*** - 
    * Use the following link to sign on and then login to the Heroku Dashboard
      * ***https://signup.heroku.com/*** - to sign on and login to Heroku Dashboard
    * The screenshot below:
      ![Create ](../images/002-011-herokusignonandlogin.png)
      ---------------------------------------------------------------------------------

  * Step 3 : ***Create *** - 
    * The 
    * Please see code below -
      ```
      ```
    * The screenshot below:
      ![Create ](../images/002-011-create.png)
      ---------------------------------------------------------------------------------
 
### Testing the project:
  * Now the project is ready for testing, you can repeat all the operations you tested in previous exercise like register, login, add a product, update a product, delete a product, get one product, get all products. 
  * Since we did not change the existing functionality and just injected the ORM functionality to the app, it should work.
  * The screenshot for register user below:
  ![Register user](../images/002-11-registeruser.png)
  ---------------------------------------------------------------------------------
  * The screenshot for login user below:
  ![Login user](../images/002-11-loginuser.png)
  ---------------------------------------------------------------------------------
  * The screenshot for POST category below:
  ![POST Category](../images/002-11-postcategory.png)
  ---------------------------------------------------------------------------------
  * The screenshot for POST product below:
  ![POST Product](../images/002-11-postproduct.png)
  ---------------------------------------------------------------------------------
  * The screenshot for PUT Category below:
  ![PUT Category](../images/002-11-putcategory.png)
  ---------------------------------------------------------------------------------
  * The screenshot for PUT Product below:
  ![PUT Product](../images/002-11-putproduct.png)
  ---------------------------------------------------------------------------------
  * The screenshot for GETCategory below:
  ![GET Category](../images/002-11-getcategory.png)
  ---------------------------------------------------------------------------------
  * The screenshot for GETProduct below:
  ![GET Product](../images/002-11-getproduct.png)
  ---------------------------------------------------------------------------------
  * The screenshot for GET All Categorys below:
  ![GET All Categorys](../images/002-11-getallcategory.png)
  ---------------------------------------------------------------------------------
  * The screenshot for GET All Products below:
  ![GET All Products](../images/002-11-getallproducts.png)
  ---------------------------------------------------------------------------------
  * The screenshot for DELETE Product below:
  ![DELETE Product](../images/002-11-deleteproduct.png)
  ---------------------------------------------------------------------------------
  * The screenshot for DELETE Category below:
  ![DELETE Category](../images/002-11-deletecategory.png)
  ![DELETE Category Cascade](../images/002-11-deletecategoryimpact.png)
  ---------------------------------------------------------------------------------