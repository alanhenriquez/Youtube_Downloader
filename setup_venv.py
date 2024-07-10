import os
import shutil
import subprocess
import sys

def main():
    # Define the files and directories to keep
    items_to_keep = ['downloader.py', 'README.md', 'setup_venv.py', '.git']
    current_dir = os.path.dirname(os.path.abspath(__file__))
    temp_venv_dir = os.path.join(current_dir, 'venv_downloader_temp')

    # Delete all contents except the files and directories to keep
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if item not in items_to_keep:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

    # Create a new virtual environment in a temporary directory
    subprocess.check_call([sys.executable, '-m', 'venv', temp_venv_dir])

    # Install required packages in the new virtual environment
    subprocess.check_call([os.path.join(temp_venv_dir, 'Scripts', 'pip'), 'install', 'pytube', 'colorama'])

    # Move contents of the new virtual environment back to the current directory
    for item in os.listdir(temp_venv_dir):
        shutil.move(os.path.join(temp_venv_dir, item), os.path.join(current_dir, item))

    # Remove the temporary virtual environment directory
    os.rmdir(temp_venv_dir)

    print("Entorno virtual recreado exitosamente.")

if __name__ == '__main__':
    main()
