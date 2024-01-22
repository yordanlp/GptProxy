from flask import Flask, request, jsonify
from dotenv import load_dotenv

from LLMClients.LLMClientFactory import LLMClientFactory

load_dotenv()

app = Flask(__name__)

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

    client = LLMClientFactory.CreateClient("OPEN_AI", {"model_name": model_identifier})

    response = client.query(prompt_text)

    try:
        response = client.query(prompt_text)
    except Exception as e:
        return jsonify({"errors": ["Something went wrong"]}), 500
    
    if len(response.errors) > 0:
        return jsonify({"errors": response.errors}), response.status_code
    
    return jsonify({'data': response.content})

if __name__ == '__main__':
    app.run(debug=True)
