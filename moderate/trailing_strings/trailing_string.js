var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== '') {
        line = line.split(',');
        if (line[0].substring(line[0].length - line[1].length) === line[1]) {
            console.log(1);
        } else {
            console.log(0);
        }
    }
});
