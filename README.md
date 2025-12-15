# Note taking app

#### an mvp

## Main idea

Make summaries with protected data, from meetings.

To do that, this service uses an open model and stores everything locally.

## Implementation of phase 1 or the core of the app

There are multiple services, the flow is still under construction, but there is a main idea.

The app will have a bot that can enter a meeting via meeting link, and it will start recording the meeting audio after the meeting starts.

The audio recording will be transformed into a meeting transcript with timestamp, speaker, and text.

The meeting transcript will be uploaded to the summary service that will take the transcript and generate the summary based on the given prompt.

Once the summary was created, it will be delivered through mail, based on a given mailing list.

## Challenges in progress

- [x] Recording audio of a browser instance
- [x] Generating a decent summary using an open model
- [x] Handling meeting start
- [ ] Handling meeting ends
- [ ] Associating speaker with voice for transcript
- [ ] Adding the recording implementation for a linux server
- [ ] Project documentation (how to develop / deploy)

## Supported platforms for note taking

- [x] Microsoft Teams
