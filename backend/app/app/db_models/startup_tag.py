from sqlalchemy import Table, Boolean, Column, Integer, ForeignKey, String, LargeBinary
from app.db.base_class import Base

startup_tag = Table('startup_tag', Base.metadata,
                    Column("StartupID", Integer, ForeignKey("Startup.id")),
                    Column("TagID", Integer, ForeignKey("Tag.id")))
