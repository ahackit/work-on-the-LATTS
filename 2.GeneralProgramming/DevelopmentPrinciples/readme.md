# Development Principles

These are principles that should transfer to any area of programming and are typically good foundations to build off of.

## DRY
- Don't Repeat Yourself 
  - Any time you repeat yourself, there is probably room for an abstraction or a more efficient way of resolving a problem
  - Repeated codes mean if logic breaks, it breaks in multiple places.
  - Use Best Judgement

## YAGNI
- You aren't gonna need it. 
  - Don't try to pre-optomize code.
  - Don't put in solutions that we don't need yet.
  - Build out your MVP Functionality
  - Or Build closely to the requirements of your card.
  - Use your best judgement.

## KISS
- Keep It Simple Stupid
  - Don't be cute. Get the job the done. Implement the simplest solution and then go back to optomize if needed.

## SOLID

### Single Responsibility Principle
- A Class or Function should only be responsible for a single unit of work/domain knowledge.

### Open/Closed Principle
- open–closed principle states "software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification" that is, such an entity can allow its behaviour to be extended without modifying its source code
  - This just means use OOP to your advantage. Make reuasble classes/objects that can be extended(inherited, composed from, etc)
  - Code shouldn't modify the internal object or definition.

### Liskov Substitution Principle
- An overridden method of a subclass needs to accept the same input parameter values as the method of the superclass. That means you can implement less restrictive validation rules, but you are not allowed to enforce stricter ones in your subclass.
- The return value of a method of the subclass needs to comply with the same rules as the return value of the method of the superclass. You can only decide to apply even stricter rules by returning a specific subclass of the defined return value, or by returning a subset of the valid return values of the superclass.

### Interface Segregation Principle
- Don't bloat existing interfaces or classes, if a subclass doesn't require a parent method, there is a nother abstraction level lower required.
- Typically create new interfaces based on the parent interface. Subclasses use new interfaces

### Dependency Inversion
- High-level modules should not depend on low-level modules. Both should depend on abstractions.
- Abstractions should not depend on details. Details should depend on abstractions.

## Domain Driven Design
- Domain-driven design (DDD) is the concept that the structure and language of software code (class names, class methods, class variables) should match the business domain. For example, if a software processes loan applications, it might have classes such as LoanApplication and Customer, and methods such as AcceptOffer and Withdraw.

## Test Driven Development
- Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: requirements are turned into very specific test cases, then the code is improved so that the tests pass. This is opposed to software development that allows code to be added that is not proven to meet requirements.
- Write Test - Write Code to make Test Pass - Repeat
- Knowing the ending output is hard, difficult skill