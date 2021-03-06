# Deploying a Machine Learning Model on Heroku with FastAPI

Project from the ML DevOps Engineer Nanodegree of Udacity

## Project Description
This is a project to develop a classification model on publicly available Census Bureau data. 
The model is described in a model card.
Some unit tests have been created to monitor the model performance on various slices of the data. The model is deployed to Heroku using the FastAPI package and tested through API tests. Both the slice-validation and the API tests are incorporated into a CI/CD framework using GitHub Actions.
Finally, the dataset and model are updated are tracked with git and DVC.

## Request to the API
An example of querying the api is provided here:
```python
import requests

url = "https://app-fastapi-cicd.herokuapp.com/predict"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{ "workclass": "State-gov", "education": "Bachelors", "marital-status": "Never-married", "occupation": "Adm-clerical", "relationship": "Not-in-family", "race": "White", "sex": "Male", "native-country": "United-States" }'

response = requests.post(url, headers=headers, data=data)
pred = response.json()
```
## Ideas for improvement
- Re-organize each script to work as a class.
- Use codecov or equivalent to measure the test coverage.
- Implement FastAPI’s advanced features such as authentication.
- Create a front end for the API.
