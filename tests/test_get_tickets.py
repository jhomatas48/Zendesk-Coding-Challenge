import pandas as pd
from tickets.ticket import Ticket
from tickets.get_tickets import get_tickets, get_name_and_email, format_tickets, get_requester_info
from tests.credentials import credentials
from datetime import datetime
import base64

creds = credentials()
email = creds['email']
password = creds['password']
subdomain = creds['subdomain']
name = creds['name']
domain = subdomain + ".zendesk.com"
print('hi')
combined = email + ':' + password
encoded_u = base64.b64encode(combined.encode()).decode()
auth = "Basic " + encoded_u
data = {"url": "https://mock_url.zendesk.com/api/v2/tickets/1.json",
        "id": 143,
        "external_id": None,
        "via": {
            "channel": "sample_ticket",
            "source": {
                "from": {},
                "to": {},
                "rel": None
            }
        },
        "created_at": "2021-11-24T01:48:54Z",
        "updated_at": "2021-11-24T23:48:54Z",
        "type": "incident",
        "subject": "This is a test.",
        "raw_subject": "This is a test.",
        "description": "Hi there,\n\nThis is simply a test message!\n\nThanks,\n The Customer\n\n",
        "priority": "normal",
        "status": "closed",
        "recipient": None,
        "requester_id": 10000000000,
        "submitter_id": 10000000,
        "assignee_id": 1010101010,
        "organization_id": None,
        "group_id": 12345678,
        "collaborator_ids": [],
        "follower_ids": [],
        "email_cc_ids": [],
        "forum_topic_id": None,
        "problem_id": None,
        "has_incidents": False,
        "is_public": True,
        "tags": [
            "this",
            "is",
            "a",
            "test"
        ],
        "custom_fields": [],
        "satisfaction_rating": None,
        "sharing_agreement_ids": [],
        "fields": [],
        "followup_ids": [],
        "ticket_form_id": 300000030300,
        "brand_id": 100000000,
        "allow_channelback": True,
        "allow_attachments": False
    }


def test_ticket_class():

    test_ticket = Ticket(data)
    res = test_ticket.ticket_format()
    assert res['id'] == 143
    assert res['submitter_id'] == 10000000
    assert res['description'] == "Hi there,\n\nThis is simply a test message!\n\nThanks,\n The Customer\n\n"
    assert res['status'] == "closed"
    assert res['subject'] == "This is a test."
    assert res['type'] == "incident"
    assert res['tags'] == 'this, is, a, test'
    created = datetime(year=2021, month=11, day=24, hour=1, minute=48, second=54)
    assert created == res['created_date']
    updated = datetime(year=2021, month=11, day=24, hour=23, minute=48, second=54)
    assert updated == res['updated_date']
    assert res['due_date'] is None
    assert res['created_at'] == "Nov 24 2021 01:48 AM"
    assert res['updated_at'] == "Nov 24 2021 11:48 PM"
    assert res['due_at'] == "None"
    assert res['assignee_id'] == 1010101010
    assert res['allow_attachments'] == False
    assert res['channelback'] == True
    assert res['incidents'] == False
    assert res['public'] == True
    assert res['safe_update'] == False


def test_get_requester_info():
    requester = get_requester_info(auth, domain)
    assert requester is not None
    assert requester[2] == email
    requester_invalid_auth = get_requester_info("Basic should fail", domain)
    assert requester_invalid_auth is None
    requester_invalid_domain = get_requester_info(auth, "/?Invalid/")
    assert requester_invalid_domain is None
    requester_invalid_domain2 = get_requester_info(auth, "this should not work")
    assert requester_invalid_domain2 is None


def test_get_name_and_email():
    requester = get_requester_info(auth, domain)
    assert requester is not None
    assert requester[0] is not None
    requester_id = requester[0]
    mock_data = {1:
                 {"submitter_id": requester_id,
                 "assignee_id": None,
                 "status": open,
                 "allow_attachments": True,
                 "requester_id": requester_id,
                 "name": "None",
                 "email": "None",
                 "assignee_name": "None",
                 "assignee_email": "None"}}
    res = get_name_and_email(mock_data, str(requester_id), auth, domain)
    mock_res = {1:
                {"submitter_id": requester_id,
                 "assignee_id": None,
                 "status": open,
                 "allow_attachments": True,
                 "requester_id": requester_id,
                 "name": name,
                 "email": email,
                 "assignee_name": "None",
                 "assignee_email": "None"}}
    assert res == mock_res


def test_get_tickets():
    data = get_tickets(auth, domain)
    assert data is not None
    invalid_auth = get_tickets("Basic Invalid", domain)
    assert invalid_auth is None
    invalid_domain = get_tickets(auth, "Invalid Domain")
    assert invalid_domain is None