from sqlalchemy import Column, Integer, String

from .db import Base


class Activity(Base):
    # https://docs.sqlalchemy.org/en/14/orm/mapping_columns.html
    __tablename__ = 'activity'
    __table_args__ = {'schema': 'innometrics'}
    activity_id = Column('activityid', Integer, primary_key=True)
    browser_title = Column('browser_title', String)
    executable_name = Column('executable_name', String)


def activity_to_dict(activity: Activity):
    return {
        'id': activity.activity_id,
        'executable_name': activity.executable_name,
        'browser_title': activity.browser_title
    }
