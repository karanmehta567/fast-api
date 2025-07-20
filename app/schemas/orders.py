from pydantic import BaseModel
from typing import List

class order_Item(BaseModel):
    product_id:str
    qty:int

class order_create(BaseModel):
    user_id:str
    items:List[order_Item]
    
class Product_details(BaseModel):
    name:str
    id:str

class Order_Item_Out(BaseModel):
    productDetails:Product_details
    qty:int
    
class orderout(BaseModel):
    id:str
    items:List[Order_Item_Out]
    total:float