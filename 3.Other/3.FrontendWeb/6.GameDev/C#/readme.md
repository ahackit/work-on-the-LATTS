# C#

- [C](#c)
  - [Strucutre](#strucutre)
  - [Data Types](#data-types)
  - [Type Conversion](#type-conversion)
  - [Variables](#variables)
  - [Conditionals](#conditionals)
    - [Switch](#switch)
    - [Ternary Operations](#ternary-operations)
  - [Loops](#loops)
  - [Encapsulation](#encapsulation)
  - [Functions](#functions)
  - [Arrays](#arrays)
  - [Structs](#structs)
  - [Enums](#enums)
  - [Classes](#classes)
    - [Inheritance](#inheritance)
    - [Polymorphism/Abstract Classes](#polymorphismabstract-classes)
  - [Interfaces](#interfaces)
  - [Namespaces](#namespaces)
  - [Preprocessor Directives](#preprocessor-directives)
  - [Attributes](#attributes)
  - [Reflections](#reflections)
  - [Properties](#properties)
  - [Delegates](#delegates)
    - [Instantiating Delegate](#instantiating-delegate)
    - [MultiCasting Delegate](#multicasting-delegate)
  - [Events](#events)
  - [Collections](#collections)

## Strucutre

```
using System;

namespace RectangleApplication {
   class Rectangle {

      // member variables
      double length;
      double width;

      public void Acceptdetails() {
         length = 4.5;
         width = 3.5;
      }
      public double GetArea() {
         return length * width;
      }
      public void Display() {
         Console.WriteLine("Length: {0}", length);
         Console.WriteLine("Width: {0}", width);
         Console.WriteLine("Area: {0}", GetArea());
      }
   }
   class ExecuteRectangle {
      static void Main(string[] args) {
         Rectangle r = new Rectangle();
         r.Acceptdetails();
         r.Display();
         Console.ReadLine();
      }
   }
}
```

## Data Types

- bool Boolean value True or False False
- byte 8-bit unsigned integer 0 to 255 0
- char 16-bit Unicode character U +0000 to U +ffff '\0'
- decimal 128-bit precise decimal values with 28-29 significant digits (-7.9 x 1028 to 7.9 x 1028) / 100 to 28 0.0M
- double 64-bit double-precision floating point type (+/-)5.0 x 10-324 to (+/-)1.7 x 10308 0.0D
- float 32-bit single-precision floating point type -3.4 x 1038 to + 3.4 x 1038 0.0F
- int 32-bit signed integer type -2,147,483,648 to 2,147,483,647 0
- long 64-bit signed integer type -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 0L
- sbyte 8-bit signed integer type -128 to 127 0
- short 16-bit signed integer type -32,768 to 32,767 0
- uint 32-bit unsigned integer type 0 to 4,294,967,295 0
- ulong 64-bit unsigned integer type 0 to 18,446,744,073,709,551,615 0
- ushort 16-bit unsigned integer type 0 to 65,535 0

## Type Conversion

- toDataType

## Variables

- `<data_type> <variable_name> = value;`

## Conditionals

```
using System;

namespace DecisionMaking {
   class Program {
      static void Main(string[] args) {
         /* local variable definition */
         int a = 100;

         /* check the boolean condition */
         if (a < 20) {
            /* if condition is true then print the following */
            Console.WriteLine("a is less than 20");
         } else {
            /* if condition is false then print the following */
            Console.WriteLine("a is not less than 20");
         }
         Console.WriteLine("value of a is : {0}", a);
         Console.ReadLine();
      }
   }
}
```

### Switch

```
switch(expression) {
   case constant-expression1  :
      statement(s);
      break;
   case constant-expression2  :
   case constant-expression3  :
      statement(s);
      break;

   /* you can have any number of case statements */
   default : /* Optional */
   statement(s);
}
```

### Ternary Operations

- Exp1 ? Exp2 : Exp3;

## Loops

```
while(condition) {
   statement(s);
}
```

```
for ( init; condition; increment ) {
   statement(s);
}
```

- break/continue

## Encapsulation

- Public
- Private
- Protected
- Internal
- Protected internal

## Functions

```
<Access Specifier> <Return Type> <Method Name>(Parameter List) {
   Method Body
}
```

```
class NumberManipulator {

   public int FindMax(int num1, int num2) {
      /* local variable declaration */
      int result;

      if (num1 > num2)
         result = num1;
      else
         result = num2;

      return result;
   }
   ...
}
```

- passing refs

```
      public void swap(ref int x, ref int y) {
         int temp;

         temp = x; /* save the value of x */
         x = y;    /* put y into x */
         y = temp; /* put temp into y */
      }
```

## Arrays

```
int [] marks = new int[]  { 99,  98, 92, 97, 95};
int[] score = marks;
```

```
         foreach (int j in n ) {
            int i = j-100;
            Console.WriteLine("Element[{0}] = {1}", i, j);
         }
```

## Structs

```
struct Books {
   public string title;
   public string author;
   public string subject;
   public int book_id;
};

 Books Book1;
      /* book 1 specification */
      Book1.title = "C Programming";
      Book1.author = "Nuha Ali";
      Book1.subject = "C Programming Tutorial";
      Book1.book_id = 6495407;
```

## Enums

```
using System;

namespace EnumApplication {
   class EnumProgram {
      enum Days { Sun, Mon, tue, Wed, thu, Fri, Sat };

      static void Main(string[] args) {
         int WeekdayStart = (int)Days.Mon;
         int WeekdayEnd = (int)Days.Fri;

         Console.WriteLine("Monday: {0}", WeekdayStart);
         Console.WriteLine("Friday: {0}", WeekdayEnd);
         Console.ReadKey();
      }
   }
}
```

## Classes

```

using System;

namespace LineApplication {
   class Line {
      private double length;   // Length of a line
      public static int num;

      public Line() {   // constructor
         Console.WriteLine("Object is being created");
      }
      ~Line() {   //destructor
         Console.WriteLine("Object is being deleted");
      }
      public void setLength( double len ) {
         length = len;
      }
      public double getLength() {
         return length;
      }
      static void Main(string[] args) {
         Line line = new Line();

         // set line length
         line.setLength(6.0);
         Console.WriteLine("Length of line : {0}", line.getLength());
      }
   }
}
```

### Inheritance

```
   class Shape {
      public void setWidth(int w) {
         width = w;
      }
      public void setHeight(int h) {
         height = h;
      }
      protected int width;
      protected int height;
   }

   // Base class PaintCost
   public interface PaintCost {
      int getCost(int area);
   }

   // Derived class
   class Rectangle : Shape, PaintCost {
      public int getArea() {
         return (width * height);
      }
      public int getCost(int area) {
         return area * 70;
      }
   }
```

### Polymorphism/Abstract Classes

```
using System;

namespace PolymorphismApplication {
   class Shape {
      protected int width, height;

      public Shape( int a = 0, int b = 0) {
         width = a;
         height = b;
      }
      public virtual int area() {
         Console.WriteLine("Parent class area :");
         return 0;
      }
   }
   class Rectangle: Shape {
      public Rectangle( int a = 0, int b = 0): base(a, b) {

      }
      public override int area () {
         Console.WriteLine("Rectangle class area :");
         return (width * height);
      }
   }
   class Triangle: Shape {
      public Triangle(int a = 0, int b = 0): base(a, b) {
      }
      public override int area() {
         Console.WriteLine("Triangle class area :");
         return (width * height / 2);
      }
   }
   class Caller {
      public void CallArea(Shape sh) {
         int a;
         a = sh.area();
         Console.WriteLine("Area: {0}", a);
      }
   }
   class Tester {
      static void Main(string[] args) {
         Caller c = new Caller();
         Rectangle r = new Rectangle(10, 7);
         Triangle t = new Triangle(10, 5);

         c.CallArea(r);
         c.CallArea(t);
         Console.ReadKey();
      }
   }
}
```

## Interfaces

```
   public interface ITransactions {
      // interface members
      void showTransaction();
      double getAmount();
   }
   public class Transaction : ITransactions {
      private string tCode;
      private string date;
      private double amount;

      public Transaction() {
         tCode = " ";
         date = " ";
         amount = 0.0;
      }
      public Transaction(string c, string d, double a) {
         tCode = c;
         date = d;
         amount = a;
      }
      public double getAmount() {
         return amount;
      }
      public void showTransaction() {
         Console.WriteLine("Transaction: {0}", tCode);
         Console.WriteLine("Date: {0}", date);
         Console.WriteLine("Amount: {0}", getAmount());
      }
   }
```

## Namespaces

- namespace is designed for providing a way to keep one set of names separate from another.

```
using System;

namespace first_space {
   class namespace_cl {
      public void func() {
         Console.WriteLine("Inside first_space");
      }
   }
}
namespace second_space {
   class namespace_cl {
      public void func() {
         Console.WriteLine("Inside second_space");
      }
   }
}
class TestClass {
   static void Main(string[] args) {
      first_space.namespace_cl fc = new first_space.namespace_cl();
      second_space.namespace_cl sc = new second_space.namespace_cl();
      fc.func();
      sc.func();
      Console.ReadKey();
   }
}
```

## Preprocessor Directives

- #define:It defines a sequence of characters, called symbol.
- #undef:It allows you to undefine a symbol.
- #if:It allows testing a symbol or symbols to see if they evaluate to true.
- #else:It allows to create a compound conditional directive, along with #if.
- #elif:It allows creating a compound conditional directive.
- #endif:Specifies the end of a conditional directive.
- #line:It lets you modify the compiler's line number and (optionally) the file name output for errors and warnings.
- #error:It allows generating an error from a specific location in your code.
- #warning:It allows generating a level one warning from a specific location in your code.
- #region: It lets you specify a block of code that you can expand or collapse when using the outlining feature of the Visual Studio Code Editor.
- #endregion: It marks the end of a #region block.

```
#define PI
using System;

namespace PreprocessorDAppl {
   class Program {
      static void Main(string[] args) {
         #if (PI)
            Console.WriteLine("PI is defined");
         #else
            Console.WriteLine("PI is not defined");
         #endif
         Console.ReadKey();
      }
   }
}
```

```
#define DEBUG
#define VC_V10
using System;

public class TestClass {
   public static void Main() {
      #if (DEBUG && !VC_V10)
         Console.WriteLine("DEBUG is defined");
      #elif (!DEBUG && VC_V10)
         Console.WriteLine("VC_V10 is defined");
      #elif (DEBUG && VC_V10)
         Console.WriteLine("DEBUG and VC_V10 are defined");
      #else
         Console.WriteLine("DEBUG and VC_V10 are not defined");
      #endif
      Console.ReadKey();
   }
}
```

## Attributes

```
#define DEBUG
using System;
using System.Diagnostics;

public class Myclass {
   [Conditional("DEBUG")]

   public static void Message(string msg) {
      Console.WriteLine(msg);
   }
}
class Test {
   static void function1() {
      Myclass.Message("In Function 1.");
      function2();
   }
   static void function2() {
      Myclass.Message("In Function 2.");
   }
   public static void Main() {
      Myclass.Message("In Main function.");
      function1();
      Console.ReadKey();
   }
}
```

## Reflections

- Reflection objects are used for obtaining type information at runtime. The classes that give access to the metadata of a running program are in the System.Reflection namespace.

## Properties

```
   class Student {
      private string code = "N.A";
      private string name = "not known";
      private int age = 0;

      // Declare a Code property of type string:
      public string Code {
         get {
            return code;
         }
         set {
            code = value;
         }
      }
      }
```

- abstract properties

```
   public abstract class Person {
      public abstract string Name {
         get;
         set;
      }
      public abstract int Age {
         get;
         set;
      }
   }
```

## Delegates

- A delegate is a reference type variable that holds the reference to a method. The reference can be changed at runtime.
- Delegates are especially used for implementing events and the call-back methods. All delegates are implicitly derived from the System.Delegate class

```
public delegate int MyDelegate (string s);
```

### Instantiating Delegate

```
public delegate void printString(string s);
...
printString ps1 = new printString(WriteToScreen);
printString ps2 = new printString(WriteToFile);
```

### MultiCasting Delegate

```
         NumberChanger nc;
         NumberChanger nc1 = new NumberChanger(AddNum);
         NumberChanger nc2 = new NumberChanger(MultNum);

         nc = nc1;
         nc += nc2;
```

## Events

- Events are user actions such as key press, clicks, mouse movements, etc., or some occurrence such as system generated notifications.
- Applications need to respond to events when they occur.
- The class containing the event is used to publish the event. This is called the publisher class. '
- Some other class that accepts this event is called the subscriber class. Events use the publisher-subscriber model

```
using System;

namespace SampleApp {
   public delegate string MyDel(string str);

   class EventProgram {
      event MyDel MyEvent;

      public EventProgram() {
         this.MyEvent += new MyDel(this.WelcomeUser);
      }
      public string WelcomeUser(string username) {
         return "Welcome " + username;
      }
      static void Main(string[] args) {
         EventProgram obj1 = new EventProgram();
         string result = obj1.MyEvent("Tutorials Point");
         Console.WriteLine(result);
      }
   }
}
```

## Collections

- The following are the various commonly used classes of the System.Collection namespace.
- ArrayList: It represents ordered collection of an object that can be indexed individually. It is basically an alternative to an array. However, unlike array you can add and remove items from a list at a specified position using an index and the array resizes itself automatically. It also allows dynamic memory allocation, adding, searching and sorting items in the list.
- Hashtable: It uses a key to access the elements in the collection. A hash table is used when you need to access elements by using key, and you can identify a useful key value. Each item in the hash table has a key/value pair. The key is used to access the items in the collection.
- SortedList: It uses a key as well as an index to access the items in a list. A sorted list is a combination of an array and a hash table. It contains a list of items that can be accessed using a key or an index. If you access items using an index, it is an ArrayList, and if you access items using a key , it is a Hashtable. The collection of items is always sorted by the key value.
- Stack:It represents a last-in, first out collection of object. It is used when you need a last-in, first-out access of items. When you add an item in the list, it is called pushing the item and when you remove it, it is called popping the item.
- Queue:It represents a first-in, first out collection of object. It is used when you need a first-in, first-out access of items. When you add an item in the list, it is called enqueue and when you remove an item, it is called deque.
- BitArray: It represents an array of the binary representation using the values 1 and 0. It is used when you need to store the bits but do not know the number of bits in advance. You can access items from the BitArray collection by using an integer index, which starts from zero.
- Dictionary:

```
// Create a new dictionary of strings, with string keys.
//
Dictionary<string, string> openWith =
    new Dictionary<string, string>();

// Add some elements to the dictionary. There are no
// duplicate keys, but some of the values are duplicates.
openWith.Add("txt", "notepad.exe");
openWith.Add("bmp", "paint.exe");
openWith.Add("dib", "paint.exe");
openWith.Add("rtf", "wordpad.exe");
```

- Lists:

```
        // Create a list of parts.
        List<Part> parts = new List<Part>();

        // Add parts to the list.
        parts.Add(new Part() {PartName="crank arm", PartId=1234});
        parts.Add(new Part() { PartName = "chain ring", PartId = 1334 });
        parts.Add(new Part() { PartName = "regular seat", PartId = 1434 });
        parts.Add(new Part() { PartName = "banana seat", PartId = 1444 });
        parts.Add(new Part() { PartName = "cassette", PartId = 1534 });
        parts.Add(new Part() { PartName = "shift lever", PartId = 1634 });

        // Write out the parts in the list. This will call the overridden ToString method
        // in the Part class.
        Console.WriteLine();
        foreach (Part aPart in parts)
        {
            Console.WriteLine(aPart);
        }
```
