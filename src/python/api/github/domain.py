from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic.main import Extra

from ..common import ImmutableSerializable

String = str
URL = String
Isotime = String



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


# action: Actions
# check_run: CheckRun
# repository: Repository
# organization: Organization
# installation: Installation
# sender: Sender

# class CheckSuite( dict ):
# 	#
# 	pass


# endregion


# region objects
class CheckRun( ImmutableSerializable ):
	status: CheckRunStatuses
	conclusion: Optional[ CheckRunConclusions ]
	name: String


# check_suite: CheckSuite


class RequestedAction:
	identifier: String


class Release( ImmutableSerializable ):
	html_url: URL
	tag_name: String
	target_commitish: String
	name: String
	body: String
	created_at: Isotime


class Payload( ImmutableSerializable ):
	action: Actions

	class Config:
		extra = Extra.allow


class Sender( ImmutableSerializable ):
	login: String
	html_url: String
	avatar_url: String


class ReleasePayload( Payload ):
	action: Actions
	release: Release
	sender: Sender


# endregion


# region enums
class Actions( String, Enum ):
	PUBLISHED: String = "published"
	RELEASED: String = "released"
	OPENED: String = 'opened'
	CREATED: String = 'created'
	COMPLETED: String = 'completed'
	REREQUESTED: String = 'rerequested'
	REQUESTED_ACTION: String = 'requested_action'


class CheckRunStatuses( String, Enum ):
	QUEUED: String = "queued"
	IN_PROGRESS: String = "in_progress"
	COMPLETED: String = "completed"


class CheckRunConclusions( String, Enum ):
	SUCCESS: String = "success"
	FAILURE: String = "failure"
	NEUTRAL: String = "neutral"
	CANCELLED: String = "cancelled"
	TIMED_OUT: String = "timed_out"
	ACTION_REQUIRED: String = "action_required"
	STALE: String = "stale"
	NULL: String = "null"

# endregion
