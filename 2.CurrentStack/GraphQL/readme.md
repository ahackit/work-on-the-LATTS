# GraphQL
GraphQL is a specification for an API query language and a server engine capable of executing such queries

## Queries
- GraphQL has queries with Fields
```
query {
    me {
        name
    }
}
```
- Client sends the above query to a GraphQL server -- usually as a string. 
- A successful GraphQL response always has a data key, under which is found the response the client is looking for.
- Queries can get more complex
```
query {
    me {
        name
            friends(first: 2) {
                name
                age
        }
    }
}
```

## Type System
- Type system of GraphQL typically referred to Schema
```
type Shop {
    name: String!
    # Where the shop is located, null if online only.
    location: Location
    products: [Product!]!
}
type Location {
    address: String
}
type Product {
    name: String!
    price: Price!
}
```
- The most basic and crucial primitive of a GraphQL schema is the Object Type. Object types describe one concept in your GraphQL API
- fieldName: Type
```
query {
    # 1. The shop field returns a `Shop` type.
    shop(id: 1) {
        # 2. field location on the `Shop` type
        # Returns a `Location` type.
        location {
            # 3. field address exists on the `Location` type
            # Returns a String.
            address
        }
    }
}
```
### Schema Roots
- A GraphQL schema must always define a Query Root,a type that defines the entry point to possibilities. Usually, we call that typeQuery:
```
type Query {
    shop(id: ID): Shop!
}
```
- A query root has to be defined on a GraphQL schema, but two other types of roots that can be defined: the Mutation, and the Subscription roots.

### Arguments
- Just like a function, a GraphQL field can define arguments that a GraphQL server can use to affect the runtime resolution of the field. These fields are defined between parentheses after the field name, and you can have as many of them as you like:
```
type Query {
shop(owner: String!, name: String!, location: Location): Shop!
}
```
- Can also have InputTypes
```
input PriceFormat {
    displayCents: Boolean!
    currency: String!
}
```

### Variables
- allows clients to send variables along with a query and have the GraphQL server execute it, instead of including it directly in the query string itself:
```
query FetchProduct($id: ID!, $format: PriceFormat!) {
    product(id: $id) {
        price(format: $format) {
        name
        }
    }
}
```
- Would send query like so
```
{
"id": "abc",
    "format": {
    "displayCents": true,
    "currency": "USD"
    }
}
```

### Aliases
- Can specify aliases on return data
```
query {
    abcProduct: product (id: "abc") {
        name
        price
    }
}
```
- Data comes back as so
```
query {
    abcProduct: product (id: "abc") {
        name
        price
    }
}
```

### Mutations
- how we can perform changes to data
```
mutation {
    addProduct(name: String!, price: Price!) {
        product {
            id
        }
}
}
```
```
type Mutation {
addProduct(name: String!, price: Price!): AddProductPayload
}
type AddProductPayload {
    product: Product!
}
```
- Almost the same as query fields but
  - Top-level fields under the mutation root are allowed to have side effects /make modifications.
  - Top-level mutation fields must be executed serially by the server, whileother fields could be executed in parallel.

### Enums
- Can define enums
```
type Shop {
    # The type of products the shop specializes in
    type: ShopType!
}
enum ShopType {
    APPAREL
    FOOD
    ELECTRONICS
}
```

### Abstract Types
- Can decide to return specific types based on interface or concrete type
```
interface Discountable {
    priceWithDiscounts: Price!
    priceWithoutDiscounts: Price!
}
type Product implements Discountable {
    name: String!
    priceWithDiscounts: Price!
    priceWithoutDiscounts: Price!
}
type GiftCard implements Discountable {
    code: String!
    priceWithDiscounts: Price!
    priceWithoutDiscounts: Price!
}

type Cart {
    discountedItems: [Discountable!]!
}
```
- If a client wants to query the other fields, it must specify which concrete type they want to be selecting against.
```
query {
    cart {
    discountedItems {
        priceWithDiscounts
        priceWithoutDiscounts
        ... on Product {
        name
        }
        ... on GiftCard {
        code
        }
        }
    }
}
```

- Can also use unions to resolve separate concrete types
```
union CartItem = Product | GiftCard
    type Cart {
        items: [CartItem]
}
query {
    cart {
    discountedItems {
        ... on Product {
        name
        }
        ... on GiftCard {
        code
        }
        }
    }
}
```

### Fragments
- Fragments allow clients to define parts of a query to be reused elsewhere:
```
query {
    products(first: 100) {
        ...ProductFragment
    }
}
fragment ProductFragment on Product {
    name
    price
    variants
}
```

### Directives
-  Directives are a kind of annotation that we can use on various GraphQL primitives. The GraphQL specification defines two builtin directives that are really useful: @skip and @include.
```
query MyQuery($shouldInclude: Boolean) {
    myField @include(if: $shouldInclude)
}
```
- In this example, the @include directive makes sure the myField field is only queried when the variable shouldInclude is true. 
- Can also include custom directives
```
"""
Marks an element of a GraphQL schema as
only available with a feature flag activated
"""
directive @myDirective(
    """
    The identifier of the feature flag that toggles this field.
    """
    flag: String
) on FIELD

query {
    user(id: "1") @myDirective {
        name
    }
}
```

## GraphQL Schema Design
- The best way to create a schema that will delight our users is to start thinking of the design very early in the journey.
- GraphQL is a client-centric API. This philosophy affects how we should design our GraphQL APIs too While it’s tempting to be designing APIs in terms of backend resources or entities, it’s very important to design GraphQL APIs with client use cases in mind first, before anything else.
- GraphQL schema is an entry point to functionality and you should avoid tying it to any implementation detail on the backend
- Use the schema to build a self-documenting API

## List & Pagination
- , pagination is almost always an essential component of a good API. Because you gonna allow retrieval lsits of some point
- Use offset pagination - doesn't scale well on large elements
```
type Query {
    products(limit: Int!, page: Int!): [Product!]!
}
```
- Use cursor pagination to keep track
```
type Query {
    products(limit: Int!, after: String): [Product!]!
}
```

## Global Identification
- Use global ID for any retrieval in the graph

```
interface Node {
    id: ID!
}
type User implements Node {
    id: ID!
    name: String!
}
```