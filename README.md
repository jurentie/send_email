# send_email	

`send_email.py` is a short script written to send an email with attachment using smtp.

### Usage: ###

First add your own personal host and port to the following line

`39: smtp = smtplib.SMTP(host='', port=)` 

Arguments:

* `sender`: the "sender of the email" this will be seen as the sent from email address in the received email. This can be any string you want.

* `subject`: the subject of the email

* `path/to/contacts.txt`: a file holding a list of recipient contacts each contact on one line.

  ex:

  ```
  email.here@gmail.com
  another.email@domain.com
  ```

* `path/to/message.txt`: a file with the message body of the email.

  ex:

  ```
  This is the message that will be sent.
  
  sincerely,
  justin
  ```

* `path/to/attachment`: the path to the attachment file



example:

`py send_email.py "no-reply@email.com" "This is the subject" contacts.txt message.txt "attachment.txt"`



*It is my intention to update this script to allow attachments as optional*
