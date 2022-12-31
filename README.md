# QR-code-generator
this code is use to generate unique QR code to a given text/URL. not only that , we can also extract the contents of a QR code by just uploading the image of the QR code.  
Modules Required:<br />
pip3 install tkinter<br />
pip3 install pyqrcode<br />
pip3 install PIL<br />
How to Run:  python <file_name>.py

## Usage :

* Run the parent.py file using the command -- python3 parent.py  <br />
* in the parent.py you can create topics, you can do this by using the command -- create TopicName NoPartations  <br />
* Now we need to specify the topic name while running the producer-3.py file.  -- python3 producer-3.py TopicName  <br />
  Now you can start writing messages in the  producer, what will get displayed in the consumer which is subscribed to the same topic<br />
* Finally, we can run the consumer.py file by specifing the topic name and </br>
  we can even add an optional flag -- python3 consumer.py TopicName  (OR)  python3 consumer.py TopicName --from_beginning
  
