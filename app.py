from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройка базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных
db = SQLAlchemy(app)

# Модель задачи (таблица Agent)
class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), nullable=False, unique=True)
    contact_number = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    access_level = db.Column(db.String(50), nullable=False)

# Создаем таблицу в базе данных
with app.app_context():
    db.create_all()

### 📌 CRUD-МАРШРУТЫ

# 📌 Главная страница: список агентов
@app.route('/')
@app.route('/agents')
def get_agents():
    access_level = request.args.get('access_level')
    if access_level:
        agents = Agent.query.filter_by(access_level=access_level).all()
    else:
        agents = Agent.query.all()

    return render_template('agents.html', agents=agents)

# 📌 Добавление нового агента
@app.route('/add', methods=['GET', 'POST'])
def add_agent():
    if request.method == 'POST':
        nickname = request.form['nickname']
        contact_number = request.form['contact_number']
        email = request.form['email']
        access_level = request.form['access_level']

        new_agent = Agent(
            nickname=nickname,
            contact_number=contact_number,
            email=email,
            access_level=access_level
        )

        db.session.add(new_agent)
        db.session.commit()
        return redirect(url_for('get_agents'))
    return render_template('add_agent.html')

# 📌 Редактирование информации об агенте
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_agent(id):
    agent = Agent.query.get_or_404(id)

    if request.method == 'POST':
        agent.nickname = request.form['nickname']
        agent.contact_number = request.form['contact_number']
        agent.email = request.form['email']
        agent.access_level = request.form['access_level']
        db.session.commit()
        return redirect(url_for('get_agents'))
    return render_template('edit_agent.html', agent=agent)

# 📌 Страница с досье
@app.route('/agent/<int:id>')
def agent_detail(id):
    agent = Agent.query.get_or_404(id)
    return render_template('agent_detail.html', agent=agent)

# 📌 Удаление агента
@app.route('/delete/<int:id>', methods=['POST'])
def delete_agent(id):
    agent = Agent.query.get_or_404(id)
    db.session.delete(agent)
    db.session.commit()
    return redirect(url_for('get_agents'))

# 📌 Удаление всего
@app.route('/secret_wipe', methods=['POST'])
def secret_wipe():
    Agent.query.delete()
    db.session.commit()
    return redirect(url_for('get_agents'))

# Запуск сервера
if __name__ == "__main__":
    app.run(debug=True)