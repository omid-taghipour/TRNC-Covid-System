from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Covid_Test
from datetime import datetime
from selenium import webdriver
import time
from selenium.common.exceptions import (NoSuchElementException, 
                                        ElementNotInteractableException)
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from django.contrib.auth.models import User
from .models import Profile
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def upload_test(request):
    if request.method == 'POST':
        
        user_obj = User.objects.get(id=request.user.id)
        profile_obj = Profile.objects.get(student=user_obj)

        new_barcode = request.POST['barcode']
        chrome_option = Options()
        chrome_option.add_argument("--headless")
        web = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_option)
        web.get('https://covid-19.gov.ct.tr/')

        time.sleep(1)

        # Finding and Entering the barcode into the related field
        barcode_input = web.find_element(By.XPATH, '//*[@id="barkod"]')
        barcode_input.send_keys(new_barcode)
        # Finding and Clicking on the "Test soncunu ara" button
        test_soncunu_ara = web.find_element(By.XPATH, '//*[@id="ara"]')
        test_soncunu_ara.click()

        try:
            time.sleep(1)
            # Finding and Entering Passport or Kimlik to the related field
            passport_input = web.find_element(By.XPATH, '//*[@id="belge_no"]')
            passport_input.send_keys(profile_obj.passport)
        except (NoSuchElementException, ElementNotInteractableException):
            print("Barcode invalid")

        else:
            time.sleep(2)

            # Finding and Clicking on the "Test soncunu ara" button
            test_soncunu_ara.click()

            # Reading the test result if exist using try exception block
            try:
                date_field = web.find_element(By.CSS_SELECTOR, '#sonuclarForm > div.center > div > h3 > span:nth-child(3)')
                result_field = web.find_element(By.XPATH, '//*[@id="sonuclarForm"]/div[3]/div/h3/span[4]')

            except (ElementNotInteractableException, NoSuchElementException):
                print("Test did not evaluate successfully.")

            except:
                print("An ERROR OCCURRED. TRY AGAIN LATER")

            else:
                # What to do if the test founded on the system
                if result_field.text == "POZİTİF":
                    test_result = "POZITIF"
                elif result_field.text == "NEGATİF":
                    test_result = "NEGATIF"

                test_date_time = date_field.text
                # test_date, test_time = test_date_time.split()[0], test_date_time.split()[1]

                # Creating list of information about the test
                context = {
                    "student_id": request.user.id,
                    "barcode": new_barcode,
                    "result": test_result,
                    "date_time": datetime.strptime(test_date_time, '%d/%m/%Y %H:%M'),
                }
                (Covid_Test.objects.filter(student__student__id=request.user.id)
                                   .update(barcode=context['barcode'], 
                                           result=context['result'], 
                                           date_time=context['date_time']))

            finally:
                web.quit()

            print("Test is OKAY!")

        return render(request, 'index.html', context)
    else:
        tested_student = Covid_Test.objects.filter(student__student__id=request.user.id)

        if tested_student:
                
            # test_date = datetime.strptime(test_result[0].date, '%m-%d-%Y').date()
            test_date = (tested_student[0].date_time).date()
            today = datetime.today().date()
            df = (today - test_date).days
            
            context = {
                    'test_barcode':tested_student[0].barcode,
                    'test_result': tested_student[0].result, 
                    'test_date_':tested_student[0].date_time,
                    'test_duration':df,
                    }
        else:
            context = {'test_result':None}

        return render(request, 'upload.html', context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('corona:index')

def user_login(request):
    if request.method == 'POST':
        std_id = request.POST['std_id']
        password = request.POST['password']

        user = authenticate(request, username=std_id, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('corona:upload_test')
            else:
                print('User account is not active')
                return redirect('corona:user_login')
        else:
            print("Student ID or Password is not correct")
            return redirect('corona:user_login')

    else:
        return render(request, 'login.html')
