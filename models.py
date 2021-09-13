from flask_sqlalchemy import SQLAlchemy


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
db = SQLAlchemy()

#
class Plants(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    scientific_name = db.Column(db.String(), nullable=True)
    primary_color = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f''' ||| ---- >>> Plants :
            ID -> {self.id}
            name -> {self.name}
            scientific_name -> {self.scientific_name}
            primary_color -> {self.primary_color}
        <<<<< ----- |||'''
