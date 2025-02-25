# FeepaymentAlert_with_OTPValidation
## Overview
`feepaymentAlert_with_OTPValidation` is a Python-based system that allows an admin to manage student fee payment statuses. The script includes OTP validation for secure access and provides email notifications for students with pending or cleared fees.

## Features
- **Admin Login with OTP Verification**: Ensures secure access using an OTP sent to the admin's email.
- **User Details Management**: Allows the admin to update students' fee payment statuses.
- **Email Notifications**: Automatically sends email reminders to students with pending fees and confirmations to those who have paid.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required modules (`feepending`, `feepaid`, `otp`)
- SMTP configured for email notifications

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/feepaymentAlert_with_OTPValidation.git
