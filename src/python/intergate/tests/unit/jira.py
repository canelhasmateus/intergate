import pathlib
from typing import Dict

from intergate import tests
from intergate.apis import jira

examplesPath: pathlib.Path = tests.example.PATH
example: Dict

for example in tests.example.generator( examplesPath / "jira", glob = "jira-*.json" ):
	print( jira.Event( **example ) )
