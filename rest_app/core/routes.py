from flask import Blueprint, render_template, abort
from rest_app.crud.models import Table, Product

core = Blueprint(
    'core',
    __name__,
    template_folder='templates',
)

@core.route('/', methods=['GET'])
def index():
    return render_template('core/home.html')

@core.route('/list-active-tables', methods=['GET'])
def list_active_tables():
    tables = Table.query.filter_by(is_active=True).order_by(Table.table_name).all()
    context = {
        'tables': tables,
    }
    return render_template('core/list_tables.html', **context)

@core.route('/list-tables/<string:status>', methods=['GET'])
def list_tables(status):
    dict_status = {
        'active': True,
        'nonactive': False,
    }
    
    if status not in list(dict_status.keys()): abort(404)
    
    tables = Table.query.filter_by(is_active=dict_status[status]).order_by(Table.table_name).all()
    context = {
        'tables': tables,
    }
    return render_template('core/list_tables.html', **context)



@core.route('/manage-tables')
def manage_tables():
    return render_template('core/manage_tables.html')

@core.route('/open-new-table/<int:id>')
def open_new_table(id):
    return render_template('core/new_table.html')


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
