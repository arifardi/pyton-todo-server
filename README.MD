# Server setup


1. Let's begin by installing Flask in a virtual environment. If you don't have virtualenv installed in your system, you can download it from [Download Virtualenv](https://pypi.python.org/pypi/virtualenv "Google's Homepage")
2. To run this application we have to execute app.py
    * ``$ chmod a+x app.py``
    * ``./app.py``
3. And now you can launch your web browser and type http://localhost:5000 to see this tiny application in action.


# API
``This is how to hit api from terminal``
1. Get All Todo
    * ``curl -i http://localhost:5000/todo``
2. Get One Todo
    * ``curl -i http://localhost:5000/todo/:todo_id``
3. Create Todo
    * ``curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/:todo_id``
4. Update Todo
    * ``curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true, "title": "Updated Title", "description": "Updated Description"}' http://localhost:5000/todo/:todo_id``
5. Delete Todo
    * ``curl -i -X "DELETE" http://localhost:5000/todo/:todo_id``