# Building For Scale

## Mitigation Strategies

### Graceful Degradation in Web
- The ability for a website to respond accordingly to less-performant devices. If a user interacts with a device with worse performance, latency, or older software - the web server should attempt to handle that and make the site useable.

### Throttling

- Throttling prevents excessive requests. Throttles indicate a temporary state, and are used to control the rate of requests that clients can make to an API.
  - DRF has throttling policies that can be applied globally, at a class/function level.

### Backpressure
- Simply its when your input is coming in at a faster rate than you can output. 
- There are typically three ways to handle backpressure
  - Control the producer (slow down/speed up is decided by consumer)
  - Buffer (accumulate incoming data spikes temporarily)
  - Drop (sample a percentage of the incoming data)

### Loadshifting

- Loadshifting is about taking non-priority tasks and sending them to non-peak hours

### Circuit Breaker

- Strategy to handle when a service depends on another and eventually stops requesting from that service when too many failures occur.

## Horizontal Vs Vertical Scaling

- Vertical scaling is scaling up the resources on individual pieces of hardware. Some types of software require this.
- Horizontal Scaling is providing new pieces of hardware to service requests. Typically the preferred instance to scaling apps.

## Building with Obversability in Mind

- Three Pillars of Observability = Logs, metrics, and Traces

### Instrumentation - Traces
- Measures the performance of a component. 
  - Typically seen as traces of execution of code to see where the problem areas are.

## Monitoring
- Monitoring allows us to look at overall health of the infastructure and major errors/failures.

## Telemetry
- Allows us to see specifics metrics of the app.