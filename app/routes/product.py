from fastapi import APIRouter,status,Query
from app.schemas.products import ProductCreate
from app.db import products_collection
from bson import ObjectId

router=APIRouter()

@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_product(product:ProductCreate):
    try:
        result=await products_collection.insert_one(product.dict())
        return {"id":str(result.inserted_id)}
    except Exception as e:
        print('Error',e)
        return {"error":str(e)}

@router.get('/',status_code=status.HTTP_200_OK)
async def list_product(name:str=Query(None),size:str=Query(None),limit:int=10,offset:int=0):
    query={}
    if name:
        query["name"]={"$regex":name,"$options":"i"}
    if size:
        query["sizes"]={"$elemMatch":{"size":size}}
    result=products_collection.find(query).skip(offset).limit(limit)
    data=[]
    async for doc in result:
        data.append({
            "id": str(doc["_id"]),
            "name": str(doc["name"]),
            "price": str(doc["price"])
        })
    return {
        "data":data,
        "page":{
            "next":str(offset+limit),
            "limit":limit,
            "previous":str(offset-limit)
        }
    }
    