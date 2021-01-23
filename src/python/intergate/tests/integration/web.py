import os
import pathlib
import threading
from typing import Dict

import requests

from intergate import web, tests
from intergate.types import Integer, String

# region webserver
port: Integer = 80
discordUrl = os.environ[ "DISCORD_URL" ]
thread = threading.Thread( target = web.Server( port = port,
		discordUrl = discordUrl,
		jiraDomain = "..." ) )
thread.start()
# endregion

# region aliases
example: Dict
localserver: String = f"http://localhost:{port}"
examplesPath: pathlib.Path = tests.example.PATH

send_post = lambda resource, json: requests.post( f"{localserver}/{resource}",
		json = json )
# endregion

for example in tests.example.generator( examplesPath / "github", "github-*.json" ):
	print( send_post( "github",
			json = example ) )

for example in tests.example.generator( examplesPath / "jira", "jira-*.json" ):
	print( send_post( "jira",
			json = example ) )
