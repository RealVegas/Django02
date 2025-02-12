import os


if __name__ == '__main__':
    os.chdir('web_project')
    os.system('python manage.py runserver')