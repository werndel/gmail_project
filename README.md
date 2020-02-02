

# Gmail Testing – Project with Selenium WebDriver and PyTest

> Test project for learning test automation with Selenium WebDriver and Python - a variation of test cases related to some function of Gmail service. 



## Recommends
#### Python
- Python 3.7+
- pip (included by default with Python 3.7+)

#### Drivers
In order to use Selenium, drivers will need to be installed for any browser tests will be run on.
Chromedriver used in this project: version 79.0 for Windows.  
#### Packages installation
The packages can be installed using pip:
```shell
$ pip install -r requirements.txt
```
#### Allure-commandline installation
To generate the test reports, the installation Allure-commandline interpreter is required (Installation instruction: https://docs.qameta.io/allure/, look p. 2.1.4)
#### Running tests
1. Create directory "reports" 
2. To run all test:
```
$ pytest --alluredir=[path_to_reports_dir]
```
#### Generating reports
1. To view the test results in Allure Reports:
```
$ allure serve [path_to_reports_dir]
```

