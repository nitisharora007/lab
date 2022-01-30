#Student Record Management (Sqlite)

## Run the application
There are two ways to run the application

### Using Virtual environment, on the machine.
Step 1) Create a virtual environment in the machine
Step 2) Install the packages required using command
    `pip install -r requirements.txt `
Step 3) Create the environment variable
    
    `export FLASK_APP=app`
    `export FLASK_ENV=development`
    `flask run --port 8080`
    
Step 4) Open the browser and navigate to url:
    `http://127.0.0.1:8080`

### Running the docker image in your machine
Step 1) Make sure the docker is running in your machine
    `docker --version`

If the version is printed, then docker daemon is running.

Step 2) Execute the command:
    `docker run -d -p 80:8080 <>`


<b>Assumption</b>: The application is running on port 8080 and the url is http://localhost


### Student List
Send a GET method request to the url: http://localhost:8080/student

### Student Details
Send a GET method request to the url: http://localhost:8080/student?rollno=<rollno_of_student>

### Adding student
Send a POST method request to the url: http://localhost:8080/student with the data as following:

    Header: 'Content-Type: application/json'
    
    Body: {"fname": "Nitish", "lname": "Arora", "age": 21}

### Student Delete
Send a DELETE method request to the url: http://localhost:8080/student?rollno=<rollno_of_student>
