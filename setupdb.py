import db


def init():
    dbstring = "create table users (username varchar(100), activity varchar(1000), last_heard_at bigint);"
    db.dbexecute(dbstring, False)

    dbstring = "create table transactions (sender varchar(100), receiver varchar(100), amount float, timestamp bigint, message varchar(1000));"
    db.dbexecute(dbstring, False)
