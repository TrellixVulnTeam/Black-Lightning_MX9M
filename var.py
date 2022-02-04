import os

if ENV := bool(os.environ.get("ENV", "ANYTHING")):
    from heroku_config import Var as config
else:
    from localconfig import config


Var = config
