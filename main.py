from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime
from tickets.get_tickets import format_tickets
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class TicketList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submitter_name = db.Column(db.String)

    description = db.Column(db.String)
    subject = db.Column(db.String)
    type = db.Column(db.String)

    assignee_id = db.Column(db.Integer)
    submitter_id = db.Column(db.Integer)
    assignee_name = db.Column(db.String)
    assignee_email = db.Column(db.String)

    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    due_at = db.Column(db.String)

    attachments = db.Column(db.Boolean)
    channelback = db.Column(db.Boolean)
    incidents = db.Column(db.Boolean)
    public = db.Column(db.Boolean)
    safe_update = db.Column(db.Boolean)

    def __repr__(self):
        return '<Ticket %r>' % self.id


@app.route('/', methods=['POST'])
def index():
    engine = create_engine("sqlite:///tickets.db")
    df = format_tickets()
    df.to_sql('tickets', con=engine, if_exists='replace')
    return render_template('index.html', tickets=df)


@app.route('/update')
def update():
    return redirect('/')


@app.route('/view/<int:id>')
def view(id):
    return render_template('view.html', ticket=)


if __name__ == "__main__":
    app.run(debug=True)