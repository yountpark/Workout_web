from application import db

class User(db.Model):
    __table_name__ = 'user'

    google_id = db.Column(db.String(30), primary_key=True)
    age = db.Column(db.Integer(), nullable=False)
    sex = db.Column(db.Boolean(), nullable=False) # 0 : Male, 1 : Female
    height = db.Column(db.Integer(), nullable=True)
    weight = db.Column(db.Integer(), nullable=True)

    def __repr__(self):
        return "Google ID : %r  /  나이 : %r  /  성별 : %r" % (self.google_id, self.age, ("Male" if self.sex == 0 else "Female"))

    def get_id(self):
        return self.id

    def get_google_id(self):
        return self.google_id

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex