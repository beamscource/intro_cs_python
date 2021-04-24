## ProblemSet 7
import string

class AdoptionCenter(object):

    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    
    def __init__(self, name, species_types, location):
        assert type(name) == str
        assert type(location) == tuple
        assert type(species_types) == dict
        
        self.name = name
        self.species_types = species_types
        self.location = location

    def get_name(self):
        return self.name

    def get_location(self):
        x = self.location[0]
        y = self.location[1]
        return (float(x), float(y))

    def get_species_count(self):
        return dict(self.species_types)

    def get_number_of_species(self, species_name):
        if species_name in self.species_types:
            return self.species_types[species_name]
        else:
            return 0

    def adopt_pet(self, species_name):
        if species_name in self.species_types:
            if self.species_types[species_name] != 0:
                self.species_types[species_name] = self.species_types[species_name] - 1
            if self.species_types[species_name] == 0:
                self.species_types.pop(species_name, None)

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.name,
                                  self.score)


class Adopter(object):
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    
    def __init__(self, name, desired_species):
        assert type(name) == str
        assert type(desired_species) == str

        self.name = name
        self.desired_species = desired_species


    def get_name(self):
        return self.name

    def get_desired_species(self):
        return self.desired_species

    def get_score(self, adoption_center):
        score = 0
        matches = 0
        desired = self.desired_species

        if desired in adoption_center.species_types:
                matches += 1
                score = matches*adoption_center.species_types[desired]

        return float(score)

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.name,
                                  self.score)

class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """

    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        # this is a list
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        desired = self.desired_species

        score = 0
        if desired in adoption_center.species_types:
                score = 1*adoption_center.species_types[desired]

        bonusSum = 0
        for species in self.considered_species:
            if species in adoption_center.species_types:
                bonusSum += adoption_center.species_types[species]

        bonus = 0.3*bonusSum

        totalScore = score + bonus
        return float(totalScore)


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """

    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        desired = self.desired_species

        score = 0
        if desired in adoption_center.species_types:
                score = 1*adoption_center.species_types[desired]

        bonusSum = 0
        if self.feared_species in adoption_center.species_types:
                bonusSum = adoption_center.species_types[self.feared_species]

        bonus = 0.3*bonusSum

        totalScore = score - bonus

        if totalScore < 0:
            return float(0)
        else:
            return float(totalScore)


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """

    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):

        if type(self.allergic_species) == str:
            if self.allergic_species in adoption_center.species_types:
                return float(0)
        else:
            for species in self.allergic_species:
                if species in adoption_center.species_types:
                    return float(0)

        desired = self.desired_species

        score = 0
        if desired in adoption_center.species_types:
                score = 1*adoption_center.species_types[desired]

        return float(score)


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """

    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):

        allergic_keys = []
        for species in self.allergic_species:
            if species in adoption_center.species_types:
                allergic_keys.append(species)

        effectiveness = 1.0
        try:
            for species in allergic_keys:
                if self.medicine_effectiveness[species] < effectiveness:
                    effectiveness = self.medicine_effectiveness[species]
        except TypeError:
            effectiveness = self.medicine_effectiveness[species]
        
       
        desired = self.desired_species

        score = 0
        if desired in adoption_center.species_types:
                score = 1*adoption_center.species_types[desired]
                
        return float(score*effectiveness)

##  EVERYTHING WRONG HERE
##
##        def get_score(self, adoption_center):
##
##        allergic_keys = []
##        for species in self.allergic_species:
##            if species in adoption_center.species_types:
##                allergic_keys = allergic_keys.append(species)
##
##        least_effective = 1.0
##        if len(allergic_keys) == 0:
##            effectiveness = 1.0
##        else:
##            try:
##                for key in allergic_keys:
##                    if self.medicine_effectiveness[key] < least_effective:
##                        least_effective = self.medicine_effectiveness[key]
##            except TypeError:
##                least_effective = self.medicine_effectiveness[allergic_keys]
##
##        effectiveness = least_effective[:]
##        
##        desired = self.desired_species
##
##        score = 0
##        if desired in adoption_center.species_types:
##                score = 1*adoption_center.species_types[desired]
##
##        return float(score*effectiveness)
##    
##    #version with copy
##    def get_score(self, adoption_center):
##
##        medicine_effectiveness_copy = self.medicine_effectiveness.copy()
##    
##        for species in self.medicine_effectiveness.keys():
##            if species not in adoption_center.species_types:
##                medicine_effectiveness_copy.pop(species, None)
##        
##        least_effective = min(medicine_effectiveness_copy, key=medicine_effectiveness_copy.get)
##
##        if least_effective in adoption_center.species_types:
##            effectiveness = self.medicine_effectiveness[least_effective]
##        
##        desired = self.desired_species
##
##        score = 0
##        if desired in adoption_center.species_types:
##                score = 1*adoption_center.species_types[desired]
##
##        return float(score*effectiveness)

import random as rand

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_score(self, adoption_center):

        def get_linear_distance(self, to_location):

            x1 = float(self.location[0])
            y1 = float(self.location[1])

            x2 = float(to_location[0])
            y2 = float(to_location[1])
        
            d = ( (x2-x1)**2 + (y2-y1)**2 ) ** 0.5
            return d

        desired = self.desired_species

        score = 0
        if desired in adoption_center.species_types:
                score = 1*adoption_center.species_types[desired]

        d = get_linear_distance(self, adoption_center.location)
        
        if d < 1:
            finalScore = 1*score
        elif d >= 1 and d < 3:
            finalScore = rand.uniform(0.7, 0.9)*score
        elif d >= 3 and d < 5:
            finalScore = rand.uniform(0.5, 0.7)*score
        elif d >= 5:
            finalScore = rand.uniform(0.1, 0.5)*score
            
        return float(finalScore)
    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """

    def getKey(adoption_center):
        return adoption_center.score

##    def getKey2(adoption_center):
##        return adoption_center.name

##    orderedList = {}

    for center in list_of_adoption_centers:
        center.score = adopter.get_score(center)

    return sorted(list_of_adoption_centers, key=getKey, reverse=True)

##        centerName = center.get_name()
##        orderedList.update({str(centerName): score})
##        
##    decreasingList = sorted(orderedList.items(), key=lambda x:x[1], reverse=True)
        
##    for i in range(len(decreasingList)):
##        print decreasingList[i][0]

##    return decreasingList
    
def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """

    def getKey(adopter):
        return adopter.score

    def getKey2(adopter):
        return adopter.name

##    orderedList = {}

    for adopter in list_of_adopters:
        adopter.score = adopter.get_score(adoption_center)

    for i in range(len(list_of_adopters)):
        print adopter.score
        
    sortedList = sorted(list_of_adopters, key=getKey2)
    wholeList = sorted(sortedList, key=getKey, reverse = True)
    return wholeList[0:n]

##        adopterName = adopter.get_name()
##        orderedList.update({str(adopterName): score})

##    decreasingList = sorted(orderedList.items(), key=lambda x:x[1], reverse=True)

##    for i in range(n):
##        try:
##            print decreasingList[i][0]
##        except IndexError:
##            break

##    return decreasingList

adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": rand.random()})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat") 
ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": rand.randint(20, 50), "Dog": rand.randint(1, 10)}, (-2,10))
