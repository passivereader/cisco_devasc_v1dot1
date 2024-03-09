#! /path/to/venv python
# pip install dnacentersdk

import pprint
from dnacentersdk import DNACenterAPI

# among others dnacentersdk reads the following env vars by default
# export DNA_CENTER_ENCODED_AUTH="base64encoded user SPACE pw"
# export DNA_CENTER_BASE_URL="https://sandbox.example.com/"

def main():
    apiobject = DNACenterAPI() # self-signed cert? BASE_URL verify = False!

    devices = apiobject.devices.get_device_list()

    for device in devices.response: # note the dot notation
       print(f"Hostname/Type/Uptime: {device.hostname} / {device.type} / {device.upTime}") 

    # use client health API to get list of devices
    clients = apiobject.clients.get_overall_client_health(timestamp = 1234567890)
    for client in clients.response:
        pprint.pprint(client)

if __name__ == "__main__":
    main()
    print("Script ran standalone and was not imported.")
