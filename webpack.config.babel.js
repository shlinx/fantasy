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
        // filename: 'js/[name].[hash].js'
        filename: 'js/[name].js'
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
                test: /\.(ttf|eot|woff2?)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                // loader: "url-loader?limit=10000&name=fonts/[name].[hash].[ext]&publicPath=../"
                loader: "url-loader?limit=10000&name=fonts/[name].[ext]&publicPath=../"
            },
            {
                test: /\.(png|jpg|jpeg|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                // loader: "url-loader?limit=10000&name=images/[name].[hash].[ext]&publicPath=../"
                loader: "url-loader?limit=10000&name=images/[name].[ext]&publicPath=../"
            }
        ]
    },
    plugins: [
        new BundleTracker({filename: 'webpack-stats.json'}),
        // new ExtractTextPlugin('css/[name].[contenthash].css'),
        new ExtractTextPlugin('css/[name].css'),
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