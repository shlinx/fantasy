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
        index: path.join(__dirname, 'assets/js/index'),
        listing: path.join(__dirname, 'assets/js/listing')
    },
    output: {
        path: path.join(__dirname, 'dist'),
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
                loader: ExtractTextPlugin.extract('style', 'css!sass')
            },
            {
                test: /\.woff2?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: "file-loader?name=fonts/[name].[hash].[ext]&publicPath=../"
            },
            {
                test: /\.(ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: "file-loader?name=fonts/[name].[hash].[ext]&publicPath=../"
            },
            {
                test: /\.(png|jpg|jpeg|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: "file-loader?name=images/[name].[hash].[ext]&publicPath=../"
            }
        ]
    },
    plugins: [
        new BundleTracker({filename: 'webpack-stats.json'}),
        new ExtractTextPlugin('css/[name].[contenthash].css'),
        // new webpack.ProvidePlugin({
        //     $: 'jquery',
        //     jQuery: 'jquery',
        //     'window.jQuery': 'jquery'
        // }),
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false
            }
        })
    ]
};

export default config;