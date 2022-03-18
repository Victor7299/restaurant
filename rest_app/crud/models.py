from rest_app.extensions import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Numeric(10,2), default=0.0)
    order_item = db.relationship('OrderItem', backref='product')

    def __str__(self) -> str:
        return f'Product: {self.name}'
    def __repr__(self) -> str:
        return f'Product: {self.name}'


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'))
    is_active = db.Column(db.Boolean, default=True, nullable=False)    
    type_payment = db.Column(db.Integer, db.ForeignKey('type_payments.id'))
    orders = db.relationship('OrderItem', backref='order')

    def __str__(self) -> str:
        return f'Order #{self.id}'
    def __repr__(self) -> str:
        return f'Order #{self.id}'


class OrderItem(db.Model):
    __tablename__ = 'order_item'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, default=1)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    # table_id = db.Column(db.Integer, db.ForeignKey('table.id'))

    def __str__(self) -> str:
        return f'Product: {self.product_id} X {self.quantity}'
    def __repr__(self) -> str:
        return f'Product: {self.product_id} X {self.quantity}'


class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    order = db.relationship('Order', backref='order')

    def __str__(self):
        return f'Table: {self.table_name}'
    def __repr__(self):
        return f'Table: {self.table_name}'


class TypePayment(db.Model):
    __tablename__ = 'type_payments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # order = db.relationship('Order', backref='order')

