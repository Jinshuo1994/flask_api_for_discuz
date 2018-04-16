# coding: utf-8
from sqlalchemy import Column, Integer, SmallInteger, String, text, Text
from exts import db


class PreUcenterPmIndex(db.Model):
    extend_existing = True
    __tablename__ = 'pre_ucenter_pm_indexes'

    pmid = Column(Integer, primary_key=True)
    plid = Column(Integer, nullable=False, server_default=text("'0'"))


class PreUcenterPmMember(db.Model):
    __tablename__ = 'pre_ucenter_pm_members'

    plid = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    uid = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    isnew = Column(Integer, nullable=False, server_default=text("'0'"))
    pmnum = Column(Integer, nullable=False, server_default=text("'0'"))
    lastupdate = Column(Integer, nullable=False, server_default=text("'0'"))
    lastdateline = Column(Integer, nullable=False, server_default=text("'0'"))