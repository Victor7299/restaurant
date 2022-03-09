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
    order_item = db.relationship('OrderItem', backref='product')

    def __str__(self) -> str:
        return f'Product: {self.name}'
    def __repr__(self) -> str:
        return f'Product: {self.name}'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orders = db.relationship('OrderItem', backref='order')

    def __str__(self) -> str:
        return f'Order #{self.id}'
    def __repr__(self) -> str:
        return f'Order #{self.id}'

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, default=1)

    def __str__(self) -> str:
        return f'Product: {self.product_id} X {self.quantity}'
    def __repr__(self) -> str:
        return f'Product: {self.product_id} X {self.quantity}'
    


# Routes

@app.get('/')
def home():
    bill = Product.query\
            .join(OrderItem, Product.id==OrderItem.id)\
            .add_columns(Product.name, OrderItem.quantity)\
            .filter(OrderItem.order_id==1).all()

    return render_template('home.html', bill=bill)


@app.route('/open-new-table', methods=['GET', 'POST'])
def new_table():
    return render_template('new_table.html')


@app.route('/active-tables', methods=['GET', 'POST'])
def active_tables():
    return render_template('active_tables.html')


@app.route('/billing', methods=['GET', 'POST'])
def billing():
    return render_template('billing.html')


if __name__ == '__main__':
    app.run(debug=True)