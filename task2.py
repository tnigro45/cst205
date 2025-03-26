"""
~ Name: Thomas Nigro
~ Class: CST 205
~ Date: 3/26/205
~ Description:  Creates a "Hello World" Flask app that
                displays a classmate's favorite acronym
                and why it is, using HTML paragraph tags.
"""

"""
import(s)
"""
# import flask
from flask import Flask

# import bootstrap
from flask_bootstrap import Bootstrap5


"""
functions
"""
# main program
def main():

    # create Flask instance
    app = Flask(__name__)

    # create Boostrap instance
    bootstrap = Bootstrap5(app)

    # route - home
    @app.route('/')
    def hello():

        # display title hello
        html_content = "<h1>Hello World from Flask!</h1>"

        # add to it person's acronym
        html_content += ("<p><b>Jacob</b>: WHO - "
                         "World Health Organization; "
                         "is a good organization</p>")

        return html_content

    # start the flask server
    app.run(debug=True)


"""
program start here
"""
if __name__ == "__main__":
    main()

