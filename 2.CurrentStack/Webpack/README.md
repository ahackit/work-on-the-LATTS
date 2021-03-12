# LATT-Webpack

Learn All The Things - Webpack

## What is Webpack?

Webpack helps JS developers manage dependencies and assests because it sucks doing it the old school way. That old way is managing all that information through script tags in the correct order

## How to install WebPack?

npm init -y: create your initial package.json
npm install --save-dev webpack webpack-cli
npm script "start": "webpack

## How do I work with webkpack

Need to separate code through ES6 import/exports.
Once set up - can run "npm start" or "npm webpack" to bundle to /dist (initial config)

## Configuring Webpack

Get yourself a webpack.config.js file in your directory
Can config lots of things. The big ones are the following:

- Entry Point
- Output
- Mode: Development or Production (Not minified or minified)
- Modules: Give them rules which is RegEx for filetype and the type of loader to translate those files
  - Remember that the loaders run from right to left
- Cache Busting: Dynamcic filenames
- Plugins: Configure the build process

Once config is set up set up npm script for webpack to use --config

## Loaders

Loaders are ways of translating different derivates of javscript/css/html back into the standard language

- Loading CSS: We can use css-loader (translates CSS to javascript) and style-loader (loads CSS javascript into dom)
- Loading SASS: Need sass-loader/node-sass with rule configured to scss.

## Cache Busting

Changes the name of the javascript file so Cache knows to redownload.

- Configure using contentHash

## Plugins

Help you change your build process

- HtmlWebpackPlugin: Generate HTML files with hashed JS files. Build files based off templates

## Splitting for Dev and Production

Use multiple webpack files to optomize webpack for either development or production

- Use webpack merge to utilize common webpack files for shared configuration
- Can then setup different npm scripts for dev/prod
- Can set up a dev server during development using webpack-dev-server

## Loading Images

Use HTML Loader to instead of using the SRC attribute, it will utilize a JS require statement
Can also then use File Loader to load all sorts of image types

## Cleaning up

Can use CleanWebPackg to keep webpack from rebuilding many files.
