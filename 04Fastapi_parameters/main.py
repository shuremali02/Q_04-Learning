from fastapi import FastAPI,Path,Query,Body
from pydantic import BaseModel

app=FastAPI()
@app.get("/item/{item_id}")
async def read_item(
    item_id:int=Path(
        ...,
        title="the item id ",
        description="any description",
        ge=1

        
    )
):
    return {"item_id":item_id}

@app.get("/items/")
async def read_items(
    q:str|None=Query(
        None,
        title="string query",
        description="string query searching item",
        min_length=3,
        max_length=50
    ),
    skip:int=Query(0,ge=0),
    limit:int=Query(10,le=100)
):   
    return {"q":q,"skip":skip,"limit":limit}

class Item(BaseModel):
    title:str
    description:str|None=None
    price:float

@app.put("/items/validated/{item_id}")
async def update_item(
    item_id:int=Path(..., title="Item id",ge=1),
    q:str|None =Query(None,min_length=3),
    item :Item |None=Body(None,description="Optional item data (JSON body)")
):
    result={"item_id":item_id}
    if q:
        result.update({"q":q})
    if item :
        result.update({"item":item.model_dump()})    

    return result
