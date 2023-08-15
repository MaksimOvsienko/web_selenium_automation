This is my pet project to try myself in automation of website which was developed on my previous job, and which I tested as manual qa.

### About the product I tested
It's a website for helping people with HIV. On the site you can register as a patient and order a free kit with an HIV test and other useful things.

### Technologies used:
* Selenium webdriver
* Pytest framework
* Python version 3.11

### Main features:
* End to end tests:
* * login with invalid and valid inputted data
* * making successfull order of product
* Generation of html reports with pytest-html
* Automatic screenshot for failed tests

### How to run project:
1. In conftest.py input correct website homepage url into variable BASIC_URL
2. Write "pytest" into console and enjoy.
2.5. If you want to generate html report then type py.test --html=report.html into console
