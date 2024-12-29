import os
import subprocess
import sys


def create_and_activate_venv(venv_dir=".venv"):
    """
    Create and activate a virtual environment.

    Args:
        venv_dir (str): Directory for the virtual environment (default: ".venv").

    Returns:
        None
    """
    if not os.path.exists(venv_dir):
        try:
            print(f"Creating virtual environment in {venv_dir}...")
            subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
            print(f"Virtual environment {venv_dir} created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating virtual environment: {e}")
    else:
        print(f"Virtual environment {venv_dir} already exists.")


def activate_venv(venv_dir=".venv"):
    """
    Activate the virtual environment.

    Args:
        venv_dir (str): Directory of the virtual environment (default: ".venv").

    Returns:
        None
    """
    if os.name == "nt":  # Windows
        activate_script = os.path.join(venv_dir, "Scripts", "activate")
    else:  # macOS/Linux
        activate_script = os.path.join(venv_dir, "bin", "activate")

    try:
        print(f"Activating virtual environment: {activate_script}")
        if os.name == "nt":
            subprocess.run([sys.executable, "-m", "venv", "--activate"], check=True)
        else:
            subprocess.run(["source", activate_script], check=True)
        print("Virtual environment activated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error activating virtual environment: {e}")


def update_pip_in_venv(venv_dir=".venv"):
    """
    Update pip in the virtual environment.

    Args:
        venv_dir (str): Directory of the virtual environment (default: ".venv").

    Returns:
        None
    """
    if os.name == "nt":  # Windows
        pip_path = os.path.join(venv_dir, "Scripts", "pip.exe")
    else:  # macOS/Linux
        pip_path = os.path.join(venv_dir, "bin", "pip")

    try:
        print("Updating pip in the virtual environment...")
        subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
        print("Pip updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating pip: {e}")


def main():
    venv_dir = ".venv"

    create_and_activate_venv(venv_dir)
    update_pip_in_venv(venv_dir)


if __name__ == "__main__":
    main()