# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy.orm import sessionmaker
from shiyanlougithub.models import Repository, engine
import re

class ShiyanlougithubPipeline(object):

    def process_item(self, item, spider):

        item['update_time'] = datetime.strptime(item['update_time'], '%Y-%m-%dT%H:%M:%SZ')

        item['commits'] = int(re.sub('\D','',item['commits']))
        item['branches'] = int(item['branches'])
        item['releases'] = int(item['releases'])
        self.session.add(Repository(**item))
        return item

    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self,spider):
        self.session.commit()
        self.session.close()



