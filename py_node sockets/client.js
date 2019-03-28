var net = require('net');
var client = new net.Socket();
client.connect(65432, '127.0.0.1')
client.write("Hello World");
