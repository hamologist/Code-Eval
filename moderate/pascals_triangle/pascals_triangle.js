var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line !== '') {
    var stop = parseInt(line)-1;
    var triangle = new Array(stop);
    triangle[0] = [1];
    for (var pos = 0; pos < stop; pos++) {
      row = triangle[pos];
      newRow = new Array(row.length+1);
      newRow[0] = row[0];
      newRow[row.length] = row[row.length-1];
      for (var newPos = 1; newPos < row.length; newPos++) {
        newRow[newPos] = row[newPos-1] + row[newPos];
      }
      triangle[pos+1] = newRow;
    }
    console.log(triangle.map(function (row) {
      return row.join(' ');
    }).join(' '));
  }
});
