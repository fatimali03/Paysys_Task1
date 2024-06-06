# Paysys_Task1
**Code Implemented in Python:**
![image](https://github.com/fatimali03/Paysys_Task1/assets/136559675/d2b57ce0-508b-481a-b05f-6b2a9ef4b304)

**Unit Testing**
![image](https://github.com/fatimali03/Paysys_Task1/assets/136559675/48778c5d-8527-41e8-8d4c-0f99c151c1a6)

**CI/CD PIPELINE (Implemented using GitHub Actions)**
![image](https://github.com/fatimali03/Paysys_Task1/assets/136559675/59fa8d8b-7fad-4f28-bb7f-cd273da4ec54)

The .github/workflows/ directory defines the CI/CD pipeline steps to automatically run the unit tests whenever changes are pushed to the repository.

1.Checkout Code:
This step fetches the code from the repository so that the workflow can access it.
2.Set up Python:
It configures the environment to use Python, ensuring that the correct version is available for running the tests.
3.Install dependencies:
This step installs any required dependencies, such as libraries or packages needed for the tests to run successfully.
4.Run tests:
Here, the unit tests are executed. The output, typically in the form of test results, is saved to a file named test-results.xml.
5.Publish test results:
The test results saved in test-results.xml are uploaded as an artifact. This allows viewing the results in the GitHub Actions interface, aiding in debugging and analysis.

**Github Action**
![image](https://github.com/fatimali03/Paysys_Task1/assets/136559675/1da754d1-3817-4a61-9f4c-2d296ec102e4)

**Run Test Cases**
![image](https://github.com/fatimali03/Paysys_Task1/assets/136559675/b9d3e7cf-7a6a-42af-ab7f-62f4e87e922e)
