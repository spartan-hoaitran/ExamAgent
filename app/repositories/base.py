from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column,DateTime
from uuid import uuid4 
from sqlalchemy.dialects.postgresql import UUID
import datetime
 
@as_declarative()
class BaseEntity:
    id =Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    created_at = Column(DateTime,default=datetime.datetime.utcnow)
    updated_at = Column(DateTime,default=datetime.datetime.utcnow)
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        uppercase_indices = [index for index, char in enumerate(cls.__name__) if char.isupper()][1:]
        table_name=cls.__name__.lower()
        count=0
        for index in uppercase_indices:
            index_insert=index+count
            count+=1
            table_name=table_name[:index_insert] + "_" + table_name[index_insert:]
        return table_name