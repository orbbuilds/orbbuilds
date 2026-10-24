# Design doc: Orb Builds nightly publish flow

## Problem
One new YouTube episode must go public every day, right after the daily upload quota resets, without a person awake.

## Plan
1. 9:28 PM: the production job picks the freshest AI release, writes the script, renders the video and thumbnail, and writes a queue file whose status is READY.
2. 1:28 AM: the publish job lists every queue file marked READY or CARRIED and ranks them freshest first.
3. It uploads #1 as public, then sets the thumbnail, posts a vote comment, and adds the video to the playlist.
4. If quota remains, it uploads the vertical Short for #1.
5. Any READY file that was not uploaded becomes CARRIED to the next night. After 3 nights it becomes STALE.
6. Every step writes a line to a run log, so a crash shows the last step reached.

## Out of scope
Posting to X or Bluesky (a daytime job does that).
