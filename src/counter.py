from flask import Flask

from src import status

app = Flask(__name__)


COUNTERS = {}


# We will use the app decorator and create a route called slash counters.
# specify the variable in route <name>
# let Flask know that the only methods that is allowed to called
# on this function is "POST".
@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS
    if name in COUNTERS:
        return {"Message": f"Counter {name} already exists"}, status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


@app.route('/counters/<name>', methods=['DELETE'])
def delete_counter_successful(name):
    """Delete a counter"""
    global COUNTERS
    app.logger.info(f"Request to delete counter: {name}")
    if name in COUNTERS:   # check if exists before deleting
        return {"Message": f"Counter {name} does not exist"}, status.HTTP_409_CONFLICT
    del COUNTERS[name]
    return "", status.HTTP_404_NOT_FOUND
