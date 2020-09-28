# Connect4
API LINK - https://connect4-akashtyagi.herokuapp.com/
A API based Game, First to connet 4 dots win.

Board size = 6*7

API calls Supported:

	# Start a new instance (returns token)
	* https://connect4-akashtyagi.herokuapp.com/START

	# Play move, validate token, 30min session
	
	* https://connect4-akashtyagi.herokuapp.com/MOVE?u="Y/R"&c="1....7"&t=token_recieved_form_start_api
	```
	u = This parameter defines which user makes move. Possible options are [Y,R].<br>
	c = This parameter defines which in column coin is dropped. Possible options are [1,2,3,4,5,6,7]<br>
	t = This parameter defines which token/session are you in. Possible option is "token" you recieved when used 'START/' api.
	```

	# Returns all moves so far

	https://connect4-akashtyagi.herokuapp.com/ALL_MOVES?t=token_value

Backend Features:
1. Validate each request for a Valid Token.
2. Each game session expires after 30min.
3. When request recieves with expired session, deletes game data from DB and returns "INVALID" .
4. Validate each request for correct user order, maintains alternate user game play.
