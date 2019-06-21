import * as mongoose from 'mongoose';
import { config } from './config'

let db = config.mlab;

function connection() {
  mongoose.connect(`mongodb://${db.dbuser}:${db.dbpassword}@${db.dburl}`);
  var conn = mongoose.connection;
  conn.on('error', console.error.bind(console, 'Cannot connect to mlab'));
  conn.once('open', function() {
    console.log('Connect to mlab success');
  });
}

export { connection }