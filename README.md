# Cleo Api Project

This is project created with fpython flask in purpose of an application

## Getting Started

### Requirements
* It make it easier to run the application on pycharm or on intellij, because of the dependencies
* Be sure about your python version 3.10 and above
* Be sure about to install the dependencies before

First, for starting of the server please install the dependencies 
```bash
pip install -r requirements.txt
```
and run the following code in your terminal:
```bash
python3 app.py
```
or when you are in pycharm, just click on the run button inside app.py

Open [http://localhost:4000] with your browser and you can login yourself
Or just call the api endpoints within postman. There is a list of the api down here.

#### Before you start create a user for yourself to login and use the api. You can do that with `/auth/register`

### Project Structure
+ `/database` here you will find an instance of the database. (SQLite)
+ `/models` here are the classes which are used for the instances
+ `/routes`there are the routes and the whole api endpoints
+ `/templates` here are the html files for the web version
+ `/utlis` there you will find the instance of the jwt db

### Endpoints and the body you want for the call
+ `/auth/register` to register and create an account [POST]
```bash
{
    "username": "your username",
    "password": "your password"
}
```
+ `/auth/login` to login with your account [POST]
```bash
{
    "username": "your username",
    "password": "your password"
}
```
+ `/contracts/all_contracts` to see the whole contracts [GET, Token required]
+ `/contracts/add_contract` to post a contract [POST, Token required]
```bash
{
    "contract_id": contract_id,
    "contract_name": "contract_name",
    "customer_id": customer_id
}
```
+ `/customers/${customerID}/contracts` to get contracts by customer id [GET, Token required]
+ `/customers/${customerID}/contracts/${contractID}` to get a specific contract by contract id and customer id [GET, Token required]
+ `/customers/${customerID}/contracts/${contractID}` to update a specific contract by contract id and customer id [PUT, Token required]
```bash
{
    "contract_name": "contract_name",
    "customer_id": customer_id
}
```

And now just have fun with it and I'm exited about your feedback :)