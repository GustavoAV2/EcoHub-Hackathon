import json
from flask import Blueprint, render_template
from app.actions.garbage_actions import get_garbage, get_garbage_by_id
from app.actions.cooperative_actions import get_cooperative, get_cooperative_by_id

actions_views = Blueprint('views', __name__)


# Templates
@actions_views.route('/garbage', methods=['GET'])
def view_get_garbage():
    # _json = request.get_json()
    return get_garbage()


@actions_views.route('/cooperative', methods=['GET'])
def view_get_cooperative():
    # _json = request.get_json()
    return get_cooperative()


@actions_views.route('/vote/<id>', methods=['GET'])
def view_get_cooperative():
    # _json = request.get_json()
    return get_cooperative()

