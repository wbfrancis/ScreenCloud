import script_objects as scr
import file_parser as fp

# returns fully initialized Script object
def initialize_script(script_name):
	# right now, we're getting the dict of the script from the .json file. 
	# This is technically an extra step, as we already get a dict from the .fdx file
	# Should probably convert root_dict to a global variable or do this in a more OOP way,
	# but I'm not yet sure how I'm structuring the project, so that's **TO DO**
	
	root_dict = fp.get_root_dict(script_name)
	
	para_list = root_dict["FinalDraft"]["Content"]["Paragraph"]

	#  initialize Script object
	script = scr.Script(script_name)

	#  initialize dict of string names to Character objects
	character_dict = {}
	action_lines = []

	#  loop through json file, building ScriptObjects
	# TODO Should stuff like "Nate's Text" appear as Nate?
	for i in range(len(para_list)):
		obj = para_list[i]
		
		if obj["@Type"] == "Character" and obj["Text"] != None:
			# print(obj)
			name = removeParentheticals(obj["Text"]).lower()
			if (not name in character_dict):
				character_dict[name] = scr.Character(script, name)
			parenth = ""
			if para_list[i+1]["@Type"] == "Parenthetical":
				parenth = para_list[i+1]["Text"]
				text = getText(para_list[i+2]["Text"])
			else:
				text = getText(para_list[i+1]["Text"])
			dlg = scr.Dialogue(script, text, parenth)
			character_dict[name].add_dialogue(dlg)
			
		if obj["@Type"] == "Action" and obj["Text"] != None:
			if (type(obj["Text"])is dict):
				if '#text' in obj['Text']:
					action_lines.append(scr.ActionLine(script, obj["Text"]['#text']))
			elif (type(obj["Text"])is list):
				action_lines.append(scr.ActionLine(script, getText(obj["Text"])))
			else: action_lines.append(scr.ActionLine(script, obj["Text"]))


	#  give the Script object a list of its Characters and a list of its ActionLines
	script.initialize(character_dict, action_lines)
	return script
	
	# DATA STRUCTURE
	# Script
	# 	[Characters]
			# [Dialogue]
	# 	[ActionLines]

def getText(d):
	string = ""
	if type(d) is list:
		for x in d:
			if type(x) is dict:
				if '#text' in x:
					string+= " " + x["#text"] + " "
	elif type(d) is dict:
				string+= " " + d['#text'] + " "
	else: string = d
	return string.strip()

def removeParentheticals(string):
	if (type(string) == dict):
		string = string['#text']

	firstHalf, secondHalf = "", ""
	for i in range(len(string)):
		if string[i] == "(":
			firstHalf = string[0:i]
		elif string[i] == ")":
			if i != len(string)-1:
				secondHalf = string[i+1, len(string)]
	if firstHalf == "": return string
	return firstHalf.strip() + secondHalf