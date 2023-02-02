import click
import time
import shutil
import logging
import os


@click.command()
@click.option('--src', required=True, help='Source folder to sync.')
@click.option('--dest', required=True, help='Destination folder to sync.')
@click.option('--interval', required=True, type=int, help='Interval in seconds for syncing the folders.')
@click.option('--log_file', required=True, help='Location and name of the log file')
def sync_folders(src, dest, interval, log_file):
    # Defining the basic config and creating the log file based on user input mapped to log_file
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s:  %(message)s')
    while True:
        try:
            logging.info(f'Syncing folders from {src} to {dest}')
            # Checking if the destination folder exists
            if not os.path.exists(dest):
                # Creating the destination folder
                os.mkdir(dest)
            # Creting a replica of the src folder to the destination folder
            copytree(src, dest)
        except Exception as e:
            logging.error(f'An error occurred while syncing the folders: {e}')
        # Sleep for the remaining sync period and get up
        time.sleep(interval)


def copytree(src, dst):
    """ Iterates through all the files/folders of the directory 'src' and creates an
        exact replica in the 'dest' directory

    :param src: directory in src folder (or the destination folder itself)
    :param dst: directory in destination folder (or the destination folder itself)
    :return: None
    """
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if not os.path.exists(d):
                os.mkdir(d)
            copytree(s, d)
        else:
            shutil.copy(s, d)


if __name__ == '__main__':
    sync_folders()
