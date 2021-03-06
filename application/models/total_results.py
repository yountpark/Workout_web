from application import db
import datetime


class TotalResults(db.Model): # 매번 운동 할 때마다 기록하는 값 ==> 전체 사람의 데이터
    __table_name__ = 'total_results'

    google_id = db.Column(db.String(30), primary_key=True)
    time = db.Column(db.DateTime(), primary_key=True, default=datetime.datetime.now())
    # (datetime.datetime.now().isoformat() + 'Z')[:10] + ' ' + (datetime.datetime.now().isoformat() + 'Z')[11:16]
    count = db.Column(db.Integer(), nullable=False)
    #accuracy = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return "Google ID : %r  /  시간 : %r   /  개수 : %r  /  정확도 : %r  /  운동 종류 : %r" % (self.google_id, self.time, self.count, self.accuracy, self.type)

    def get_id(self):
        return self.id

    def get_time(self):
        return self.time

    def get_count(self):
        return self.count

    def get_accuracy(self):
        return self.accuracy

    def get_type(self):
        return self.type
