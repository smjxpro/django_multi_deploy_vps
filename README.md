# Deploy Multiple Django app on VPS using Nginx and Gunicorn

### _This is a deployment example of multiple Django app (project) using Nginx and Gunicorn. This particular example uses two separate Django app (project) namely `django_lyrics` which is a simple lyrics app and `django_poems` which is a simple poem app. This example also covers the recommended initial project setup in Django apps (Setting up `STATIC` and `MEDIA` roots and URLs, Custom `AUTH_USER_MODEL`, `local_settings.py` to protect secret keys and configurations etc.)_

##

# 

**1. Install Nginx:**

`sudo apt install nginx`

**2. Clone repo:**

`git clone https://github.com/smjxpro/django_multi_deploy_vps.git`

##

## Lyrics app

**1. `cd` into `django_lyrics`:**

**2. Create and activate virtual environment:**

`virtualenv -p python3 venv`

`source venv/bin/activate`

**3. Install requirements:**

`pip install -r requirements.txt`

**4. Create and adjust _`local_settings.py`_ in _`django_lyrics/django_lyrics/`_**

**5. Collect static files:**

`python manage.py collectstatic`

**6. Apply database migrations:**

`python manage.py migrate`

**7. Create a superuser for django-admin:**

`python manage.py createsuperuser`

**8. `cd` into `nginx-gunicorn-deploy-config/django-lyrics`**

**9. Make necessary changes to config files (i.e. update path)**

**10. Copy `lyrics.socket` to `/etc/systemd/system/`**

`sudo cp lyrics.socket /etc/systemd/system/lyrics.socket`

**11. Copy `lyrics.service` to `/etc/systemd/system/`**

`sudo cp lyrics.service /etc/systemd/system/lyrics.service`

**12. Enable and start `lyrics` service**

`sudo systemctl enable lyrics && sudo systemctl start lyrics`

**13. Copy `lyrics` to `/etc/nginx/sites-available/`**

`sudo cp lyrics /etc/nginx/sites-available/lyrics`

**14. Create symlink `/etc/nginx/sites-available/lyrics` to `/etc/nginx/sites-enabled/lyrics`**

`sudo ln -S /etc/nginx/sites-available/lyrics /etc/nginx/sites-enabled/lyrics`

**15. Test the Nginx configurations**

`sudo nginx -t`

**16. Restart Nginx**

`sudo systemctl restart nginx`

**17. Visit `lyrcis_domain` to confirm that everything's working**

##

## Poems app

**1. `cd` into `django_poems`:**

**2. Create and activate virtual environment:**

`virtualenv -p python3 venv`

`source venv/bin/activate`

**3. Install requirements:**

`pip install -r requirements.txt`

**4. Create and adjust _`local_settings.py`_ in _`django_poems/django_poems/`_**

**5. Collect static files:**

`python manage.py collectstatic`

**6. Apply database migrations:**

`python manage.py migrate`

**7. Create a superuser for django-admin:**

`python manage.py createsuperuser`

**8. `cd` into `nginx-gunicorn-deploy-config/django-poems`**

**9. Make necessary changes to config files (i.e. update path)**

**10. Copy `poems.socket` to `/etc/systemd/system/`**

`sudo cp poems.socket /etc/systemd/system/poems.socket`

**11. Copy `poems.service` to `/etc/systemd/system/`**

`sudo cp poems.service /etc/systemd/system/poems.service`

**12. Enable and start `poems` service**

`sudo systemctl enable poems && sudo systemctl start poems`

**13. Copy `poems` to `/etc/nginx/sites-available/`**

`sudo cp poems /etc/nginx/sites-available/poems`

**14. Create symlink `/etc/nginx/sites-available/poems` to `/etc/nginx/sites-enabled/poems`**

`sudo ln -S /etc/nginx/sites-available/poems /etc/nginx/sites-enabled/poems`

**15. Test the Nginx configurations**

`sudo nginx -t`

**16. Restart Nginx**

`sudo systemctl restart nginx`

**17. Visit `poems_domain` to confirm that everything's working**

##

##### _You can deploy as many app you want following above method_
