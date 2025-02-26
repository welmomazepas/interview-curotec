from fastapi import FastAPI
from sqlalchemy import create_engine, String, Float, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

db_engine = create_engine("sqlite:///db1.db", echo=True)


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)


Base.metadata.create_all(db_engine)

app = FastAPI()


@app.post("/")
async def create_item(request: dict):
    try:
        with Session(db_engine) as session:
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


@app.get("/")
async def get_all_items():
    try:
        with Session(db_engine) as session:
            items_query = session.query(Item)
                        
            return items_query.all()
    except Exception as error:
        print(error)
        return {"message": "Error"}


@app.get("/{item_id}")
async def get_by_item_id(item_id: int):
    try:
        with Session(db_engine) as session:
            return session.query(Item).filter(Item.id == item_id).first()
    except Exception as error:
        print(error)
        return {"message": "Error"}


@app.put("/{item_id}")
async def update_item(item_id: int, request: dict):
    try:
        with Session(db_engine) as session:
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


@app.delete("/{item_id}")
async def delete_item(item_id: int):
    try:
        with Session(db_engine) as session:
            item = session.query(Item).filter(Item.id == item_id).first()
            session.delete(item)
            session.commit()
    except Exception as error:
        print(error)
        return {"message": "Error"}
