from website import create_app

app = create_app()

if __name__ == '__main__': # only True when running this file
    app.run(debug=True) # debug: everytime change the python code, re-run the web server