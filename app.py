import os
from dotenv import load_dotenv, find_dotenv
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS


load_dotenv(find_dotenv()) # load the environment variables from the .env file (which is not included in the repo for security reasons)
openai.api_key = os.getenv("OPENAI_API_KEY") # get the API key from the .env file

def main():
    
    app = Flask(__name__)
    CORS(app)

    @app.route('/test', methods=['GET'])
    def test():
              return jsonify({
                "message" : "Hello World"
              })

    @app.route('/api', methods=['POST'])
    def gpt3():
          data = request.get_json(force=True) # get the data from the request (the data is in JSON format) 
          message = data['message'] 
          response = openai.Completion.create(
          model="text-davinci-003",
          prompt=message,
          max_tokens=3000,
          temperature=0.9,
          )
          print (response.choices[0].text)
          # send back the response to the client
          return jsonify({
            "message" : response.choices[0].text,
            "created" : response.created
            })
              
    return app      
              
if __name__ == '__main__': 
         from waitress import serve
         app = main()
         app.run( host='0.0.0.0',port=8000)
        # localhost:8000/api
        # Path: python/requirements.txt
        # openai==0.2.0
        # flask==1.1.2
    

    
  
