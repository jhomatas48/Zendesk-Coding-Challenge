import json
import requests
from tickets.ticket import Ticket
import pandas as pd

url = "https://zccvanderbilt.zendesk.com/api/v2/tickets"
auth = "Basic temp"


def get_tickets():
    header = {'Content-Type': 'application/json',
        'Authorization': auth}
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        return -1
    data = json.loads(response.text)
    return data


def get_name_and_email(res, id_lst):
    user_url = "https://zccvanderbilt.zendesk.com/api/v2/users/show_many.json?ids=" + id_lst
    header = {'Authorization': auth}
    response = requests.get(user_url, headers=header)
    if response.status_code != 200:
        data = {}
    else:
        data = json.loads(response.text)
    new_data = {}
    for i in data['users']:
        new_data[int(i['id'])] = {'name': i['name'], 'email': i['email']}
    for i in range(len(res)):
        if res[i]['submitter_id'] is not None:
            res[i]['name'] = new_data[res[i]['submitter_id']]['name']
            res[i]['email'] = new_data[res[i]['submitter_id']]['email']
        if res[i]['assignee_id'] is not None:
            res[i]['assignee_name'] = new_data[res[i]['assignee_id']]['name']
            res[i]['assignee_email'] = new_data[res[i]['assignee_id']]['email']
    return res


def format_tickets():
    val = get_tickets()
    if val == -1:
        print("Error: Could not connect to Zendesk API")
        exit()
    res = {}
    id_set = ""
    for i, t in enumerate(val['tickets']):
        ticket = Ticket(t)
        t_format = ticket.format
        res[i] = t_format
        id_set += str(ticket.submitter_id) + ',' + str(ticket.assignee_id) + ','
    res = get_name_and_email(res, id_set)
    return pd.DataFrame.from_records(res).T


if __name__ == '__main__':
    res = format_tickets()
    print(res)
