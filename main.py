from website import create_app

#to run the server

app = create_app()

if __name__ == '__main__':
  app.run(debug=True)

