from flask import Blueprint, url_for, redirect, request, render_template, flash
from appoms import User, Service

provider = Blueprint('provider', __name__)

@provider.route('/providers/list', methods=['GET'])
def list_providers():
    providers = User.query.filter_by(roles='provider').all()
    if providers:
        return render_template('users/list_providers.html', providers=providers)


@provider.route('/provider/view', methods=['GET'])
def get_provider():
    provider_name = request.args.get('provider_name')
    print(provider_name)
    user = User.query.filter_by(username=provider_name).first()
    provider_services = Service.query.filter_by(user_id=user.id).all()
    print(provider_services)
    if user:
        return render_template('users/provider.html', user=user, services=provider_services)
    flash('Provider not in database', 'danger')
    return "No data too"



