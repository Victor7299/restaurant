from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import InputRequired

class ProductForm(FlaskForm):
    name = StringField(
        label='Product Name',
        validators=[
            InputRequired(),
        ],
    )
    price = DecimalField(
        label='Price',
        validators=[
            InputRequired()
        ],
        places=2,
    )


class TableForm(FlaskForm):
    table_name = StringField(
        label='Table Name',
        validators=[
            InputRequired(),
        ],
    )
