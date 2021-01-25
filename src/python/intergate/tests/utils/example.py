import json
import os
import pathlib
from typing import Iterable, Dict

from intergate.types.alias import String


def example_generator( path: pathlib.Path, glob: String ):
	exampleList: Iterable[ pathlib.Path ] = path.glob( glob )
	for example in exampleList:
		payload: Dict

		with open( str( example ), "r" ) as file:
			payload = json.load( file )

		yield payload


EXAMPLES_PATH = pathlib.Path( os.path.dirname(os.path.realpath(__file__))).parent /  "example"
