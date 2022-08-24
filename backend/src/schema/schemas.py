import datetime
from pydantic import BaseModel, HttpUrl
from typing import Set, Optional, Union, List
from uuid import uuid4

class Client(BaseModel):
    id: Optional[str] = None
    name: str
    cpf: str
    birth_date: str
    main_phone: str
    secondary_phone:str
    email:str
    instagram_url: HttpUrl

class Address(BaseModel):
    id: uuid4
    client: Client
    street:str
    num: int
    district:str
    city: str
    state: str
    cep:str
    complement: Optional[str] = 'Sem complemento'

class Measure(BaseModel):
    client: Client
    name: str
    bust: Optional[float]='None' #busto
    chest: Optional[float]='None' #torax
    sholder: Optional[float]='None' #ombro
    armhole: Optional[float]='None' #cava
    sleeve: Optional[float]='None' #manga
    cuf:Optional[float]='None' #punho
    waist: Optional[float]='None' #cintura
    hip: Optional[float]='None' #quadril
    thigh: Optional[float]='None' #coxa
    height:Optional[float]='None' #altura


class Order(BaseModel):
    client: Client
    address: Address
    creation_date: datetime.datetime = datetime.now()
    value_freight:float
    value_total:float
    value_entry: float
    status: Optional[str] = 'Em produção'


class Image(BaseModel):
    url: HttpUrl
    name: str
    

class Item_Add(BaseModel):
    name:str
    price:float

class Add(BaseModel):
    id: uuid4
    item_add: Union[List[Item_Add],None] = None
    price: float

class Product(BaseModel):
    id: uuid4
    model: str
    image: Union[List[Image], None] = None
    add: Optional[Add] = 'None'
    color: Set[str] = set()
    price: float
    description: Optional[str] = 'None'
    
class Item(BaseModel):
    products: Union[List[Product], None] = None
    address: Address
    measure: Measure
    quantity: int
    price: float


    

    
