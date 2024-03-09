# NOTE: use access token for development purposes only
import os, requests

AUTH_STRING = str("Bearer " + os.environ["WEBEX_DEV_TOKEN"]) # bash export!
GET_HEADER = {"Authorization": AUTH_STRING, "Accept": "application/json"}

POST_HEADER = {"Authorization": AUTH_STRING,
    "Content-Type": "application/json"}
CREATE_ROOM_URL = "https://webexapis.com/v1/rooms"
# if room data specifies teamId or classificationId these must be valid
POST_ROOM_DATA = '''{
  "title": "room1",
  "isLocked": false,
  "isPublic": false,
  "description": "I'm hereby creating this Webex Room",
  "isAnnouncementOnly": false
}'''
 

def main():
    cr = requests.post(CREATE_ROOM_URL, headers=POST_HEADER,
        data=POST_ROOM_DATA)

    org_r = requests.get("https://webexapis.com/v1/organizations",
    headers=GET_HEADER)
    print("Number of Webex orgs received from GET request: " +
        str(len(org_r.json()['items'])))

    list_of_org_dicts = org_r.json()['items']
    #for org in list_of_org_dicts:
    #    for all_keys, all_values in org.items():
    #        print(f"{all_keys}: {all_values}")

    print("'NAME: ID' of all Webex orgs received from GET request:")
    for i in range(len(list_of_org_dicts)):
        print(list_of_org_dicts[i]['displayName'] +
            ": " + list_of_org_dicts[i]['id'])

if __name__ == "__main__":
    main()
    print("Script ran standalone and was not imported.")
