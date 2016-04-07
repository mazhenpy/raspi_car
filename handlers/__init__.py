import redis


class RedisDriver:
    def __init__(self):
        self.host = 'localhost'
        self.password = ''
        self.port = 6379

        self._master_12 = None


    @property
    def master_12(self):
        if self._master_12 is None:
            self._master_12 = redis.StrictRedis(host=self.host, password=self.password, port=self.port, db=12,
                                                decode_responses=True)
        return self._master_12
