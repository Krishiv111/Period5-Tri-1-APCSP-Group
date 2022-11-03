import random, requests, json

url = "https://quotsy.p.rapidapi.com/author/dalai%20lama/page/2/index.json"

response = requests.request("GET", url)
output = json.loads(response.text)
print(response.text)

team_db = []
team_names = []
team_roles = []

team_db.append({
	"Name": "Dhruva",
	"Role": "Backend Developer"
})

team_db.append({
	"Name": "Krishiv",
	"Role": "Scrum Master"
})

team_db.append({
	"Name": "Prasith",
	"Role": "Frontend Developer"
})

team_db.append({
	"Name": "Advay",
	"Role": "Frontend Developer"
})

team_db.append({
	"Name": "Shivansh",
	"Role": "Dev Ops"
})

for person in team_db:
	name = person["Name"]
	role = person["Role"]
	team_names.append(name)
	team_roles.append(role)

def getRandomTeamMember():
    return(random.choice(team_db))


#print(random_team_member)