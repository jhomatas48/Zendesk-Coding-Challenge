import json
import pandas as pd
from tickets.ticket import Ticket
from tickets.get_tickets import get_tickets, get_name_and_email, format_tickets
from tickets.get_tickets import get_tickets

def test_ticket_class():
    data = json.loads({
            "url": "https://zccvanderbilt.zendesk.com/api/v2/tickets/1.json",
            "id": 1,
            "external_id": null,
            "via": {
                "channel": "sample_ticket",
                "source": {
                    "from": {},
                    "to": {},
                    "rel": null
                }
            },
            "created_at": "2021-11-24T21:48:54Z",
            "updated_at": "2021-11-24T21:48:54Z",
            "type": "incident",
            "subject": "Sample ticket: Meet the ticket",
            "raw_subject": "Sample ticket: Meet the ticket",
            "description": "Hi there,\n\nI’m sending an email because I’m having a problem setting up your new product. Can you help me troubleshoot?\n\nThanks,\n The Customer\n\n",
            "priority": "normal",
            "status": "open",
            "recipient": null,
            "requester_id": 421988152152,
            "submitter_id": 421988150252,
            "assignee_id": 421988150252,
            "organization_id": null,
            "group_id": 4411237682452,
            "collaborator_ids": [],
            "follower_ids": [],
            "email_cc_ids": [],
            "forum_topic_id": null,
            "problem_id": null,
            "has_incidents": false,
            "is_public": true,
            "due_at": null,
            "tags": [
                "sample",
                "support",
                "zendesk"
            ],
            "custom_fields": [],
            "satisfaction_rating": null,
            "sharing_agreement_ids": [],
            "fields": [],
            "followup_ids": [],
            "ticket_form_id": 360003523752,
            "brand_id": 360007072512,
            "allow_channelback": false,
            "allow_attachments": true
        })


'''
def test_retrieved_data():
    with open("tests/tickets.json") as tickets_json:
        input_tickets = json.loads(tickets_json.read())
        res = {}
        id_set = ""
        for t in input_tickets['tickets']:
            ticket = Ticket(t)
            t_format = ticket.format
            ticket_id = t_format['id']
            res[ticket_id] = t_format
            id_set += str(ticket.submitter_id) + ',' + str(ticket.assignee_id) + ','
        assert 0
        res = get_name_and_email(res, id_set)
        retrieved_df = format_tickets()
        retrieved_df.drop(1)
        assert res != 1
        assert pd.DataFrame.from_records(res).T == retrieved_df

if __name__ == '__main__':
    test_retrieved_data()
    print(0)
'''
