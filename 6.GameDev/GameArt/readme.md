# Game Art Basics

- [Game Art Basics](#game-art-basics)
  - [Pixel Art Basics](#pixel-art-basics)
    - [How to start](#how-to-start)
    - [Software](#software)
    - [Canvas Size](#canvas-size)
  - [Line Art](#line-art)
    - [Jaggies](#jaggies)
    - [Diaganols](#diaganols)
    - [Outlining Styles](#outlining-styles)
  - [Anti-Aliasing](#anti-aliasing)
  - [Reasons to put AA](#reasons-to-put-aa)
    - [How to apply:](#how-to-apply)
  - [Colours](#colours)
    - [Temperature](#temperature)
    - [Color Schemes](#color-schemes)
    - [Colour Palletes are good for](#colour-palletes-are-good-for)
    - [Hue Shifting](#hue-shifting)
    - [Choosing Colours](#choosing-colours)
  - [Readability](#readability)
    - [How big should my sprite be?](#how-big-should-my-sprite-be)
    - [How to make hands readable](#how-to-make-hands-readable)
    - [How to make eyes readable](#how-to-make-eyes-readable)
    - [Head Vs Body Proportions](#head-vs-body-proportions)
    - [Silhoullettes](#silhoullettes)
    - [Light & Shadow](#light--shadow)
      - [Lighting terms](#lighting-terms)
      - [Steps for adding lighting and shadows](#steps-for-adding-lighting-and-shadows)
    - [Sprites and backgrounds](#sprites-and-backgrounds)
    - [Ways to spot readability issues.](#ways-to-spot-readability-issues)
  - [Dithering](#dithering)
    - [When to use dithering](#when-to-use-dithering)
  - [Game Perspectives](#game-perspectives)
    - [Terminiology](#terminiology)
    - [Othographic Projections](#othographic-projections)
      - [Side Scroller:](#side-scroller)
      - [Top-Down:](#top-down)
      - [Top:](#top)
      - [Isometric:](#isometric)
      - [45 dimetric:](#45-dimetric)
      - [Oblique:](#oblique)
  - [Clean Up](#clean-up)
    - [Things to check for cleanup](#things-to-check-for-cleanup)
    - [Other tweaks for cleanup](#other-tweaks-for-cleanup)
  - [SubPixeling](#subpixeling)
    - [Places to use subpixeling](#places-to-use-subpixeling)
    - [Shifting Pixels](#shifting-pixels)
    - [Line Weight](#line-weight)
    - [Using Direction with subpixeling](#using-direction-with-subpixeling)
    - [Using motion with subpixeling](#using-motion-with-subpixeling)
  - [Animation](#animation)
    - [Timing Standards](#timing-standards)
    - [Key Animation Techniues](#key-animation-techniues)
    - [Working methods for animation](#working-methods-for-animation)
    - [Parallax Scrolling](#parallax-scrolling)
  - [AESprite Nice to knows](#aesprite-nice-to-knows)

## Pixel Art Basics

- Have total control and can maniupulate every pixel vs large brush strokes
- There are shortcuts

### How to start

- Sketch -> Line Art -> Refine -> Shade, cleanup, & complete
- BlockShapes -> Refine -> Shade, cleanup, & complete
- Doesn't matter which method

### Software

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

### Canvas Size

- Decide Canvas Size from the start

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

### Jaggies

- Jaggies are an issue when drawing lines or curves in pixel art
- To fix jaggies, don't surround a row of pixels with bigger ones
  - so to fix, 2px, 1px, 3 px (Jaggie)
  - go 1px, 2px, 3px
- Basically take a pixel from the bottom row and shift up
- Don't draw lines pixel by pixel. Draw rough lines and chisel away parts that yuo don't need.
- Contrasting Colour creates lines and causes jaggies. Fix even in shading

### Diaganols

- Pixel art loves same stairs. Looks smoother. The steeper the line the higher the step
  - Don't mix stairs, will create jaggies
- Pixel-perfect option, but don't rely on it. Not perfect

### Outlining Styles

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

## Reasons to put AA

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
- Hue: called the identity of the color, if it’s red, green, blue, but not how bright or intense it is.
- Saturation: the intensity of color or pigment in a color. A bright red has high saturation, opposing a grey color, which has very low saturation.
- Value: amount of light a color has. A light orange has a high value, a dark orange has a low value. Usually this is directly related to light; where there’s light there’s a high value color and the opposite in the shadow.

### Temperature
- Red hues are hot and blue hues are cold
- High saturation is for the extremes (hot or cold) and low saturation are for temperatures in the middle. Pure gray is usually perceived as slightly cold.
- Value is complicated, but most of the time, high values mean hot and low values mean cold.

### Color Schemes
- Monochromatic: Single hue with many different shades
- Complemenatary Colors: Usually one of the colors is the main one, while the complementary color, the one on the other side of the wheel, is used in some details. Red and green, blue and orange, and purple and lime are some other examples.
- Analogous is a scheme made by choosing a main color, green in this example, and two others from nearby hues. This color scheme is usually very calming and comfortable. It’s great for low-contrast and harmonious images.
- 

### Colour Palletes are good for
  - Eye-drop to save time
  - Keeps you organized
  - Makes animation easier by reusing colours
- Pixel art and having a low amount of colours go hand in hand.
- Reuse same colours across different shades (ramps).
- Doesn't matter how you use your pallette as long as it makes sense to you.

### Hue Shifting

- Hue Shifting or coloured Shadows, to create an atmosphere or feeling
  - Regular Hue Shift: When you shift hue, for a brown, the shadow becomes a warm red. Up to you how much to sift hues. Either left or right.
    - Yellow is brighest clour of the rainbow. Purple is the darkest. Why generaly people often hue shift from yellow to purple
    - You can see hue shifting in greyscale
- Multiple layers - Can experiment with different colours by overlaying layers with opacity. Just eye drop after
- Saturation shifting is important too, more for highlights a particular area of your shading.
- Grey is great for canceling out colours and blending.

### Choosing Colours

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
- In small sprites, one pixel can make the difference in how things are interpreted

### How big should my sprite be?

- When asking yourself how big your sprite needs to be ask these feature questions:
  - Do I need to see their hands moving?
  - Do their mouths need to be visible or animated
  - Must facial expression be readable?
  - Do they wear or hold an item?
  - Do the sword have a megical gem in it?
- Try to figure out the smallest part that needs to be visisble, then you can figure out the minimal sprite size.
- Less is more, find what makes the character unique.
- Try taking photo art and pairing down to the essetentials.

### How to make hands readable

- start hands by painting shapes. Tiny line art is too hard. Flat shapes then detail.
- Draw hands like mittens. Then add detail.
- No point in highlighting every single finger.
- Focus on index and the thumb. They define the hand.
- Draw only 3 fingers and a thumb if needed.
- Use different colours to separate each finger.

### How to make eyes readable

- eyes are main focus and highly important.
- If no space for eyes, work our the shadows cast on the face to create the eye area.
- Glasses: keep it simple
- A few pixels make a big different when zoomed out.

### Head Vs Body Proportions

- Big heads give room for emotions and expressions. Not suited for every situation.
- Heads ae the main reference for human proportin and they easily vary.
- Characters with realistic proportions, focus on body language.
- Give bodies personality by diversifying poses and body proportions.
- Dif proportions can serve different functions ( world sprite, battle sprite, icon sprite, dialogue sprite)

### Silhoullettes

- Shows imortant features.
- Highlights the character or objects action or function.
- Can draw rough siloutte base and fill up with details.
- Try not to overlay things, use colour contrast to tell features apart.

### Light & Shadow

- Outlines take a lot of precious space.
- Play with dark and light tones instead.
- Light is used to show important details.
- Dark fills the silhouette or outlines different features.
- Use both to form shape, volume and depth depending on your light source.
- Spacing and Tangents is used so two objects dont tough and get blurred. Give it more room to breath. Can do so by getting rid of lines or re-arrange pixels.

#### Lighting terms
- Volume Shadow: elf-projected soft shadow. It’s the result of the light being blocked by the object’s own volume.
- Terminator: transition zone between the light area and the dark area of an object. It can be soft or sharp. In pixel art we favor sharp transitions to avoid banding
- Projected Shadow: When one object projects a patch of shadow into another. This is usually a very sharp shadow.
- Reflection: known as specular highlight, it’s the brightest spot in the object. Glossy and reflective objects have small and focused highlights. Rougher objects may not have a reflection highlight.
- Highlight: basic lighter area of an object, imagine it as the reverse of the volume shadow.
- Rim Light:  the light is coming from the back it looks almost like a bright outline. This is usually cast by a secondary, dimmer light.
- Bounce Light:  little hard to see sometimes but this is a slightly brighter spot in the volume shadow, caused by the light bouncing off the ground and back onto the object.

#### Steps for adding lighting and shadows
- Start with the basic colors and shapes, I like to start with the darker colors and paint the brighter ones later, but that’s a personal preference.
- Paint the basic light/shadow inside the object, keep your color count low for now.
- Draw projected shadows.
- Draw the details, engravings and other small parts.
- Correct the shapes, reinforce the shadows and highlights.
- Finish up with some extra anti-alias and outlines, if necessary.

### Sprites and backgrounds

- Sprites should always stand out from backgrounds
- Add Outlines
- Correcting Colours
- Focus (foreground is sharp, background is blurrier)

### Ways to spot readability issues.

- Using review thumbnails
- Try blurring the picture you should be able to tell what it is
- Waifu2x allows you to upscale any picture.

## Dithering

- technique to make gradients using limited colours.
- You use patterns to mix colours, like checkers.

### When to use dithering

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

### Terminiology

- Plane: 2d flat surface that shows length and width.
- Axis: geometric line with a fixed direction. Y up and down. X left and right. Z back and forth.
- Vanishing point: two parallele lines mee at a single point. Like a road that extends toward the horizion and disappears into a single dot.
- Projection: the way a 3d view is drawn in 2d.
- Othographic: Flat views with no perspective.

### Othographic Projections

#### Side Scroller:

- Just front
- Most common perspective. Often associated with Platformers.

#### Top-Down:

- Mostly front, some top.
- grid made up of square tiles which makes creating worlds and environments a breeze.
- Associated with free-roaming overworld and suitable for exploration.

#### Top:

- All top
- Exactly 90 degrees. Only works with particular set of game-play types.

#### Isometric:

- Top-side-side
- Means that all axes are equal.
- Often associated with diagonal movement.
- Can't have exact 30 degrees in pixel art, so stairs of 2 pixels is common.
- TO convert sprite to an isometric view, skew it by 30 degrees, adjust te sprite to add more depth, clean up and fill the gaps.

#### 45 dimetric:

- mostly top-little side- little side
- Only 2 axes are equal
- Very uncommon. Useful for high structures.

#### Oblique:

- large front, little size, big top
- Front is flat, rest is slanted.
- Side scrollers + 2 more planes
- Use grid and lines to help with perspectives.

## Clean Up

- Describes all the finishing touches and possible improvements. Always more adjustments before calling it a day.
- Shape - Refine - Finish
- Sketch - Flat Colours - Shading - Details
- Cleaner shapes is pixels of the same colour clustered together.
- Create multiple versions and vote on your favorite.
- Use selection tool to move pixels about instead of redrawing.
- To make things sharp, play with light and shadows, add more higlights, and add darker ines to make things pop

### Things to check for cleanup

- silhouette
- design
- colours
- pixel shapes
- lighting
- readability

### Other tweaks for cleanup

- Change contrast
- Clean up tangents
- Tought u plight and shadow
- Change proportions

## SubPixeling

- Gives the illusion of something smaller than 1 pixel. Subpixel means under a pixel or smaller than a pixel.
- Can be found in still-images and animation
- AA is behind SubPixeling

### Places to use subpixeling

- Easing in and Out: Difficult to draw in-betweens tightly together without an unwanted wobble effect
- Idle Animations: You either create bouncy or subtle animations using subpixeling along with moving parts.
- Giving Life to Still Parts: Giving still parts subpixeling will help it stand out.
- Small Resolutins: Tought to move anything around in a small canvas
- Wind Effects, Laughing, Shaking, Shivering, Staggering: Movements where the characters or objects barely move can easily benefit from some subpixels

### Shifting Pixels

- Moving a pixel 1/2 px ahead turns the next pixel darker or lighting by changing brightness.
- Value and colour are carried over to next pixel in animation
- Don't need to move every pixel. Thats banding which is bad. Animation and readability matters more than overdoing subpixeling
- Re-use colours already found in your psirte for subpixeling

### Line Weight

- Dark Backgrounds thin lines = dark
- Light backgrounds thin lines - light

### Using Direction with subpixeling

- Subpixeling aniomation requires you to duiplicate frames and edit it slighty. Quickly switch back and forth
- Direction of subpixeling follows the angle of the shape.
- Angle horizontal = subpixeling horizontal
- Angle vertical = subpixeling vertial

### Using motion with subpixeling

- AA follows every movement in your animation.
- Try to keep 1-2 shades for subpixeling motion AA

## Animation

- Animation is the study of motion
- Good animation relies on readable key frames

### Timing Standards

- Ones: 60FPS Drawings Per Second: 30 FPS Drawings per second
- Twos: 30 Drawings Per Second: 15 Drawings per second
- Threes: 20 Drawings Per Second: 10 Drawings per second

### Key Animation Techniues

- Squash and Stretch: Volume is conserve. If you squash something in height, you need to stretch it's width.
- Anticipation: SET part in ready...set...go... Moment you preare an action. No mater how subtle or how extreme. Movement most often goes in the opposite direction of where the main action is going.
- Breakdown: You don't need to go directly from A to B keyframes. Add something inbetween. Actor raising arm but gets there in a diagnaol.
- Ease in and out: Easining means that the inbetweens faour the key frame. Accelration and deceleration.
- Smears: In-betweens that mimic the effects of motion blur. Visual trick. don't stay long. Smears best animated on ones at 24FPS. Can also have smeared after image but hold with a looping effect.
- Overshoots: Frames where part your animating goes past its destination only bounce back to keyframe. GIves animations a nice snap or pop
- Overlap & follow through:
  - Overlap: Some parts lead, others ffollow with a delay.
  - FOllow Through: Adds extra movement to characters and objects. Make motions more realistic.
  - Main Action - Overlap -Held Drawing Action has ended, follow thourgh

### Working methods for animation

- Silhoutte animation: useful for large moments
- Recycling Frames: Useful to keep a consistent style and for staying on a model. Uses selection stool. C
  - Copy, Resize, sliding,rotating, cutting, skeweing
  - Combine with Silhoutte!
- Simple lineart: line art, colours, shading, clean-up. Its the whole pixel art process with little reuse.
- Pose to Pose: plannign your work with key frames, adding inbetweens to connect them.
- Straight ahead: animating frames as you go, improvising your way through timeline.
- Pose to Pose + straight ahead: mix of both
- Limited Frames
  - Have strong keyframe techniques.
  - Minimum amount of frames is 3.

### Parallax Scrolling

- Add more depths ny dividing background into layers and moving at different speeds.
- Closer = faster, farther= slower

## AESprite Nice to knows

- ctrl+0 fit to window +/- for zooming
- b for pencil
- Try to keep a .ase file along with exported versions
  - ctrl+alt+shift+s
  - Can also resize on the export
- Go with pixel perfect on initial lines, but turn it off for outlines
- Alt +B for new animation frame. <> to mvoe frames
- 