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

## Colours

- Most subjective part of sprites as they build the atmosphere of a game/picture
- Colour Theory is universal.
- Hue/Saturation/Value
- Colour Palletes are good for
  - Eye-drop to save time
  - Keeps you organized
  - Makes animation easier by reusing colours
- Pixel hart and having a low amount of colours go hand in hand.
- Reuse same colours across different shades (ramps).
- Doesn't matter how you use your pallette as long as it makes sense to you.
- Hue Shifting or coloured Shadows, to create an atmosphere or feeling
  - Regular Hue Shift: When you shift hue, for a brown, the shadow becomes a warm red. Up to you how much to sift hues. Either left or right.
    - Yellow is brighest clour of the rainbow. Purple is the darkest. Why generaly people often hue shift from yellow to purple
    - You can see hue shifting in greyscale
- Multiple Players - Can experiment with different colours by overlaying layers with opacity. Just eye drop after
- Saturation shifting is important too, more for highlights a particular area of your shading.
- Grey is great for canceling out colours and blending.
- Choosing Colours
  - Try to keep darker and lighter colours together on your ramps.
  - Amount of colours depends on pixel art.
  - Small sprites should be one ramp of 2-3 colours.
  - Avoid pure black when possible.
  - Give shadows a colour tint too. Compliment the shadow coulour.
  - Using blue, pruple, teals can give impressin of cold/sadder emotion.
  - reds, oranges, yellows can give a warmer/happier emotion
- Contrast:
  - Try choosing colours that add a lot of contrast to sprites.
  - Can have 1 main colour for each character design. either makes up most of the character or highlights most important features.
  - Then use sub colour to add extra features.

## Readability

- Means clarity, how well does the pixel art convey itself to the audience.
- Size matters. Smaller sprites are naturally harder to convey things.
- Big sprites need clean lines and solid drawings.
- Small sprites need recognizable features for readability.
- Even within the same canvas, your sprites can always be improved
- For small sprites, simplicity usually works. Don't overdo details and stick to simple shapes.
- In small sprites, one pixel can make te difference in how things are interpreted
- When asking yourself how big your sprite needs to be ask these feature questions:
  - Do I need to see their hands moving?
  - Do their mouths need to be visible or animated
  - Must facial expression be readable?
  - Do they wear or hold an item?
  - Do the sword have a megical gem in it?
- Try to figure out the smallest part that needs to be visisble, then you can figure out the minimal sprite size.
- Less is more, find what makes the character unique.
- Try taking photo art and pairing down to the essetentials.
- Hands:
  - start hands by painting shapes. Tiny line art is too hard. Flat shapes then detail.
  - Draw hands like mittens. Then add detail.
  - No point in highlighting every single finger.
  - Focus on index and the thumb. They define the hand.
  - Draw only 3 fingers and a thumb if needed.
  - Use different colours to separate each finger.
- Eyes:
  - eyes are main focus and highly important.
  - If no space for eyes, work our the shadows cast on the face to create the eye area.
  - Glasses: keep it simple
  - A few pixels make a big different when zoomed out.
- Head V Body Proportions.
  - Big heads give room for emotions and expressions. Not suited for every situation.
  - Heads ae the main reference for human proportin and they easily vary.
  - Characters with realistic proportions, focus on body language.
  - Give bodies personality by diversifying poses and body proportions.
  - Dif proportions can serve different functions ( world sprite, battle sprite, icon sprite, dialogue sprite)
- Sihoutees
  - Shows imortant features.
  - Highlights the character or objects action or function.
  - Can draw rough siloutte base and fill up with details.
  - Try not to overlay things, use colour contrast to tell features apart.
- Light & Shadow
  - Outlines take a lot of precious space.
  - Player with dark and light tones instead.
  - Light is used to show important details.
  - Dark fills the silhouette or outlines different features.
  - Use both to form shape, volume and depth depending on your light source.
- Spacing and Tangents is used so two objects dont tough and get blurred. Give it more room to breath. Can do so by getting rid of lines or re-arrange pixels.
- Sprites and Backgrounds
  - Sprites should always stand out from backgrounds
  - Add Outlines
  - Correcting Colours
  - Focus (foreground is sharp, background is blurrier)
- Spot readability issues by:
  - Using review thumbnails
  - Try blurring the picture you should be able to tell what it is
  - Waifu2x allows you to upscale any picture.

## Dithering

- technique to make gradients using limited colours.
- You use patterns to mix colours, like checkers.
- When to use dithering
  - too much makes it look rough and grainy.
  - large cel-shaded gradients without dithering result in flat and striped areas.
  - use when gradients that would otherwise use too many colours to do manually.
  - Things that don't animate
  - Textures (stylized dithering)
  - Heavy colour limitations
  - Backgrounds (skies, space, vast areas)

## Game Perspectives

- Perspective is how the world is viewed by the human eye.
- Further an object is, the smaller it looks. Closer it is the biger it looks.
- Terminology:
  - Plane: 2d flat surface that shows length and width.
  - Axis: geometric line with a fixed direction. Y up and down. X left and right. Z back and forth.
  - Vanishing point: two parallele lines mee at a single point. Like a road that extends toward the horizion and disappears into a single dot.
  - Projection: the way a 3d view is drawn in 2d.
  - Othographic: Flat views with no perspective.
- Othographic Projections:
  - Side Scroller: Just front
  - Top-Down: Mostly front, some top.
  - Top: All top
  - Isometric: Top-side-side
  - 45 dimetric: mostly top-little side- little side
  - Oblique: large front, little size, big top

## AESprite Nice to knows

- ctrl+0 fit to window +/- for zooming
- b for pencil
