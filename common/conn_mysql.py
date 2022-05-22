import pymysql
import settings
from common.logger import log

logger = log()

pymysql.connections.DEBUG = False  # 开启DEBUG


class SQLMysql(object):
    def __init__(self):
        self.conn = pymysql.connect(host=settings.Config.mysql_config['host'],
                                    port=settings.Config.mysql_config['port'],
                                    user=settings.Config.mysql_config['user'],
                                    passwd=settings.Config.mysql_config['passwd'],
                                    db=settings.Config.mysql_config['db'])
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query_one(self, sql, args=None):
        self.cur.execute(sql, args)
        return self.cur.fetchone()

    def query_all(self, sql, args=None):
        self.cur.execute(sql, args)
        return self.cur.fetchall()

    def create_one(self, sql, args=None):
        try:
            # 防止SQL注入
            self.cur.execute(sql, args)
            self.conn.commit()
            return True
        except Exception as e:
            # 异常回滚
            self.conn.rollback()
            # logger_text.error(e)
            return False

    def update_one(self, sql, args=None):
        try:
            self.cur.execute(sql, args)
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            # logger_text.error(e)
            return False
