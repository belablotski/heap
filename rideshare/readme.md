# Problem:

Design and implement a system for a ride-sharing service that can efficiently match riders with available drivers.

## Considerations:

1. Efficiency: The system must be able to quickly match riders with nearby drivers, especially during peak hours.
2. Scalability: The system should be able to handle a large number of concurrent requests and a growing number of users and drivers.
3. Reliability: The system should be highly available and fault-tolerant to ensure continuous service for riders and drivers.
4. Accuracy: The matching algorithm should accurately estimate the expected travel time and cost for each ride.
5. User Experience: The system should provide a seamless and user-friendly experience for both riders and drivers.

## Possible Approaches:

1. Use a real-time database: A database like Redis or Firebase can efficiently store and update the locations of drivers and riders.
2. Implement a spatial indexing algorithm: Techniques like geohashing or k-d trees can be used to efficiently find drivers within a certain radius of a rider's location.
3. Consider using a distributed system architecture: This can improve scalability and fault tolerance.
4. Develop a robust matching algorithm: This algorithm should consider factors such as driver availability, rider preferences, and estimated travel time.

## Coding Challenges:

1. Implement a simplified version of the matching algorithm.
2. Design and implement a data structure to efficiently store and update driver locations.
3. Write unit tests to ensure the correctness and reliability of your code.
4. This problem provides a good opportunity to practice various coding skills, including:
  * Algorithm design and implementation
  * Data structures and algorithms
  * Object-oriented programming
  * System design
  * Testing and debugging

# Solution

## The Process

1. Understand the problem and establish the design scope
2. Propose a high-level design and get buy-in
3. Design deep dive into selected areas - make it interactive, work together
4. Wrap-up - you’ve delivered in full

### Scoping

**Understand the problem.**

> Develop a service to provide a driver for a rider based on their preferences and geo locations. Driver preferences: time window, min rate. Rider preferences: time windows, max rate.

**Collect functional requirements:**

> Let's assume we're dealing with one metropolian area with a population around 2M. 

1. What are the most important features?
   > Geo location of a driver and a rider.
2. How do people use them? Web app, mobile, APIs, etc.?
   > App and web. Focus on APIs.
3. Limits (max file size, number of requests, etc.)
   > 10 ride requests for rider per hour
4. How many users?
   > Up to 100k drivers and 500k riders
5. Daily active users
   > Up to 10k drivers and 50k riders
6. User signed on into the system
   > Up to 100k drivers and 500k riders

**Collect non-functional requirements:**
1. Reliability
   > 99.9%
2. Speed / throughput / bandwidth usage
   > 5k requests on average high
3. Scalability
   > The area servers should be able to elastically scale to 3x.
4. High availability
   > System should be HA
5. Disaster recovery
   > System should have a backup

**Back on the envelope estimations**
1. Assume how many objects one user operates on daily.
   > Average user sends 2-4 requests during the ride booking process
2. Assume how big they are on average.
   > 50k riders can generate 200k requests
3. Calculate the size of the system.
   > Rider: id (4 bytes), max rate (2 bytes), time window (4 bytes unix timestamp x 2), GPS coordinates (float x 2) = 22 bytes
   > Driver: id (4 bytes), min rate (2 bytes), time window (4 bytes unix timestamp x 2), GPS coordinates (float x 2) = 22 bytes
3. Read to write ratio.
   > Write - new rider and driver is entering into the system or their coordinates significantly changed and require an update. Read - search for a driver
4. Data vs metadata.
   > Data is location and preferences. Metadata is name, password, status, etc.
5. Calculate QPS
   > 50k riders / 24 = 2083 users hourly * 10 requests max = 20830 requests per hour / 3600 seconds = 5.8 requests per second (QPS)
6. Estimate peak QPS (typically 2-3x)
   > Peak QPS = 20 requests per second

**Establish design scope**

Clearly explain what we’re going to design.

The features we’re taking into account.

> We're designing a REST API web service to match riders and drivers in real-time based of their preferences and geo locations.

The system boundaries.

> One instance of the system will cover a metropolian area.

### High-level design

Propose the design and get a buy-in!

1. Propose a high-level design
   > One service instance covers one metropolian area. Users data are stored in NoSQL DB. Active drivers are loaded into the matching service memory for search.
2. Explain each component
   > NoSQL DB stores users data and metadata. The DB has 4 instances in 2 different DCs (based on 600k users).

   > The Driver Seach Service (DSS) runs in K8s cluster. All drivers will take 10k drivers x 22 bytes = 220K bytes memory and with 20 peak QPS we can service them from one node. We'll also need one node in stand-by mode in a different DC. Also DSS has async garbage collector that removes drivers whos time windows are in the past. The new drivers will be loaded into DSS from the DB when their time window start becomes in 24h from now (assuming that riders are booking their rides no more than 24h in advance).

   > API end-point to search (sync HTTP REST API): retrieves data about the best suitable driver (if any) to handle the ride. The controller calls DSS. All calls are synchronous.

   > API end-point to update coordinates (sync HTTP REST API): updates data in DSS and DB.

   > API end-point to update preferences (sync HTTP REST API): updates data in DSS and DB. Also it covers the use-case of out-of-service drivers.

   > API end-points to CRUD on metadata (sync HTTP REST API): updates metadata in DB.

   > DSS and API controller service will be in one K8s cluster to avoid cross-region traffic.
3. Say that we’ll deep dive into selected or most critical parts
4. Get buy-in

Keep in mind:

1. Identify the key elements: web-server (APIs), DB (metadata), storage (data).
   1. Decouple all them.
   2. Caching
2. Business logic
   1. Different “flows” to support different scenarios.
   2. Consistency model
   3. Race conditions - multiple users try to do the same thing at the same time.
3. Failure handling (negative logic)
4. Security
   1. Authentication/authorization
5. Logging, metrics, alerting.
   1. Change history. Audit.
6. HA/DR
   1. Data replication. Some region or cross region.
   2. Load balancer to scale API
   3. Replicate and shard a DB (for DR and scalability)
7. Garbage collection
   1. Old versions of objects, orphan objects, etc.
   2. Archive in cold storage.

### Deep dive
Explain the key blocks of the system in detail.

### Wrap-up
Explain what we’ve just done.
We’ve designed the system that covers requirements we’ve agreed upon at the very beginning.
We’ve done a deep dive into X, Y and Z components, those support the critical flows A and B.
There is no silver bullet in the design world. We designed to fix the constraints. WIth different constraints/assumptions it would be a different architecture.
The trade-offs we made..
Other possible design choices.
How to extend the system further to cover more real-world type of scenarios.
