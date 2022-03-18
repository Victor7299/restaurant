from flask import Blueprint, render_template, url_for, redirect
from sqlalchemy.exc import IntegrityError
from rest_app.crud.froms import ProductForm, TableForm
from rest_app.crud.models import Table, Product
from rest_app.extensions import db


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
        new_table = Table(table_name=table_name)
        db.session.add(new_table)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print('Error: ', e)
        return redirect(url_for('crud.create_table'))

    return render_template('crud/create_table.html', **context)


@crud.route('/create-product', methods=['GET', 'POST'])
def create_product():
    products = Product.query.all()

    product_form = ProductForm()

    context = {
        'products': products,
        'product_form': product_form,
    }

    if product_form.validate_on_submit():
        product_name = str(product_form.name.data).upper()
        price = product_form.price.data
        new_product = Product(name=product_name, price=price)
        db.session.add(new_product)
        try:
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
        return redirect(url_for('crud.create_product'))

    return render_template('crud/create_product.html', **context)