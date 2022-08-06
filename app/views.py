from flask import render_template, redirect, Blueprint

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/create')
def update():
    # add code here
    return redirect('/')


@main_blueprint.route('/update')
def update():
    # add code here
    return redirect('/')

