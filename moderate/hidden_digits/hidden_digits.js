var fs = require('fs');

var dict = {
  'a': '0',
  'b': '1',
  'c': '2',
  'd': '3',
  'e': '4',
  'f': '5',
  'g': '6',
  'h': '7',
  'i': '8',
  'j': '9',
};

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line !== '') {
    var output = [];
    line.split('').forEach(function (character) {
      if (!isNaN(character)) {
        output.push(character);
      } else if (dict[character] !== undefined) {
        output.push(dict[character]);
      }
    });
    if (output.length) {
      console.log(output.join(''));
    } else {
      console.log('NONE');
    }
  }
});
