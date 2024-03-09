# NOTE: use access token for development purposes only
# pip install webexteamssdk

# webexteamssdk expects WEBEX_TEAMS_ACCESS_TOKEN in your environment
# export WEBEX_TEAMS_ACCESS_TOKEN
from webexteamssdk import WebexTeamsAPI

# search for people
for people in api.people.list(email=None, displayName=None, id=None, orgId=None, max=None):
    print(people)

# create a room aka space
api.rooms.create("Created from Python")

# invite someone to a room as a moderator
api.memberships.create("veryLongRoomIdString", personEmail="someone@example.com", isModerator=True)

# create a team
api.teams.create("I'm old enough to think it's funny to call this team THE A-TEAM")

# check team memberships
for member in api.team_memberships.list("veryLongTeamIdString"):
    print(member)

# send a message to a room or person
api.messages.create(roomId=None, toPersonEmail=None, text="message here")
for message in api.messages.list(roomId="veryLongRoomId"):
    print(message)
