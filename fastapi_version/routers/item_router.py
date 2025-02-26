from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi_version.db_config import get_db
from fastapi_version.models.item_model import Item

router = APIRouter(
    prefix="/items",
    tags=["Items"],
)


@router.post("/")
async def create_item(
    request: dict,
    session: Session = Depends(get_db),
):
    try:

        new_item = Item(
            name=request["name"],
            description=request["description"],
            price=request["price"]
        )
        session.add(new_item)
        session.commit()

        return {"message": "Item Created"}
    except Exception as error:
        print(error)
        return {"message": "Error"}


@router.get("/")
async def get_all_items(session: Session = Depends(get_db)):
    try:
        return session.query(Item).all()
    except Exception as error:
        print(error)
        return {"message": "Error"}


@router.get("/{item_id}")
async def get_by_item_id(item_id: int, session: Session = Depends(get_db)):
    try:
        return session.query(Item).filter(Item.id == item_id).first()
    except Exception as error:
        print(error)
        return {"message": "Error"}


@router.put("/{item_id}")
async def update_item(
    item_id: int, 
    request: dict,
    session: Session = Depends(get_db)
):
    try:
        old_item = session.query(Item).filter(Item.id == item_id).first()
        print(old_item)
        if "name" in request:
            old_item.name = request["name"]
        if "description" in request:
            old_item.description = request["description"]
        if "price" in request:
            old_item.price = request["price"]

        session.add(old_item)
        session.commit()
  
        return old_item
    except Exception as error:
        print(error)
        return {"message": "Error"}


@router.delete("/{item_id}")
async def delete_item(item_id: int, session: Session = Depends(get_db)):
    try:
        item = session.query(Item).filter(Item.id == item_id).first()
        session.delete(item)
        session.commit()
    except Exception as error:
        print(error)
        return {"message": "Error"}
