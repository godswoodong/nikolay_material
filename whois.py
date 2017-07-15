




#!/usr/bin/python
import datetime
import csv
import json
import pythonwhois

domain_name = [line.rstrip('\n') for line in open('domain.csv')]


data = []

def json_fallback(obj):
	if isinstance(obj, datetime.datetime):
		return obj.isoformat()
	else:
		return obj

for domain in domain_name:
	test = pythonwhois.net.get_whois_raw(domain, with_server_list=False)
	parsed = pythonwhois.parse.parse_raw_whois(test,normalized=True)
	json_test = json.dumps(parsed, default = json_fallback)
	really_json = json.loads(json_test)
	keys = really_json.keys()
	data.append(really_json)


f = csv.writer(open("result_test.csv","wb+")) 
f. writerow(keys)
print(len(data))
for x in data:
	f.writerow([x["status"],
	    x["updated_date"],
	    x["contacts"],	
            x["nameservers"],
	    x["expiration_date"],
	    x["creation_date"],
	    x["raw"],
	    x["whois_server"],
	    x["registrar"]])
f.close()
