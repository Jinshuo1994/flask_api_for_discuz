from exts import db

from sqlalchemy import *
from sqlalchemy.orm import *

def create_pre_ucenter_pm_message(plid_last_digit):
    # engine1 = create_engine('mysql+mysqldb://root:root@192.168.232.146:3306/ultrax')
    metadata = MetaData(db.engine)
    # print dir(engine1)
    # print dir(db.engine)
    # metadata = MetaData(create_engine(db.engine))

    table_name = 'pre_ucenter_pm_messages_%s' % plid_last_digit
    t = Table(table_name, metadata,  Column('pmid', Integer, primary_key=True, server_default=text("'0'"))
                        , Column('plid', Integer, nullable=False, server_default=text("'0'"))
                        , Column('authorid', Integer, nullable=False, server_default=text("'0'"))
                        , Column('message', Text, nullable=False)
                        , Column('delstatus', Integer, nullable=False, server_default=text("'0'"))
                        , Column('dateline', Integer, nullable=False, server_default=text("'0'"))
              )
    # metadata.create_all()
    return map_class_to_some_table(Foo, t, "pre_ucenter_pm_messages_anyname")

def map_class_to_some_table(cls, table, entity_name, **kw):
     newcls = type(entity_name, (cls, ), {})
     mapper(newcls, table, **kw)
     print newcls
     return newcls

class Foo(object):
    pass






