import * as express from 'express'
import * as bodyParser from 'body-parser'

import { connection } from './db'
import { addQuote, getAllQuotes } from './qoutes'

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
connection();

app.get('/api/hello', async (req, res) => {
  res.send("Hello World!");
});

app.get('/api/quote/list', async (req, res) => {
  getAllQuotes(req, res);
});

app.post('/api/qoute/add', async (req, res) => {
  addQuote(req, res);
});

app.listen(process.evn.PORT || 3000, function () {
  console.log('listening on port 3000');
});