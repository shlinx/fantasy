/**
 * Created by xlin on 6/12/16.
 */

import path from 'path';
import webpack from 'webpack';
import BundleTracker from 'webpack-bundle-tracker';

const config = {

    context: __dirname,

    entry: {
        index: path.join(__dirname, './static/js/index'),
        listing: path.join(__dirname, './static/js/listing')
    },
    output: {
        path: path.resolve('./static/dist/'),
        filename: '[name]-[hash].js'
    },
    resolve: {
        modulesDirectories: ['node_modules'],
        extensions: ["", ".js", ".jsx"]
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel-loader'
            }
        ]
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        }),
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false
            }
        })
    ]
};

export default config;