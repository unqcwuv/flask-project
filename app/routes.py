from flask import render_template, request, redirect, url_for
from datetime import datetime
from app import app

@app.route('/')
def index():
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)

@app.route('/about')
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template('about.html', team_members=team_members)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('contact.html', success=True)

    contact_manager = {
        'name': 'Alice',
        'address': {
            'street': '123 Main St',
            'city': 'Wonderland',
            'zip': '12345'
        }
    }

    return render_template('contact.html', success=False, contact_manager=contact_manager)
