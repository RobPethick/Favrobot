from lib.app.app import App
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="the email address to log in to Favro with")
    parser.add_argument("password", help="the password to log in to Favro with")
    parser.add_argument("organization_id", help="the id of the Favro organization")
    parser.add_argument("collection_name", help="the name of the Favro collection")
    args = parser.parse_args()

    app = App(args.email, args.password, args.organization_id)
    app.createWeeklyBoard(args.collection_name)

    if(app.success):
        print("App completed successfully")
    else:
        print("App failed")

if __name__ == "__main__":
   main()
