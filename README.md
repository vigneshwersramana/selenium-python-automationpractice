# Selenium Python AutomationPractice Website 
 
## Installation Steps:
* Clone this repo
* Navigate to root folder
* pip3 install -r requirements.txt
* To run all test case
  - pytest --html=reports/report.html
* To execute test cases in parellel
  - pytest -n 5 --html=reports/report.html
* To Run all positive test case
  - pytest -n 5 -m positive
* To Run all negative test case
  - pytest -n 5 -m negative
* Please refer [Pytest Markers](pytest.ini) for other markers to execute scripts

## Added Centime Kick Off event Scheduler
* Added a Flow to validate Home Page and Try It Free registration(tool will not schdule event)
* Added email id validation(Negative Flow)
* To run enter the commant pytest --app="centime" --html=reports/report.html


## List of Scenarios Covered

### Centime
* Schedule a Event(will not create)
* Validate email id in Scheduler

### Registration
* Valid email id Registration
* Invalid email id Registration
* Already existing email Id Registration
* Valid email id Registration without entering Mandatory Fields
* Valid email id Registration with entering invalid values
* Valid email id Registration invalid Country

### Login
* Valid credentials Login
* Invalid email Id Login
* Invalid Password Login
* Missing email id Login
* Missing Password Login

### Add Product
* Add First product(Loging and then select product)
* Add Product from the data provided in input test data file

### Delete Product
* Delete a product in the Cart Page

## Results
* In [Reports](reports) there are 3 HTML report files which was executed earlier. Below attached are the execution results for the same.
<img src = "img/Centime Results.png">
<img src = "img/Automation Practice with All Pass.png">
<img src = "img/Automation Practice with Failures.png">