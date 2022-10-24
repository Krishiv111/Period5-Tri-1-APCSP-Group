s_ff_user_structure = []

s_ff_user_structure.append({
    "Firstname": "",
    "Lastname": "",
    "Age": "",
    "Height": ""
})


# Main db of all users
ff_db = []
ff_db.append({
    "Firstname": "Dhruva",
    "Lastname": "Iyer",
    "Age": 15,
    "Height": 70
})

user0 = ({
    "Firstname": "Kanishka",
    "Lastname": "Iyer",
    "Age": 13,
    "Height": 50
})



# An API function that adds a new user to the db
def add_ff_user(new_user):
    ff_db.append(new_user)
    
add_ff_user(user0)

# An API function that removes an existing user from the db
# This is done by looking up their user ID
#def del_ff_user(new_user):
    #userid = new_user["ID"]
    #ff_db.remove(user)



length = (len(ff_db))
print(length)