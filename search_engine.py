from flask import Blueprint,request
search_engine = Blueprint("search_engine", __name__)

from psycopg_pool import ConnectionPool

"""
                id INTEGER PRIMARY KEY,
                item INTEGER,
                image TEXT,
                name TEXT,
                family TEXT,
                size TEXT,
                locality TEXT,
                note TEXT,
                seller TEXT,
                start_price TEXT,
                current_price TEXT,
                owner TEXT
"""
# 数据库连接配置
pool = ConnectionPool(
    conninfo="postgresql://postgres:Tu1994125@127.0.0.1:5432/postgres",
    min_size=1,
    max_size=50,
    open=True  # 立即开始连接过程
)

@search_engine.route("/")
def search():

    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select * from shellauction limit 1;")
            greeting = cur.fetchone()
            print(greeting)
            return ""


def construct_query(where:str,order:str)->str:
    limit = 50
    kw_map = {
        "nto":f"order by item desc limit {limit}",
        "otn":f"order by item limit {limit}",
        "cpd":f"order by current_price desc limit {limit}",
        "cpu":f"order by current_price limit {limit}",
        "spd":f"order by start_price limit {limit}",
        "spu":f"order by start_price limit {limit}",
    }
    order_fix = kw_map.get(order,'')

    re = f"SELECT item,image,name,family,size,note,seller,start_price,current_price FROM shellauction WHERE "

    return