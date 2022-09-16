import requests

url = "https://api.amberscript.com/api/jobs/export-srt"

querystring = {"jobId":"630d0937051b936b5d803c40", "apiKey":"26fe6e92ac6ec36f7cb5c311dd36436fd"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)
