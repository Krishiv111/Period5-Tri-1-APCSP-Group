import requests

url = "https://motivational-quotes1.p.rapidapi.com/motivation"

payload = {
	"key1": "value",
	"key2": "value"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "825200d0f8msh414d353da41bfcfp1ddcfcjsnb40ef386fce9",
	"X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)
random_quote = response.text
print(random_quote)