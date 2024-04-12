"""
This code is a scraper for the metro.ca website.
It is designed to run with Python 3.8.2
Running this code with a different version of Python may result in errors such as 'undetected_chromedriver' and 'distutils' errors.

Review:

1. Commented Code: Some lines of code, like the headless option and disable notifications, are commented out. Ensure these comments reflect a specific purpose, such as troubleshooting or development version considerations.

2. Logging: Logging is implemented to capture debug information in the 'Metro.log' file. Consider adding more fine-grained logging messages, such as success notifications, exceptions, or detailed steps to aid in troubleshooting and debugging.

3. Exception Handling: Generally, handling exceptions is a good practice. However, in some places, exceptions are caught without handling or logging the error. Make sure to review these exceptions and implement appropriate error handling or logging for a more robust application.

4. Error Messages: The variable 'p' is assigned with a string value in various exception cases, but it is not used or logged elsewhere. Ensure that error messages and logging capture meaningful information about encountered errors.

5. Code Formatting: Format the code consistently to improve readability and maintainability. Follow PEP 8 guidelines, including indentation with four spaces, consistent capitalization, proper space usage, and line length limitations.

6. Code Separation: Consider breaking down the large `scrape_website()` method into smaller, more manageable functions or methods. This modular approach makes the code easier to maintain, test, and understand.

7. Chrome Driver: Ensure the 'chromedriver.exe' path specified in the `run_browser()` method is correctly set for the target environment.

8. Implicit Waits: Implementing implicit waits (e.g., `driver.implicitly_wait(10)`) can help reduce explicit wait statements, making the code more efficient.

9. Reusability: Consider making the code more reusable by accepting the target URL as a command-line argument or as a parameter to the `run_browser()` method.

Overall, the code demonstrates a functional web scraper for the metro.ca website. Addressing the mentioned points will help enhance its functionality and maintainability.
"""