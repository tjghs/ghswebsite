import sys

from ghswebsite import app

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Please specify a port")
        exit()
    app.run(host="0.0.0.0", port=int(sys.argv[1]))
