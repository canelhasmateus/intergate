from __future__ import annotations

from typing import List, Optional

from pydantic import Extra

# region Common
from intergate.types.alias import String, URL, Integer
from intergate.types.data import Immutable


class IssueType( Immutable ):
	name: String
	self: URL
	iconUrl: URL


class AvatarHolder( Immutable ):
	x16: URL
	x24: URL
	x32: URL
	x48: URL

	class Config:
		fields = {
				"x16": "16x16",
				"x24": "24x24",
				"x32": "32x32",
				"x48": "48x48",
				}


class Project( Immutable ):
	self: URL
	key: String
	name: String
	avatarUrls: AvatarHolder


class Status( Immutable ):
	self: URL
	description: String
	iconUrl: URL
	name: String


class User( Immutable ):
	self: URL
	accountId: String
	displayName: String
	avatarUrls: AvatarHolder


class Fields( Immutable ):
	issueType: IssueType
	project: Project
	status: Status
	creator: Optional[User]
	reporter: Optional[User]
	assignee: Optional[User]
	class Config:
		fields = { "issueType": "issuetype" }


class Comment( Immutable ):
	self: URL
	author: User
	body: String


# endregion


# region Comment

class CommentHolder( Immutable ):
	total: Integer
	comments: List[ Comment ]


class CommentFields( Fields ):
	comment: Optional[ CommentHolder ]


class JiraEvent( Immutable ):
	self: URL
	key: String
	fieldDict: Fields

	class Config:
		extra: Extra.allow
		fields = { "fieldDict": "fields" }


class CommentEvent( JiraEvent ):
	fieldDict: CommentFields


# endregion


# region Transition
class StatusFields( Fields ):
	pass


class TransitionEvent( JiraEvent ):
	fieldDict: StatusFields

	class Config:
		extra: Extra.allow
		fields = { "fieldDict": "fields" }
# endregion
