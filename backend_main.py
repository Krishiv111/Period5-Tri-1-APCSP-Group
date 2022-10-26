import requests

url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"

querystring = {"muscle":"biceps"}

headers = {
	"X-RapidAPI-Key": "825200d0f8msh414d353da41bfcfp1ddcfcjsnb40ef386fce9",
	"X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response_text = (response.text)
print(response_text)