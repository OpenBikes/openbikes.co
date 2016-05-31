const express = require('express');
const erv = require('express-react-views');

// Predefine needed stylings
const error = clc.red.bold;
const warn = clc.yellow;
const info = clc.cyan.bold;
const debug = clc.magenta.italic;
const server = clc.yellow.bold;

// Launch app
let app = express();

// app.set('views', 'src/main.jsx');
// app.set('view engine', 'jsx');

// app.engine('jsx', erv.createEngine());

// // Launch server
// app.listen(3000, function() {
//   console.log('Server is running on http://localhost:3000 or http://127.0.0.1:3000');
// });

