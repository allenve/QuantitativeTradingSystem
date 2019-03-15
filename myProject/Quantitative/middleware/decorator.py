from functools import wraps

def logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(session)
        if session.get('sessionid') is not None:
            return f(*args, **kwargs)
        else:
            flash('Please log in first.', 'error')
            return redirect(url_for('login'))
    return decorated_function