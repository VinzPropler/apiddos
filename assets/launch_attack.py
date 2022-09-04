from .parse_attack import *
import os

def launch_attack(method, host, port, time):
	parsed_cmd = parse_attack(method, host, port, time)
	return os.system(parsed_cmd)