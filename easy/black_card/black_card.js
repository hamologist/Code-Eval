var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line !== '') {
    line = line.split(' | ');
    players = line[0].split(' ');
    count = parseInt(line[1]);
    while (players.length !== 1) {
      if (count > players.length) {
        players.splice(players.length - (count % players.length) - 1, 1);
      } else {
        players.splice(players.length - (players.length % count) - 1, 1);
      }
    }
    console.log(players[0]);
  }
});
