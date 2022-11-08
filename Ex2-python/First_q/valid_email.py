'''
Input: read from a text file that contains emails
output: 2 lists, 1. valid emails; 2. invalid emails

https://help.xmatters.com/ondemand/trial/valid_email_format.htmתקינות:

prefix - Allowed characters: letters (a-z), numbers, underscores, periods, and dashes.
       - An underscore, period, or dash must be followed by one or more letter or number.

In the middle we have a @ that is true on all the email address

email domain - Allowed characters: letters, numbers, dashes.
             - The last portion of the domain must be at least two characters, for example: .com, .org, .cc
'''
import re


def valid_or_invalid(file_name: str):
    with open(file_name, 'r') as file:
        emails = file.readlines()  # emails is now a list contains all the emails in the text file

    pattern = re.compile("^([a-zA-Z0-9]+[._-])*[a-zA-Z0-9]+@{1}[a-zA-Z0-9-]+\.{1}[a-zA-Z0-9]{2,}$")

    valid_emails = []
    invalid_emails = []

    for email in emails:
        if pattern.search(email) is not None:
            valid = pattern.search(email).group()
            valid_emails.append(valid)
        else:
            invalid_emails.append(
                email[:-1])  # The -1 is because the \n that adds to the string when using readlines()

    print(f'valid: {valid_emails}')
    print(f'invalid: {invalid_emails}')
    print(len(valid_emails), len(invalid_emails))


if __name__ == '__main__':
    valid_or_invalid('emails_file_text')
