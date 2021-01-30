from flask import Blueprint

core = Blueprint('core', __name__)


@core.route('/test', methods=['GET'])
def user_register():
    return {'message': 'access'}
