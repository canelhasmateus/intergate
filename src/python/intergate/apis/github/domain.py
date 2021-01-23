from __future__ import annotations

from collections import defaultdict
from enum import Enum
from typing import Optional, Type, Dict

from pydantic.main import Extra

from intergate.types import Immutable, String, URL, Isotime


# region enums

class CheckRunStatuses( Enum ):
	QUEUED = "queued"
	IN_PROGRESS = "in_progress"
	COMPLETED = "completed"


# TODO  23/01/2021 deal with .value
class Actions( String, Enum ):
	PUBLISHED = "published"
	RELEASED = "released"
	OPENED = "opened"
	CREATED = "created"
	COMPLETED = "completed"
	REREQUESTED = "rerequested"
	REQUESTED_ACTION = "requested_action"


class CheckRunConclusions( Enum ):
	SUCCESS = "success"
	FAILURE = "failure"
	NEUTRAL = "neutral"
	CANCELLED = "cancelled"
	TIMED_OUT = "timed_out"
	ACTION_REQUIRED = "action_required"
	STALE = "stale"
	NULL = "null"


# endregion


# region entities

class RequestedAction:
	identifier: String


class CheckRun( Immutable ):
	status: CheckRunStatuses
	conclusion: Optional[ CheckRunConclusions ]
	name: String


class Release( Immutable ):
	html_url: URL
	tag_name: String
	target_commitish: String
	name: String
	body: String
	created_at: Isotime


class Sender( Immutable ):
	login: String
	html_url: String
	avatar_url: String


# endregion

# region events

class Event( Immutable ):
	action: Actions

	class Config:
		extra = Extra.allow


class ReleaseEvent( Event ):
	action: Actions
	release: Release
	sender: Sender


# endregion

# region TODO  21/01/2021
# class Repository( dict ):
# 	#
# 	pass


# class Organization( dict ):
# 	#
# 	pass


# class Installation( dict ):
# 	#
# 	pass


# class Sender( dict ):
# 	#
# 	pass


# class CheckSuite( dict ):
# 	#
# 	pass


# endregion


# region action - event mapping

# region todo
# TODO Are there better ways of doing these "Switches"?
#  AFAIK, there is , but requires pattern matching ( python 3.10+ ) -> push to Event.__new__ or similar

# TODO  22/01/2021 implement match ( :Pattern )

_action_mapping: Dict[ Actions, Type[ Event ] ] = (
		defaultdict( lambda: Event ))

_action_mapping[ Actions.PUBLISHED ] = ReleaseEvent
# endregion
