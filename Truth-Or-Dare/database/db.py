from sqlalchemy import create_engine
from itertools import islice


engine = create_engine('postgresql://postgres:pass@localhost:5432')
connection = engine.connect()

create_player_table = """
CREATE TABLE PLAYER (
    IDPLAYER SERIAL PRIMARY KEY,
    USERNAME VARCHAR(20),
    PASSWORD VARCHAR(50)
)
"""

connection.exec_driver_sql(create_player_table)
connection.exec_driver_sql(
    "INSERT INTO PLAYER (username, password) VALUES ('ejik', '123')"
)

xs = connection.exec_driver_sql("SELECT * FROM player")
print(list(islice(xs, 10)))
