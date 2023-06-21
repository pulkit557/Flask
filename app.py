# from flask import Flask
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_ TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
app.app_context().push()
migrate = Migrate(app, db)
class Todo(db.Model):
    SNo=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.title}"
    
    
@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo=Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo=Todo.query.all()
    print(allTodo)
    # create_tables()
    return render_template('index.html',allTodo=allTodo)
    
    
@app.route('/show',methods=['GET'])
def products():
    # print(2)
    allTodo=Todo.query.all()
    print(allTodo)
    return 'This is product page'

# def create_tables():
#     with app.app_context():
#          db.create_all()
    # app.config['SQLALCHEMY_ TRACK_MODIFICATIONS']=True

if __name__ == '__main__':

    app.run(debug=True,port=8000)
