import json
import requests
token = "secret_xisVGUAj3HvxM5XSeYwpdFh1dHZK99Dvrf2Cd2OcpNO"
database_id = "python-9a26ff581763452d9544d7ab9082ee46"


def getMovies():
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    r = requests.post(url, headers={"Authorization": f"Bearer {token}","Notion-Version": "2021–08–16"})
    result_dict = r.json()
    print(result_dict)


getMovies()