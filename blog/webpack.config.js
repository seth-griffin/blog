var webpack = require('webpack');

var definePlugin = new webpack.DefinePlugin({
    __DEV__: JSON.stringify(JSON.parse(process.env.BUILD_DEV || 'true')),
    __PRERELEASE__: JSON.stringify(JSON.parse(process.env.BUILD_PRERELEASE || 'false'))
});

module.exports = {
    cache: true,
    entry: {    
      main:  './views/admin/index.jsx'   
    },
    output: {
      path: __dirname + '/public/build',
      filename: '[name].js'    
    },
    module: {
        rules: [
            {
              test: /\.jsx?$/,
              use: [
                {
                  loader: 'babel-loader',
                  query: { 
                    presets: [
                      'react', 
                      'es2015'
                    ] 
                  }
                }
              ],
              exclude: /(node_modules|bower_components)/, 
            },
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx']
    },
    plugins: [
        definePlugin
    ]
};
