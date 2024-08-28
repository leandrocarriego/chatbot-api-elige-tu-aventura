from src.config import db

node_options = db.Table('node_options',
    db.Column('node_id', db.Integer, db.ForeignKey('nodes.id'), primary_key=True),
    db.Column('option_id', db.Integer, db.ForeignKey('options.id'), primary_key=True)
)
