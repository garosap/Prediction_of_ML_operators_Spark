import csv
import random
import os

# List of words to create sentences from
words = ["Chair", "Table", "Window", "Carpet", "Lamp", "Plant", "Computer", "Television", "Phone", "Book", "Pen", "Paper", "Bicycle", "Clock", "Picture", "Sofa", "Rug", "Bed", "Dresser", "Wall", "Door", "Ceiling", "Floor", "Mirror", "Vase", "Candles", "Flowers", "Paintings", "Statues", "Curtains", "Pillows", "Blankets", "Sheets", "Towels", "Soap", "Shampoo", "Conditioner", "Lotion", "Perfume", "Toothbrush", "Toothpaste", "Razor", "Shaver", "Hairbrush", "Hairties", "Combs", "Scissors", "Nailclippers", "Lipbalm", "Handsanitizer", "Tissues", "Trashcan", "Trashbags", "Papertowels", "Cleaningsupplies", "Detergent", "Softener", "Dryersheets", "Hangers", "Hamper", "Iron", "Vacuumcleaner", "Mop", "Broom", "Dustpan", "Dustcloth", "Furniturepolish", "Glasscleaner", "Kitchentowels", "Dishsoap", "Sponges", "Scrubbrush", "Potholders", "Cuttingboard", "Knives", "Spoons", "Forks", "Plates", "Bowls", "Glasses", "Cups", "Canopener", "Bottleopener", "Corkscrew", "Saltandpeppershakers", "Sugarbowl", "Creamer", "Coasters", "Napkins", "Trashbin", "Recyclingbin", "Compostbin", "Paperplates", "Plasticutensils", "Plasticcups", "Cooler", "Icecubetray", "Icepack", "Stove", "Oven", "Microwave", "Toaster", "Blender", "Coffeemaker", "Kettle", "Teapot", "Pot", "Pan", "Fryingpan", "Griddle", "Wok", "Bakingsheet", "Roastingpan", "Cuttingknife", "Chefsknife", "Paringknife", "Breadknife", "Carvingknife", "Knifeset", "Mixingbowl", "Measuringcup", "Measuringspoon", "Spatula", "Tongs", "Whisk", "Ladle", "Slottedspoon", "Colander", "Steamerbasket", "Potatomasher", "Canopener", "Peeler", "Grater", "Zester", "Mandoline", "Rollingpin", "Pastrybrush", "Siliconebakingmats", "Cakepan", "Piedish", "Bakingdish", "Casseroledish", "Breadpan", "Muffintin", "Cupcaketin", "Loafpan", "Springformpan", "Tartpan", "Quichedish", "Ramekins", "Saucepan", "Stockpot", "Dutchoven", "Souppot", "Chafingdish"]

def w2v_generate_data(num_samples, num_features):
    
    with open("w2v_dataset.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Generate sentences
        for i in range(num_samples):
            sentence = []
            for j in range(num_features):
                word = random.choice(words)
                sentence.append(word)

            # Write the data to a CSV file
            writer.writerow(sentence)

    with open('data.libsvm.meta', 'w') as f:
            f.write('num_samples,{}\n'.format(num_samples))
            f.write('num_features,{}\n'.format(num_features))
            f.write('dataset_size,{}'.format(os.path.getsize('w2v_dataset.csv')/10**6))
            print("dataset size is: {} MB".format(os.path.getsize('w2v_dataset.csv')/10**6))
            f.close()

    
    return num_features, num_samples




