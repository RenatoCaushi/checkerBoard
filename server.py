from flask import Flask, render_template, redirect, session, request # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'dsasdasdasdasdsdfa'


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def staticCheckerboard():
    return render_template('index.html')  # Return the string 'Hello World!' as a response



@app.route('/<int:y>')          # The "@" decorator associates this route with the function immediately following
def dynaminCheckerboardByColumns(y):
    return render_template('index2.html', col = y)  # Return the string 'Hello World!' as a response


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def dynaminCheckerboard(x,y, color1, color2):
    return render_template('index3.html', rows=x, col = y, color1=color1, color2=color2) 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
