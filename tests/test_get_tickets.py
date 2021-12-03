import json
import pandas as pd
from tickets.ticket import Ticket
from tickets.get_tickets import get_tickets, get_name_and_email, format_tickets
from tickets.get_tickets import get_tickets


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
