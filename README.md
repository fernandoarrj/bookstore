# How use 

git clone https://github.com/fernandoarrj/bookstore
    
# Backend configuration
cd backend
virtualenv env
source env/bin/active
pip install -r requirements.txt
cd source
python manage.py migrate
python manage.py runserver

# Frontend configuration
cd frontend
npm -i 
npm start
