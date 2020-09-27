activete virtual env - "python ./myenv/bin/activate"


API calls
	# Start a new instance (returns token)
	http://127.0.0.1:8000/START

	# Play move, validate token, 30min session
	http://127.0.0.1:8000/MOVE?u="Y or R"&c="1....7"&t=token_recieved_form_start_api

	# Returns all moves so far
	http://127.0.0.1:8000/ALL_MOVES?t=token_value


Coudnt complete all functionality
Code also on : https://github.com/Akashtyagi08/Challange