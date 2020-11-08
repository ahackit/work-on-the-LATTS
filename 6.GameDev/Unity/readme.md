# Unity

- [Unity](#unity)
  - [Input](#input)
  - [2D](#2d)
    - [2D Sorting](#2d-sorting)
    - [Sprite Tools](#sprite-tools)
    - [Importing and Setting Up Sprites](#importing-and-setting-up-sprites)
    - [Setting Image as a Sprite](#setting-image-as-a-sprite)
      - [Sprite Renderer](#sprite-renderer)
      - [Sprite Editor](#sprite-editor)
    - [Tilemap](#tilemap)
      - [Workflow](#workflow)
    - [Physics](#physics)
      - [Rigidbody2D](#rigidbody2d)
      - [Collider2D](#collider2d)
      - [Physics 2D](#physics-2d)
  - [Graphics](#graphics)
    - [Render Pipelines](#render-pipelines)
    - [Cameras](#cameras)
    - [Post-processing](#post-processing)
    - [Lighting](#lighting)
    - [Particle Systems](#particle-systems)
  - [Scripting](#scripting)
    - [Events](#events)
    - [Coroutnes](#coroutnes)
    - [Important Classes](#important-classes)
  - [Audio](#audio)
  - [Animation](#animation)
  - [UI](#ui)

## Input

- The Input Manager window allows you to define input axes and their associated actions for your Project.
- To access it, from Unity’s main menu, go to Edit > Project Settings, then select the Input category.

```
float moveSpeed = 10;
//Define the speed at which the object moves.

float horizontalInput = Input.GetAxis("Horizontal");
//Get the value of the Horizontal input axis.

float verticalInput = Input.GetAxis("Vertical");
//Get the value of the Vertical input axis.

transform.Translate(new Vector3(horizontalInput, 0, verticalInput) * moveSpeed * Time.deltaTime);
//Move the object to XYZ coordinates defined as horizontalInput, 0, and verticalInput respectively.
```

## 2D

- Sprites are rendered with a Sprite Renderer component
- you can use a Sprite Creator tool to make placeholder 2D images.
- Unity has a separate physics engine for handling 2D physics so as to make use of optimizations only available with 2D. The components correspond to the standard 3D physics components such as Rigidbody, Box Collider and Hinge Joint, but with “2D” appended to the name. So, sprites can be equipped with Rigidbody 2D, Box Collider 2D and Hinge Joint 2D

### 2D Sorting

- Order of sorting
  - Sorting Layer and Order in Layer
    - Set the Renderer to an existing Sorting Layer or create a new one to determine its priority in the rendering queue. Change the value of the Order in Layer to set the Renderer’s priority among other Renderers within the same Sorting Layer.
  - Specify Render Queue
    - can specify the Render Queue type of the Renderer in its Material settings or in the Shader settings of its Material.
  - Distance to Camera
  - Perspective/Orthographic
  - Custom Axis sort mode
  - Sprite Sort Point
  - Sorting Group
  - Material/Shader
  - A Tiebreaker occurs when multiple Renderers have the same sorting priorities.

### Sprite Tools

- Sprite Creator: Create placeholder sprites in your project
- Sprite Editor: lets you extract sprite graphics from larger image and edit a number of component images with a single texture.
- Sprite Renderer: Sprites are rendered with a Sprite Renderer component rather than the Mesh Renderer
  used with 3D objects
- Sprite Packer: Use Sprite Packer to optimize the use and performance of video memory by your project.

### Importing and Setting Up Sprites

- Place directly into your Unity asets folder
- In Unity, go to Assets > Import New Asset

### Setting Image as a Sprite

- Automatic if your project is 2D
- if Not, change the Texture Type on the asset

```
var camera = GetComponent<Camera>();

camera.transparencySortMode = TransparencySortMode.CustomAxis;

camera.transparencySortAxis = new Vector3(0.0f, 1.0f, 0.0f);
```

#### Sprite Renderer

- Automatically creates Sprite Renderer when Sprite is created
- Important Properties
  - Sprite: Sprite texture assigned
  - Color: Tints the Sprites image
  - Flip: Flips texture among the checked axis.
  - Material: Defines Material on sprite
  - Draw Mode: Defines how sprite scales
    - Simple: Default option
    - Sliced: for 9-sliced
    - Tiled: Caused 9-sliced to stile
    - Continous: the midsection tiles evenly when the Sprite dimensions change.
    - Adapative: Sprite texture stretches when its dimensions change, similar to Simple mode.
  - Sorting Layer: Controls priority
  - Order in Layer: Set the render priority of the Sprite within its Sorting Layer.
  - Mask Interaction - Set how the Sprite Renderer behaves when interacting with a Sprite Mask

#### Sprite Editor

- Sprite Mode to Multiple in the Texture Import Inspector if Sprite Sheet
- Can Provide dimensions to slice
- Can also Automatic Slice
- Can change Physics Shape

### Tilemap

- Tilemap component is a system which stores and handles Tile Assets for creating 2D levels.
- It transfers the required information from the Tiles placed on it to other related components such as the Tilemap Renderer and the Tilemap Collider 2D
- Download the 2D Tilemap Editor package via the Package Manager, as it is not included in the Unity Editor default installation.
- the Grid component is automatically parented to the Tilemap and acts as a guide when you lay out Tiles onto the Tilemap.
- Grid component is a guide which helps to align GameObjects, such as Tiles, based on a selected layout.
- Tilemap Renderer component is part of the Tilemap GameObject. It determines how Tileset on the Tilemap are rendered.

#### Workflow

- Create a Tilemap that you will paint your Tiles on. A Grid GameObject is also automatically created as a parent to the Tilemap in the process.
- Create Tile Assets directly, or generate Tiles automatically by bringing Sprites into the Tile Palette window.
- Create a Tile Palette that contains your Tile Assets and use a variety of painting Brushes to Paint onto Tilemaps.
- You can attach the Tilemap Collider 2D component to your Tilemaps to have them interact with Physics2D.

### Physics

#### Rigidbody2D

- The 2D physics engine is able to move colliders and make them interact with each other, so a method is required for the physics engine to communicate this movement of colliders back to the Transform components. This movement and connection with colliders is what a Rigidbody 2D component is for.
- Rigidbody 2Ds cannot collide with each other without colliders.
- Dynamic Rigidbody 2D is designed to move under simulation. It has the full set of properties available to it such as finite mass and drag, and is affected by gravity and forces. A Dynamic body will collide with every other body type, and is the most interactive of body types.
  - Do not use the Transform component to set the position or rotation of a Dynamic Rigidbody 2D. The simulation repositions a Dynamic Rigidbody 2D according to its velocity; you can change this directly via forces applied to it by scripts
    , or indirectly via collisions and gravity.
- Kinematic Rigidbody 2D is designed to move under simulation, but only under very explicit user control. While a Dynamic Rigidbody 2D is affected by gravity and forces, a Kinematic Rigidbody 2D isn’t.
- Kinematic Rigidbody 2D is designed to be repositioned explicitly via Rigidbody2D.MovePosition or Rigidbody2D.MoveRotation.
  - Kinematic Rigidbody 2D does still move via its velocity, but the velocity is not affected by forces or gravity. A Kinematic Rigidbody 2D does not collide with other Kinematic Rigidbody 2Ds or with Static Rigidbody 2Ds; it only collides with Dynamic Rigidbody 2Ds
- Static Rigidbody 2D is designed to not move under simulation at all; if anything collides with it, a Static Rigidbody 2D behaves like an immovable object (as though it has infinite mass). It is also the least resource-intensive body type to use. A Static body only collides with Dynamic Rigidbody 2Ds. Having two Static Rigidbody 2Ds collide is not supported, since they are not designed to move.

#### Collider2D

- Collider 2D components define the shape of a 2D GameObject for the purposes of physical collisions.
  - Circle Collider 2D for circular collision areas.
  - Box Collider 2D for square and rectangle collision areas.
  - Polygon Collider 2D for freeform collision areas.
  - Edge Collider 2D for freeform collision areas and areas - which aren’t completely enclosed (such as rounded convex - corners).
  - Capsule Collider 2D for circular or lozenge-shaped - collision areas.
  - Composite Collider 2D for merging Box Collider 2Ds and Polygon Collider 2Ds.

#### Physics 2D

- Physics Material 2D is used to adjust the friction and bounce that occurs between 2D physics objects when they collide. You can create a Physics Material 2D from the Assets menu (Assets > Create > Physics Material 2D ).

## Graphics

### Render Pipelines

- In Unity, you can choose between different render pipelines. A render pipeline performs a series of operations that take the contents of a Scene, and displays them on a screen. At a high level, these operations are culling, rendering, post-processing
- The Built-in Render Pipeline is Unity’s default render pipeline. It is a general-purpose render pipeline that has limited options for customization.
- The Universal Render Pipeline (URP) is a Scriptable - Render Pipeline that is quick and easy to customize, and lets you create optimized graphics across a wide range - of platforms.
- The High Definition Render Pipeline (HDRP) is a - Scriptable Render Pipeline that lets you create - cutting-edge, high-fidelity graphics on high-end - platforms.
- You can create your own custom Scriptable Render Pipeline (SRP) using Unity’s Scriptable Render Pipeline API. You can do this from scratch, or you can modify URP or HDRP to suit your needs.

### Cameras

- Can have many cameras and can switch them

```
public class ExampleScript : MonoBehaviour {
    public Camera firstPersonCamera;
    public Camera overheadCamera;

    // Call this function to disable FPS camera,
    // and enable overhead camera.
    public void ShowOverheadView() {
        firstPersonCamera.enabled = false;
        overheadCamera.enabled = true;
    }

    // Call this function to enable FPS camera,
    // and disable overhead camera.
    public void ShowFirstPersonView() {
        firstPersonCamera.enabled = true;
        overheadCamera.enabled = false;
    }
}
```

### Post-processing

- Unity provides a number of post-processing effects and full-screen effects that can greatly improve the appearance of your application with little set-up time. You can use these effects to simulate physical camera and film properties, or to create stylised visuals.

### Lighting

### Particle Systems

- Two Particle Systems
- The Built-in Particle System: A solution that gives you full read/write access to the system, and the particles it contains, from C# scripts. You can use the Particle System API to create custom behaviors for your particle system.
- The Visual Effect Graph: A solution that can run on the GPU to simulate millions of particles and create large-scale visual effects. The Visual Effect Graph also includes a visual graph editor to help you author highly customizable visual effects.

## Scripting

- Create script and attach to GameObject
- Update function is the place to put code that will handle the frame update for the GameObject.
- Start function will be called by Unity before gameplay begins (ie, before the Update function is called for the first time) and is an ideal place to do any initialization.
- `public string myName;` makes field editable in inspector
- Prefabs come in very handy when you want to instantiate complicated GameObjects
  or collections of GameObjects at run time

```
 public GameObject myPrefab;
 Instantiate(myPrefab, new Vector3(0, 0, 0), Quaternion.identity);
```

### Events

### Coroutnes

Coroutines
Normal coroutine updates are run after the Update function returns. A coroutine is a function that can suspend its execution (yield) until the given YieldInstruction finishes. Different uses of Coroutines:

yield The coroutine will continue after all Update functions have been called on the next frame.
yield WaitForSeconds Continue after a specified time delay, after all Update functions have been called for the frame
yield WaitForFixedUpdate Continue after all FixedUpdate has been called on all scripts
yield WWW Continue after a WWW download has completed.
yield StartCoroutine Chains the coroutine, and will wait for the MyFunc coroutine to complete first.

```
IEnumerator Fade()
{
    for (float ft = 1f; ft >= 0; ft -= 0.1f)
    {
        Color c = renderer.material.color;
        c.a = ft;
        renderer.material.color = c;
        yield return new WaitForSeconds(.1f);
    }
}
void Update()
{
    if (Input.GetKeyDown("f"))
    {
        StartCoroutine("Fade");
    }
}
```

### Important Classes

- GameObjectThe fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. More info
- See in Glossary: Represents the type of objects which can exist in a Scene.
- MonoBehaviour: The base class from which every Unity script derives, by default.
- Object: The base class for all objects that Unity can reference in the editor.
- Transform: Provides you with a variety of ways to work with a GameObject’s position, rotation and scale via script, as well as its hierarchical relationship to parent - and child GameObjects.
- Vectors: Classes for expressing and manipulating 2D, 3D, and 4D points, lines and directions.
- Quaternion: A class which represents an absolute or relative rotation, and provides methods for creating and manipulating them.
- ScriptableObject: A data container that you can use to save large amounts of data.
- Time (and framerate management): The Time class allows you to measure and control time, and manage the framerate of your project.
- Mathf: A collection of common math functions, including trigonometric, logarithmic, and other functions commonly required in games and app development.
- Random: Provides you with easy ways of generating various commonly required types of random values.
- Debug: Allows you to visualise information in the Editor that may help you understand or investigate what is going on in your project while it is running.
- Gizmos and Handles: allows you to draw lines and shapes in the Scene view and Game view, as well as interactive handles and controls.

## Audio

- Unity can import audio files in AIFF, WAV, MP3 and Ogg formats

## Animation

## UI
