var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== '') {
        line = line.split('');
        while (line.length !== 0) {
            var character = line[0];
            var beginLength = line.length;
            line = line.filter(function (item) {
                return item !== character;
            });
            if (line.length === beginLength-1) {
                console.log(character);
                break;
            }
        }
    }
});
