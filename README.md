# Covid-19 test upload system

This system has been created using Django and Web Scraping technology. It is specially designed for Corona tests which are done in Turkish Republic of Northern Cyprus.

# How to use the system
The system is developed using Django version 4.0.2. There are some more packages required to be installed on your system which are listed below:
  1. Selenium
  2. Webdriver-manager
  3. Pillow

After installing those libraries create a superuser in Django using "python manage.py createsuperuser". Provide the username, email and password for the admin account. 

Then by running the project using "python manage.py runserver", you can open the project on your web browser. From the header select admin, then fill the login form using infomation you have provided. 

In admin panel, find the Profile table. Create a new Profile using "std1" user or you may create another user. The profile requires the passport or National ID. It is important to be correct because it will be used in test result evaluation process.

After creating the profile account, you should log out from admin account and go back to the user login page. Enter the username ("std1" if you have not created a new user with password of "std1password".) By logging in "Covid-19 Test" tab will appear. In there you can insert the barcode number of the test and within a few seconds it will give you the results back.

# How to generate the Secret Key
You should generate yout own secret key by using the following code and replace the content in the quotation.
Use 'python manage.py shell' in your terminal
Write the following commands sequentialy:
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()

Then copy the output of 'print(get_random_secret_key())' and paste it in Portal->settings.py as the value of SECRET_KEY variable.

#Limits
As mentioned this system is valid only for tests that had been done in TRNC.

