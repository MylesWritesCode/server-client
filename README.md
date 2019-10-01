# Overview
This project will use a pre-existing backend and attempt to create the
client-side frontend for users. In total, three servers will be running:
1. MongoDB server
2. Python3 pymongo server (API for DB)
3. Angular server (client for frontend)

# Server Instructions
### Requirements
- Python3 (3.7.3 used in development)
- pymongo
- MongoDB installed
* * *
The datastore server connects to MongoDB that is already filled with data. To
populate the database, make sure MongoDB is installed and perform the following
commands in terminal from the server-client folder:

```
cd backend/data
// The following line will import our stock data into MongoDB.
mongoimport --db market --collection stocks stocks.json

// Ensure pymongo is installed
pip install pymongo
cd ../stocks/server
python3 server.py
```

Once you're done with this, MongoDB should have all the data, and our backend
server should be running. 


# Frontend Instructions
### Requirements
- Angular 7
* * *
The client server will be opened in another termianl window. Open the frontend
folder in terminal then do the following:

```
npm install
ng serve
```

Once this is done, you should be able to go to localhost:4200 in your browser
to view the data from the backend server.

* * *