from sqlalchemy import Table, Date, Boolean, Column, Enum, Binary, Integer, ForeignKey, String

from app.db.base_class import Base


investor_tag = Table('investor_tag', Base.metadata,
                     Column("InvestorID", Integer, ForeignKey("Investor.id")),
                     Column("TagID", Integer, ForeignKey("Tag.id")))
