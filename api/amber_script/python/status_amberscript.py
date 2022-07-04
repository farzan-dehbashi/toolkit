import requests

url = "https://api.amberscript.com/api/jobs/status"

querystring = {"jobId":"62c31f2dc168d83541d4d4b7","apiKey":"26fe6e92ac6ec36f7cb5c311dd36436fd"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)
