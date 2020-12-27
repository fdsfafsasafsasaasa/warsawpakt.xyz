from paktsite.errors import errors
from paktsite.errors.routes import *

from paktsite.main import main
from paktsite.main.routes import *

from paktsite.upload import upload
from paktsite.upload.routes import *

from paktsite import app

app.register_blueprint(upload)
app.register_blueprint(errors)
app.register_blueprint(main)







