"""Project File Structure:
# Importing necessary libraries
# Declaring functions to send emails
# Defining function to monitor website
# Read the user input for website monitoring details
# Call monitor_website() function
"""

# Importing necessary libraries
import urllib.request  # To open a website and obtain the status
import smtplib  # To establish an SMTP connection with gmail
import time  # To create the delay for monitoring loop
import hashlib # To create hashcodes using which we can observe any changes in the website

# Declaring functions to send emails and monitor website
# Function to send email
def send_email(email_string):
    # Fill credentials for sender's email and recipient's email
    email_from = 'Enter Sender\'s Email'
    password = 'Enter Sender\'s login Password'
    email_to = 'Enter Recipient\'s Email'

    # Enter subject line
    subject = "Status of the Monitored Website"

    # Connect to gmail's smtp server
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Login to the gmail server
    smtp_server.login(email_from, password)

    # Email's body
    message = f"Subject: {subject}\n\n{email_string}"

    # Send email through the smtp server
    smtp_server.sendmail(email_from, email_to, message)

    # Close the server connection
    smtp_server.close()

# Function to monitor website
def monitor_website():
    # Infinite loop to keep monitoring with time delay
    while True:
        # Access the website to ascertain it's status
        status = urllib.request.urlopen(input_website).getcode()
        # If it returns 200, the website is up
        if status != 200:
            # Call email function
            send_email("The website is currently down")
        else:
            send_email("The website is in working condition")
            # Open url and create the hash code using SHA224
            response = urllib.request.urlopen(input_website).read()
            current_hash = hashlib.sha224(response).hexdigest()
            # Time delay to revisit the website
            time.sleep(time_delay)
            # Revisit the website after delay & generate new hash code
            response = urllib.request.urlopen(input_website).read()
            new_hash = hashlib.sha224(response).hexdigest()
            # Check the hash codes
            if new_hash != current_hash:
                send_email("The website has been updated")

# Read the user input for website monitoring details
input_website = input('Enter the Website to be monitored: ')
input_website = 'https://'+input_website
time_delay = int(input('Enter time interval in seconds to check website status: '))
 
# Call Monitoring Website Function
monitor_website()
