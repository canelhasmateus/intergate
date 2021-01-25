from typing import Dict

from intergate.apis.jira.domain import JiraEvent, CommentEvent, TransitionEvent
from intergate.tests.utils.example import example_generator, EXAMPLES_PATH as EXAMPLES_PATH

example: Dict

for example in example_generator( EXAMPLES_PATH / "jira", glob = "jira-*.json" ):
	print( JiraEvent( **example ) )

for example in example_generator( EXAMPLES_PATH / "jira", glob = "jira-comment-*.json" ):
	print( CommentEvent( **example ) )
for example in example_generator( EXAMPLES_PATH / "jira", glob = "jira-status-*.json" ):
	print( TransitionEvent( **example ) )


