import requests

url = "https://api.amberscript.com/api/jobs/status"

querystring = {"jobId":"62e96a8d2ba2ee71d3a6f0ac","apiKey":"26fe6e92ac6ec36f7cb5c311dd36436ff"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)
