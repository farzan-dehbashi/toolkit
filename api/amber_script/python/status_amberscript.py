import requests

url = "https://api.amberscript.com/api/jobs/status"

querystring = {"jobId":"6333161a4383511659b838ee","apiKey":"26fe6e92ac6ec36f7cb5c311dd36436fd"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)
