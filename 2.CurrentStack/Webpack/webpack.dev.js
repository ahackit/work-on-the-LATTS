const common = require('./webpack.common');
const merge = require('webpack-merge');
const path = require('path');

module.exports = merge(common, {
  mode: 'development',
  output: {
    filename: 'hello.js',
    path: path.resolve(__dirname, 'code'),
  },
});
