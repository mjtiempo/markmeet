# markmeet
Meeting Manager for Jitsi using Token Auth

Follow the steps below to install markmeet

Download markmeet
`git clone https://github.com/mjtiempo/markmeet.git`
`cd markmeet`

Setup Virtual Environment and install dependencies
`python3 -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

Configure Environment variables
`cp env-example .env`

Initialize Database
`python app/manage.py db init`
`python app/manage.py db migrate`
`python app/manage.py db upgrade`

Start the app
`python app/wsgi.py`
