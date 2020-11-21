from ..base import db


class ProblemTest(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    problem_id = db.Column(db.Integer(), db.ForeignKey('problem.id'), nullable=False)
    problem = db.relationship('Problem')

    _input_data = db.Column(db.String(), nullable=False)
    _output_data = db.Column(db.String(), nullable=False)
    _max_execution_time = db.Column(db.Float(), nullable=False)
    _max_memory_size = db.Column(db.Integer(), nullable=False)
    _points = db.Column(db.Integer, nullable=False)

    def __init__(self):
        pass
