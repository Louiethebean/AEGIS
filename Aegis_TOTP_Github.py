#!/usr/bin/env python3



print("""

            ,----------------,              ,---------,

        ,-----------------------,          ,"        ,"|

      ,"                      ,"|        ,"        ,"  |

     +-----------------------+  |      ,"        ,"    |

     |  .-----------------.  |  |     +---------+      |

     |  |                 |  |  |     | -==----'|      |

     |  |    WECLOME TO   |  |  |     |         |      |

     |  |     AEGIS!!     |  |  |/----|`---=    |      |	

     |  |   |`-._/\_.-`|  |  |  |     |         |      |

     |  |   |    ||    |  |  |  |     |         |      |

     |  |   |____||____|  |  |  |     |         |      |

     |  |   |____**____|  |  |  |     |         |      |

     |  |   \    ||    /  |  |  |     |         |      |

     |  |    \   ||   /   |  |  |     |         |      |

     |  |     \  ||  /    |  |  |     |         |      |

     |  |      '.||.'     |  |  |     |         |      |

     |  |        ``       |  |  |   ,/|==== ooo |      ;

     |  |                 |  |  |  // |(((( [33]|    ,"

     |  `-----------------'  |," .;'| |((((     |  ,"

     +-----------------------+  ;;  | |         |,"     

        /_)______________(_/  //'   | +---------+

   ___________________________/___  `,

  /  oooooooooooooooo  .o.  oooo /,   \,"-----------

 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"

/_==__==========__==_ooo__ooo=_/'   /___________,"

`-----------------------------'



""")





import sys

import smtplib

import random

import subprocess

import pty

import time

import select



# Function to send the email containing the token

def send_token_email(email_address):

    # Generate a random 6-digit token

    token = str(random.randint(100000, 999999))

    # Construct the email message

    subject = 'Token for SSH Authentication'

    body = f'Your token is: {token}'

    message = f'Subject: {subject}\n\n{body}'

    # Send the email using a third-party email service (e.g., Gmail)

    sender_email = 'insert_email'

    sender_password = 'insert_email_password'

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender_email, sender_password)

    server.sendmail(sender_email, email_address, message)

    server.quit()

    # Return the token for later verification

    return token, time.time()

# Function to verify the token entered by the user

def verify_token(entered_token, sent_token, sent_time):

	if entered_token == sent_token and time.time() - sent_time <= 30:

		return True

	else:

		return False

# Example usage:

email_address = 'insert_email'

sent_token, sent_time = send_token_email(email_address)

print('A token has been sent to your email address. You have 30 seconds to enter the token.')

print('Please check your email and enter the 6-digit token: ')

# in seconds

timeout = 30

inputs = [sys.stdin]

start_time = time.time()

while inputs:

    if select.select(inputs, [], [], timeout)[0]:

        entered_token = input('Enter the token: ')

        if entered_token.strip() == '':

            print('Token cannot be blank. Please enter the 6-digit token.')

            continue

        if verify_token(entered_token, sent_token, sent_time):

            print('Authentication Successful')

        # Connect to the terminal using SSH

            ssh_username = 'insert_host_username'

            ssh_host = 'insert_host_ip'

            ssh_port = 'insert_port'

            ssh_command = f'ssh -p {ssh_port} {ssh_username}@{ssh_host}'

            subprocess.call(ssh_command, shell=True)

            pty.spawn("/bin/bash")

            sys.exit()

        else:

            print('Authentication failed')

    else:

        print('No token entered. Exiting script.')

        sys.exit()

    if time.time() - start_time >= 30:

        print('Time limit exceeded. Exiting script.')

        sys.exit()

