from flask import Flask,jsonify
import redis
import threading
import json
from dotenv import load_dotenv
import os
load_dotenv() 

app = Flask(__name__)
redis_client = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"))
#redis_client = redis.Redis(host='localhost', port=6379)



#route for presenting the results list in redis
@app.route('/')
def home():
    result_list = []
    while redis_client.llen('results'):
        result_data = redis_client.rpop('results')
        if result_data:  
            # deserialized the json string data 
            decentralized_data = json.loads(result_data.decode('utf-8'))
            print(decentralized_data)
            result_list.append(decentralized_data)
    return jsonify(result_list)



if __name__ == '__main__':
    app.run(debug=True)