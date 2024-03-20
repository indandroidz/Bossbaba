import os

from app.victus import Victus

def main():
    try:
        os.system("clear")
        app = Victus()
        app.run()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()