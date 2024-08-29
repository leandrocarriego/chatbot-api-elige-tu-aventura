from src.config import db

class Option(db.Model):
    __tablename__ = 'options'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    next_node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'), nullable=True)

    nodes = db.relationship('Node', secondary='node_options', back_populates='options')
    next_node = db.relationship('Node', foreign_keys=[next_node_id])
