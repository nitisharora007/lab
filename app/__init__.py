from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
db.create_all()

class Student(db.Model):
    roll_no = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(120))
    age = db.Column(db.Integer)
    mobile_num = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Student({self.roll_no}): {self.fname}, {self.age} >"

    @property
    def serialize(self):
        return {'fname': self.fname, 'lname': self.lname, 'rollno': self.roll_no, 'age': self.age}


@app.route("/")
def home():
    return jsonify({'message': 'Welcome to the Flask app', 'status': 'ok'})


@app.route("/status")
def status():
    return jsonify({'message': 'Web application is up & running',
                    'status': 'ok'})


@app.route("/clear")
def clear():
    # db.drop_all()
    return jsonify({'message': 'DB has been cleared up', 'status': 'ok'})


@app.route("/student", methods=["GET"])
def get_students():

        students = [stu.serialize for stu in db.session.query(Student).all()]
        return jsonify({'result': students})


@app.route("/student/<int:rollno>", methods=["GET"])
def get_student(rollno):

    student = db.session.query(Student).filter_by(roll_no=rollno).first()
    if student is None:
        return jsonify({'message': 'Please provide the valid roll number'})

    return jsonify(student.serialize)


@app.route("/student", methods=["POST"])
def update_student():

    data = request.get_json(True)
    roll_no = data['rollno'] if "rollno" in data else None
    fname = data['fname'] if "fname" in data else None
    lname = data['lname'] if "lname" in data else None
    age = data['age'] if "age" in data else None

    # Add the student
    if roll_no is None or roll_no == "":
        student = Student(fname=fname, lname=lname, age=age)
        db.session.add(student)
        db.session.commit()
        return jsonify({'message': f'Student {fname} has been added'})

    student = db.session.query(Student).filter_by(roll_no=roll_no)
    stu_o = student.first()
    if stu_o is None:
        return jsonify({'message': f'Please provide a valid roll number'})
    fname = fname if fname is not None else stu_o.fname
    lname = lname if lname is not None else stu_o.lname
    age = age if age is not None else stu_o.age
    student.update({Student.fname: fname, Student.lname: lname, Student.age: age})
    db.session.commit()
    return jsonify({'message': f'Student {fname} has been updated'})


# Return the stats about the ticket generation for users
@app.route("/student", methods=["DELETE"])
def remove_student():

    roll_no = request.args.get("rollno")
    if roll_no is None or roll_no == "":
        return jsonify({'message': 'Please provide the roll number'})

    student = db.session.query(Student).filter_by(roll_no=roll_no).first()
    if student is None:
        return jsonify({'message': 'Please provide the valid roll number'})

    Student.query.filter_by(roll_no=roll_no).delete()
    db.session.commit()
    return jsonify({'message': 'Student has been deleted from the system.'})


@app.route("/test")
def test():
    return jsonify({"fname": "Nitish","lname": "Arora","age": 21})