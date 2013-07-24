from . import app

app.config.update(
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db',
    CHECKOUT_ROOT='/home/phil/checked-out/',
)
