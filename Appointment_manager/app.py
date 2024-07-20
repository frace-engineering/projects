from appoms import create_app, db
from appoms.models.users import Role
from flask_sqlalchemy import SQLAlchemy

app = create_app()
with app.app_context():
    if not Role.query.filter_by(name='user'):
        user_role = Role(name='user')
        db.session.add(user_role)
    if not Role.query.filter_by(name='user'):
        provider_role = Role(name='provideer')
        db.session.add(provider_role)
    if not Role.query.filter_by(name='user'):
        admin_role = Role(name='admin')
        db.session.add(admin_role)
    db.session.commit()

if __name__ == "__main__":
    app.run(port=4000, host="0.0.0.0", debug=True)
