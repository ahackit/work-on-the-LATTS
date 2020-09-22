# CSS

## The Fundamentals

- CSS is the way styling is applied to most, if not all, websites.
- CSS = Cascadin Style Sheets, meaning the last style applied to an attribute on a element is the style that gets applied.
- CSS can be writtin on the HTML element, in an HTML file in style tags, or in a separate CSS style sheet that the HTML file reference
- CSS can also be manipulated through Javascript.
- You can apply styles by specific the type of element either by the HTML tag, by a specific ID, or a specific class. (Hash is not class)
- CSS can also utilize psuedo selectors like on element hover or when an achor tag has been visited.
- CSS can also have scopes selectors so Style certain IDs only in this Class.
- Ultimately, there are an extrodorinary amount of properties that can be manipulated and it's best to reference documentation in general to find properties you are looking for.

## Layouts

Layouts are prob the most difficult thing to get right in CSS. We have a couple different tools to understand to get it right. 

- Box Model
  - Everything HTML element can be basically considered a box. You have the Content which is wrapped by Padding which is wrapped by a Border which is wrapped by Margin.
  - Content is the size of the text/image or basically the width defined on an element.
  - Padding is the space between the content and the border
  - Margin is the space between this HTML element and the next.
- Positioning
  - Static: Not impacted by properties set to adjust the placement of an element.
  - Relative: Positioned relative to it's normal position within the flow of a document. 
  - Fixed: Always stays in same spot in the viewport. Different from static. Doesn't leave a gap in the flow of the document.
  - Absolute: Positioned relative to the nearest positioned ancestor.
  - Sticky: Toggles between relative and fixed based on viewport position.
  - Z-index: View layers and how to organize who's on top when you have overlapping elements
- Display: 
  - Specifies the display behavior(type of rendering box) of an element
  - Inline: Height/Width properties do not impact this element
  - Block: Puts the element on a new line and takes up the width of the screen.
  - None: Removes element from flow
  - inherit: Gets it from it's momma.
  - flex/grid: More later.
- Float:
  - Specifies how an element floats in regards to sibling elements. Prob don't need to use this as much more.
- Flex Box:
  - Flex Box is a standard used to organize items within a container.
  - Organization is done against a main and cross axis.
  - You typically organize items via a Flex Container and Flex items and both can have properties used to adjust their layout.
- Grid: 
  - Where flexbox is used for one dimensional layouts, Grid is used for two dimension layouts. 
  - Grid also have grid containers and grid items.
  - Organization is done via breaking up your layout into rows and columns (Grid Tracks)
  - In those intersections on Grid Cells. 
  - Cells can be combined Grid areas to contain content.

The important take away here is you will most likely utilize all of these properties to achieve your layouts. Know why you are choosing a layout standard. IE don't need to utilize grid when we are just trying to line up items in a single dimensional way (can use flex box)

## Response Design and Media Queries
Response Design is the practice of building web pages that are organized and look great on many devices with many different view ports.

Media queries are used to accomplish this by specifying different resolutions that we target and building layouts for each of those resolutions.



