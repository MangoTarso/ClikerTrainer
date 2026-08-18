# Dog Clicker Trainer
A program that will help you train yourself with hypnosis and conditioning techniques so that your body "responds" to specific auditory stimuli (By default, the sound of a dog clicker).

## Install
Simply extract the contents of the `.zip` file into a folder. **MAKE SURE THAT THE FILE `dog-clicker.mp3` IS IN THE SAME FOLDER AS THE EXECUTABLE**.

## Play
- Open the executable.
- It will ask how many clicks do you wish to hear each time it plays (`int` value). Try to always use the same number always so that your brain has an easier time relating sensation with stimulus.
- It will ask if you wish to hear binaural beats (`[y/n]` options). These are designed to be dynamic, aka. they will change randomly, varying the binaural difference (Sounds like faster or slower pace) and the pitch (Sounds more or less intense).
- It will ask if you want a chance to be denied by the end (`[y/n]` options). It will chose a random number so that theres a 3/10ths of a chance to be shut down at the end instead of encouraged.
- It will ask for how long do you want the session to last (`int` value). Since the program is very dependant on random events, the real duration might end up being longer or shorter than the one defined, but not by much.
- Finally, enjoy of some "content" of your choice while the program plays in the background. The random clicking will form a relationship between the sound and the sensation.
- Don't forget to press enter when you finish to see how long you lasted.

## Dependencies
Library dependencies are:

- `playsound`
- `time`
- `random`
- `inputimeout`
- `pysinewave`
- `math`
- `copy`

## Release
Latest release is [here](https://github.com/MangoTarso/ClikerTrainer/releases/tag/v1.2)

## FAQ
### Can I change the sound played?
For the sound player, the code looks for the file called `dog-clicker.mp3`, which is provided but could be replaced with any `.mp3` file. Bear in mind that the code asks for a time limit (`int`) input and a larger `.mp3` file would alter said time limit.