import xmltodict, json, os
from os import listdir
from os.path import isfile, join


def get_root_dict(script_name):
	if not has_file('./backend/fdx_scripts/', script_name + '.fdx'):
		raise FileNotFoundError("can't find " + script_name)
	else:
		return get_dict_from_xml(script_name)

def get_root_dict_from_file(file):
	return xmltodict.parse(file.read())

def has_file(path, filename):
	for file in os.walk(path):
			if (filename in file[2]):
				return True
	return False

# def convert_fdx_to_json(script_name):
# 	with open('./resource/json_scripts/' + script_name + '.json', 'w') as file:
# 		json.dump(get_dict_from_xml(script_name), file)

def get_dict_from_xml(script_name):
	with open('./backend/fdx_scripts/' + script_name + '.fdx') as file:
		return xmltodict.parse(file.read())

def get_dict_from_json(script_name):
	with open('./backend/fdx_scripts/' + script_name + '.json') as file:
		return json.load(file)
