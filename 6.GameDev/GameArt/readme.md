# Game Art Basics

## Pixel Art Basics

- Have total control and can maniupulate every pixel vs large brush strokes
- There are shortcuts
- How to start
  - Sketch -> Line Art -> Refine -> Shade, cleanup, & complete
  - BlockShapes -> Refine -> Shade, cleanup, & complete
  - Doesn't matter which method
- Pick software and use it but must have some things to make your life easier

  - Pencil Tool: 1PX workhorse
  - Eyedropper: Absorb colours and make pallettes
  - Eraser
  - Bucket: Fills an empty area with 1 solid colour.
  - Selection Tool
  - Recolour Tool
  - Line Tool
  - Rotation Tool
  - Colour Settings
  - Circle Tool
  - Avoid Blur, Brushes, Blurred Gradient

  - Decide canvas size from the start.
  - 3DS: 400X240
  - DS: 256X192
  - GBA: 240X160
  - GB: 160X44

  - Decide on Sprite to Canvas Ratio

    - Large is about 1:24 or 4%
    - Low 1:38 or about 2.5%
    - Tiny: 1:300, .33%

  - When resizing pixels, stick to whole numbers, 100/200/300%

  - Don't mix different pixel ratios.

## Line Art

- Base of your sprite
- Try to keep same line thickness through whole sprite
- Thin lines are better for small areas
- Most pixel art has 1 px line art.
- Jaggies are an issue when drawing lines or curves in pixel art
- To fix jaggies, don't surround a row of pixels with bigger ones
  - so to fix, 2px, 1px, 3 px (Jaggie)
  - go 1px, 2px, 3px
- Basically take a pixel from the bottom row and shift up
- Don't draw lines pixel by pixel. Draw rough lines and chisel away parts that yuo don't need.
- Pixel art loves same stairs. Looks smoother. The steeper the line the higher the step
  - Don't mix stairs, will create jaggies
- Contrasting Colour creates lines and causes jaggies. Fix even in shading
- Pixel-perfect option, but don't rely on it. Not perfect

- Sprites have different outlining styles
  - No outline: Pixels with vector shaped graphics. Solid colours, have shading and broken outlines
  - Black Inline: Black outlines that go into the sprite as well. Can make sprites rather muddy.
  - Black Contour: Only he contour has a black outline, inside is completely coloured. Helps sprite standout from backgrounds and look clean.
  - Coloured: All outline is coloured corresponding to the colour it touches. Outline of a block will be the darkest shade of the inner block
  - Selective Outline: outline shaded with a light source. Most commpon type. Works great with backgrounds.

## Anti-Aliasing

- AA helps smooth out edges by placing pixels in little corners.
- Usually blend dark areas with light areas.
- Found between 2 shades as well, smoothing highlights from shadows.
- AA is not better than no AA antirerely, but most of the time will help your pixel art.
- Seomtimes AA can be icing on the cake
- If the style is relatiely simple, AA isn't necessary.
- If style has soft and smooth shapes, without AA detail is lost
- Colours with low constrast don't need much AA.

- AA
  - Pros:
    - Smootht curves on small sprites
    - Necessary for large sprites
    - Sub-pixeling animation
  - Cons:
    - Tedious if overdone
    - Blurs tiny sprites
- No AA

  - Pros:
    - Makes small sprites more readable
    - Limits your colours
    - Faster
  - Cons:
    - Creates jagged lineart
    - Sharp & Blocky

- Other reasons to put AA
  - Clarity: characters,faces, eyes usually draw attnetion. Want to make them recognizable
  - Detail: Smaller curves are often more jagged. Requires more AA than bigger curves
  - Line weight: AA can add or remove line weight.
  - High Constrast: try blending with intermediary pixels

### How to apply:

- About half of the length of the line. Too little is better than too much.
- One shade to start practicing.
- Two for smoother results.
- 3 if you are confident and got colours.
- Longer steps = Longer AA/More shades of AA
- Zoom out and judge for yourself
- AA on 45 degrees is uncommon.
- Centre of the cruve can be either lighter or darker. Depends on the curve type.
  - Convex Curve: Centre Light Colours, Ends dark colours
  - Concanve Cruve: Centre Dark Colours, Ends light colours
- AA impacts line weight. Dark = thicker, Light = thinner
- Banding is bad: two rows of pixels perfectly hugh each other. Makes curves look blocker. Lines appear thicker. Blurs your outline.

## AESprite Nice to knows

- ctrl+0 fit to window +/- for zooming
- b for pencil
