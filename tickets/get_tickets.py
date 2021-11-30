import json
import requests
from tickets.ticket import Ticket
import pandas as pd

url = "https://zccvanderbilt.zendesk.com/api/v2/tickets"
auth = "Basic temp"


def get_tickets(auth, domain):
    """
    get_tickets calls the Zendesk API to get a list of tickets.
    If there are more than 100 entries, calls the next page

    :return: list of dictionaries of each page of up to 100 tickets each
    """
    header = {'Content-Type': 'application/json',
        'Authorization': auth}
    url = "https://" + domain + "/api/v2/tickets"
    curr_url = url
    data = []
    while curr_url is not None:
        response = requests.get(curr_url, headers=header)
        if response.status_code != 200:
            return None
        curr_data = json.loads(response.text)
        curr_url = curr_data["next_page"]
        data.append(curr_data)
    return data


def get_requester_info(auth, subdomain):
    me_url = "https://" + subdomain + "/api/v2/users/me"
    header = {'Authorization': auth}
    response = requests.get(me_url, headers=header)
    if response.status_code != 200:
        return None
    data = json.loads(response.text)
    my_id = data['user']['id']
    name = data['user']['name'] if 'name' in data['user'] else ''
    email = data['user']['email'] if 'email' in data['user'] else ''
    return [my_id, name, email]


def get_name_and_email(res, id_lst, auth, domain):
    """
    get_name_and_email calls the Zendesk API to get the name and email
    of each submitter and assignee.
    :param res: dictionary containing all ticket information
    :param id_lst: comma-separated list of all submitters and requesters
    :return: updated dictionary with names and emails added
    """
    user_url = "https://" + domain + "/api/v2/users/show_many.json?ids=" + id_lst
    header = {'Authorization': auth}
    curr_url = user_url
    while curr_url is not None:
        response = requests.get(curr_url, headers=header)
        if response.status_code != 200:
            return None
        else:
            data = json.loads(response.text)
        new_data = {}
        for i in data['users']:
            new_data[int(i['id'])] = {'name': i['name'], 'email': i['email']}
        for i in res:
            if res[i]['submitter_id'] is not None:
                res[i]['name'] = new_data[res[i]['submitter_id']]['name']
                res[i]['email'] = new_data[res[i]['submitter_id']]['email']
            if res[i]['assignee_id'] is not None:
                res[i]['assignee_name'] = new_data[res[i]['assignee_id']]['name']
                res[i]['assignee_email'] = new_data[res[i]['assignee_id']]['email']
        curr_url = data["next_page"]
    return res


def format_tickets(auth, domain):
    """
    format_tickets calls get_tickets and creates a Ticket object for every ticket.
    Formats the information in each ticket and calls get_name_and_email.

    :return: DataFrame containing all ticket information
    """
    val = get_tickets(auth, domain)
    if val is None:
        print("Error: Could not connect to Zendesk API")
        return None
    res = {}
    id_set = ""
    for v in val:
        for t in v['tickets']:
            ticket = Ticket(t)
            t_format = ticket.format
            ticket_id = t_format['id']
            res[ticket_id] = t_format
            id_set += str(ticket.submitter_id) + ',' + str(ticket.assignee_id) + ','
    res = get_name_and_email(res, id_set, auth, domain)
    if res is None:
        return None
    return pd.DataFrame.from_records(res).T


if __name__ == '__main__':
    res = format_tickets("Basic temp")
    print(res)