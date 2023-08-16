# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from ResolutionManager import environment as env
from ResolutionManager.API.CredentialsManager import CredentialsManager
from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository

import ResolutionManager.executables.make_folders_for_plenary as make_folders

# import environment as env

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_folders.main()

    # doc_repo = DocumentRepository()
    # file_repo = FileRepository()
    #
    # doc_repo.create_file('test 7')
    # print_hi('PyCharm')
    #
    # file_repo.list_files()

    # file_repo.create_folder('ascsu testing')

    # file_repo.move_file_to_folder(file_id='1YoDaD6uqvmisICn0TZzGhNMQdjeYj2Wjt186hDARKS0', folder_id='1p0nw_jsf8nfFIrCDLF6IejKLyngtcYtg')
    # file_repo.copy_file('1YoDaD6uqvmisICn0TZzGhNMQdjeYj2Wjt186hDARKS0')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
