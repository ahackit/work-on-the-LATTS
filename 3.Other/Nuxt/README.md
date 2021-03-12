# LATT-Nuxt

Learn All The Things - Nuxt

## Why Nuxt?

### Server Side Rendering

SPAs suck at SEO and Meta Tags. No content or index to parse before JS runs.Some crawlers don't even support JS.

Above is solved by Nuxt using Server Side Rendering (SSR). Also is more performant.

### Pre Rendering

Can get even more SSR bonuses by pre rendering into HTML files. Those can then be statically served, for usualy free.

### Code Splitting

If I got tons of components, the only thing the user should have to load is the ones they are using.

## How to install Nuxt?

Just use npx create-nuxt-app and pick all your options silly.

## So many folders - what they do?

Most if not all can be deleted if they aren't used.

### Assets

Store your fonts, SASS files, images here.

### Components

Place your vue.js components here

### Layout

A directory to store all your different layouts for your project.
Layouts operate like top level app.vue if you are making a normal Vue project
Styling will cascade down from here

### Middlewares

Code that can be run between the rendering of a single page or group of pages

### Pages

This is going to have all your individual pages and routes. Nuxt going to read all the pages in here and create vue router for you.

Can build dynamic routes with the \_ prefix. Ex: Create new folder called Posts with \_id.vue

### Plugins

Store your global stuff here, other plugins, constants, functions, componenents, etc.

### Static

Can place static assets here that will be available at the domain/static_asset_name

### Store

Vuex Store

## Nuxt Config File

### Global CSS

Sometimes it be that you need multiple layouts, do yourself a favor and make a css file that you configure to be global in nuxt config. ~/assests/mycss.css

## SEO Basics

Can set all the SEO needs through the head function in a component. Meta tags/Title/etc.

## Async Data

Async data can be fetched just like normal through a mounted component. However, if you have header information that is required by this async data, it will not be available.

Nuxt comes with asyncData property that allows you to fetch data before the component is rendered to allow for SSR capabilities.

Can also use context parameter in asyncData method to access router parameters n such

Also just use the nuxt Axios module \$axios.

If we want async data with Vuex we need to use the Fetch Method with a computed property instead of asyncData

### Axios Module

Can configure axios configuration in nuxt.config - axios. Can set baseURL. Can set Global Auth through plugins. Check documentation for details

## SSG - Static Site Generation

If you just have static routes, just run nuxt generate and you are good

If you have dynamic routes, there is a couple of ways to pre-render. You can specify routes option in generate in nuxt.config

If typing out routes isn't possible, you can use either a function to generate the routes or an API call against a API endpoint that has all the IDs for the resources you need

To cache data to avoid many API calls, you can store the fetched data and pass it as a object then access through asyncFetch context {route: // payload: post}

Generate just got changed -- so learn how to use nuxt build/export
