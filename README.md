# 

## Objective


## Project Structure
```markdown
Reports/
  ├── 2025_01_30/
      ├── 30_01_2025_15_06_27_271530012025.png
      ├── report_150614.html
configs/
  ├── configs.py
page_objects/
  ├── __init__.py
  ├── base_page.py  
  ├── home_page.py
test_cases/
  ├── __init__.py
  ├── conftest.py
test_data/
utilities/
  ├── __init__.py
  └── utilities.py
README.md
install_package.bat
requirements.txt
run.bat
```

## **Features**  


### **3. Reporting**  

- Logs test results (pass/fail) in a **pytest HTML report**.  

### **4. Additional Features**  
- Tests website responsiveness by simulating different screen sizes:  
  - **Desktop:** 1920 × 1080  
  - **Tablet:** 768 × 1024  
  - **Mobile:** 375 × 667  
- Supports **parallel test execution** using **pytest-xdist**.

## Prerequisites
* Python 3.8+
* Required Python Libraries listed in requirements.txt
* Pip
* Google Chrome or any other supported browser

## Tools and Frameworks Used
* Selenium: For automating the web crawling and functional testing.
* pytest: For running the tests.
* pytest-xdist: Parallel Execution

## Steps to Execute the Script
1. **Step 1**: Clone the Repository
```cmd

```

2. **Step 2**: Install Dependencies
There are two ways to install the required dependencies for this project:
* Option 1: Using pip install (Manual Method)
```cmd
cd your-repository-directory
pip install -r requirements.txt
```

* Option 2: Using install_package.bat (Automated Method)
Double-click the install_package.bat file or run the following command from the terminal or command prompt:
```cmd
install_package.bat
```

3. **Step 3**: Run the tests
There are two ways to run the test for this project:
* Option 1: Using Terminal (Manual Method)
```cmd
# Basic crawling
pytest test_card_page_functionality.py

# whole suite
pytest

# Parallel Execution
pytest -n=3
```

* Option 2: Using run.bat (Automated Method)
Double-click the run.bat file or run the following command from the terminal or command prompt:
- Note: currently setup for whole suite
```cmd
run.bat
```
4. **Step 4**: Check the Output
* Logs and screenshots will be stored in the Reports/2025_01_30/ folder

## Test Execution"# LetCode_Pytest_Selenium_Tests" 
