from sqlalchemy.exc import IntegrityError
from rest_app.extensions import db

from flask_sqlalchemy import BaseQuery
from flask_sqlalchemy.model import DefaultMeta

from typing import Union

# def check_model_class(_subclass, _class):
#     try:
#         if not issubclass(_subclass, _class):
#             raise Exception("A db.Model sub class must be given")
#     except Exception as e:
#         print(e)
#     return True

def crud(model: Union[DefaultMeta,BaseQuery], method:str = 'c', **kwargs) -> None:
    """
    args:
        - model: ORM's class  
            - If method is 'c' a db.Model (flask_sqlalchemy.DefaultMeta) must be given
            - If method is 'd' or 'u', a BaseQuery Object must be given (Class.query.filter_by(key=value))
        
    kwargs:
        - method: Used to make operations
            - 'c' : create (default)
            - 'u' : update
            - 'd' : delete 
        - **kwargs : All data needed for creating the model

    """
    if method == 'u':
        # check_model_class(model, db.Model)
        model.update(kwargs)
          
    elif method == 'c':
        model = model(**kwargs)    
        db.session.add(model)     

    elif method == 'd':

        model = model.first()
        db.session.delete(model)

    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
