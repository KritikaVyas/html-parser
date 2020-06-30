# HTML Parser  - Parse the information of the Buyer/Sellers from an email in html format and extract useful information such as name, mobile number etc.
## Requirements

### Basic
* Python 3.6 (should work with Python3.x, although it has not been tested)
* [virtualenv](https://virtualenv.pypa.io/en/stable/installation.html)
* [Docker](https://docs.docker.com/engine/install/ubuntu/) 19.03.8 
* docker-compose 1.24.1
## Install
In project root directory
Run: 
```
python3 src/htmlparser.py
```


#Deployment
In `deploy/systemd/html-parser.service`, customise

```
After=<PATH_TO_DOCKER>.service
Requires=<PATH_TO_DOCKER>.service
WorkingDirectory=<PREFERRED_WORKING_DIRECTORY>
ExecStart=<PATH_TO_DOCKER_COMPOSE_EXECUTABLE> up
ExecStop=<PATH_TO_DOCKER_COMPOSE_EXECUTABLE> down
ExecReload=<PATH_TO_DOCKER_COMPOSE_EXECUTABLE> up
```

In `deploy/nginx/html-parser`, customise
```
server-name
Install certbot certificate and include the relevant certificate path based on server-name
```

#Setup
```
sudo cp deploy/systemd/html-parser.service /etc/systemd/system/
sudo systemctl enable html-parser.service
sudo cp deploy/config.env .
sudo cp deploy/nginx/html-parser
```

Server Logs can be checked using 
```
sudo journalctl -f -u html-parser.service
```

# Deploy

- Ensure that `DEBUG = False` in settings.py
- Launch `sudo systemctl restart html-parser.service`

# Know Issues
- Html parser will support similar cases as sample template. For any new templates the logic would change slightly