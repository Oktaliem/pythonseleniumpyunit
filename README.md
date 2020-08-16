<h1 align="center"><img src="https://user-images.githubusercontent.com/26521948/72658109-63a1d400-39e7-11ea-9667-c652586b4508.png" alt="Apache JMeter logo" /></h1>
<h4 align="center">SOFTWARE TESTING ENTHUSIAST</h4>
<br>

# Selenium - Python - PyUnit

This is a sample of Selenium Python (PyUnit) Framework having HTML reporting and Test runner. 

### Dependencies
```
$ pip install selenium
$ pip install webdriver_manager
$ pip install selenium-page-factory
```

## Run the Test
```
Set environment
$ export PYTHONPATH=`pwd`   (optional)

Run Test per Class
i.e.
$ python test/Module_1/Scenario1.py -v
$ python test/Module_1/Scenario2.py -v
$ python test/Module_1/Scenario3.py -v
$ python test/Module_1/Scenario4.py -v 	

Run Test with Test Runner
$ python test/testrunner/TestRunner.py -v


```

## References
Special Thanks to [NayakwandiS](https://github.com/NayakwadiS)

This repository is a modification version of original repository [Github](https://github.com/NayakwadiS/Selenium_Python_UnitTest_HTML)

## Additional features :
- Add webdriver manager capabilities.
- Remove unnecessary codes.
- Compatible version to run demo in Linux and MacOS.
- Add information how to run the test.

## Libraries
- https://wiki.python.org/moin/PyUnit
- https://pypi.org/project/selenium/
- https://pypi.org/project/webdriver-manager/
- https://pypi.org/project/selenium-page-factory/
