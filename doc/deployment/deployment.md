##  Deployment

This project was developed using **Visual Studio Code**, version-controlled with **Git**, and is hosted on **GitHub**. The live application is deployed on **Heroku**.

### 🔧 Deployment Steps

1. **Prepare the Project**
   - Install necessary packages:
     ```bash
     pip install gunicorn whitenoise dj-database-url psycopg2
     pip freeze > requirements.txt
     ```
   - Create a `Procfile` in the root directory with the following content:
     ```bash
     web: gunicorn blog.wsgi
     ```
   - Create a `runtime.txt` file to specify the Python version:
     ```bash
     python-3.12.8
     ```
   - Update `settings.py`:
     - Set `DEBUG = False`
     - Configure `ALLOWED_HOSTS` to include your Heroku app's domain
     - Add `'whitenoise.middleware.WhiteNoiseMiddleware'` to `MIDDLEWARE`
     - Configure static files:
       ```python
       STATIC_URL = '/static/'
       STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
       ```
   - Collect static files:
     ```bash
     python manage.py collectstatic
     ```

2. **Push to GitHub**
   - Initialize Git repository and commit your code:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     ```
   - Create a new repository on GitHub and push your code:
     ```bash
     git remote add origin https://github.com/maggku/cats.git
     git push -u origin master
     ```

3. **Deploy on Heroku**
   - Create a new Heroku app:
     ```bash
     heroku create posts
     ```
   - Set environment variables:
     ```bash
     heroku config:set SECRET_KEY='<the secret key>'
     heroku config:set DEBUG=False
     ```
   - Push code to Heroku:
     ```bash
     git push heroku master
     ```

4. **Run Migrations**
   ```bash
   heroku run python manage.py migrate
