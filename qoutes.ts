import * as mongoose from 'mongoose';

var Schema = mongoose.Schema;

var quoteSchema = new Schema({
  author: String,
  quote: String
});

var Quote = mongoose.model('quotes', quoteSchema);

var addQuote = (req, res) => {
  Quote.create(req.body, function (err, data) {
    if (err) {
      console.log(err);
      res.json({ message: 'Fail to add' });
    }
    res.json({ message: 'Add new quote success' });
  });
}

var getAllQuotes = (req, res) => {
  Quote.find().exec(function (err, data) {
    if (err) {
      console.log(err);
      res.json({ message: 'Fail to get all quotes' });
    }
    res.json(data);
  })
}

export { addQuote, getAllQuotes }