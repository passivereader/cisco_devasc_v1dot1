#! /path/to/venv python
# pip install meraki
# export MERAKI_DASHBOARD_API_KEY=assuming_key_exported_in_bash

import meraki, os, random

def main():
    dashboard = meraki.DashboardAPI(
        api_key = os.environ["MERAKI_DASHBOARD_API_KEY"],
        base_url="https://n149.meraki.com/api/v1"
        )

    orgs = dashboard.organizations.getOrganizations()
    org_list = []
    for org in orgs:
        org_list.append((org['name'], org['id']))

    random_org = org_list[random.randrange(0, len(org_list))]
    print("Random org chosen: " + str(random_org))

    org_networks = dashboard.organizations.getOrganizationNetworks(
        random_org[1])
    org_network_dict = org_networks[0] # not random, choosing 1st network
    print(f"Choosing 1st net the API returned: {org_network_dict['id']}")

    org_net_devices_1st_network = dashboard.networks.getNetworkDevices(
        org_network_dict['id'])
    
    print(org_net_devices_1st_network) 

if __name__ == "__main__":
    main()
    print("Script ran standalone and was not imported.")
