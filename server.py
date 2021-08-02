from web_server import create_server


if __name__ == "__main__":
    server = create_server()
    server.run(debug=True)