## About

Example P2P project for EC530.  Based on tutorials we discussed in class.

**Resources**: 
https://www.geeksforgeeks.org/simple-chat-room-using-python/
https://realpython.com/python-sockets/


## Install

### Dependencies

```console
pip install -r requirements.txt
```


## Usage

Start the server and any number of clients with the following commands.

```console
python chat_server.py <ip-address> 8081
python client.py <ip-address> 8081
python client.py <ip-address> 8081
```

Then send messages to either of the client to see them appear on the other client (and server).


## Data Protection/Input Sanitization

Basic input sanitation has been implemented to ensure malicious commands are not sent via the messaging system.

Inputs are screened for special characters, primarily those indicative of a potential SQL query. 

An error is returned if the user has tried to transmit a potentially malicious message. 


## Contributors

Chris Krenz


## License

[MIT License](LICENSE)
