var fs = require('fs');
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line !== '') {
    nums = line.split(',').map(function (num) { return parseInt(num); });
    console.log(Math.round((nums[0]/nums[1] - Math.floor(nums[0]/nums[1])) * nums[1]));
  }
});
