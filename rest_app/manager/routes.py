from flask import Blueprint, render_template
from rest_app.crud.models import Table, Order, OrderItem, Product

manager = Blueprint(
    'manager',
    __name__,
    template_folder='templates',
)

@manager.route('/', methods=['GET'])
def index():
    return render_template('manager/home.html')

@manager.route('/open-new-table', methods=['GET', 'POST'])
def new_table():
    return render_template('manager/new_table.html')


@manager.route('/active-tables', methods=['GET', 'POST'])
def active_tables():
    return render_template('manager/active_tables.html')


@manager.route('/billing', methods=['GET', 'POST'])
def billing():
    bill = OrderItem.query\
            .join(Product, OrderItem.product_id==Product.id)\
            .add_columns(
                OrderItem.order_id,
                Product.name,
                OrderItem.quantity,
                Product.price,
            )\
            .filter(OrderItem.order_id==1)\
            .filter(Order.id==OrderItem.order_id).all()

    # for i in bill:
    #     print("Order Id:", i.order_id,
    #             "| Table id:", i.table_id,
    #             "| Product Name:", i.name,
    #             "| Quantity:", i.quantity)

    return render_template('manager/billing.html', bill=bill)
