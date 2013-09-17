"""
The Premedicant Dose for animal type is the weight of animal multipled
by drug dose rate, divided by drug concertration.
"""

from __future__ import division
import re  

drug_concerntrations = {"meloxicam" : 5.0, "amoxicillin clavulanic acid" : 32.5, "ketamine" : 100, "enrofloxacin 2.5 percent solution" : 25, "enrofloxacin 5.0 percent solution" : 50 }

rates = {
    'dog' : {"meloxicam" : [0.2], "amoxicillin clavulanic acid" : [8.75,12.5], "ketamine" : [5.0,7.0]},
    'cat' : {"meloxicam" : [0.2], "amoxicillin clavulanic acid" : [8.75,12.5], "ketamine" : [5.0,7.5]},
    'rabbit' : {"meloxicam" : [0.6], "ketamine" : [20], "enrofloxacin 2.5 percent solution" : [10.0, 15.0, 20.0, 25.0], "enrofloxacin 5.0 percent solution" : [10.0, 15.0, 20.0, 25.0]}
}

# maximum weight inputs
weight_max = {"dog" : 100.0, "cat" : 15.0, "rabbit" : 15.0}
valid_species = [ name for name in weight_max.keys() ]

def prompt_for_species():
    # force input of species. Keep looping until valid.
    while True:
        species = raw_input("\nEnter species as one of {} : ".format(valid_species))
        species_stripped = species.lower().strip()
        
        # match input with species dict, or first letter of species
        # else keep looping. return species
        possible_species = filter(lambda species: species.startswith(species_stripped), rates.keys())
        species_stripped = possible_species[0] if len(possible_species) == 1 else ""
        if species_stripped != "":
            return species_stripped
        
        else:
            print("\n\tOops! Please try again.")

def prompt_for_weight(species_stripped):
    # force input of weight. Keep looping until valid.
    weight_re = re.compile('\d+(\.\d+)?')

    while True:
        weight = raw_input("\nEnter the weight for a {} [maximum is {}kg]: ".format(species_stripped, weight_max[species_stripped]))

        # valid, but in range?
        if (weight_re.match(weight) != None) and (float(weight) > 0.0) and (float(weight) < weight_max[species_stripped]):
            weight_float = float(weight) 
            return weight_float
            break
        
        else:
            print("\n\tOops! Please try again.")

def calculate_premeds(species_stripped, weight_float):

    #Calculate Vet's premed dosage based on animal type.
    #weight * dose_rate  / drug_concentration

    print("\nCalculate Premedicant Dose for:\n\tSpecies = {} \n\tWeight = {}kg\n".format(species_stripped, weight_float))

    # iterate every drug, since none was chosen for this animal
    for species_rates in sorted(rates[species_stripped]):
        print("\n\t{}:".format(species_rates.title()))
        for drug_list, dose_rate in enumerate(rates[species_stripped][species_rates]):
            value = float(dose_rate)
            dosage_calculated = (weight_float * value) / float(drug_concerntrations[species_rates])
            print("\tdose rate = {:.2f}ml, calculated dosage = {:.2f}ml".format(dose_rate, dosage_calculated))


restart = "y" 
while restart == "y":
    species_stripped = prompt_for_species()
    weight_float
    = prompt_for_weight(species_stripped)
    calculate_premeds(species_stripped, weight_float)
    restart = raw_input("\nTO RESTART ENTER 'Y'.")
