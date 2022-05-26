def convert(number):
    raindrop_sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    raindrops = ""
    for factor, sound in raindrop_sounds.items():
        if number % factor == 0:
            raindrops += sound
    return raindrops or str(number)


