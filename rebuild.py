from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import and_, asc, desc, or_
import pandas as pd
from tqdm import tqdm
from model import WebpageInfo, WebpageInfoAbs
import os
import time

sqlconn = 'mysql+pymysql://root:1101syw@localhost:3306/youtube_twitter_url?charset=utf8mb4'
vpn = 'SG'
twitter_re_root = ''
twitter_root = 'D:\\Project\\YouTube Twitter URL data\\'


def main():
    engine = create_engine(sqlconn, echo=False, max_overflow=16)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    df = pd.read_csv('./url_list.csv', engine='python')
    url_list = df.iloc[:, 0].values
    data_bar = tqdm(url_list)
    for url in data_bar:
        data_bar.set_description('Processing ' + url)
        webpage_info = WebpageInfo()
        webpage_info.url = url
        webpage_info.landing_page = ''
        webpage_info.intermediate_urls = ''
        webpage_info.html = ''
        webpage_info.text = ''
        webpage_info.vpn = vpn
        webpage_info_abs = WebpageInfoAbs()
        webpage_info_abs.url = url
        webpage_info_abs.landing_page = ''
        webpage_info_abs.intermediate_urls = ''
        webpage_info_abs.vpn = vpn

        id = url.split('/')[-1]
        # landing page url and intermediate urls
        landing_page_file = twitter_re_root + id + '\\' + vpn + '\\' + id + '_landing_page_url.txt'
        if os.path.exists(landing_page_file):
            with open(landing_page_file, 'r', encoding='utf-8') as f:
                webpage_info.landing_page = f.read()
                webpage_info_abs.landing_page = f.read()
        intermediate_urls_file = twitter_re_root + id + '\\' + vpn + '\\' + id + '_redirect_info.txt'
        if os.path.exists(intermediate_urls_file):
            with open(intermediate_urls_file, 'r', encoding='utf-8') as f:
                webpage_info.intermediate_urls = f.read()
                webpage_info_abs.intermediate_urls = f.read()

        # html and text
        html_file = twitter_root + id + '\\' + vpn + '\\' + id + '_page_source.html'
        if os.path.exists(html_file):
            with open(html_file, 'r', encoding='utf-8') as f:
                webpage_info.html = f.read()
        text_file = twitter_root + id + '\\' + vpn + '\\' + id + '_text.txt'
        if os.path.exists(text_file):
            with open(text_file, 'r', encoding='utf-8') as f:
                webpage_info.text = f.read()

        session.add(webpage_info)
        session.commit()
        session.add(webpage_info_abs)
        session.commit()
    session.close()
    engine.dispose()


if __name__ == '__main__':
    main()
