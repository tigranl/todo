import time
from flask.ext.login import LoginManager
from app import db, app

login_manager = LoginManager()
login_manager.init_app(app)


class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_lenght=40, required=True)
    last_name = db.StringField(max_lenght=40, required=True)
    password = db.StringField(required=True)

    def __init__(self, email=None, first_name=None,
                 last_name=None, password=None, *args, **kwargs):
        super(db.Document, self).__init__(*args, **kwargs)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

    meta = {'allow_inheritance': True}


class Note(db.Document):
    date = db.DateTimeField(default=time.strftime("%Y-%m-%d %H:%M"), required=True)
    note = db.StringField(required=True)
    author = db.ListField(db.EmbeddedDocumentField('User'))

    meta = {'allow_inheritance': True,
            'indexes': ['date'],
            'ordering': ['date']
            }


class NotePics(Note):
    pics = db.StringField()

if __name__ == "__main__":
    a = User("qwe@qwe.ru", "32", "2", "221")
