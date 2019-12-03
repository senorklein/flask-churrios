from api.dbobjects.dbuser import User
from api.containers.cuser import CUser

def get_user_uuid(uuid):
    return CUser(User.query.filter_by(uuid=uuid).first())







