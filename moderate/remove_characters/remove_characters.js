var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== '') {
        line = line.split(',');
        remove = line[1].trim().split('');
        console.log(line[0].split('').filter(function (character) {
            if(remove.indexOf(character) === -1) {
                return true;
            } else {
                return false;
            }
        }).join(''));
    }
});
