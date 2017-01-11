import arrow
from app import db


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    first_name = db.StringField(max_lenght=40, required=True)
    last_name = db.StringField(max_lenght=40, required=True)
    password = db.BinaryField(required=True)

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
        return str(self.id)

    def __repr__(self):
        return "data: %r, %r, %r, %r" % (self.email, self.first_name,
                                         self.last_name, self.password)

    meta = {'allow_inheritance': True}


class Note(db.Document):
    time = arrow.utcnow()
    date = db.DateTimeField(default=time.format("YYYY-MM-DD HH:mm"),
                            required=True)
    note = db.StringField(required=True)
    author = db.ListField(db.ReferenceField('User'))

    meta = {'allow_inheritance': True,
            'indexes': ['date'],
            }


class NotePics(Note):
    pics = db.StringField()