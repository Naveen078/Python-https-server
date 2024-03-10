# Python-https-server
Python https server

Generate SSL certificate and key

$ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"

Run server:

$  python3 https.py

Server will start at port 8002
