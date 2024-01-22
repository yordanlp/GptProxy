import os
from flask import Flask, request, jsonify
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import openai

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")

valid_vendors = ["VendorA", "VendorB", "VendorC"]

def validate_input(vendor, model_id, text):
    result = { 'is_valid': True, 'errors': [] }
    if vendor not in valid_vendors:
        result['is_valid'] = False
        result['errors'].append('The vendor provided is not valid')

    if model_id == None:
        result['is_valid'] = False
        result['errors'].append('Please provide a model')

    if len(text) > 200:
        result['is_valid'] = False
        result['errors'].append('The maximum lenght of the promt should not exceed 200 charachets')

    return result

@app.route('/chat', methods=['POST'])
def generate_text():
    data = request.json

    vendor = data.get('vendor')
    model_identifier = data.get('model_identifier')
    prompt_text = data.get('prompt_text')

    validation = validate_input(vendor, model_identifier, prompt_text)
    if( validation['is_valid'] == False ):
        return jsonify({"errors": validation['errors']}), 400

    llm = ChatOpenAI(openai_api_key=api_key, model_name=model_identifier)

    try:
        response = llm.invoke(prompt_text)
    except openai.APIError as error:
        return jsonify({"errors": [error.body]}), error.status_code
    except Exception as e:
        return jsonify({"errors": ["Something went wrong"]}), 500
    
    return jsonify({'data': response.content})

if __name__ == '__main__':
    app.run(debug=True)