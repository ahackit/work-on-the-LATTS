# TypeScript

## Can also add types through JSDoc
- way to annotate our code using comments
```
/**
 * Adding two numbers. This annotation tells
TypeScript
 * which types to expect. Two parameters (params) of
 * type number and a return type of number
 *
 * @param {number} numberOne
 * @param {number} numberTwo
 * @returns {number}
 */

function addNumbers(numberOne, numberTwo) {
 return numberOne + numberTwo
}
```

## TypeScript tooling
`npm install -g typescript`
- This is typescript compiler to run against `.tsc` files
- use `tsc --init` to get a default `tsconfig.json` file
```
{
 "compilerOptions": {
 "target": "ES2020",
 "module": "es2020",
 "allowJs": true,
 "checkJs": true,
 "typeRoots": [
 "@types",
 "node_modules/@types"
 ],
 "esModuleInterop": true,
 }
}
```
- `tsc --watch`

## Types
- string
- number
- boolean
- any
- unknown


## Typing Functions
```
function addVAT(price: number, vat: number = 0.2):
 number {
 return price * (1 + vat)
}
```

## Control Flow in TypeScript
```
function selectDeliveryAddresses(addressOrIndex:unknown): string {
 if(typeof addressOrIndex === 'number' &&
 addressOrIndex < deliveryAddresses.length) {
 return deliveryAddresses[addressOrIndex]
 } else if(typeof addressOrIndex === 'string') {
 return addressOrIndex
 }
 return ''
}
```


## Defining Shapes in Composite Types
- How we define complex types
- Can't define more/less properties than exists in the structure
  - You can bypass that by defining the object first and assigning later.
```
type Article = {
 title: string,
 price: number,
 vat: number,
 stock: number,
 description: string
}

const movie: Article = {
 title: 'Helvetica',
 price: 6.66,
 vat: 0.19,
 stock: 1000,
 description: '90 minutes of gushing about Helvetica'
}
```

### Use TypeOf for quick type creation
`type Order = typeof defaultOrder`

### Use Optional Types
` stock?: number,`
