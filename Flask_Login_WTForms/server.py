from flask import Flask, flash, redirect, render_template, request, url_for, session, abort
from flask_wtf.csrf import CSRFProtect, CSRFError

from forms import AdminLoginForm
from database import check_admin_login


def create_app():
    csrf = CSRFProtect()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "powerful secretkey"
    app.config['WTF_CSRF_SECRET_KEY'] = "powerful csrf secretkey"
    csrf.init_app(app)

    # ----------------------------- #
    # Home Page Route Handler ##### #
    # ----------------------------- #
    @app.route('/', methods=['GET', 'POST'])
    def home_page():

        msg = None
        admin_login_form = AdminLoginForm()
        admin_logged_state = session.get('logged_in', None)

        if request.method == 'POST' and admin_login_form.validate_on_submit():
            admin_id = admin_login_form.admin_id.data
            admin_password = admin_login_form.admin_password.data
            # print(admin_id, admin_password)

            if check_admin_login(admin_id, admin_password):
                session['logged_in'] = True
                return admin_dashboard()
            else:
                msg = 'Failed'

        return render_template('index.html', welcome_title='Sample App', msg=msg, admin_login_form=admin_login_form, admin_logged_state=admin_logged_state)

    # ----------------------------- #
    # Admin Dashboard Route Handler #
    # ----------------------------- #
    @app.route('/admin_dashboard')
    def admin_dashboard():

        if session.get('logged_in'):
            return render_template('admin_dashboard.html')
        else:
            return home_page()

    # ----------------------------- #
    # Country Manager Route Handler #
    # ----------------------------- #
    @app.route('/admin_country_manager')
    def country_manager():
        if session.get('logged_in'):
            return render_template('admin_country_manager.html')
        else:
            return home_page()

    # ----------------------------- #
    # Admin Logout Route Handler ## #
    # ----------------------------- #
    @app.route('/admin_logout')
    def admin_logout():
        session['logged_in'] = False
        session.pop('logged_in', None)
        return home_page()

    # ----------------------------- #
    # Error Handler ############### #
    # ----------------------------- #
    @app.errorhandler(404)
    def not_found(error):
        return render_template('helpers/404.html'), 404

    # ----------------------------- #
    # CSRF Error Handler ########## #
    # ----------------------------- #
    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('helpers/csrf_error.html', reason=e.description), 400

    all_routes = [home_page, admin_dashboard, country_manager,
                  admin_logout, not_found, handle_csrf_error]
    assert type(all_routes) is list

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
