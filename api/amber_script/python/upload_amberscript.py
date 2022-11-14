import requests

url = 'https://api.amberscript.com/api/jobs/upload-media'
# url = "https://httpbin.org/post"
<<<<<<< HEAD
filepath = "music.mp3"
=======
filepath = "broadcast_264059.mp4"
>>>>>>> ac295a94faef9ed69e353ca4bd06751128c41820
querystring = {"jobType":"direct","language":"fi","transcriptionType":"transcription",
"apiKey":"26fe6e92ac6ec36f7cb5c311dd36436fd"}
files = {'file': open(filepath, 'rb')}

response = requests.post(url, files=files, verify=False, params=querystring)

print(response.status_code)
print(response.text)
