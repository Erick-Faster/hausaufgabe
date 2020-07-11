from db import db

class AntwortModel(db.Model):

    __tablename__ = 'antworten'

    id = db.Column(db.Integer, primary_key=True)
    antwort = db.Column(db.String(80))
    success = db.Column(db.Boolean())

    def __init__(self, antwort, success):
        self.antwort = antwort
        self.success = success

    def json(self):
        return {
            'id': self.id,
            'antwort': self.antwort,
            'success': self.success}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(antwort=antwort).first() #posso colocar varios filter_by 

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()