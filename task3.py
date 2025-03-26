"""
~ Name: Thomas Nigro
~ Class: CST 205
~ Date: 3/26/25
~ Description:  Creates a route to the template of my
                first name and displays my favorite
                acronym there.
"""

"""
import(s)
"""
# import flask
from flask import Flask, render_template

# import bootstrap
from flask_bootstrap import Bootstrap5

"""
global variable(s)
"""

"""
classes
"""

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

        return "Hello world from Flask!"

    # hello_flask.py
    @app.route('/thomas')
    def t_test():

        return render_template('template.html')

    # start the Flask server
    app.run(debug=True)


"""
program start here
"""
if __name__ == "__main__":
    main()

