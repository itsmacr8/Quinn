# Quinn: Driving productivity through smart automation

As a Squad Leader, my day-to-day responsibilities include ensuring that every intern is on track with their assigned tasks. To streamline this process, I've developed Quinn using Selenium. This tool is designed to enhance our workflow by automatically logging in, identifying the correct team member within our group chats, and sending reminders to each intern. It meticulously avoids messaging non-targeted members, ensuring that each communication is relevant and direct. After completing its rounds, she gracefully exits the browser.

## Technologies

This project uses the following technologies:

- [Selenium Framework](https://www.selenium.dev/documentation/)
- [Microsoft Edge browser](https://www.microsoft.com/en-us/edge/download)

## Installation

To run the project locally, you need to have [Python](https://www.python.org/downloads/) installed on your machine. Then follow the below steps:

- Clone the project repository:

```sh
git clone https://github.com/itsmacr8/quinn.git
```

- Navigate to the project directory

```sh
cd quinn
```

- Install the dependencies:

```sh
pip install -r requirements.txt
```

- Download the appropriate [web driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) based on your [browser version](https://support.microsoft.com/en-us/microsoft-edge/find-out-which-version-of-microsoft-edge-you-have-c726bee8-c42e-e472-e954-4cf5123497eb). After downloading the web driver, **move the 'edgedriver'** folder inside this projects **root folder.**

## Files

- main.py (Main file of this script)
- _controller.py (Contains all logics)
- _variables.py (Contains all variables)
- _utils_functions.py (Contains utility functions)
- _driver.py (Contains driver setting to open the browser)

## How to Use

### Run the script

To run the script in test mode, run the following command. This will check all the functionality.

```sh
python main.py test
```

Run the following command to run the script.

```sh
python main.py
```

### Web Element CSS Selectors

Quinn uses CSS selectors to identify and interact with web elements. The selectors are on the ```_variables.py``` file. Here are the selectors used:

```py
MS_ACC_LOG_IN
DROPDOWN_SELECT_TEAM
CHOOSE_TEAM
TEAM_LOG_IN
CHAT_ICON
COMMON_GROUP_MEMBER_NAME
INTERNS_IMC
INTERN_IMC_NAME
LAST_VISIBLE_INTERN_IMC_BEFORE_SCROLL
INPUT
```

### Functionality

Quinn has the following functionality (```main.py```):

1. Login: Logs into the Microsoft account using the MS_ACC_LOG_IN selector.
2. Select Team: Selects the team from the dropdown using the DROPDOWN_SELECT_TEAM and CHOOSE_TEAM selectors.
3. Team Login: Logs into the team using the TEAM_LOG_IN selector.
4. Open Chat: Opens the chat using the CHAT_ICON selector.
5. Find Interns: Finds the interns in the chat using the find_interns_imc method.
6. Create Intern Dictionary: Creates a dictionary of intern names and web elements using the create_intern_name_and_web_element_dict method.
7. Log Intern Names: Logs the names of the interns using the log_interns_name_list method.
8. Send Message: Sends a message to each intern using the send_message method.

### Debugging

In case the Quinn fails to find an element with the provided CSS selector, it's important to debug the issue to understand what went wrong. Here are some steps you can follow:

1. **Check the Logs:** The first step in debugging is to check the log files. Quinn should log all its actions, so if it fails to find an element, the error will be logged.
2. **Verify the CSS Selector:** Ensure that the CSS selector used to identify the element is correct. Even a small typo can cause Quinn to fail to find the element.
3. **Check the Page Source:** If the CSS selector is correct, check the source code of the webpage. The element might not be available at the time Quinn is looking for it.
4. **Synchronization Issues:** Web elements on some pages might load at different speeds. If Quinn is trying to find an element before it has fully loaded, it will fail. Adding wait times or using explicit waits can help resolve this issue.
5. **Dynamic Content:** If the webpage has dynamic content, the elements might change, causing Quinn to fail to find the element. In this case, you might need to update Quinn to handle the dynamic content.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
