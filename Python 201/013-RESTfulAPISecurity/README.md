### How to secure and speed up your RESTful APIs:
  * ***Issues***: 
    * Till now we have deployed our RESTful API to Heroku as well as our own custom servers.
    * While during Heroku deployement we saw that the main control on how the it runs is dependent on Heroku
    * On the other side, when we deployed on our own servers, we had a better control on how to deploy and what feature to enable or disable.
    * But still in both case, there are few issues, which should be resolved to make our RESTful API perform better.
      * The HTTPS is still disabled, thus there is no SSL based security - we will install and configure ***SSL certificates*** for this purpose.
      * The RESTful API is still not effeciently cached on renowned CDN servers like ClocuFront, CloudFlare etc - we will Configure ***CloudFlare*** for this purpose.
      * It is still having a long and custom name as confifured by the cloud provider, no domain is registered - we will ***register a domain*** on GODaddy.com.
  * ***Solution***
    * Install and configure ***SSL certificates*** for security.
    * Configure ***CloudFlare*** for caching, security, Denial of service attacks.
    * ***Register a domain*** for proper nomenclature.

### How does the DNS(Domain Naming System) works?:
  * DNS is a way to trnslate the string based domain name to the actual IP of the server.
  * This request is resolved with something called as DNS Query.
  * The snapshot below explain the flow:
    * First of all the client/browser sends a request to view a website e.g. "***www.mohdnaeem.com***"
      * ***Root Server*** - is manage by internet data providers as harcoded list of servers
        * Root servers returns with the info that it does not know the IP of "www.mohdnaeem.com" but knows the servers which maintain .com domains
        * The browser now requests the TLD server
      * ***TLD Server*** - manage a list of specific domain of servers maintained by specific organizations
        * TLD Server returns with the info that it does not know the IP of "www.mohdnaeem.com" but knows the servers which actually holds the address of your server
        * The browser now requests the Name server  
      * ***Name Server*** - is manage by domain registrars and other specific organizations
        * Name Servers now returns with the actual IP of "www.mohdnaeem.com" and that server is then requsted with the page
        * The browser then displays that page
    * ![How DNS works](../images/002-13-howdnsworks.png)

### Using a ***Registered domain*** to access the RESTfulAPI(Configure GoDaddy and CloudFlare): 
  * ClodFlare is is a renowned CDN service similar like CloudFront in AWS which helps caching data, pages, images etc,
  * In a Content Delivery Network(CDN), the data is pulled from the neearest edge location and cached till the TTL is exipred,
  * TTL is Time To Live, once this is expired, the fresh data is pushed from the origin location.
  * To register or login to CloudFlare, please use link - ***https://dash.cloudflare.com/sign-up*** or ***https://dash.cloudflare.com/login***
  * Once registered and logged in, you will be prompted to add the website(the IP address or DNS name of the domain we purchased - e.g ***ecloudwiz.com***)
    ![add a website to cloudflare](../images/002-13-addawebsite-1.png)
  * CloudFlare then connects to check the details of the domain name and prompts with details about how to configure the name servers in the domain registrar(GoDaddy.com for me) to get connected to CloudFlare:
    ![name server settings](../images/002-13-nameserversettings.png)
  * Now go to the domain registrar page(For me www.godaddy.com) and selected the domain we registretd and then choose option "Manage Domain"
    ![manage domain settings](../images/002-13-managedomainsettings.png)
  * Now update the Nameserver 1 and 2 with the nameservers provided by CloudFlare in the previous steps.
    ![update nameserver settings](../images/002-13-updatenameserversettings.png)
  * Now go to the CDN(CloudFlare here) dashboard and select the website and then ***"DNS" settings***:
    * Enter a 'A' recrod and a CNAME record as shown in the snapshot and explained below
    * The DNS Listing contains a mapping on how to reach your website using A records and CNAME records
      * ***A*** Record - maps the your domians root DNS with the IP address of the server where your app is deployed.(We have deployed it in ***mnaeemsiddiqui3c.mylabserver.com***)
      * The Public IP of the server  - mnaeemsiddiqui3c.mylabserver.com is as in the snapshot(can change)
        ![Public IP of Server](../images/002-13-PublicIPofServer.png)
      * ***CNAME*** Record - maps an ALIAS e.g. if a user types "www.ecloudwiz.com" instead of "ecloudwiz.com"
      * ***AAAA*** Record(future) - maps the your domians root DNS with the DNS of the Named servers with IP6 protocol
    ![DNS List settings](../images/002-13-dnslistsettings.png)

### Testing the project (The Own Server End Point - ***ecloudwiz.com***):
  * Now the project is ready for testing, you can repeat all the operations you tested in previous Heroku related exercise like register, login, add a product, update a product, delete a product, get one product, get all products. 
  * Since we did not change the existing functionality and just changed the security through domain registration, certificate installation and HTTPs enabling.
  * The screenshot for register user below:
  ![Register user](../images/002-13-registeruser.png)
  ---------------------------------------------------------------------------------
  * The screenshot for login user below:
  ![Login user](../images/002-13-loginuser.png)
  ---------------------------------------------------------------------------------
  * The screenshot for products and categories below:
  ![Products and Categories](../images/002-13-productsandcategories.png)
  ---------------------------------------------------------------------------------
  * The screenshot of the traffic through Cloudflare:
  ![Traffic through Cloudflare](../images/002-13-TrafficthroughCloudflare.png)
  ---------------------------------------------------------------------------------