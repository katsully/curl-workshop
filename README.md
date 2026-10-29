# From Curl Requests to Web Apps

curl is a command line tool for url manipulations and data transfers. Try

```
curl --help
```

to see some of the options.



The main pipeline with curl requests is:

make request --> get data --> send data --> retrieve information



**HTTP (hypertext transfer protocol)** is when you fetch data from a **web server**. A web server is a piece of software or hardware that stores and delivers website content. 

HTTP is built on top of **TCP/IP (transmission control protocol/internet protocol)**. 

TCP is in charge of making sure individual packets of data are reassembled in the correct order and implements any error checking. 

Internet Protocol is an address system of the internet. The core function is delivering packets of information from the source (server) to the target (client).

Think of it like someone sending a puzzle through the mail:

Puzzle --> puzzle pieces --> different routes --> reordering the pieces --> destination



### Making a Request

When making a request you need to specify the **method**:

1. GET - getting information from the database
2. POST - adding information to the database
3. PUT - changing existing information in the database
4. DELETE - deleting information from the database

You also typically need **headers** and **query parameters**.


