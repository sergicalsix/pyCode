from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

#engine = create_engine("{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}?charset={charset_type})
"""
dialect: DBの種類を指定する．sqlite, mysql, postgresql, oracle, mssqlとか．

driver : DBに接続するためのドライバーの指定をする．指定しなければ，"default" DBAPIになる．

username: DBに接続することができるユーザ名を指定する．
password: DBに接続するためのパスワードを指定する．
host: ホスト名を指定する．localhostとかIPアドレスとか．
port: ポート番号を指定する．指定しなければ，defaultのポート番号になるっぽい？
database接続するデータベース名を指定する．
charset_type文字コードを指定する．utf8とか．
"""
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


Base.metadata.create_all(engine) #Baseを継承しているテーブルの作成
