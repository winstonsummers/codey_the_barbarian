### Codey the Barbarian

<em>A simple bot born in low valleys of the paciffic northwest, he conquers his foes with literary prowess!</em>

Codey is a python bot designed to emulate the writing of Robert E. Howard. The cool thing about how this, and similar, bots work is that you can change the style it writes in by changing the text you give it. I believe Conan was a good choice because there are seventeen open domain short stories that I could use.

This code is fairly simple and I have left in comments for the parts that aren't very human readable for clarity. Hopefully others can use this for thier education as I made it for mine.

Below I have my goals as I have reached them so far; aswell as my primary resources for understanding and starting. I highly recommend the Youtube video for a base model and that you build from there. The host of the video explains the concept at a high level so you can understand what is going on as you follow along and with a little more reading have a strong grasp of the concepts at hand.

Further more, I hope you enjoy Codey the Barbarian as much as I have!


## Commands

	"python3 learn.py dictionary.json Conan.txt"
		This tells Codey to learn from Conan.txt and put it into dictionary.json. If it can't find dictionary.json it will create one. You can change either of these parameters to different files if you want Codey to from a different source or store what it learns somewhere else.

	"pyhton3 generate.py 40 dictionary.json"
		This tells Codey to write something that is 40 units long based on what it stored in dictionary.json. You can change the length(the integer) to however long or short you would like and if you have saved something you learned in a different .json file you can use that.

	Happy Writing!

## Initial Goals

	[x]take input to make "dictionary"
	[x]generate "stories" even if they don't makes sense
	[]refine generation repeatedly until they do make sense


## Stretch Goals

	[]print new stories to a .txt file





## Resources

https://en.wikipedia.org/wiki/Markov_chain </br>
https://en.wikipedia.org/wiki/N-gram </br>
https://www.youtube.com/watch?v=L97yQMT0jn8