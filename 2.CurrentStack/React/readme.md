# React


## Bare Minimum React
- Need two libraries
  - React/ReactDOM

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>React Samples</title>
    </head>
    <body>
        <div id="root"></div>
        <script src="https://unpkg.com/react@16/umd/react.development.js></script>
        <script src="https://unpkg.com/react@16/umd/react-dom.development.js></script>
        <script>
        //Pure REact and Javascript
        </script>
    </body>
</html>
```

### React vs ReactDOM
- React libaries allows us to create elements
```
const dish = React.createElement("h1", "recipe-0"}, "Baked Salmon");
````
- ReactDOM allows us to render elements
```
ReactDOM.render(dish, document.getElementByID("root"));
```

### Elements can have children
```
React.createElement(
    "ul"
)
