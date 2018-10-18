This is a sample of how SSD can be used to detect cars in video cameras

# How to run:

### With docker
if you have docker and docker-compose installed on your machine, run:

    $ cd flask
    $ docker-compose up

and go to [localhost:5555](localhost:5555)

This will serve the website using gunicorn.


### With virtual env
Please run:

    cd flask
    # skip this if you already have virtual env installed
    $ pip install virtualenv

    $ virtualenv <virtualenv_name>
    $ source <virtualenv_name>/bin/activate
    $ pip install -r requirements.txt 
    $ export FLASK_APP=app.py
    $ flask run --host=0.0.0.0

and go to [localhost:5000](localhost:5000)


##TODO

The car detection code is not included in this repo. Only the result of analysis for a sample video.