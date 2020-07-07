import pymysql
import config

db = config.DBS
_db_config = db.Config

_conns = {
    db.gqylpy: pymysql.connect(**_db_config.gqylpy),
    db.hello_world: pymysql.connect(**_db_config.hello_world)
}


class MySQL(pymysql.connections.Connection):
    ...


class DBConn:
    def __init__(self, commit: bool = False, database: str = db.gqylpy):
        self.commit = commit
        self.database = database
        _conns[database].ping(reconnect=True)
        self.cur = _conns[database].cursor()

    def execute(self, sql: str) -> int:
        result = self.cur.execute(sql)
        if self.commit:
            _conns[self.database].commit()
        return result

    @property
    def fetchone(self) -> ():
        return self.cur.fetchone()

    @property
    def fetchall(self) -> ((), ...):
        return self.cur.fetchall()

    def __del__(self):
        self.cur.close()


def exec_sql(sql: str, commit: bool = False, fetchone: bool = False, database: str = db.gqylpy) -> int or tuple:
    """
    :param sql:
    :param commit: 是否执行提交操作, 当sql语句为写入时，此参数应为True
    :param fetchone: 为False时返回cursor.fetchall(), 为True时返回cursor.fetchone()
    :param database: 指定要操作的数据库
    :return: 写入操作返回cur.execute(sql), 查询操作返回cursor.fetchall()或cursor.fetchone()
    """
    _conns[database].ping(reconnect=True)
    cur = _conns[database].cursor()
    result = cur.execute(sql)
    commit and _conns[database].commit()
    return result if commit else \
        cur.fetchone() if fetchone else cur.fetchall()
