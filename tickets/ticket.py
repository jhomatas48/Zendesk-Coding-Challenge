from datetime import datetime


class Ticket:
    def __init__(self, ticket) -> None:
        self.requester_id = ticket['requester_id']

        self.allow_attachments = ticket['allow_attachments'] if 'allow_attachments' in ticket else True
        self.allow_channelback = ticket['allow_channelback'] if 'allow_channelback' in ticket else True

        self.assignee_email = ticket['assignee_email'] if 'assignee_email' in ticket else None
        self.assignee_id = ticket['assignee_id'] if 'assignee_id' in ticket else None
        self.attribute_value_ids = ticket['attribute_value_ids'] if 'attribute_value_ids' in ticket else None
        self.brand_id = ticket['brand_id'] if 'brand_id' in ticket else None
        self.collaborator_ids = ticket['collaborator_ids'] if 'collaborator_ids' in ticket else None
        self.collaborators = ticket['collaborators'] if 'collaborators' in ticket else 'None'
        self.comment = ticket['comment'] if 'comment' in ticket else 'None'
        self.created_date = datetime.strptime(ticket['created_at'], '%Y-%m-%dT%H:%M:%SZ') \
            if ('created_at' in ticket and ticket['created_at'] is not None) else None
        self.created_at = self.created_date.strftime("%b %d %Y %#I:%#M %p") if self.created_date is not None else 'None'
        self.custom_fields = ticket['custom_fields'] if 'custom_fields' in ticket else None
        self.description = ticket['description'] if 'description' in ticket else 'None'
        self.due_date = datetime.strptime(ticket['due_at'], '%Y-%m-%dT%H:%M:%SZ') \
            if ('due_at' in ticket and ticket['due_at'] is not None) else None
        self.due_at = self.due_date.strftime("%b %d %Y %#I:%#M %p") if self.due_date is not None else 'None'
        self.email_cc_ids = ticket['email_cc_ids'] if 'email_cc_ids' in ticket else None
        self.email_ccs = ticket['email_ccs'] if 'email_ccs' in ticket else None
        self.external_id = ticket['external_id'] if 'external_id' in ticket else None
        self.follower_ids = ticket['follower_ids'] if 'follower_ids' in ticket else None
        self.followers = ticket['followers'] if 'followers' in ticket else None
        self.followup_ids = ticket['followup_ids'] if 'followup_ids' in ticket else []
        self.forum_topic_id = ticket['forum_topic_id'] if 'forum_topic_id' in ticket else None
        self.group_id = ticket['group_id'] if 'group_id' in ticket else None
        self.has_incidents = ticket['has_incidents'] if 'has_incidents' in ticket else False
        self.id_val = ticket['id'] if 'id' in ticket else None
        self.is_public = ticket['is_public'] if 'is_public' in ticket else False
        self.macro_id = ticket['macro_id'] if 'macro_id' in ticket else None
        self.macro_ids = ticket['macro_ids'] if 'macro_ids' in ticket else []
        self.metadata = ticket['metadata'] if 'metadata' in ticket else None
        self.organization_id = ticket['organization_id'] if 'organization_id' in ticket else None
        self.priority = ticket['priority'] if 'priority' in ticket else 'None'
        self.problem_id = ticket['problem_id'] if 'problem_id' in ticket else None
        self.raw_subject = ticket['raw_subject'] if 'raw_subject' in ticket else 'None'
        self.recipient = ticket['recipient'] if 'recipient' in ticket else 'None'
        self.requester = ticket['requester'] if 'requester' in ticket else None
        self.safe_update = ticket['safe_update'] if 'safe_update' in ticket else False
        self.satisfaction_rating = ticket['satisfaction_rating'] if 'satisfaction_rating' in ticket else None
        self.sharing_agreement_ids = ticket['sharing_agreement_ids'] if 'sharing_agreement_ids' in ticket else []
        self.status = ticket['status'] if 'status' in ticket else 'None'
        self.subject = ticket['subject'] if 'subject' in ticket else 'None'
        self.submitter_id = ticket['submitter_id'] if 'submitter_id' in ticket else None
        self.tags = ticket['tags'] if 'tags' in ticket else None
        self.ticket_form_id = ticket['ticket_form_id'] if 'ticket_form_id' in ticket else None
        self.type = ticket['type'] if 'type' in ticket else 'None'
        self.updated_date = datetime.strptime(ticket['updated_at'], '%Y-%m-%dT%H:%M:%SZ') \
            if ('updated_at' in ticket and ticket['updated_at'] is not None) else None
        self.updated_at = self.updated_date.strftime("%b %d %Y %#I:%#M %p") if self.updated_date is not None else 'None'
        self.updated_stamp = ticket['updated_stamp'] if 'updated_stamp' in ticket else None
        self.url = ticket['url'] if 'url' in ticket else 'None'
        self.via = ticket['via'] if 'via' in ticket else None
        self.via_followup_source_id = ticket['via_followup_source_id'] if 'via_followup_source_id' in ticket else None
        self.via_id = ticket['via_id'] if 'via_id' in ticket else None
        self.voice_comment = ticket['voice_comment'] if 'voice_comment' in ticket else None

        self.format = self.ticket_format()

    def ticket_format(self):
        res = {'id': self.id_val, 'submitter_id': self.submitter_id, 'name': 'None', 'email': 'None',

               'description': self.description, 'status': self.status, 'subject': self.subject, 'type': self.type,

               'created_at': self.created_at, 'due_at': self.due_at, 'updated_at': self.updated_at,
               'created_date': self.created_date, 'due_date': self.due_date, 'updated_date': self.updated_date,

               'assignee_id': self.assignee_id, 'assignee_name': 'None', 'assignee_email': 'None',

               'allow_attachments': self.allow_attachments, 'channelback': self.allow_channelback,
               'incidents': self.has_incidents, 'public': self.is_public, 'safe_update': self.safe_update
               }
        return res