from fastapi import APIRouter,status
from app.schemas.orders import order_create
from app.db import orders_collection,products_collection
from bson import ObjectId
router=APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_order(order:order_create):
    doc = order.dict()
    doc["items"] = [
        {"product_id":ObjectId(item["product_id"]),"qty":item["qty"]}
        for item in doc["items"]
    ]
    result=await orders_collection.insert_one(doc)
    return {"id":str(result.inserted_id)}
    
@router.get("/{user_id}",status_code=status.HTTP_200_OK)
async def list_order_list(user_id:str,limit:int=10,offset:int=0):
    input=orders_collection.find({"user_id":user_id}).skip(offset).limit(limit)
    data=[]
    
    async for order in input:
        items_out=[]
        total=0.0
        for item in order["items"]:
            product=await products_collection.find_one({"_id":item["product_id"]})
            if product:
                items_out.append({
                    "productDetails": {
                        "name": product["name"],
                        "id": str(product["_id"])
                    },
                    "qty":item["qty"]
                })
                total+=product["price"]*item["qty"]
        data.append({
            "id":str(order["_id"]),
            "items":items_out,
            "total":round(total,2)
        })
    return{
        "data":data,
        "page":{
            "next":str(offset+limit),
            "limit":limit,
            "previous":str(offset-limit)
        }
    }