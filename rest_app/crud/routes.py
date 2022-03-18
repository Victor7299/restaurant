from flask import Blueprint, render_template
from rest_app.crud.froms import ProductForm, TableForm


crud = Blueprint(
    'crud',
    __name__,
    url_prefix='/crud',
    template_folder='templates',
)

@crud.route('/', methods=['GET'])
def index():
    return render_template('crud/home.html')

@crud.route('/table', methods=['GET', 'POST'])
def create_table():
    table_form = TableForm()

    if table_form.validate_on_submit():
        return 'VALIDATE'

    return render_template('crud/create_table.html', table_form=table_form)

@crud.route('/product', methods=['GET', 'POST'])
def create_product():
    product_form = ProductForm()

    return render_template('crud/create_product.html', product_form=product_form)