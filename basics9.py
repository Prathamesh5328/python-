# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
def get_last_name(): 
    return actor["name"].split()[1]

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
 

#this is the practice done to revise the context 
actor2 = {"name": "John Cleese keote", "rank": "awesome"}

def last_name():
    return actor['name'].split()[2]

print('the last name of the given first name was %s' %(last_name()))

