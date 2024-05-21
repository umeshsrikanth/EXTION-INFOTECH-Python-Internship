import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import csv

# Function to read recipients from a CSV file
def read_recipients(file_path):
    recipients = []
    # Open the CSV file in read mode
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Append the email address (assumed to be in the first column) to the recipients list
            recipients.append(row[0])
    return recipients


# Function to send emails
def send_email(sender_email, password, recipients, subject, message):
    try:
        # Connect to the Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)  # Log in to the server

        # Iterate over each recipient and send the email
        for recipient in recipients:
            # Create the email headers and body
            email_message = f"Subject: {subject}\nTo: {recipient}\nFrom: {sender_email}\n\n{message}"
            
            # Send the email
            server.sendmail(sender_email, recipient, email_message)

        server.quit()  # Quit the server connection
        print("Emails sent successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

# Main function to gather user inputs and call other functions
def main():
    # Get the sender's email and password
    sender_email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")
    # Get the path to the recipient list file
    recipient_list_path = input("Enter the path to the recipient list file: ")
    # Get the email subject and message
    subject = input("Enter the email subject: ")
    message = input("Enter the email message: ")

    # Read the recipients from the CSV file
    recipients = read_recipients(recipient_list_path)
    # Send the email to the recipients
    send_email(sender_email, password, recipients, subject, message)

# Entry point of the script
if _name_ == "_main_":
    main()
