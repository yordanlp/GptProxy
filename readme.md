## Installation 
This section provides step-by-step instructions on how to set up the application on your local machine.

### Requirements:
 - Python 3.x
 
 #### Step 1:
 ```
 cd ./GptProxy
 ```

 #### Step  2: Create a virtual environment
 ```
python3 -m venv env
 ```
 
 #### Step  3: Activate the virtual environment
 ```
source ./env/bin/activate
 ```

 #### Step  4: Install the dependencies
 ```
pip install -r requirements.txt
 ```

 #### Step  5: Configure the environment variables
 ```
create a copy of .env.example file and rename it to .env and fill it with your OpenAI Api Key
 ```

 #### Step  7: Run the application
 ```
./env/Scripts/python.exe run.py
 ```
---

Now you will be able to make a POST request to [http://127.0.0.1:5000/chat]() with the following body

```
{
    "vendor": "VendorA",
    "model_identifier": "gpt-3.5-turbo-0301",
    "prompt_text": "Hi"
}
```
 
And get a response like 
```
{
    "data": "Hello! How can I assist you today?"
}
```

if you make a validation error or provide an invalid parameter for OpenAI api your response will be like 

```
{
    "errors": [
        "The vendor provided is not valid"
    ]
}
```

or

```
{
    "errors": [
        {
            "code": "model_not_found",
            "message": "The model `my_model` does not exist",
            "param": null,
            "type": "invalid_request_error"
        }
    ]
}
```

## Author

- [@yordanlp](https://www.github.com/yordanlp)