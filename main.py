from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Models

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Numeric(10,2), default=0.0)


    order_item = db.relationship('OrderItem', backref='product')

    def __str__(self) -> str:
        return f'Product: {self.name}'
    def __repr__(self) -> str:
        return f'Product: {self.name}'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))
    orders = db.relationship('OrderItem', backref='order')
    # tables = db.relationship('OrderItem', backref='table')
    

    def __str__(self) -> str:
        return f'Order #{self.id}'
    def __repr__(self) -> str:
        return f'Order #{self.id}'

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, default=1)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    # table_id = db.Column(db.Integer, db.ForeignKey('table.id'))

    def __str__(self) -> str:
        return f'Product: {self.product_id} X {self.quantity}'
    def __repr__(self) -> str:
        return f'Product: {self.product_id} X {self.quantity}'
    
class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String(20))
    order = db.relationship('Order', backref='order')

    def __str__(self):
        return f'Table # {self.table_name}'
    def __repr__(self):
        return f'Table # {self.table_name}'

# Routes

@app.get('/')
def home():
    bill = Product.query\
            .join(OrderItem, Product.id==OrderItem.id)\
            .add_columns(Product.name, OrderItem.quantity)\
            .filter(OrderItem.order_id==1).all()

    return render_template('home.html')


@app.route('/open-new-table', methods=['GET', 'POST'])
def new_table():
    return render_template('new_table.html')


@app.route('/active-tables', methods=['GET', 'POST'])
def active_tables():
    return render_template('active_tables.html')


@app.route('/billing', methods=['GET', 'POST'])
def billing():
    bill = OrderItem.query\
            .join(Product, OrderItem.product_id==Product.id)\
            .add_columns(
                OrderItem.order_id,
                Order.table_id,
                Product.name,
                OrderItem.quantity,
                Product.price,
            )\
            .filter(OrderItem.order_id==3)\
            .filter(Order.id==OrderItem.order_id).all()

    # for i in bill:
    #     print("Order Id:", i.order_id,
    #             "| Table id:", i.table_id,
    #             "| Product Name:", i.name,
    #             "| Quantity:", i.quantity)

    return render_template('billing.html', bill=bill)


if __name__ == '__main__':
    app.run(debug=True)