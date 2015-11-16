var fs = require('fs');

var isRepetable = function(sub, original) {
    if (!(original.length % sub.length) && Array(original.length/sub.length+1).join(sub) === original) {
        return true;
    } else {
        return false;
    }
}

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== '') {
        var match = '';
        var shortest = line.length;
        line.substring(0, line.length/2).split('').some(function (letter) {
            match += letter;
            if (isRepetable(match, line)) {
                shortest = match.length;
                return true;
            }
        });
        console.log(shortest);
    }
});
