
## About Pittsburgh Councilmatic  
  
[Pittsburgh Councilmatic](https://councilmatic.pittsburghpa.gov) helps you keep track of city representatives and their legislative activity.  
  
Councilmatic is an open-source tool that started as a Code for America project by Mjumbe Poe, who designed the earliest version for [Philadelphia](http://philly.councilmatic.org/). The civic technology company [DataMade](datamade.us) then implemented it in [New York City]([https://laws.council.nyc.gov/](https://laws.council.nyc.gov/)), [Chicago]([https://chicago.councilmatic.org](https://chicago.councilmatic.org/)), and [Los Angeles]([https://boardagendas.metro.net](https://boardagendas.metro.net/)).  

The project is written using Python's Django framework, and relies upon [the Open Civic Data specification]([http://docs.opencivicdata.org/en/latest/](http://docs.opencivicdata.org/en/latest/)), a standard for describing people, organizations, events, and bills. It uses web scrapers (housed in [a separate repository](https://github.com/opencivicdata/scrapers-us-municipal)) to pull data from [Legistar]([https://pittsburgh.legistar.com/Legislation.aspx](https://pittsburgh.legistar.com/Legislation.aspx)), Pittsburgh's legislative management software, before transforming it to  OCD format for consumption by the client application housed in this repository.

If you'd like to try adapting the project for another city, consult DataMade's [starter template]([https://github.com/datamade/councilmatic-starter-template](https://github.com/datamade/councilmatic-starter-template)) along with [the OCD scraper documentation]([http://docs.opencivicdata.org/en/latest/](http://docs.opencivicdata.org/en/latest/)).
  
## Getting started
  
### Install OS-level dependencies  
  
* Python 3.4+
* PostgreSQL 9.4+  
  
### Make a virtualenv and install Python dependencies  
  
We recommend using [virtualenv](https://virtualenv.readthedocs.io/en/latest/)  and  [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) for working in a virtualized development environment. Read about how to set up virtualenv [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/).  
  
Once you have virtualenvwrapper set up, enter the following in your terminal:  
  
```bash  
mkvirtualenv python=python3 councilmatic  
cd councilmatic-pittsburgh
workon councilmatic
pip install -r requirements.txt  
```  
  
Whenever you want to use this virtual environment again, run:  
  
```bash  
workon councilmatic  
```   
  
### Set up your database  
  
Before we can run the website, we need to create a database: 
  
```bash  
createdb pittsburgh_councilmatic
psql -d pittsburgh_councilmatic -c "create extension postgis"  
```  

Create the cache table:

```
python manage.py createcachetable
```  


Then, run migrations. (Be sure that you are working in the correct virtual environment.)  
  
```bash  
python manage.py migrate --fake-initial  
```  
  
Finally, create an admin user. Set a username and password when prompted.  
  
```bash  
python manage.py createsuperuser  
```  
  
  
## Import data from the Open Civic Data API  
  
The `import_data` management command populates bills, people, committees, and events via the OCD API. Run it with:
  
```bash  
python manage.py import_data  
```  
 You can explore the nitty-gritty of this code [here](https://github.com/datamade/django-councilmatic/blob/master/councilmatic_core/management/commands/import_data.py). The import may take a while, depending on data volume.
  
By default, the `import_data` command looks carefully at the OCD API; it's a smart management command. If you already have bills stored, it will not look at everything on the API; it will look at the most recently updated bill in your database, see when that bill was last updated on the OCD API, and then look through everything on the API from after that point. If you'd like to load things that are older than what you currently have loaded, you can run the import_data management command with a `--delete` option, which removes everything from your database before loading.  
  
## Running Councilmatic locally  
  
Now you're ready for action! To fire Councilmatic up locally, run:
  
``` bash  
python manage.py runserver  
```  
  
The site will be available at [http://localhost:8000/](http://localhost:8000/).  
  
## Configuring search  
  
Users can search bills on Councilmatic with query parameters. To power our searches, we use [Solr](http://lucene.apache.org/solr/), an open-source tool written in Java.  
  
**Requirements: Open JDK or Java**  
  
On Ubuntu:  
  
``` bash  
$ sudo apt-get update  
$ sudo apt-get install openjdk-7-jre-headless  
```  
  
On OS X:  
  
1. Download latest Java from  
[http://java.com/en/download/mac_download.jsp?locale=en](http://java.com/en/download/mac_download.jsp?locale=en)  
2. Follow normal install procedure  
3. Change system Java to use the version you just installed:  
  
 ```
 sudo mv /usr/bin/java /usr/bin/java16  
 sudo ln -s /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java /usr/bin/java
 ```
  
**Download & set up Solr**  
  
``` bash  
wget http://archive.apache.org/dist/lucene/solr/4.10.4/solr-4.10.4.tgz  
tar -xvf solr-4.10.4.tgz  
sudo cp -R solr-4.10.4/example /opt/solr  
  
# Copy schema.xml for this app to solr directory  
sudo cp solr_scripts/schema.xml /opt/solr/solr/collection1/conf/schema.xml  
```  
  
**Run Solr**  
```bash  
# Next, start the java application that runs solr  
# Do this in another terminal window & keep it running  
# If you see error output, somethings wrong  
cd /opt/solr  
sudo java -jar start.jar  
```  
  
**Index the database**  
```bash  
# back in the councilmatic directory:  
python manage.py rebuild_index  
```  
  
**OPTIONAL: Install and configure Jetty for Solr**  
  
Running Solr as described above is fine in a development setting. To deploy Solr in production, you'll want to use something like Jetty. Here's how you'd do that on Ubuntu:  
  
``` bash  
sudo apt-get install jetty  
  
# Backup stock init.d script  
sudo mv /etc/init.d/jetty ~/jetty.orig  
  
# Get init.d script suggested by Solr docs  
sudo cp solr_scripts/jetty.sh /etc/init.d/jetty  
sudo chown root.root /etc/init.d/jetty  
sudo chmod 755 /etc/init.d/jetty  
  
# Add Solr specific configs to /etc/default/jetty  
sudo cp solr_scripts/jetty.conf /etc/default/jetty  
  
# Change ownership of the Solr directory so Jetty can get at it  
sudo chown -R jetty.jetty /opt/solr  
  
# Start up Solr  
sudo service jetty start  
  
# Solr should now be running on port 8983  
```  
  
**Regenerate Solr schema**  
  
While developing, you may want to make changes to the fields being indexed; if so, you'll need to regenerate the  `schema.xml` file Solr uses to make its magic. That can be done via:  
  
```  
python manage.py build_solr_schema > solr_scripts/schema.xml  
cp solr_scripts/schema.xml /opt/solr/solr/collection1/conf/schema.xml  
```  
  
In order for Solr to use the new schema file, you'll then need to restart it.  
   
## Errors/Bugs  
  
If something is not behaving intuitively, it is likely a bug, and should be reported.  
Do so [here](https://github.com/cityofpittsburgh/councilmatic-pittsburgh/issues)! 
  
## Note on Patches/Pull Requests  
  
We welcome your ideas and feedback! Here's how to make a contribution:  
  
* Fork the project.  
* Make your feature addition or bug fix.  
* Commit (please be descriptive but concise).
* For pull requests that alter UI functionality, include a screen-capture gif demonstrating the new feature.  
* Submit the pull request. Bonus points for well-titled topic branches!  
  
## Maintainers
* [James O'Toole](https://github.com/jtotoole), Digital Services Developer - City of Pittsburgh

## Copyright  
  
Released under the [MIT License](https://github.com/datamade/councilmatic-starter-template/blob/master/LICENSE).