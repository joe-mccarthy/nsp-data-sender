import argparse

from app.main import run


def nsp_data_sender():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--configuration", type=str, required=True)
    parser.add_argument("-nsp", "--nsp-configuration", type=str, required=True)
    arguments = parser.parse_args(None)
    run(arguments)


if __name__ == "__main__":
    nsp_data_sender()