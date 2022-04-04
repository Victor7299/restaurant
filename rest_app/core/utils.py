from rest_app.extensions import db
from rest_app.crud.models import Table
from rest_app.core.models import Order

def change_table_status(id):
    table = Table.query.get(id)
    table.is_active = not table.is_active

def create_order(table_id):
    order = Order(table_id=table_id)
    try:
        db.session.add(order)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    return order
