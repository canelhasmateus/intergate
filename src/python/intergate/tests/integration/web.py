import os
import threading
from typing import Dict

import requests

# region webserver
from intergate.tests.utils.example import EXAMPLES_PATH as EXAMPLES_PATH, example_generator
from intergate.types.alias import Integer, String
from intergate.web.server import Webserver

port: Integer = 80
DISCORD_URL = os.environ[ "DISCORD_URL" ]
thread = threading.Thread( target = Webserver( port = port,
		discordUrl = DISCORD_URL,
		jiraDomain = "..." ) )
thread.start()
# endregion

# region aliases
example: Dict
localserver: String = f"http://localhost:{port}"

send_post = lambda resource, json: requests.post( f"{localserver}/{resource}",
		json = json )
# endregion

for example in example_generator( EXAMPLES_PATH / "github", "github-*.json" ):
	print( send_post( "github",
			json = example ) )

for example in example_generator( EXAMPLES_PATH / "jira", "jira-*.json" ):
	print( send_post( "jira",
			json = example ) )

for example in example_generator( EXAMPLES_PATH / "jira", "jira-*.json" ):
	print( send_post( "jira",
			json = example ) )



