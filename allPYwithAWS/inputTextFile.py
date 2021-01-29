import argparse # argparse is a built in python package, we add it with an import statement
import boto3

def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input("The Quick Brown Fox")

if __name__=="__main__":
    main()
