from sqlalchemy import Column, String, create_engine, Integer, SmallInteger, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql

Base = declarative_base()


# 定义对象
class WebpageInfoTwitter(Base):
    # 表名
    __tablename__ = 'webpage_info_twitter_all'

    id = Column(mysql.BIGINT, primary_key=True)
    url = Column(String(1000))
    landing_page = Column(String(3000))
    intermediate_urls = Column(Text)
    html = Column(Text)
    text = Column(Text)
    vpn = Column(String(50))


class WebpageInfoTwitterAbs(Base):
    # 表名
    __tablename__ = 'webpage_info_twitter_all_abs'

    id = Column(mysql.BIGINT, primary_key=True)
    url = Column(String(1000))
    landing_page = Column(String(3000))
    intermediate_urls = Column(Text)
    vpn = Column(String(50))
