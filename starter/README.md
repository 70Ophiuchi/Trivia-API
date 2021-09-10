# Trivia App

A simple Trivia game with numerous questions each bounded to a category, this project is a part of the Udacity Full Stack Development Course.

This project follows the PEP8 Style Guidelines

# Getting Started

* Prerequisites
  * Python 3.x.x +
  * Node.js
  * An IDE to Run and Edit the code
  * A web browser to use the APIs, Google Chrome is preferred
  * Basic knowledge of python, APIs, and JavaScript

* Base URL: localhost:5000

* How to run the backend?
  * While in the Trivia API directory, nstall the required libraries and dependencies by running:
   ```
   cd starter && cd backend && pip3 install -r requirements.txt
   ```
   OR
   ```
   cd starter && cd backend && pip install -r requirements.txt
   ```
  * While in the backend directory, run the backend server by running this in your command line:
   ```
   export FLASK_APP=flaskr && export FLASK_ENV=development && flask run
   ```
* How to run the frontend?
  * While in the front end directory, run the front end by running this in your command line:
  ```
  npm install && npm start
  ```

* How to run tests?
  * To run tests locally, cd into the backend directory and run the test_flaskr.py file:
  ```
  cd backend && python test_flaskr.py
  ```
  OR
  ```
  cd backend && python3 test_flaskr.py
  ```

* API Endpoints

  * This project includes various API endpoints, each referring to a different resource and CRUD operation in the backend database.

  * GET /categories
    * To get a list of all the categories
    * BODY: not required
    * RESPONSE: 
    ```
    categories: Science, Art, ...
    ```

  * GET /questions?page=[page_number]
    * To get a list of all the questions
    * BODY:
    ```
    {
        category: science
    }
    ```
    * RESPONSE: 
    ```
    {
        'questions': "List of Questions",
        'total_questions': "Total number of questions in the database",
        'current_category': "Current category",
        'categories': "All categories"
    }
    ```

  * DELETE /questions?[id]
    * To delete a question
    * BODY: Not required

    * RESPONSE: 
    ```
    {
        'status_code': 200
    }
    ```

  * POST /questions
    * To create a new question OR search for a question
    * BODY:
    ```
    {
        "question": "test_question",
        "answer": "test_answer"
        "category": "test_category",
        "difficulty": "test_difficulty"
    }
    OR
    {
        "search": "Search Term"
    }
    ```
    * RESPONSE: 
    ```
    {
        'status_code': 200
    }
    ```
    OR
    {
        "questions": "Search Results",
        "total_questions": "Number of total questions in the database",
        "current_category": "Current Category"
    }

  * GET /category/[id]/questions
    * To get questions by category
    * BODY: Not required

    * RESPONSE: 
    ```
    {
        'questions': "List of Questions",
        'total_questions': "Total number of questions in the database",
        'current_category': "Current category"
    }
    ```

  * POST /quizzes
    * To play the Trivia API game
    * BODY:
    ```
    {
        "category": science
    }
    ```
    * RESPONSE: 
    ```
    {
        'questions': "Random Question",
        'current_category': "Current category"
    }
    ```

  * Errors
    
    * Errors you may run into while running this program.

    * In case of an error, the app will return a useful error message:
      ```
      "success": False,
      "message": "ERROR MESSAGE"
      "error_code": ERROR_CODE
      ```

      * 404: Resource not found
      * 422: Unprocessable
      * 400: Bad Request
      * 405: Method not allowed
      * 408: Request timed out
      * 500: Internal server error

    * If there's no error, the status code will be 200: OK

