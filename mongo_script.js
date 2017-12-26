var current_time = 1445299200000;
var end_time = 1508371200000;
var term = 1440*60*1000;
var start = new Date();
var start_int = start.getTime();
print(start_int);
while(current_time < end_time){
  var last_time = current_time + term - 60000;
  var range = db.things.find({"time": { $gt: current_time, $lt: last_time } });

  var first = range[0];
  var last = range[0];
  var high = range[0];
  var low = range[0];

  db.things.find({"time": { $gt: current_time, $lt: last_time } }).forEach(function(minute) {
    if (minute['high'] > high['high']){
      high = minute;
    }
    if (minute['low'] < low['low']){
      low = minute;
    }
    if (minute['time'] < first['time']){
      first = minute;
    }
    if (minute['time'] > last['time']){
      last = minute;
    }
  });
  db.candledata.insertOne({start_time: current_time, end_time: last_time, high: high['high'], low: low['low'], open: first['open'], close: last['close'], term: 33 });

  current_time = current_time + term;

}

var end = new Date();

print(end.getTime() - start_int);
