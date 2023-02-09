from controllers.user_controller import users
from controllers.pets_controller import pets
from controllers.index_controller import index
from controllers.commands_controller import erase
# from rents_controller import rents


registerable_controllers = [
    users,
    pets,
    index,
    erase
    # rents
]
