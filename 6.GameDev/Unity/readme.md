# Unity

- [Unity](#unity)
  - [Scenes](#scenes)
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
  - [Audio](#audio)
  - [Animation](#animation)
  - [UI](#ui)
  - [Scripting](#scripting)
    - [Important Classes](#important-classes)
    - [ScriptableObjects](#scriptableobjects)
    - [MonoBehaviour](#monobehaviour)
      - [Finding GameObjects](#finding-gameobjects)
    - [Prefabs](#prefabs)
    - [SceneManagement](#scenemanagement)
    - [Sprites/Textures](#spritestextures)
    - [Input](#input-1)
      - [Mouse](#mouse)
    - [Time](#time)
    - [UI](#ui-1)
    - [Audio](#audio-1)
    - [Events](#events)
    - [Coroutnes](#coroutnes)
      - [Courutines Vs Async](#courutines-vs-async)
    - [Open-Closed Principles](#open-closed-principles)
    - [Dependency Injection](#dependency-injection)
    - [Debugging](#debugging)

## Scenes
- Scenes are ways to reference many Gameobjects.
- You can have multiple scenes
- You can also have scenes separated for specific types of Objects
  - This requires abstract ways of communicating since FindObject can't find objects not in the scene
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
- Should try to Prefab your camera as early as possible to avoid making changes and not having it reflect to to other places.

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

## Audio

- Unity can import audio files in AIFF, WAV, MP3 and Ogg formats

## Animation

## UI

## Scripting

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


### ScriptableObjects
- START HERE AND USE MONOBEHAVIOUR WHEN YOU NEED IT
- Great way of sharing data, state.
```
public class PlayerData {

  [SerializeField]
  private float maxHealth;

  private float _currentHealth;

  public float HealthPercentage => (_currentHealth * 100f) / maxHealth;
}
```
- Great way of removing depedencies on monobehaviours and having to find them all over the place
```
public abstract class
AAbility : ScriptableObject {
  public abstract void CastAbility (Entity self, Entity target);
}

public class LifeStealAbility : AAbility {

[SerializeField]
float damage;

public override void CastAbility (Entity self, Entity target) {
    target.TakeDamage(damage);
    self.Heal(damage/2f);
  }
}
```
- Most of your "systems" can just be ScriptableObjects, serve nearly the same purpose as Singletons.
- Can use ScriptableObjects to act as Event Systems
  
### MonoBehaviour

- Create script and attach to GameObject
- Awake happens before Start
- Start function will be called by Unity on First Frame and is an ideal place to do any initialization.
- `public string myName;` makes field editable in inspector
- Update runs every frame
- Fixed update runs every physics tick (50 times per second, can be edited)
  - Independent of frame rate, so is consistent for physics updates.
- Try to Avoid things happening in update unless they need to like conditionals and checks
- OnEnable/Disable - very handy for object pooling
- Create references if you need to use a reflection method
- Use LazyInitialization to avoid Script Execution Order
```
public class EnemyManager {
  private List<IEnemy> _enemiesInCombat;
  public static EnemyManager INSTANCE;


  private bool _initialized = false;

   //returns true if inited now
  private bool Init() {
    if(_initialized)
      return false;
    
    INSTANCE = this;
    _enemiesInCombat = new List<IEnemy>();
    _initialized = true;
    return true;
  }

  public void AddEnemyToCombatList (IEnemy enemy) { 
    Init();
    _enemiesInCombat.Add(enemy);
  }

  public IEnemy GetEnemyClosestToPoint(Vector3 point) {
    if(Init()) { return null; }

    //...finding enemy logic…

    return closestEnemyToPoint;
  }
}
```

#### Finding GameObjects
- FindObjectOfType is slowest, but most maintable.
- Use caching to avoid performance hits


### Prefabs
- Prefabs come in very handy when you want to instantiate complicated GameObjects or collections of GameObjects at run time

```
 public GameObject myPrefab;
 Instantiate(myPrefab, new Vector3(0, 0, 0), Quaternion.identity);
```
- Prefab variants are copies of a prefab that we can then pass a ScriptableObject to modify it slightly.

### SceneManagement
- Need `using UnityEngine.SceneManagement;`
- We can ` SceneManager.LoadScene`
- Can also specify the mode in which a scene loads
- Can hook into Scene Events and provided callbacks
```
SceneManager.sceneLoaded += CoreSceneLoaded;
    void CoreSceneLoaded(Scene scene, LoadSceneMode mode)
    {

        if (SceneManager.GetActiveScene().buildIndex == 1)
        {
            coreSceneLoaded.Invoke();
        }

    }
```
### Sprites/Textures
- Becareful when scaling images as the width of your image will not be the same as the texture size imported

### Input

#### Mouse
- We can get mousePosition by `Input.mousePosition`
- Can conver that to worldCoordinates with `Camera.main.ScreenToWorldPoint`
- Can check input for mouseClicks with `Input.GetMouseButtonDown(0)`
  

### Time 
- Time is a way to track the time taken regardless of frames executed
```
    // Update is called once per frame
    void Update()
    {
        UpdateTime();

        if (TimeToEnd())
            FindObjectOfType<LevelManager>().LoadNextLevel();
    }

    void UpdateTime()
    {
        totalTimeElapsed += Time.deltaTime;
        timerChanged.Invoke((int)(endGameTime - totalTimeElapsed));
    }

    bool TimeToEnd()
    {
        if (totalTimeElapsed >= endGameTime)
            return true;

        return false;
    }
```
### UI 
- Remember to use many Canvas to avoid unneccessary rerenders of UI elements. 
- To interact with TMPro `using TMPro;`
- Getting and setting text on TextMeshPro `).GetComponent<TextMeshProUGUI>().SetText();`

### Audio 



### Events
- Great way to avoid depedencies.
- When you can use a C# Event over UnityEvent, or just a ScriptableObject event wrapper
```
public class PlayerHealth : MonoBehaviour {

public static event Action<int> OnHealthChanged = delegate {}; 


  public static void ModHealth(int amount)
  {
    _health += amount;

    OnHealthChanged(_health);
  }
}

class Lifebar : MonoBehaviour {
[SerializeField] Slider slider;

void OnEnable() {
  	PlayerHealth.OnHealthChanged += UpdateLifebar;
	
}

void OnDisable() {

	PlayerHealth.OnHealthChanged -= UpdateLifebar;
}

  void UpdateLifebar(int currentHealth) {
    slider.value = currentHealth;
  }
}
```
- Pass abitrary amounts of data with `Event<Struct>`

### Coroutnes

Normal coroutine updates are run after the Update function returns. A coroutine is a function that can suspend its execution (yield) until the given YieldInstruction finishes. Different uses of Coroutines:

- yield The coroutine will continue after all Update functions have been called on the next frame.
- yield WaitForSeconds Continue after a specified time delay, after all Update functions have been called for the frame
- yield WaitForFixedUpdate Continue after all FixedUpdate has been called on all scripts
- yield WWW Continue after a WWW download has completed.
- yield StartCoroutine Chains the coroutine, and will wait for the MyFunc coroutine to complete first.

- Cache courotuines so you know when to stop them

```

IEnumerator _currentShootCoroutine;

private void BurstFire() {

  if(_currentShootCoroutine != null) {
    StopCoroutine(_currentShootCoroutine);
  }

_currentShootCoroutine = BurstFireRoutine();

StartCoroutine(_currentShootCoroutine);

IEnumerator BurstFireRoutine() {

  for(int i = 0; i < 3; i++) {
    Shoot();
    
    yield return new WaitForSeconds(timeBetweenShots);
    }
  }
}
```
#### Courutines Vs Async
- Use Async for IO Bound Events (Input, Network calls)
- Use courotines for routine-and-forget 
- Don't intertwine
  
```
public static class MethodDelayer
{

  public async static void DelayMethodByTimeAsync(Action action, float timeToDelay){
  float t = 0f;

      while (t < timeToDelay)
      {
          t += Time.unscaledDeltaTime;
          await Task.Yield();
      }
    
      action.Invoke();
    }
  }

void KissSomeoneYouCareAbout() {
  heart.Stop();
  MethodDelayer.DelayMethodByTimeAsync(heart.Start, 1.0f);
}

//You can even shortcut single executory
//lines into a callback with a weird-looking
//syntax

Time.deltaTime = .1f;

MethodDelayer.DelayMethodByTimeAsync(()=>Time.deltaTime = 1.0f, 3.0f);
```

### Open-Closed Principles 
- if you find one object doing the same operation a little bit differently on different types of objects and you have to implement that with conditionals, use interfaces instead
```
public interface IHittableByPlayer {
  void OnHit();
}

if(playerHitSomething) {
  Collider c = other.collider;


 IHittableByPlayer hittableComponent = c.GetComponent<IHittableByPlayer>();
	
  if(hittableComponent != null) {
    hittableComponent.OnHit();
  }
}
```

### Dependency Injection
- Try to obey Single responsibility principle and use a "God" class/monobehaviour to handle the create of objects using constructors so they don't need to be monoaware. 
- Use ScriptableObjects/Unity Editor as as Depedency Injection system

### Debugging
- Use `Debug.Log` to log general state
- Use `Debug.LogError` to throw errors when you know something shouldn't happen
- Use `DrawRay/Gismoz` to draw Scene level debugging.