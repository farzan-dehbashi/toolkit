import requests

url = "https://api.amberscript.com/api/jobs/export-srt"

querystring = {"jobId":"62c447275e35744086521521", "apiKey":"26fe6e92ac6ec36f7cb5c311dd36436fd"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)
