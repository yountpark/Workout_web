from application import db


class CumulativeResult(db.Model): # 한 사람의 누적 값
    __table_name__ = "cumulative_result"

    google_id = db.Column(db.String(30), primary_key=True)
    times = db.Column(db.Integer(), nullable=False)
    cumulative_count = db.Column(db.Integer(), nullable=False)
    kind = db.Column(db.String(5), primary_key=True)

    def __repr__(self):
        return "Google ID : %r  /  횟수 : %r   /  누적 개수 : %r  /  운동 종류 : %r" % (self.google_id, self.times, self.cumulative_count, self.kind)

    def get_google_id(self):
        return self.google_id

    def get_times(self):
        return self.times

    def get_count(self):
        return self.cumulative_count

    def get_kind(self):
        return self.kind
