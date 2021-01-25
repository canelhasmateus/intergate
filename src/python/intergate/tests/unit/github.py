from typing import Dict

from intergate.apis.github.domain import ReleaseEvent
from intergate.tests.utils.example import example_generator, EXAMPLES_PATH as EXAMPLES_PATH

example: Dict

for example in example_generator( EXAMPLES_PATH / "github", glob = "github-release-*.json" ):
	print( ReleaseEvent( **example ) )
