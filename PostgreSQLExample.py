""" Primeiro o que temos que fazer é instalar o pyPostgreSQL, baixe o pyPostgreSQL, abra a pasta e rode:
                                    $ python ./setup.py install
"""

import postgresql
db = postgresql.open(user = 'usename', database = 'dataname', port = 5432, password = 'secret')
# OR
# db = postgresql.open("pq://user:password@host/name_of_database")

db.execute("CREATE TABLE tb_user (ds_user varchar(20) PRIMARY KEY, ds_passwd text)")

make_tb_user = db.prepare("INSERT INTO tb_user VALUES ($1, $2)")
raise_tb_user = db.prepare("UPDATE tb_user SET ds_passwd = 'new_password' WHERE ds_user = $1")
select_tb_user = db.prepare("SELECT ds_user FROM tb_user")

with db.xact():
	make_tb_user("avelino", "thiago")
	make_tb_user("thiago", "avelino")
	make_tb_user("python", "postgresql")

with db.xact():
	for row in select_tb_user():
		print(row["ds_user"])

raise_tb_user(row["ds_user"], "avelino")
