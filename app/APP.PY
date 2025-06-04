from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

router = APIRouter(prefix="/items", tags=["Items"])

# ------------------------------
# Pydantic model
# ------------------------------
class Item(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

# ------------------------------
# In-memory database (for demo)
# ------------------------------
db = {}

# ------------------------------
# CREATE
# ------------------------------
@router.post("/", response_model=Item)
def create_item(item: ItemCreate):
    item_id = str(uuid4())
    new_item = Item(id=item_id, **item.dict())
    db[item_id] = new_item
    return new_item

# ------------------------------
# READ (Get all)
# ------------------------------
@router.get("/", response_model=List[Item])
def get_all_items():
    return list(db.values())

# ------------------------------
# READ (Get by ID)
# ------------------------------
@router.get("/{item_id}", response_model=Item)
def get_item(item_id: str):
    item = db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# ------------------------------
# UPDATE
# ------------------------------
@router.put("/{item_id}", response_model=Item)
def update_item(item_id: str, update: ItemUpdate):
    item = db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    updated_data = item.dict()
    update_dict = update.dict(exclude_unset=True)
    updated_data.update(update_dict)
    
    updated_item = Item(**updated_data)
    db[item_id] = updated_item
    return updated_item

# ------------------------------
# DELETE
# ------------------------------
@router.delete("/{item_id}")
def delete_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"message": "Item deleted successfully"}