This is my pet project to try myself in automation of website which was developed on my previous job, and which I tested as manual qa.

### About the product I tested
It's a website for helping people with HIV. On the site you can register as a patient and order a free kit with an HIV test and other useful things.

### Main features
* End to end tests:
* * login with invalid and valid inputted data
* * making successfull order of product
* Generation of html reports with pytest-html
* Automatic screenshot for failed tests
* Custom logger

### Demo gifs
Both scenarios successfull:
[![SceJj.gif](https://s11.gifyu.com/images/SceJj.gif)](https://gifyu.com/image/SceJj)

Failure of tests 8-10 from the first scenario. After the fail of each test, a screenshot is taken:
[![ScePW.gif](https://s11.gifyu.com/images/ScePW.gif)](https://gifyu.com/image/ScePW)

### Technologies used
* Selenium webdriver
* Pytest framework
* Python version 3.11

### How to run project
I can click on the dev site, but you can't, so this instruction is more like a reminder for me.

Steps:
1. In conftest.py input correct website homepage url into variable BASIC_URL
2. Type "pytest" into console and enjoy.

If you want to generate html report then type into console: pytest --html=report.html
