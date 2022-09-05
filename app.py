from flask import Flask

from bp import bp_Athena, bp_Clickhouse, bp_Oracle, bp_Sqlite, bp_SQLserver, bp_Doris, bp_Redshift, bp_Mysql, bp_Impala, bp_Kylin, bp_SparkSQL, bp_Postgres
from database import init_db
from database import db_session

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/ping")
def ping():
    return {
        "success": True
    }


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# 注册蓝图
app.register_blueprint(bp_Sqlite.bp)
app.register_blueprint(bp_Clickhouse.bp)
app.register_blueprint(bp_Mysql.bp)
app.register_blueprint(bp_Oracle.bp)
app.register_blueprint(bp_Postgres.bp)
app.register_blueprint(bp_SparkSQL.bp)
app.register_blueprint(bp_SQLserver.bp)
app.register_blueprint(bp_Kylin.bp)
# meta问题
app.register_blueprint(bp_Athena.bp)
# 尚未测试
app.register_blueprint(bp_Doris.bp)
app.register_blueprint(bp_Redshift.bp)
app.register_blueprint(bp_Impala.bp)

init_db()

if __name__ == '__main__':
    # init_db()
    app.run()
