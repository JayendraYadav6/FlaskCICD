from flask import Flask
import boto3
import requests
 
app=Flask(__name__)
@app.route("/")
def home():
    return"hello This is your buddy jayendra "
 
if __name__ =="__main__":
  app.run(host="0.0.0.0" ,port=5002)
