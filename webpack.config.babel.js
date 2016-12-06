/**
 * Created by xlin on 6/12/16.
 */

import path from 'path';
import webpack from 'webpack';
import BundleTracker from 'webpack-bundle-tracker';
import ExtractTextPlugin from 'extract-text-webpack-plugin';

const config = {

    context: __dirname,

    entry: {
        index: path.join(__dirname, './assets/js/index'),
        listing: path.join(__dirname, './assets/js/listing')
    },
    output: {
        path: path.resolve('./static/'),
        filename: 'js/[name].[hash].js'
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
            },
            {
                test: /\.scss$/,
                loader: ExtractTextPlugin.extract(['css', 'sass'])
            }
        ]
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new ExtractTextPlugin('css/[name].[contenthash].css'),
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