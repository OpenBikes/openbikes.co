const path = require('path');
const merge = require('lodash/merge');
const webpack = require('webpack');

const TARGET = process.env.npm_lifecycle_event;
const PATHS = {
  in: path.join(__dirname, 'src'),
  out: path.join(__dirname, 'dist'),
};

process.env.BABEL_ENV = TARGET;

const common = {
  entry: path.join(PATHS.in, 'main.jsx'),
  resolve: {
    extensions: ['', '.js', '.jsx'],
  },
  output: {
    path: PATHS.out,
    filename: 'index.js',
  },
  module: {
    preLoaders: [
      {
        test: /\.jsx?$/,
        loaders: ['eslint'],
        include: PATHS.in,
      },
    ],
    loaders: [
      // SASS
      {
        test: /\.scss$/,
        loaders: ['style', 'css', 'sass'],
        include: PATHS.in,
      },
      // JSX
      {
        test: /\.jsx?$/,
        loader: 'babel',
        query: {
          cacheDirectory: true,
          presets: ['react', 'es2015'],
        },
        include: PATHS.in,
      },
      // Fonts and images
      {
        test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9=&.]+)?$/,
        loader: 'file-loader',
      },
    ],
  },
};

if (TARGET === 'start' || !TARGET) {
  module.exports = merge(common, {
    devServer: {
      devtool: 'eval-source-map',
      contentBase: PATHS.out,
      historyApiFallback: true,
      hot: true,
      inline: true,
      progress: true,
      stats: 'errors-only',
      host: process.env.HOST,
      port: process.env.PORT,
    },
    plugins: [
      new webpack.HotModuleReplacementPlugin(),
    ],
  });
}

if (TARGET === 'build') {
  module.exports = merge(common, {});
}
