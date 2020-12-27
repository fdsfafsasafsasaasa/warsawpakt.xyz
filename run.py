from paktsite import app

import sys

if __name__ == "__main__":
    try:
        if sys.argv[1] == "--debug":
            app.run(debug=True)
    except: 
        app.run()