#! /path/to/venv python

# acitoolkit has maturin as a dependency which requires setuptools with Rust
# on FreeBSD: pkg install py39-setuptools-rust
# pip install acitoolkit

import sys, os
import acitoolkit.acitoolkit as aci

def main():
    APIC_URL = "https://sandboxapicdc.cisco.com"
    ACI_USR = "admin"
    ACI_PW = os.environ["ACI_PASS"] # export ACI_PASS='the_password'

    SESSION = aci.Session(APIC_URL, ACI_USR, ACI_PW)

    response = SESSION.login()
    if not response.ok:
        print("Status code other than 200, exiting...")
        sys.exit()

    # see acitoolkit source code for behaviour of get method
    endpoints = aci.Endpoint.get(SESSION)

    # print(endpoints) # no endpoints in the sandbox? --> no output
    for ep in endpoints:
        epg = ep.get_parent() # endpointgroup
        app_profile = epg.get_parent()
        tenant = app_profile.get_parent()
        print(f"""
        MAC address: {ep.mac}
        IP address: {ep.ip}
        ENCAP: {ep.encap}
        Tenant: {tenant.name}
        App Profile: {app_profile.name}
        Endpoint Group: {epg.name}
        """)

if __name__ == "__main__":
    main()
    print("Script ran standalone and was not imported.")
