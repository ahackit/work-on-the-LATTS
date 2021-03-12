# Tailwind Fundamentals

- Tailwind is a utility-first post-css framework

## Setup

- npm install tailwindcss postcss-cli autoprefixer
- npx tailwind init
- create postcss.config.js
```
module.exports = {
    plugins: [
        require('tailwindcss'),
        require('autoprefixer'),
    ]
}
```
- Create default.css file
  - Tailwind searches css files for directives and replaces with style code.
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

## What does Utility first mean?
- Utility first means that we ain't leaving HTML and we have just about all the properties we need to style and layout our HTML.
- There is plenty of documentation to list all of it, but examples of utilities classes are below
  - p-: Padding
  - m-: margin
  - h-: height
  - bg-color-#: background color with shade
- Most of the values given have more choices at lower values as finetuneing pixels at larger scales doesn't really make sense.

## Responsive Design
- Tailwind has 4 breakpoints by default
- Can set whatever properties using breakpoint:utility_class : sm:bg-green-500
- flex to get flex containers
- hidden to hide elements on specific breakpoints

## Psuedo-classes
- psuedo-class:style : hover:bg-green-500
- Need to specify variants in taildwind config. Order matters
```
variants: {
    backgroundColor: ['responsive', 'hover','active']
}
```

## Sometimes you gotta reuse a element with 50 classes
- In your tailwind.css file
```
@tailwind components;
.btn {
     @apply 50 utility classes   
}
.btn:hover {
    cuz psuedo classes don't work
}
@screen sm {
    .btn {
        
    }
}
```
## Extending the Design system
- in tailwind.config - see docs for all changes
```
theme: {
    extend: {
        colors: {
            'brand-blue' : '#1992d4'
        }
    }
}
```
## Optomize for production
- use purgecss to get rid of classes you aren't using.
