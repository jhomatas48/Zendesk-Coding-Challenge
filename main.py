from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
from datetime import datetime
from tickets.get_tickets import format_tickets
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
db = SQLAlchemy(app)


class TicketList(db.Model):
    __tablename__ = "ticket_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    description = db.Column(db.String)
    status = db.Column(db.String)
    subject = db.Column(db.String)
    type = db.Column(db.String)

    assignee_id = db.Column(db.Integer)
    submitter_id = db.Column(db.Integer)
    assignee_name = db.Column(db.String)
    email = db.Column(db.String)
    assignee_email = db.Column(db.String)

    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    due_at = db.Column(db.String)

    allow_attachments = db.Column(db.Boolean)
    channelback = db.Column(db.Boolean)
    incidents = db.Column(db.Boolean)
    public = db.Column(db.Boolean)
    safe_update = db.Column(db.Boolean)

    def __repr__(self):
        return '<Ticket %r>' % self.id


@app.route('/', methods=['GET'])
def index():
    engine = create_engine("sqlite:///tickets.db")
    df = format_tickets()
    df.to_sql(con=engine, name='ticket_table', if_exists='replace', index=False)
    page = request.args.get('page', 1, type=int)
    tickets = TicketList.query.paginate(page=page, per_page=25)
    return render_template('index.html', tickets=tickets)


@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    ticket = TicketList.query.get_or_404(id)
    return render_template('view.html', ticket=ticket)


@app.route('/next/<int:id>', methods=['GET'])
def next_ticket(id):
    next_t = TicketList.query.order_by(TicketList.id.asc()).filter(TicketList.id > id).first()
    if next_t is None:
        next_t = TicketList.query.order_by(TicketList.id.asc()).first()
    next_id = str(next_t.id)
    return redirect('/view/' + next_id)


@app.route('/prev/<int:id>', methods=['GET'])
def prev_ticket(id):
    prev_t = TicketList.query.order_by(TicketList.id.desc()).filter(TicketList.id < id).first()
    if prev_t is None:
        prev_t = TicketList.query.order_by(TicketList.id.desc()).first()
    prev_id = str(prev_t.id)
    return redirect('/view/' + prev_id)


if __name__ == "__main__":
    app.run(debug=True)
