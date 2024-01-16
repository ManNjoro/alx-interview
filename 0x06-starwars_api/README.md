# Star Wars Film Characters

This Node.js script uses the SWAPI API to fetch the characters featured in a specified Star Wars film and prints their names to the console.

## Prerequisites

To run this script, you will need the following:

* Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
* Install request module and use it
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Usage
Sample Example:
```
└─$ ./0-starwars_characters.js 1
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Owen Lars
Beru Whitesun lars
R5-D4
Biggs Darklighter
Obi-Wan Kenobi
Wilhuff Tarkin
Chewbacca
Han Solo
Greedo
Jabba Desilijic Tiure
Wedge Antilles
Jek Tono Porkins
Raymus Antilles
```