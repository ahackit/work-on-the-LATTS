# LATT-WebComponents

Learn All The Things Web Components

## What Be Web Components?

No Vue, React, etc. Just write your own HTML standard and reuseable web components.

## Custom Elements

Custom HTML Tags. Can also extend other HTML Elements. Can hook into DOM LifeCycle events as well

- Constructor : Element created
- connectedCallback : everytime element is inserted into the DOM
- disconnectedCallBack: every element is removed from DOM
- attributeChangedCallback: called when attribute is removed, updated, or replaced

## Shadow DOM

Used for self contained components. Can add scoped styles and markup which aren't impacted by the rest of the CSS.

## HTML Templates

Define encapsulated markup of our web components. Templates allow us to store markup(HTML and CSS) and also can utilize slots for maximum reusability.
