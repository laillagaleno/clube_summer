from sqlalchemy import Column,Integer, Float, String
from src.infra.sqlalchemy.config.database import Base


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True,index=True)
    name =Column(String)
    cpf= Column(String)
    birth_date = Column(String)
    main_phone=Column(String)
    secondary_phone=Column(String)
    email = Column(String, unique=True, index=True)
    intagram_url=Column(String)

class Product(Base):
    __tablename__ = 'product'


    id = Column(Integer, primary_key=True,index=True)
    model= Column(String(50))
 #     image: Union[List[Image], None] = None
#     add: Optional[Add] = 'None'
#     color: Set[str] = set()
    color=Column()
    price= Column(Float)
    description = Column(String, index=True)
    





    