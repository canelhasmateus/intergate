from __future__ import annotations

from enum import Enum


class HttpMethods( Enum ):
	GET = "GET"
	POST = "POST"
	HEAD = "HEAD"
	OPTIONS = "OPTIONS"
	PUT = "PUT"
	PATCH = "PATCH"
