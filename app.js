const express = require('express');
const bodyParser = require('body-parser');

// Predefine needed stylings
const error = clc.red.bold;
const warn = clc.yellow;
const info = clc.cyan.bold;
const debug = clc.magenta.italic;
const server = clc.yellow.bold;

// Launch app
let app = express();

