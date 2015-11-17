var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line !== '') {
    trick = {
      'Vampires': 0,
      'Zombies': 0,
      'Witches': 0,
      'Houses': 0,
    };
    line.split(', ').forEach(function(stat) {
      stat = stat.split(': ');
      trick[stat[0]] = parseInt(stat[1]);
    });
    console.log(Math.floor(
      (trick['Vampires'] * 3 + trick['Zombies'] * 4 + trick['Witches'] * 5) * trick['Houses'] / 
      (trick['Vampires'] + trick['Zombies'] + trick['Witches'])
    ));
  }
});
