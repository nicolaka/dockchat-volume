##Dockchat
Dockchat is a simple Python+Mongo app built to demonstrate various Docker features. Dockchat-volumes demonstrates persistent data using a Data Volume Container ( dbdata in the docker-compose.yml). If you don't have docker-compose, install it with `pip install -U docker-compose`.

To run this app, simply run:

`dockchat# docker-compose build`

`dockchat# docker-compose up -d`

By default, this app will run on TCP port 5000. 


