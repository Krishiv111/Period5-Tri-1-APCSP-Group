import random

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

random_team_member = getRandomTeamMember()
print(random_team_member)