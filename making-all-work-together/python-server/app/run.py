from app import app

if __name__ == '__main__':
    print("python server on!")
    app.run(debug=True, port=3000)
