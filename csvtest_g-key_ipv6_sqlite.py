import csv, re, random, sqlite3

def main():
    # CSV: https://www.regionalstatistik.de/genesis/online?language=de&sequenz=tabelleAufbau&selectionname=11111-01-01-5#astructure
    with open("test2.csv", "r", encoding="iso8859_15", newline="") \
    as csvfile:
        dialect_sniffed = csv.Sniffer().sniff(csvfile.read(4096), ";")
        csvfile.seek(0)
        fieldnames = ["date", "g-key", "name", "area-size", "garbage"]
        contents = csv.DictReader(csvfile, fieldnames, \
        "garbage", "FILLER", dialect_sniffed)

        # https://datatracker.ietf.org/doc/html/rfc4193#section-3
        ipv6_rfc4193_Prefix_L = str(hex(0b11111101))[2:]
        ipv6_rfc4193_Global_ID = str(hex(random.randint(0,2**40)))[2:]
        ipv6_rfc4193_Subnet_ID = "aaaa"
        ipv6_net_combined = ipv6_rfc4193_Prefix_L + ipv6_rfc4193_Global_ID + ipv6_rfc4193_Subnet_ID
        ipv6_net_ID = re.findall("....", ipv6_net_combined)

        con = sqlite3.connect("govent.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE govent (
        g_key text,
        name text,
        area real,
        jail_ipv6 text
        )
        """)

        for row in contents:
            # {2,2} 16 Bundesland
            # {3,3} 35 Statistische Region, Regierungsbezirk
            # {5,5} 471 Landkreis, Kreis, kreisfreie Stadt, Stadtkreis
            # {8,8} 13391 Gemeinde
            m = re.search("^[0-9]{1,8}$", row["g-key"])
            if m != None:
                g_key = row["g-key"]
                name = row["name"]
                area_size = row["area-size"]
                if area_size == "-":
                    area_size = "0.00"
                elif area_size != "-":
                    area_size = area_size.replace(",", ".")

                padded_hex_g_key = \
                str(hex(int("{:9>14}".format(g_key))))
                ipv6_host_part = re.findall("....", padded_hex_g_key[2:])
                ipv6_host_part.insert(0, "bbbb")
                ipv6 = ":".join(ipv6_net_ID) + \
                ":" + ":".join(ipv6_host_part)
                #print(f"""{g_key} {name} {area_size} {ipv6}""")
                data = []
                data.append((str(g_key), str(name), float(area_size), str(ipv6)))
                cur.executemany("INSERT INTO govent VALUES(?, ?, ?, ?)", data)
        con.commit()
        con.close()

if __name__ == "__main__":
    main()
    print("Script ran standalone and was not imported.")
