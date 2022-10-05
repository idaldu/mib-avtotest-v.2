import os
import time

os.system('venv\Scripts\\activate')
os.system('pytest --alluredir=tests\\allure_results .\\tests\\login_test.py')
os.system('deactivate')
os.system('allure generate C:\\Users\\adubov\PycharmProjects\mib-avtotest-v.2\\tests\\allure_results')
os.system('allure-combine C:\\Users\\adubov\\PycharmProjects\\mib-avtotest-v.2\\allure-report')
os.system('mkdir allure_reports')
os.system('copy .\\allure-report\\complete.html .\\allure_reports')
os.system('rmdir /s /q .\\allure-report')
os.system('rmdir /s /q .\\tests\\allure_results')