import requests

url = "https://api.amberscript.com/api/jobs/export-srt"

querystring = {"jobId":"62ea86a460c0d9463c1197f8", "apiKey":"26fe6e92ac6ec36f7cb5c311dd36436ff"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)
