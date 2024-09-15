# 🎉 Birthday Email Sender

This project is a Python script designed to send personalized birthday emails to recipients based on a predefined list of birthdays. It selects a random quote and letter template, customizes the email with the recipient's name, and sends the email using Gmail's SMTP server.

## 🌟 Features

- **Birthday Detection**: Automatically detects if today matches any birthday in the list.
- **Personalized Messages**: Customizes the email content using predefined letter templates and random motivational quotes.
- **Automated Email Sending**: Sends the email using Gmail's SMTP server.
- **Logging**: Keeps a record of all emails sent, stored in the `sent_mails` directory.
  
## 🚀 Getting Started

### Prerequisites

To run this project, you need:
- Python 3.x
- A Gmail account
- Required libraries: `smtplib`, `decouple`, `pandas`

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ImanGholamii/Birthday_Wisher.git
   cd birthday-email-sender
2. Install the required Python libraries:
   ```sh
   pip install python-decouple pandas
3. Set up your .env file with your email and app password:
   ```sh
   EMAIL=your_email@gmail.com
   PASSWORD=your_app_password
   ```
   > **Note**: Gmail requires an [App Password](https://myaccount.google.com/apppasswords) for third-party apps. Ensure that your account has 2-factor authentication enabled to create an app password.
4. Prepare your data files:
   - birthdays.csv: A CSV file that contains the following columns:
     ```csv
     name,year,month,day,email
     John,1990,9,14,john@example.com
   - quotes.txt: A text file containing motivational quotes (one per line).
   - letter_templates/letter_1.txt, letter_2.txt, letter_3.txt: Predefined letter templates.
   - Use [NAME] as a placeholder for the recipient's name and [message] for the random quote.  
### Example file structure:
```css
  ├── birthdays.csv
  ├── quotes.txt
  ├── letter_templates
  │   ├── letter_1.txt
  │   ├── letter_2.txt
  │   └── letter_3.txt
  ├── sent_mails
  ├── main.py
  ├── .env
```

### Running the Program
1. Run the script:
   ```sh
   python main.py
2. The script will check if today matches any birthday from the list.
   If it does, it sends a personalized birthday email with a random quote and saves a copy of the email in the **sent_mails** folder.
## 📈 Future Enhancements
- Add Error Handling: Enhance error handling for email sending failures.
- Support for Other Email Providers: Expand support to non-Gmail providers.
- Add Scheduling: Integrate with a task scheduler (like cron or task scheduler) for daily automated email checks.

## 🛠️ Technologies Used
- Python 3
- smtplib (for sending emails)
- pandas (for reading CSV data)
- decouple (for environment variables)

## 📜 License
- This project is licensed under the [Apache version2](https://apache.org/licenses/LICENSE-2.0) License. See the [LICENSE file](https://github.com/ImanGholamii/Birthday_Wisher/blob/main/LICENSE) for details.

## 🙌 Acknowledgements
- This project is inspired by automation examples for sending emails with Python.
- Special thanks to the contributors of pandas and smtplib for enabling easy data handling and email automation and Dr **Angela Yu**.

## 🤝 Contributing
- If you'd like to contribute to this project, feel free to open a pull request or issue. Contributions are always welcome!

## ⭐ Give a Star
- If you like this project, please give it a ⭐ on [GitHub](https://github.com/ImanGholamii/Birthday_Wisher)
## 
### Enjoy automating your birthday wishes! 🎂🎉

