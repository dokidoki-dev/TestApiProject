import redis
import config.base_config as base_config
from common.logger import log

pool = redis.ConnectionPool(host=base_config.Config.redis_config['host'], port=base_config.Config.redis_config['port'],
                            decode_responses=True, db=base_config.Config.redis_config['db'], password=base_config.Config.redis_config["passwd"])
logger = log()


class RedisClass(object):
    """redis操作类"""

    def __init__(self):
        # 初始化
        self.r = redis.Redis(connection_pool=pool)

    def get(self, key):
        """
        获取redis中的key值
        key：redis中的key
        """
        try:
            n = self.r.get(key)
            return n  # value 或 None
        except BaseException as e:
            logger.error("redis-get-error" + str(e))
            return False

    def set(self, key, value, ex=None):
        """
        设置redis中的key-value值
        key：redis中的key
        value: redis中的value
        ex: 过期时间
        """
        try:
            n = self.r.set(key, value, ex=ex)
            return n  # True 或者 False
        except BaseException as e:
            logger.error("redis-set-error" + str(e))
            return False

    def delete(self, key):
        """
        删除redis中的值
        key：redis中的key
        """
        try:
            n = self.r.delete(key)
            return n  # 0 没有找到 或者 1 成功删除
        except BaseException as e:
            logger.error("redis-set-error" + str(e))
            return False

    def hget(self, name, key):
        """
        获取redis中的key值
        key：redis中的key
        """
        try:
            n = self.r.hget(name, key)
            return n  # value 或 None
        except BaseException as e:
            logger.error("redis-get-error" + str(e))
            return False

    def hset(self, name, key, value):
        """
        设置redis中的hash
        name: redis的name
        key：name对应的hash中的key
        value: name对应的hash中的value
        ex: 过期时间
        """
        try:
            n = self.r.hset(name, key, value)
            return n  # 0 值存在,添加失败 或者 1 添加成功
        except BaseException as e:
            logger.error("redis-set-error" + str(e))
            return False

    def sadd(self, name, value):
        """
        设置redis中的key值
        name: 集合中的名字
        value：集合中的value
        """
        try:
            n = self.r.sadd(name, value)
            return n  # 0失败 1表示成功
        except BaseException as e:
            logger.error("redis-set-error" + str(e))
            return False

    def smembers(self, name):
        """
        获取redis中集合的所有value
        """
        try:
            n = self.r.smembers(name)
            return n  # 成功返回集合数据 空数据返回set()
        except BaseException as e:
            logger.error("redis-get-error" + str(e))
            return False

    def srem(self, name, values):
        """
        删除集合中的指定元素
        """
        try:
            n = self.r.srem(name, values)
            return n  # 0失败 1表示成功
        except BaseException as e:
            logger.error("redis-set-error" + str(e))
            return False
