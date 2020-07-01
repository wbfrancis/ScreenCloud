# SceneCloud Backend

## Setting Up the Virtual Environment

First, navigate to the backend folder

$ cd backend

since the virtual environment is already located in the env folder, all you should need to do is...

$ source env/bin/activate

...to activate the virtual environment and be able to run the flask app.

If for some reason the venv is messing up, just delete everything inside the env folder and run...

FOR MAC/LINUX:
$ python3 -m venv env

FOR WINDOWS:
$ py -m venv env


Then to install packages, run:

$ pip3 install -r requirements.txt

Finally, to activate the virtual environment you should run:

$ source env/bin/activate


## Running the Flask App

From the SceneCloud project dir, navigate to the src folder: 

$ cd backend/src

There's already a .flaskenv file so all you need to do is:

$ flask run

And it should start up in development mode.


## SceneCloud Endpoints

I don’t know the base URI yet, but here are the endpoints as I know them right now.

### Errors

all errors return json object as follows: 

{
        "success": False,
        "error": error_number,
        "message": error_message
}



### GET (‘/scripts’)
- Gets all data for pre uploaded scripts
- On success, returns json object as follows:

{
        "success": True,
        "scripts": preuploaded_script_data
}



where preuploaded_script_data is a list/array that follows this format (but also check out movielist.py to see exactly what preuploaded_script_data looks like):

NOTE: the characters variable is a list of 2-tuples (or just a 2 element array in JavaScript) sorted in order of most lines to fewest lines. 

[
	{
		"id": 0,
		"title": "",
		"author": "",
		"characters": [
			[characterNameString,NumberOfLines], 
			[‘daisy’,40], 
			[‘tim’,30]
		]
	},
	{
		"id": 1,
		"title": "",
		"author": "",
		"characters": [
			['jimbo',80], 
			[‘daisy’,40], 
			[‘tim’,30]
		]
	}, 
		… etc
]



### POST (‘/scripts’)
*In the post request, I need the .fdx file that was uploaded as well as a "title" param that's the title of the script*

- uploads a user submitted script (must be in the .fdx format)
- I don’t know exactly about passing a file along in a request parameter, but that’s what needs to be done, I think.
- on success, returns json object as follows:

{
        "success": True,
        "scriptObject": script_object,
        "characters": [
					[characterNameString,NumberOfLines], 
					[‘daisy’,40], 
					[‘tim’,30]
				]
 }

The script_object does not need to be accessed, it only needs to be passed to the final POST call in the sequence, described below.


### POST (‘/clouds’)
- Request param has these customization options:

script_id = id of pre uploaded script we want word clouds from, ignored if script_obj != null

script_obj = if not null, this is used to make word clouds from a user uploaded script, you get this object from the /scripts POST method described above

whole_script = boolean. True if user wants a word cloud of the whole script, False if not

action_lines = boolean. True if the user wants a word cloud of all action lines/description in the script, False if not.

characters = list/array of character names that the user wants a word cloud for. If characters is empty, null, or doesn’t exist in the request params, then no character word clouds are generated

- And on success this POST returns a json object as follows:

{
        "success": True,
        "clouds": clouds
}

where clouds = a list/array of .png word clouds.

I don’t exactly know how tricky that’ll be to pack and send a bunch of .pngs, but we’ll figure it out. LMK if you have suggestions

