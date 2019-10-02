import os

from .config import SCRIPT_NAME, FOLDER_NAME, OUTPUT_FILE


def run_func(link, commit, number, script=SCRIPT_NAME):
    """Main function, that fit all test conditions.
    Works with environment and use bash commands.

       Args:
           link (str): first positional parameter. Contains link to github repository.
           commit (str): second positional parameter. Contains to git commit mark.
           number (int): third positional parameter. Contains the number that will be passed to obtained script.
           script (str): named parameter. Contains name of the script in obtained repository that should be run.
           This is hardcoded value fot the test.
           Example of link:
               git@github.com:alchemixXx/add_repo_for_darly_solutions.git.
           Example of commit:
               fdfbac7,
               fdfbac7b48f923100e58beae12a2642a109eb475.
           Example of number:
               12,
               17,
               205

       Returns:
           Script returns result of counting. Int type of value.
       """

    os.system(f"""
    mkdir target_folder
    cd target_folder
    git clone {link}
    cd {FOLDER_NAME}
    git checkout {commit}
    # python3 {script} {number} > output.txt
    python3 {script} {number} > {OUTPUT_FILE}
    """)
    with open(f'target_folder/{FOLDER_NAME}/{OUTPUT_FILE}', 'r') as file:
        result = file.readline()
    os.system(f"""
    rm -rf target_folder
    """)
    return int(result)
