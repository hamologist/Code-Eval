var fs = require('fs')
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
        var longestWord = ""
        line.split(' ').map(function (word) {
            if (word.length > longestWord.length) {
                longestWord = word;
            }
        });
        console.log(longestWord);
    }
});
