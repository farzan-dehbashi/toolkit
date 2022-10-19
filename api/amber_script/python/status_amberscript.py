import requests

url = "https://api.amberscript.com/api/jobs/status"

querystring = {"jobId":"6339f0ab59a9983d2fb6e101","apiKey":"26fe6e92ac6ec36f7cb5c311dd36436fd"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)
