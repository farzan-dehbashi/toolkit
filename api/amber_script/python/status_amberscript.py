import requests

url = "https://api.amberscript.com/api/jobs/status"

querystring = {"jobId":"6311250a2f1db60c30d535eb","apiKey":"26fe6e92ac6ec36f7cb5c311dd36436fd"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)
