from . import app

app.config.update(
    SQLALCHEMY_DATABAE_URI='sqlite://config.sqlite3',
    CHECKOUT_ROOT='/home/phil/checked-out/',
)
