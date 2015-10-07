from random import choice
#gets the choice function from random library

from flask import Flask, render_template, request
#importing the class Flask and the functions render_template and request from flask


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)
#app is an instance of the class Flask


@app.route('/')
# route to handle the landing page of a website.
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')#links the function say_hello to the url extension /hello
def say_hello():
    return render_template("hello.html") 
    #displays hello.html webpage which asks for: user name

@app.route('/greet')#links the function greet_person to the url extension /greet
def greet_person():#starts function greet_person
    player = request.args.get("person")
    #uses .get function to get the user input from the form in which greet is assigned to the form action(hello.html)

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']
        #list of compliments used by comliments variable

    compliment = choice(AWESOMENESS)
    #randomly chooses a word from the list Awesome and assigns it to variable compliments

    return render_template("compliment.html", person=player, compliment=compliment)
    #displays compliment.html page passing in these arguments to the value attribute on that page

@app.route('/game')
def show_game_form():
    # name = request.args.get("yesno")
    value = request.args.get("yesno")
    player = request.args.get("person")

    if value == "no":
        AWESOMENESS = [
            'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
            'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

        compliment = choice(AWESOMENESS)

        return render_template("goodbye.html", person=player, compliment=compliment)
    else: 
        return render_template("game.html", person=player)

@app.route('/goodbye')
def goodbye():
    player = request.args.get("person")
    #value = request.args.get("")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("goodbye.html", person=player, compliment=compliment)



@app.route('/madlib')
def show_madlib():
    noun_value = request.args.get("noun")
    color_value = request.args.get("color")
    adjective_value = request.args.get("adjective")
    player = request.args.get("person")

    return render_template("madlib.html", person=player, noun=noun_value, color=color_value, adjective=adjective_value)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
