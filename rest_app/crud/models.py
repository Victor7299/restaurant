from rest_app.extensions import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    price = db.Column(db.Numeric(10,2), default=0.0)
    # order_item = db.relationship('OrderItem', backref='product')

    def __str__(self) -> str:
        return f'Product: {self.name}'
    def __repr__(self) -> str:
        return f'Product: {self.name}'



class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String(100), unique=True)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    # order = db.relationship('Order', backref='order')

    def __str__(self):
        return f'Table: {self.table_name}'
    def __repr__(self):
        return f'Table: {self.table_name}'


class TypePayment(db.Model):
    __tablename__ = 'type_payments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # order = db.relationship('Order', backref='order')

