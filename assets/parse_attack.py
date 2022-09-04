import json

def parse_attack(method, host, port, time):
	with open("./database/attacks.json") as atkdata:
		data = json.load(atkdata)

	for i in range(len(data)):
		if data[i]["name"] == method.upper():
			cmd = data[i]["command"].replace("[HOST]", host).replace("[PORT]", port).replace("[TIME]", time)
			return cmd