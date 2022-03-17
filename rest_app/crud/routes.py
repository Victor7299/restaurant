from flask import Blueprint


crud = Blueprint(
    'crud',
    __name__,
    url_prefix='/crud',
    template_folder='templates',
)

@crud.route('/', methods=['GET'])
def index():
    return '<h1>CRUD</h1>'