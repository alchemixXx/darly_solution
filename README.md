Test task:
Build a Python3 application that:

- clones a remote git repository into a workspace directory,
- executes/evaluates the containing python file with a number parameter x,
- prints the result (e.g. x^2) and
- cleans up the working directory.

The application should take 3 parameters:
- location of the remote git repository
- git commit reference that should be executed and
- the number x

Unit tests are not required but api documentation is.
There should be a requirements.txt for easy setup and 
the app should be managed in a git repository for the main application and a git repository for the ‘script’.

# Instruction for app installation
### DO THIS IN LINUX/MAC TERMINAL
1. clone repository to target folder:
    - git clone git@github.com:alchemixXx/darly_solution.git
2. create and activate virtual environment:
    - virtualenv -p python3.7 pavlenko
    - source pavlenko/bin/python3.7
3. install all dependencies:
    - cd darly_solution
    - pip install -r requirements.txt
4. run the app:
    - flask run
After that app will be run at https://localhost:5000 (by default).
To check that everything is ok, got to browser and enter https://localhost:5000/ at the url-field.
You should see message "{'Hello world'}"
    
# Instruction for using the app
To use the app you need to use POSTMAN!
Also ssh-access to github should be provided.
1. Enter localhost:5000/ at the url field
2. Choose http-method POST
3. Open body tab.
4. Choose 'raw' and 'JSON(application/JSON)'
5. Enter request body in field below and click on 'SEND'
6. You will see result at the Response field. 


# Example of request body
{
	"link": "git@github.com:alchemixXx/add_repo_for_darly_solutions.git",
	"commit": "fdfbac7",
	"number": 15
}

