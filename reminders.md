# postgressql

`sudo -u postgres psql
CREATE ROLE amukam WITH LOGIN PASSWORD 'loc';
psql -U amukam -d locsafedb`

\l

\dt



# Flask
pip3 install flask_sqlalchemy
pip install psycopg2-binary
curl http://127.0.0.1:5000/properties
curl -X GET http://127.0.0.1:5000/hello
curl -X POST http://127.0.0.1:5000/properties \
     -H "Content-Type: application/json" \
     -d '{"name": "John", "address": 30, "rent_amount": "50"}'