import os
import argparse
from art import tprint
import uvicorn


def main(args):
    tprint('API - VC MASTER')
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='API - VC MASTER')
    parser.add_argument('--port', type=str, dest='port', help='Port ', default='5000')
    main(parser.parse_args())
