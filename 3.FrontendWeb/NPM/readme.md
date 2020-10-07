# Package Managers - NPM
- Any Project using Node needs ```package.json```
  - ```package.json file``` can be described as a manifest of your project that includes the packages and applications it depends on, information about its unique source control, and specific metadata like the project's name, description, and author.

## What's in your Package?
```
{
  "name": "metaverse", // The name of your project
  "version": "0.92.12", // The version of your project
  "description": "The Metaverse virtual reality. The final outcome of all virtual worlds, augmented reality, and the Internet.", // The description of your project
  "main": "index.js"
  "license": "MIT" // The license of your project
  "devDependencies": {
    "mocha": "~3.1",
    "native-hello-world": "^1.0.0",
    "should": "~3.3",
    "sinon": "~1.9"
  },
  "dependencies": {
    "fill-keys": "^1.0.2",
    "module-not-found-error": "^1.0.0",
    "resolve": "~1.1.7"
  }
}
```
## Essential NPM Commands
- npm init : Runs you through a prompt to create you a package.json
- npm install <module>: Installs you a NPM package  and saves to package.json
  - --save: Saves to prod deps
  - --save-dev: saves to devDeps 
  - --global: saves globally. Good for CLI tools n such
  

