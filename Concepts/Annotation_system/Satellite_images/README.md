### Concept:
Automatically annotate satellite images based on already recorded positional data of objects. Works outside of given dataset on satellites.

### Implementation:
1. (Satellite) Take an image and requests all positions of each label that is in the satellites training set given the timestamp the image was taken.
    * Timestamp: ex: 2018-09-01 09:01:15:987_654_321
    * Position: object position at that timestamp in UTM coordinates
    * Label: Label of object in string format for annotating
2. (Server) Fetches requested annotations and sends
3. (Satellite) Receives annotations of type (label: UTM coordinates)
4. (Satellite) Translates the received coordinates of that object to pixel coordinates of the satellite image.
5. (Satellite) Annotates image 

Objects like planes or boats that could be seen by satellites and are already being tracked.

and annotate the image taken at that time by translating the received coordinates of that object to pixel coordinates of the satellite image. This would result in an annotated image that could be used to further train the image classification network. Similarly as discussed in Concept 2 this system could also be a part of a swarm-learning or federated-learning network. Thus this system would require minimal bandwidth to operate, only requesting annotations which hold coordinates of an object at a given time and sending/receiving the network for aggregation of all neural networks in the given system.

This was the concept we started working on. It required an understanding of how our satellite data looked to understand if translating world coordinates to pixel coordinates of the satellite image was possible. It also required an understanding of what objects, if any, were positionally tracked. After a discussion we came to the conclusion that translating world coordinates to pixel coordinates of the satellite image was possible and that there was sufficient data of tracked objects to make this concept into reality.

However, actually implementing this system was difficult both given the time restraint and the resources that were available. So we settled for simulating the system using python classes representing satellites and the data center to gain a full grasp of the system and be sure that we did not miss anything. The code can be found here.

### Results:
To be implemented and tested.