from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

db = 'sqlite:///:memory:'
engine = create_engine(db)
Base = declarative_base()
class User(Base):
    __tablename__ = 'userPermissions'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

    def full_name(self):  # フルネームを返すメソッド
        return "{self.first_name} {self.last_name}"

SessionClass = sessionmaker(engine)  # セッションを作るクラスを作成
session = SessionClass()

user_a = User(first_name="first_a", last_name="last_a", age=20)
session.add(user_a)
session.commit()

user_a = User(first_name="first_a", last_name="last_a", age=20)
session.commit()

user_a = session.query(User).get(1)  # 上で追加したuser_id=1のレコード
user_a.age = 10
session.commit()
#session.query(User).filter(User.user_id=1).delete()
