from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from game import Game

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def start_game():
    game = Game()
    return render_template('index.html', game=game)


if __name__ == '__main__':
    app.run()
