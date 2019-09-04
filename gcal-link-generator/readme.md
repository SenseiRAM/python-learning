# Google Calendar Link Generator

Part of my job involves helping to plan events or otherwise point people to events happening around town. This little script helps quickly create Google Calendar template URLs for events that need them. I.e. when you click this link, it will open Google Calendar and prompt you to create an event with all the details filled in.

This is probably the most generalized script I've written, in that just about anyone should be able to use it, and it hasn't been built for a super specific use case.

I know there are plenty of places where the code could be simplified, but I'm pleased with how it turned out. Prior to this, I had to use [this tool][http://kalinka.tardate.com/], which works great, but it takes a loooooong time to use if you need to generate multiple links. Additionally, since the csv stores all the events I need to generate, it's easy to make changes to one or all of them, even after the fact, which can't be done using the tool linked above.

Notes: You'll need to change the code to reflect your own time zone so that times will properly be converted to UTC.
