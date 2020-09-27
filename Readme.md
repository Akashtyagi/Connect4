#Connect4
API LINK - https://connect4-akashtyagi.herokuapp.com/
A API based Game, First to connet 4 dots win.

Board size = 6*7

API calls Supported:
	# Start a new instance (returns token)
	* http://127.0.0.1:8000/START

	# Play move, validate token, 30min session
	* http://127.0.0.1:8000/MOVE?u="Y/R"&c="1....7"&t=token_recieved_form_start_api

	# Returns all moves so far
	http://127.0.0.1:8000/ALL_MOVES?t=token_value

Backend Features:
1. Validate each request for a Valid Token.
2. Each game session expires after 30min.
3. When request recieves with expired session, deletes game data from DB and returns "INVALID" .
4. Validate each request for correct user order, maintains alternate user game play.
