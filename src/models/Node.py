from src.config import db


class Node(db.Model):
    __tablename__ = 'nodes'
    
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    
    options = db.relationship('Option', secondary='node_options', back_populates='nodes')
