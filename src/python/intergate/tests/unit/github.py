import pathlib
from typing import Dict

from intergate import tests
from intergate.apis import github

examplesPath: pathlib.Path = tests.example.PATH
example: Dict

for example in tests.example.generator( examplesPath / "github", glob = "github-release-*.json" ):
	print( github.ReleaseEvent( **example ) )
