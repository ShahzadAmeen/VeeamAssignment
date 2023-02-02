import os
from script import copytree
import shutil

""" Testing copytree method used for syncing works if src contains directory 
"""


def _purge_folders(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


base_dir = os.path.join(os.getcwd(), 'playground')
# The src directory
src_temp_dir = os.path.join(base_dir, 'src')
# create dest directory
dest_temp_dir = os.path.join(base_dir, 'dest')


def test_copy_tree_dir():
    _purge_folders(src_temp_dir)
    _purge_folders(dest_temp_dir)
    # Create a temporary directory called 'DirectoryCheck' in the src directory
    temp_dir = os.path.join(src_temp_dir, 'DirectoryCheck')

    os.mkdir(temp_dir)
    copytree(src_temp_dir, dest_temp_dir)
    # assert not result.exception
    # check that the contents of the source folder were copied to the destination folder
    assert os.path.exists(os.path.join(dest_temp_dir, 'DirectoryCheck'))


""" Testing copytree method used for syncing works if src contains file 
"""


def test_copy_tree_file():
    _purge_folders(src_temp_dir)
    _purge_folders(dest_temp_dir)
    # Create a temporary directory called 'DirectoryCheck' in the src directory
    with open(os.path.join(src_temp_dir, 'test.txt'), 'w') as f:
        f.write('test')
    copytree(src_temp_dir, dest_temp_dir)
    # assert not result.exception
    # check that the contents of the source folder were copied to the destination folder
    assert os.path.exists(os.path.join(dest_temp_dir, 'test.txt'))
