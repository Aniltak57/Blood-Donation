import requests

response = requests.post("http://127.0.0.1:7860/run/predict", json={
	"data": [
		["itching"],
	]
}).json()

data = response["data"]