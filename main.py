import json
import requests
from tickets.ticket import Ticket

url = "https://zccvanderbilt.zendesk.com/api/v2/tickets"
auth = "temporary"


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
        if res[i]['submitter']['id'] is not None:
            res[i]['submitter']['name'] = new_data[res[i]['submitter']['id']]['name']
            res[i]['submitter']['email'] = new_data[res[i]['submitter']['id']]['email']
        if res[i]['contact']['assignee_id'] is not None:
            res[i]['contact']['assignee_name'] = new_data[res[i]['contact']['assignee_id']]['name']
            res[i]['contact']['assignee_email'] = new_data[res[i]['contact']['assignee_id']]['email']
    return res


def format_tickets():
    val = get_tickets()
    if val == -1:
        print("Error! Oopsies!")
        exit
    res = {}
    id_set = ""
    for i, t in enumerate(val['tickets']):
        ticket = Ticket(t)
        t_format = ticket.format
        res[i] = t_format
        id_set += str(ticket.submitter_id) + ',' + str(ticket.assignee_id) + ','
    res = get_name_and_email(res, id_set)
    return res


if __name__ == '__main__':
    res = format_tickets()
    print(str(res))