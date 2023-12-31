from game.src.Tag import Tag


class Tags:
    def __init__(self) -> None:
        pass

    TAGS = {
        "acquiredCompany": [Tag.EARTH],
        "adaptedLichen": [Tag.PLANT],
        "adaptionTechnology": [Tag.SCIENCE],
        "advancedAlloys": [Tag.SCIENCE],
        "advancedEcosystems": [Tag.PLANT, Tag.MICROBE, Tag.ANIMAL],
        "aerobrakedAmmoniaAsteroid": [Tag.SPACE, Tag.EVENT],
        "aiCentral": [Tag.SCIENCE, Tag.BUILDING],
        "algae": [Tag.PLANT],
        "antiGravityTechnology": [Tag.SCIENCE],
        "ants": [Tag.MICROBE],
        "aquiferPumping": [Tag.BUILDING],
        "archaebacteria": [Tag.MICROBE],
        "arcticAlgae": [Tag.PLANT],
        "artificialLake": [Tag.BUILDING],
        "artificialPhotosynthesis": [Tag.SCIENCE],
        "asteroid": [Tag.SPACE, Tag.EVENT],
        "asteroidMining": [Tag.JOVIAN, Tag.SPACE],
        "asteroidMiningConsortium": [Tag.JOVIAN],
        "beamFromAThoriumAsteroid": [Tag.JOVIAN, Tag.SPACE, Tag.POWER],
        "bigAsteroid": [Tag.SPACE, Tag.EVENT],
        "biomassCombustors": [Tag.POWER, Tag.BUILDING],
        "birds": [Tag.ANIMAL],
        "blackPolarDust": [],
        "breathingFilters": [Tag.SCIENCE],
        "bribedCommitee": [Tag.EARTH, Tag.EVENT],
        "buildingIndustries": [Tag.BUILDING],
        "bushes": [Tag.PLANT],
        "businessContacts": [Tag.EARTH, Tag.EVENT],
        "businessNetwork": [Tag.EARTH],
        "callistoPenalMines": [Tag.JOVIAN, Tag.SPACE],
        "capital": [Tag.CITY, Tag.BUILDING],
        "carbonateProcessing": [Tag.BUILDING],
        "caretakerContract": [],
        "cartel": [Tag.EARTH],
        "ceosFavoriteProject": [Tag.EVENT],
        "cloudSeeding": [],
        "colonizerTrainingCamp": [Tag.JOVIAN, Tag.BUILDING],
        "comet": [Tag.SPACE, Tag.EVENT],
        "commercialDistrict": [Tag.BUILDING],
        "convoyFromEuropa": [Tag.SPACE, Tag.EVENT],
        "corporateStronghold": [Tag.CITY, Tag.BUILDING],
        "cupolaCity": [Tag.CITY, Tag.BUILDING],
        "decomposers": [Tag.MICROBE],
        "deepWellHeating": [Tag.POWER, Tag.BUILDING],
        "deimosDown": [Tag.SPACE, Tag.EVENT],
        "designedMicroorganisms": [Tag.SCIENCE, Tag.MICROBE],
        "developmentCenter": [Tag.SCIENCE, Tag.BUILDING],
        "domedCrater": [Tag.CITY, Tag.BUILDING],
        "dustSeals": [],
        "earthCatapult": [Tag.EARTH],
        "earthOffice": [Tag.EARTH],
        "ecologicalZone": [Tag.PLANT, Tag.ANIMAL],
        "electroCatapult": [Tag.BUILDING],
        "energySaving": [Tag.POWER],
        "energyTapping": [Tag.POWER],
        "eosChasmaNationalPark": [Tag.PLANT, Tag.BUILDING],
        "equatorialMagnetizer": [Tag.BUILDING],
        "extremeColdFungus": [Tag.MICROBE],
        "farming": [Tag.PLANT],
        "fish": [Tag.ANIMAL],
        "flooding": [Tag.EVENT],
        "foodFactory": [Tag.BUILDING],
        "fueledGenerators": [Tag.POWER, Tag.BUILDING],
        "fuelfactory": [Tag.BUILDING],
        "fusionPower": [Tag.SCIENCE, Tag.POWER, Tag.BUILDING],
        "ganymedeColony": [Tag.JOVIAN, Tag.SPACE, Tag.CITY],
        "geneRepair": [Tag.SCIENCE],
        "geothermalPower": [Tag.POWER, Tag.BUILDING],
        "ghgFactories": [Tag.BUILDING],
        "ghgProducingBacteria": [Tag.SCIENCE, Tag.MICROBE],
        "giantIceAsteroid": [Tag.SPACE, Tag.EVENT],
        "giantSpaceMirror": [Tag.POWER, Tag.SPACE],
        "grass": [Tag.PLANT],
        "greatDam": [Tag.POWER, Tag.BUILDING],
        "greatEscarpmentConsortium": [],
        "greenhouses": [Tag.PLANT, Tag.BUILDING],
        "hackers": [],
        "heatTrappers": [Tag.POWER, Tag.BUILDING],
        "heather": [Tag.PLANT],
        "herbivores": [Tag.ANIMAL],
        "hiredRaiders": [Tag.EVENT],
        "iceAsteroid": [Tag.SPACE, Tag.EVENT],
        "iceCapMelting": [Tag.EVENT],
        "immigrantCity": [Tag.CITY, Tag.BUILDING],
        "immigrationShuttles": [Tag.EARTH, Tag.SPACE],
        "importOfAdvancedGhg": [Tag.EARTH, Tag.SPACE, Tag.EVENT],
        "importedGhg": [Tag.EARTH, Tag.SPACE, Tag.EVENT],
        "importedHydrogen": [Tag.EARTH, Tag.SPACE, Tag.EVENT],
        "importedNitrogen": [Tag.EARTH, Tag.SPACE, Tag.EVENT],
        "indenturedWorkers": [Tag.EVENT],
        "industialCenter": [Tag.BUILDING],
        "industrialMicrobes": [Tag.MICROBE, Tag.BUILDING],
        "insects": [Tag.MICROBE],
        "insulation": [],
        "interstellarColonyShip": [Tag.EARTH, Tag.SPACE, Tag.EVENT],
        "inventionContest": [Tag.SCIENCE, Tag.EVENT],
        "inventorsGuild": [Tag.SCIENCE],
        "investmentLoan": [Tag.EARTH, Tag.EVENT],
        "ioMiningIndustries": [Tag.JOVIAN, Tag.SPACE],
        "ironworks": [Tag.BUILDING],
        "kelpFarming": [Tag.PLANT],
        "lagrangeObservatory": [Tag.SCIENCE, Tag.SPACE],
        "lakeMarineris": [],
        "landClaim": [Tag.EVENT],
        "largeConvoy": [Tag.EARTH, Tag.SPACE, Tag.EVENT],
        "lavaFlows": [Tag.EVENT],
        "lichen": [Tag.PLANT],
        "lightningHarvest": [Tag.POWER],
        "livestock": [Tag.ANIMAL],
        "localHeatTrapping": [Tag.EVENT],
        "lunarBeam": [Tag.EARTH, Tag.POWER],
        "magneticFieldDome": [Tag.BUILDING],
        "magneticFieldGenerators": [Tag.BUILDING],
        "mangrove": [Tag.PLANT],
        "marsUniversity": [Tag.SCIENCE, Tag.BUILDING],
        "martianRails": [Tag.BUILDING],
        "massConverter": [Tag.SCIENCE, Tag.POWER],
        "mediaArchives": [Tag.EARTH],
        "mediaGroup": [Tag.EARTH],
        "medicalLab": [Tag.SCIENCE, Tag.BUILDING],
        "methaneFromTitan": [Tag.JOVIAN, Tag.SPACE],
        "microMills": [],
        "mine": [Tag.BUILDING],
        "mineralDeposit": [Tag.EVENT],
        "miningArea": [Tag.BUILDING],
        "miningExpedition": [Tag.EVENT],
        "miningRights": [Tag.BUILDING],
        "mirandaResort": [Tag.JOVIAN, Tag.SPACE],
        "moholeArea": [Tag.BUILDING],
        "moss": [Tag.PLANT],
        "naturalPreserve": [Tag.SCIENCE, Tag.BUILDING],
        "nitriteReducingBacteria": [Tag.MICROBE],
        "nitrogenRichAsteroid": [Tag.SPACE, Tag.EVENT],
        "nitrophilicMoss": [Tag.PLANT],
        "noctisCity": [Tag.CITY, Tag.BUILDING],
        "noctisFarming": [Tag.PLANT, Tag.BUILDING],
        "nuclearPower": [Tag.POWER, Tag.BUILDING],
        "nuclearZone": [Tag.EARTH],
        "olympusConference": [Tag.SCIENCE, Tag.EARTH, Tag.BUILDING],
        "openCity": [Tag.CITY, Tag.BUILDING],
        "optimalAerobraking": [Tag.SPACE],
        "oreProcessor": [Tag.BUILDING],
        "permafrostExtraction": [Tag.EVENT],
        "peroxidePower": [Tag.POWER, Tag.BUILDING],
        "pets": [Tag.EARTH, Tag.ANIMAL],
        "phobosSpacehaven": [Tag.CITY, Tag.SPACE],
        "physicsComplex": [Tag.SCIENCE, Tag.BUILDING],
        "plantation": [Tag.PLANT],
        "powerGrid": [Tag.POWER],
        "powerInfrastructure": [Tag.POWER, Tag.BUILDING],
        "powerPlant": [Tag.POWER, Tag.BUILDING],
        "powerSupplyConsortium": [Tag.POWER],
        "predators": [Tag.ANIMAL],
        "protectedHabitats": [],
        "protectedValley": [Tag.PLANT, Tag.BUILDING],
        "quantumExtractor": [Tag.SCIENCE, Tag.POWER],
        "radChemFactory": [Tag.BUILDING],
        "radSuits": [],
        "regolithEaters": [Tag.SCIENCE, Tag.MICROBE],
        "releaseOfInertGases": [Tag.EVENT],
        "research": [Tag.SCIENCE, Tag.SCIENCE],
        "researchOutpost": [Tag.SCIENCE, Tag.CITY, Tag.BUILDING],
        "restrictedArea": [Tag.SCIENCE],
        "roboticWorkforce": [Tag.SCIENCE],
        "roverConstruction": [Tag.BUILDING],
        "sabotage": [Tag.EVENT],
        "satellites": [Tag.SPACE],
        "searchForLife": [Tag.SCIENCE],
        "securityFleet": [Tag.SPACE],
        "shuttles": [Tag.SPACE],
        "smallAnimals": [Tag.ANIMAL],
        "soilfactory": [Tag.BUILDING],
        "solarPower": [Tag.POWER, Tag.BUILDING],
        "solarWindPower": [Tag.SCIENCE, Tag.SPACE, Tag.POWER],
        "soletta": [Tag.SPACE],
        "spaceElevator": [Tag.SPACE, Tag.BUILDING],
        "spaceMirrors": [Tag.POWER, Tag.SPACE],
        "spaceStation": [Tag.SPACE],
        "specialDesign": [Tag.SCIENCE, Tag.EVENT],
        "sponsors": [Tag.EARTH],
        "standardTechnology": [Tag.SCIENCE],
        "steelworks": [Tag.BUILDING],
        "stripMine": [Tag.BUILDING],
        "subterraneanReservoir": [Tag.EVENT],
        "symbioticFungus": [Tag.MICROBE],
        "tardigrades": [Tag.MICROBE],
        "technologyDemonstration": [Tag.SCIENCE, Tag.SPACE, Tag.EVENT],
        "tectonicStressPower": [Tag.POWER, Tag.BUILDING],
        "terraformingGanymede": [Tag.JOVIAN, Tag.SPACE],
        "titaniumMine": [Tag.BUILDING],
        "tollStation": [Tag.SPACE],
        "towingAComet": [Tag.SPACE, Tag.EVENT],
        "transNeptuneProbe": [Tag.SCIENCE, Tag.SPACE],
        "trees": [Tag.PLANT],
        "tropicalResort": [Tag.BUILDING],
        "tundraFarming": [Tag.PLANT],
        "undergroundCity": [Tag.CITY, Tag.BUILDING],
        "undergroundDetonations": [Tag.BUILDING],
        "urbanizedArea": [Tag.CITY, Tag.BUILDING],
        "vestaShipyard": [Tag.JOVIAN, Tag.SPACE],
        "viralEnhancers": [Tag.SCIENCE, Tag.MICROBE],
        "virus": [Tag.MICROBE, Tag.EVENT],
        "waterImportFromEuropa": [Tag.JOVIAN, Tag.SPACE],
        "waterSplittingPlant": [Tag.BUILDING],
        "wavePower": [Tag.POWER],
        "windmills": [Tag.POWER, Tag.BUILDING],
        "worms": [Tag.MICROBE],
        "zeppelins": [],
    }

    @staticmethod
    def getTags(id: str):
        return Tags.TAGS[id]
