from flask import Blueprint, render_template, url_for, redirect
from sqlalchemy.exc import IntegrityError
from rest_app.crud.forms import ProductForm, TableForm
from rest_app.crud.models import Table, Product
from rest_app.extensions import db

from rest_app.crud.utils import crud as _crud


crud = Blueprint(
    'crud',
    __name__,
    url_prefix='/crud',
    template_folder='templates',
)

@crud.route('/', methods=['GET'])
def index():
    return render_template('crud/home.html')

@crud.route('/create-table', methods=['GET', 'POST'])
def create_table():
    tables = Table.query.order_by(Table.table_name).all()

    table_form = TableForm()

    context = {
        'table_form': table_form,
        'tables': tables,
    }

    if table_form.validate_on_submit():
        table_name = str(table_form.table_name.data).upper()
        data = {
            'table_name': table_name,
        }
        _crud(Table, **data)
        return redirect(url_for('crud.create_table'))

    return render_template('crud/create_table.html', **context)

@crud.route('/update-table/<int:id>', methods=['GET', 'POST'])
def update_table(id: int):
    table = Table.query.filter_by(id=id)
    table_form = TableForm()

    context = {
        'table': table.first(),
        'table_form': table_form,
    }

    if table_form.validate_on_submit():
        table_name = str(table_form.table_name.data).upper()
        data = {
            'table_name': table_name,
        }
        _crud(table, method='u', **data)
        return redirect(url_for('crud.create_table'))

    return render_template('crud/update_table.html', **context)

@crud.route('/delete-table/<int:id>', methods=['GET', 'POST'])
def delete_table(id: int):
    table = Table.query.filter_by(id=id)
    _crud(table, 'd')
    return redirect(url_for('crud.create_table'))


@crud.route('/create-product', methods=['GET', 'POST'])
def create_product():
    products = Product.query.order_by(Product.id).all()

    product_form = ProductForm()

    context = {
        'products': products,
        'product_form': product_form,
    }

    if product_form.validate_on_submit():
        product_name = str(product_form.name.data).upper()
        price = product_form.price.data
        data = {
            'name': product_name,
            'price': price,
        }
        _crud(Product, **data)
        return redirect(url_for('crud.create_product'))

    return render_template('crud/create_product.html', **context)


@crud.route('/update-product/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    product = Product.query.filter_by(id=id)
    product_form = ProductForm()

    context = {
        'product': product.first(),
        'product_form': product_form,
    }

    if product_form.validate_on_submit():
        product_name = str(product_form.name.data).upper()
        price = product_form.price.data
        data = {
            'name': product_name,
            'price': price,
        }
        _crud(product, method='u', **data)
        return redirect(url_for('crud.create_product'))

    return render_template('crud/update_product.html', **context)

@crud.route('/delete-product/<int:id>')
def delete_product(id:int):
    product = Product.query.filter_by(id=id)
    _crud(product, 'd')
    return redirect(url_for('crud.create_product'))