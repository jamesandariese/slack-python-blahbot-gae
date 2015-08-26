# Slackbot Python GAE

A slack outgoing webhook written in Python and running on GAE.

This sample only responds with "blah".  It also avoids responding
to other webhooks (but probably not bot users so be careful).

## Setup in Slack

Add this to Slack by adding a new outgoing webhook and setting the
URL to the URL of your app in appspot.

    https://alpine-treasure.appspot.com/

That's it!  If you want it to respond to all messages, assign it
to a channel.  If you want it to respond on all channels when
someone writes "bats ahoy", add that as the trigger text and set
the channel to "Any".

## Further direction

This can be made into something that bridges between Slack and
something else by adding new endpoints to change persisted state.
Use `@app.route` for this.  For example, it could remember the
last 5 messages in a channel and expose a GET route to look that
data up.


