from multiprocessing import context
from flask import Blueprint, render_template, abort
from rest_app.core.models import Order, OrderItem
from rest_app.crud.models import Table, Product
from rest_app.core.utils import change_table_status, create_order

core = Blueprint(
    'core',
    __name__,
    template_folder='templates',
)

@core.route('/', methods=['GET'])
def index():
    return render_template('core/home.html')


@core.route('/list-tables/<string:status>', methods=['GET'])
def list_tables(status):
    # dict_status: use to reder tables depends on the status active or nonactive, 
    # I decided to use it for not to duplicate code...
    dict_status = { 
        'active': True,
        'nonactive': False,
    }
    
    if status not in list(dict_status.keys()): # this route only have 2 options to work
        abort(404) 
    # Using dict_status[status] to determinate the table status
    tables = Table.query.filter_by(is_active=dict_status[status]).order_by(Table.table_name).all()
    context = {
        'tables': tables,
    }
    return render_template('core/list_tables.html', **context)



@core.route('/manage-tables')
def manage_tables():
    return render_template('core/manage_tables.html')

@core.route('/open-new-table/<int:id>', methods=['GET', 'POST'])
def open_new_table(id):
    change_table_status(id)
    order = create_order(id)
    order_items = OrderItem.query.filter_by(order_id=order.id).all()
    context = {
        'order': order,
        'table_id': id,
        'order_items': order_items,
    }
    return render_template('core/new_table.html', **context)


@core.route('/active-tables', methods=['GET', 'POST'])
def active_tables():
    return render_template('core/active_tables.html')


@core.route('/billing', methods=['GET', 'POST'])
def billing():
    ## Do not dele this
    # bill = OrderItem.query\
    #         .join(Product, OrderItem.product_id==Product.id)\
    #         .add_columns(
    #             OrderItem.order_id,
    #             Product.name,
    #             OrderItem.quantity,
    #             Product.price,
    #         )\
    #         .filter(OrderItem.order_id==1)\
    #         .filter(Order.id==OrderItem.order_id).all()

    # for i in bill:
    #     print("Order Id:", i.order_id,
    #             "| Table id:", i.table_id,
    #             "| Product Name:", i.name,
    #             "| Quantity:", i.quantity)

    bill = {}

    return render_template('core/billing.html', bill=bill)
