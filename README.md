Repozitorijs programmas kodam informācijas iegūšanai no NASA API par asteorīdiem, saglabāšanai datubāzē (optional - izvietošanai Twitter).

To run the app, it requires a valid config and logging config file. You can use the templates, but update them with your settings (at least api key).

cp config.ini.template config.ini
cp log_worker.yaml.dev log_worker.yaml
cp log_migrate_db.yaml.dev log_migrate_db.yaml

open config.ini and set at least the nasa API key and the MYSQL DB parameters

------------------------------------------
Configuration file parameters:

[nasa]
user_api_key = API key used to request data from NASA asteroid API. You can request your own key on: https://api.nasa.gov/
api_url = API URL to send requests to. Default -> https://api.nasa.gov/neo/

[mysql_config]
mysql_host = 127.0.0.1
mysql_db = DB name
mysql_user = DB user
mysql_pass = DB user password

[twitter]
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

Data structure description:
ast_hazardous and ast_safe

[
	[
		0 - Name of asteroid;
		1 - URL to asteroid description;
		2 - Min diameter;
		3 - Max diameter;
		4 - TS of close approach
		5 - Date and time of close approach in UTC time zone;
		6 - Date and time of close approach in local time zone;
		7 - Speed of asteroid
		8 - Miss distance of asteroid
		9 - asteroid id from nasa
		10 - time of close approach in UTC

	],
	[

	]
]
