# React

- [React](#react)
  - [Bare Minimum React](#bare-minimum-react)
    - [React vs ReactDOM](#react-vs-reactdom)
    - [Elements can have children](#elements-can-have-children)
    - [Render many elements using array functions](#render-many-elements-using-array-functions)
    - [Can also pass props through parameters](#can-also-pass-props-through-parameters)
  - [JSX](#jsx)
    - [Babel/Webpack](#babelwebpack)
      - [Create React App](#create-react-app)
    - [React Fragments](#react-fragments)
  - [React State Management](#react-state-management)
    - [useState](#usestate)
    - [Use spread operator for more advanced public APIs](#use-spread-operator-for-more-advanced-public-apis)
    - [State in Component Trees](#state-in-component-trees)
      - [Sending state down/up](#sending-state-downup)
    - [Using Ref vs Controlled Components](#using-ref-vs-controlled-components)
      - [Use custom Input hook instead of value/event callback for forms](#use-custom-input-hook-instead-of-valueevent-callback-for-forms)
    - [React Context](#react-context)
  - [Hooks](#hooks)
    - [useEffect](#useeffect)
      - [Dependency Aray](#dependency-aray)
    - [useMemo](#usememo)
    - [useCallback](#usecallback)
    - [useLayoutEffect](#uselayouteffect)
    - [Rules to follow for hooks](#rules-to-follow-for-hooks)
    - [useReducer](#usereducer)
    - [Improve Component Perofmrnace using memo](#improve-component-perofmrnace-using-memo)
  - [React Testing](#react-testing)
  - [React Router](#react-router)


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
```
- ReactDOM allows us to render elements
```
ReactDOM.render(dish, document.getElementByID("root"));
```

### Elements can have children
```
React.createElement(
    "ul",
    null,
    React.createElement("li', null, "2 lb salmon"),
)
```

### Render many elements using array functions
- Don't forget your `key` property
```
React.createElement(
    "ul",
    { className: "ingredeients" },
    items.map((ingredient, i) => React.createElement("li", {key: i}, ingredient)
    )
);
```

### Can also pass props through parameters
```
function IngredientsList({items}){
    return React.createElement(
        "ul",
        {className: "ingredients"},
        items.map((ingredient, i) => React.createElement("li", {key: i}, ingredients))
    )
}
```

## JSX 
- Nested Components
```
<IngredientsList>
    <Ingredient />
</IngredientsList>
```
- Classes
```
<h1 className="fancy">Baked Salmon</h1>
```
- JS Expressions
```
<h1>{title}</h1>
<input type="checkbox" defaultChecked={false} />
```
- Evaluation
```
<h1> {"Hello" + title}</h1>
```
- Mapping arrays with jsx
```
<ul>
{props.ingredients.map((ingredient, i) =>(
    <li key="{i}">{ingredient}</li>
))}
</ul>
```
- JSX isn't supportedby browsers

### Babel/Webpack
- Transpiles unsupported features into browser readable code.
- below is quicky and dirty. Not production suitable, use a build tool.
```
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
```
- For production use webpack and Node and bundle.
```
npm install --save-dev webpack webpack-cli

create webpack.config.js

var path = require('path');

module.exports = {
    entry: "./src/index.js".
    output: {
        path: path.join(__dirname, "dist", "assets"),
        filename: "bundle.js"
    },
    module: {
        rules: [{ test: /\.js$/, exclude: /node_modules/, loader: "babel-loader"}]
    }
}

npm install babel-loader @babel/core @babel/preset-env @babel/preset-react --save-dev

create .babelrc

{
    "presets": ["@babe;/preset-env", "@babel/preset-react]
}

add to package.json
"scripts": {
    "build": "webpack --mode production"
}
```
#### Create React App
- nice to have and avoid all the above
```
npm install -g create-react-app
create-react-app my-project
```


### React Fragments
- Can't have sibling elements at root of render.
- Use Fragment
```
<React.Fragment>
    <h1></h1>
    <p></p>
</React.Fragment>

or

<>
    <h1></h1>
    <p></p>
</>
```


## React State Management

### useState
- a hook that allows us to store state which will trigger rerenders if update
```
const [selectedStars, setSelectedStars] = useState(0);
```
### Use spread operator for more advanced public APIs
```
function StarRating({...props}){
    return <div {...props}>
    </div>
}
```

### State in Component Trees
- Not the best idea to distribute location of state through your tree. 
- Best to organize by feature and pass to components that need it when required
- Couple methods to handle this

#### Sending state down/up
- Take data from parent method and pass down via props. Ez
- To send data or notifications back up we used callbacks passed through props
```
function MyChild(someEvent){
    return (
        <input onClick={()=>someEvent()}></input>
    )
}
```

### Using Ref vs Controlled Components
- Ref Great way to reference dom elements directly like on form submit.
- use the useRef hook
```
const txtTitle = useRef();
return (
    <input ref={txtTitle}>
)
```
- Can also use Controlled components by letting the element control the values
```
<input
value={title}
onChange={event => setTitle(event.target.value)}
/>
```
- Controlled components rerender a lot. That's ok. Just don't add expensive processes here.

#### Use custom Input hook instead of value/event callback for forms
```
export const useInput = initialValue => {
    const [value, setValue] = useState(initialValue);
    return [
        {value, onChange: e=> setValue(e.target.value)},
        ()=> setValue(initialValue)
    ]
}

const [titleProps, resetTitle] = useInput("")
...
return (
    <input {...titleProps} >
)
```

### React Context
- Sometimes passing props down many components is not good. Sometimes best to access state from a single location for a specific feature directly.
- Use React Context
```
...
export const ColorContext = createContext();
render (
    <ColorContext.Provider value={{ colors}}>
        <App />
    </ColorContext.Provider>
)
```
- This wraps entire app in context provider, don't have to do that. Can wrap specific features
- Retrieve data by using useContext
```
const {colors} = useContext(ColorContext);
```
- We also may way to provide functions to mutate state in context
```
const ColorContext = createContext();

export default function ColorProvider({children}){
    const [colors, setColors] = useState(colorData);
    return(
        <ColorContext.Provider value={{colors, setColors}}>
            {children}  
        </ColorContext.Provider>
    )
}
```
- Can abstract consumers into a custom hook
```
const ColorContext = createContext();
export const useColors = () => useContext(ColorContext);
```

## Hooks
- Besides the ones covered above (useRef, useContext, useState, etc)
- We have other hooks that give us functionality.

### useEffect
- Allows us to call code after the initial render as a side effect
```
useEffect(()=>{
    alart('Checked:')
})
```
#### Dependency Aray
- Works with other stateful hooks
- Can watch state and change based on it
```
const [val, set] = useState("")

useEffect(()=>{
    console.log('val')
}, [val]);
```
- Can invoke only once with empty dependency array
- Returns from useEffect will be ran once component is removed from the tree
```
const [val, set] = useState("")

useEffect(()=>{
    console.log('val')
    return () => console.log('being removed')
}, [val]);
```
- Can also wrap all this behavior in custom hook

### useMemo
- Allows us to create a function thats used to calculate and create a memoized value. Will only recalculate the value once depedency has changed.
```
const words = useMemo(()=>{
    const words = children.split(" ");
    return words
}, [])
```
- This allows us to utilize memoization(sp?) to allow deep comparison on depedency array

### useCallback
- Like useMemo, but for functions
```
const fn = useCallback(()=>{
    console.log("hello")
}, [])
```

### useLayoutEffect
- Happens after Render but before useEffect
- useEffect should be your go to unless you need specific data before browser paint. Like grabbing width and height on resize

### Rules to follow for hooks
- Hooks only run in the scope of the component.
- Good idea to break functionality into multiple Hooks
- Don't use hooks inside conditional logic. Use conditional logic in hooks
  - (Hooks should only be called at top level)
- Nest async calls in it's own funciton within hooks
```

useEffect(()=>{
    const fn = async () => {
        await Promise()
    }
    fn()
}, [val]);
```

### useReducer
- Takes in the current state and returns a new state
```
const [checked, toggle] = useReducer(checked => !checked, false)
```

### Improve Component Perofmrnace using memo
```
const Cat = ({ name }) => {
    console.log(`rendering ${name}`);
    return <p>{name}</p>
}

const PureCat = memo(cat)
```
- Can use predicate as second argumment to determine if should rerender
```
const PureCat = memo(cat, (prevProps, nextProps) => false)
```

## React Testing
```
test("renders a star", ()=>{
    const div = document.createElement("div");
    ReactDom.render(<star />, div);
    expect(div.querySelector("svg")).toBeTruthy();
})
```

## React Router
- Allows us to pages for routes like the web should behave
```
import {BrowserRouter as Router} from "react-router-dom";

render (
    <Router>
        <App />
    </Router>
)

function App(){
    return(
        <div>
            <Routes>
                <Route path="/" element={<Home />} >
                    <Route path="/about" element={<About />} />
                    <Route path="/:id" element={<services />} />
                </Route>
                <Link to="about">About</Link>
                <Redirect from="services" to="about/services">
                <Route path="*" element={<Whoops404 />}></Route>
            </Routes>
        </div>
    )
}
```
- Also can useRoutes hook
```
function App(){
    element = useRoutes([
        {path:"/", element: <Home />}
    ])
    return element
}
```
- useParams for router params
```
let params = useParams();
```
- useNavigate for programmatic navigation
```
<section onClick={()=> navigate('/${id}`)}>
```
