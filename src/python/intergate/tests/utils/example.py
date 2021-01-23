import json
import pathlib
from typing import Iterable, Dict

from intergate.types import String


def generator( path: pathlib.Path, glob: String ):
	exampleList: Iterable[ pathlib.Path ] = path.glob( glob )
	for example in exampleList:
		payload: Dict

		with open( str( example ), "r" ) as file:
			payload = json.load( file )

		yield payload


PATH = pathlib.Path( '../example' )
