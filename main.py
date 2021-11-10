from utility_class import utility

print("```BOT_Paimon: Version 1.0 \n Genshin Impact: Version 2.1```")

print(
    "\n-------------------------------------------------------------------------------------------------------------------")

adventurer = ["Max HP increased by 1,000.", "Opening chest regenerates 30% Max HP over 5s."]
archaicPetra = ["Gain a 15% Geo DMG Bonus.",
                "Upon obtaining an Elemental Shard created through a Crystallize Reaction, all party members gain a 35% DMG Bonus for that particular element for 10s. Only one form of Elemental DMG Bonus can be gained in this manner at any one time."]


def welcome():
    print("\nWelcome to the Genshin Impact guide! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
    print(
        "I am BOT_Paimon and I will be telling you about farming, characters, and rerolling in Genshin Impact. (づ｡◕‿‿◕｡)づ")


def error():
    print(
        "Sorry, but I did not quite understand what you have typed. Please press the corresponding letters for your response. (◕︵◕)")


def question():
    res = input(
        "\nWhat kind of help do you need for Genshin Impact? \n[a] Farming \n[b] Character \n[c] Rerolling \n> ")
    res = res.lower()
    if res == "a":
        return farming()
    elif res == "b":
        return character()
    elif res == "c":
        return rerolling()
    else:
        error()
        return question()


def farming():
    res = input("Where are you going to be farming? \n[a] City of Mondstadt \n[b] Liyue Harbor \n[c] Inazuma City \n> ")
    res = res.lower()
    if res == "a":
        return mondstadt()
    elif res == "b":
        return liyue()
    elif res == "c":
        return inazuma()
    else:
        error()
        return farming()


def mondstadt():
    print("A")


def liyue():
    print("B")


def inazuma():
    print("C")


def character():
    res = input("Which character do you need help with? \n> ")
    res = res.lower()
    if res == "aloy":
        return aloy()
    elif res == "albedo":
        return albedo()
    elif res == "amber":
        return amber()
    elif res == "ayaka":
        return ayaka()
    elif res == "barbara":
        return barbara()
    elif res == "beidou":
        return beidou()
    elif res == "bennett":
        return bennett()
    elif res == "chongyun":
        return chongyun()
    elif res == "diluc":
        return diluc()
    elif res == "diona":
        return diona()
    elif res == "eula":
        return eula()
    elif res == "fischl":
        return fischl()
    elif res == "ganyu":
        return ganyu()
    elif res == "hu tao":
        return hutao()
    elif res == "hutao":
        return hutao()
    elif res == "jean":
        return jean()
    elif res == "kaeya":
        return kaeya()
    elif res == "kazuha":
        return kazuha()
    elif res == "keqing":
        return keqing()
    elif res == "klee":
        return klee()
    elif res == "kokomi":
        return kokomi()
    elif res == "lisa":
        return lisa()
    elif res == "mona":
        return mona()
    elif res == "ningguang":
        return ningguang()
    elif res == "noelle":
        return noelle()
    elif res == "qiqi":
        return qiqi()
    elif res == "raiden":
        return raiden()
    elif res == "raiden shogun":
        return raiden()
    elif res == "razor":
        return razor()
    elif res == "rosaria":
        return rosaria()
    elif res == "sara":
        return sara()
    elif res == "kujou sara":
        return sara()
    elif res == "sayu":
        return sayu()
    elif res == "sucrose":
        return sucrose()
    elif res == "tartaglia":
        return tartaglia()
    elif res == "childe":
        return tartaglia()
    elif res == "traveler":
        return traveler()
    elif res == "traveller":
        return traveler()
    elif res == "venti":
        return venti()
    elif res == "xiangling":
        return xiangling()
    elif res == "xiao":
        return xiao()
    elif res == "xingqiu":
        return xingqiu()
    elif res == "xinyan":
        return xinyan()
    elif res == "yanfei":
        return yanfei()
    elif res == "yoimiya":
        return yoimiya()
    elif res == "zhongli":
        return zhongli()
    else:
        print(
            "That isn't an existing Genshi Impact character yet. Try asking for a character that is currently in-game.")
        return character()


def aloy():
    res = input("What kind of help do you need with Aloy? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return aloyBuild()
    elif res == "b":
        return aloyConst()
    elif res == "c":
        return aloyAbility()
    else:
        error()
        return aloy()


def aloyBuild():
    weapon = ["polar star", "the stringless"]
    altWeapon = ["sacrificial bow", "favonius warbow"]
    artifact = ["4x blizzard strayer", "2x blizzard strayer, 2x noblesse oblige"]
    artifactStats = [["Flat ATK", "ATK%, CRIT DMG, Elemental Mastery, CRIT Rate"],
                     ["Flat HP", "ATK%, CRIT DMG, CRIT Rate, Elemental Mastery"],
                     ["ATK%", "CRIT DMG, Energy Recharge, Elemental Mastery, CRIT Rate"],
                     ["Cryo DMG Bonus%", "ATK%, CRIT DMG, CRIT Rate, Energy Recharge/Elemental Mastery"],
                     ["CRIT Rate/CRIT DMG", "CRIT Rate/CRIT DMG, ATK%, Energy Recharge, Elemental Mastery"]]
    print("Cryo DPS Build:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece blizzard strayer: \n\t1. Cryo DMG Bonus +15% \n\t2. When a character attacks an opponent affected by Cryo, their CRIT Rate is increased by 20%. If the opponent is Frozen, CRIT Rate is increased by an additional 20%.")
    print("\t- The 2 piece set will increase your cryo damage by 15% and increase your elemental burst damage by 20%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def aloyConst():
    print(
        "After the release of Aloy she was not given a constellation to follow as she is expected to not be released on any banners.")
    print("Maybe later in the future her constellations will be out for others to collect.")


def aloyAbility():
    rapidFire = ["Normal Attack - Performs up to 4 consecutive shots with a bow.",
                 "Charged Attack - Charging the bow will accumulate biting frost and will. If fully charged, it will deal Cryo damage",
                 "Plunging Attack - Has a rain of arrows striking before falling on to the ground, dealing AoE DMG upon landing."]
    frozenWilds = ["Elemental Skill",
                   "Aloy throws a Freeze Bomb in the targeted direction and triggers an explosion, dealing Cryo DMG. After it explodes, the Freeze Bomb will split up into many Chillwater Bomblets that explode on contact with opponents or after a short delay, dealing Cryo DMG.",
                   "When a Freeze Bomb or Chillwater Bomblet hits an opponent, the opponent's ATK is decreased and Aloy receives 1 Coil stack.",
                   "Aloy can gain up to 1 Coil stack every 0.1s."]
    coil = ["Each stack increases Aloy's Normal Attack DMG.",
            "When Aloy has 4 Coil stacks, all stacks of Coil are cleared. She then enters the Rushing Ice state, which further increases the DMG dealt by her Normal Attacks and converts her Normal Attack DMG to Cryo DMG."]
    propheciesOfDawn = ["Elemental Burst",
                        "Aloy throws a Power Cell filled with Cryo in the targeted direction, then detonates it with an arrow, dealing AoE Cryo Damage."]
    combatOverride = ["Unlocked at Ascension 1",
                      "When Aloy gains a <Coil> her attack is increased by 16% and her nearby party members receive 8% attack increase. This lasts for 10 seconds"]
    strongStrike = ["Unlocked at Ascension 4",
                    "When Aloy is in the Rushing Ice state conferred by Frozen Wilds, her Cryo DMG Bonus increases by 3.5% every 1s. A maximum Cryo DMG Bonus increase of 35% can be gained in this way."]
    easyDoesIt = ["Unlocked Automatically",
                  "When Aloy is in the party, animals who produce Fowl, Raw Meat, or Chilled Meat will not be startled when party members approach them."]
    print("Skill Talents: ")
    print(" - Rapid Fire")
    for i in enumerate(rapidFire, start=1):
        print("\t", *i, sep=". ")
    print("\n - Frozen Wilds")
    for ii in enumerate(frozenWilds, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Coil:")
    for iii in enumerate(coil, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Prophecies Of Dawn")
    for iv in enumerate(propheciesOfDawn, start=1):
        print("\t", *iv, sep=". ")
    print("\nPassive: ")
    print(" - Combat Override")
    for v in enumerate(combatOverride, start=1):
        print("\t", *v, sep=". ")
    print("\n - Strong Strike")
    for vi in enumerate(strongStrike, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Easy Does It")
    for vii in enumerate(easyDoesIt, start=1):
        print("\t", *vii, sep=". ")


def albedo():
    res = input("What kind of help do you need with Albedo? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return albedoBuild()
    elif res == "b":
        return albedoConst()
    elif res == "c":
        return albedoAbility()
    else:
        error()
        return albedo()


def albedoBuild():
    weapon = ["skyward blade", "festering desire"]
    altWeapon = ["harbringer of dawn", "traveler's handy sword"]
    artifact = ["4x archaic petra", "2x archaic petra, 2x noblesse oblige"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, DEF%, Flat DEF"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, DEF%, Flat DEF"],
                     ["DEF%/ATK%", "CRIT DMG, CRIT Rate, DEF%, Energy Recharge/ATK%"],
                     ["Geo DMG Bonus%", "CRIT DMG, CRIT Rate, DEF%, Flat DEF"],
                     ["CRIT Rate/CRIT DMG", "CRIT Damage/CRIT Rate, DEF%, Flat DEF, Energy Recharge/ATK%"]]
    print("Geo Sub-DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece archaic petra: \n\t1. Geo DMG Bonus +15% \n\t2. Upon obtaining an Elemental Shard created through a Crystallize Reaction, all party members gain 35% DMG Bonus for that particular element for 10s. Only one form of Elemental DMG Bonus can be gained in this manner at any one time.")
    print("\t- The 2 piece set will increase your geo damage by 15% and increase your elemental burst damage by 20%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def albedoConst():
    flowerOfEden = ["Constellation Lv. 1",
                    "Transient Blossoms generated by Albedo's Abiogenesis: Solar Isotoma regenerate 1.2 Energy for Albedo."]
    openingOfPhanerozoic = ["Constellation Lv. 2",
                            "Transient Blossoms generated by Abiogenesis: Solar Isotoma grant Albedo Fatal Reckoning for 30s.",
                            "Each stack of Fatal Reckoning increases DMG by of Albedo's DEF. The effect stacks up to 4 times.",
                            "Unleashing Rite of Progeniture: Tectonic Tide consumes all stacks of Fatal Reckoning, increasing the DMG dealt by the Tectonic Tide and Fatal Blossoms based on the number of stacks consumed."]
    graceOfHelios = ["Constellation Lv. 3",
                     "Increases the level of Abiogenesis: Solar Isotoma by 3.", "Maximum upgrade level is 15."]
    descentOfDivinity = ["Constellation Lv. 4",
                         "Solar Isotoma increases Plunging Attack DMG by 30% for active party members within the AoE."]
    tideOfHadaen = ["Constellation Lv. 5",
                    "Increases the level of Rite of Progeniture: Tectonic Tide by 3.", "Maximum upgrade level is 15."]
    dustOfPurification = ["Constellation Lv. 6",
                          "If active party members within the AoE are protected by a shield created by Crystallize, Solar Isotoma increases their DMG by 17%."]
    print("Albedo's Constellations:")
    print(" - Flower Of Eden")
    for i in enumerate(flowerOfEden, start=1):
        print("\t", *i, sep=". ")
    print("\n - Opening Of Phanerozoic")
    for ii in enumerate(openingOfPhanerozoic, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Grace Of Helios")
    for iii in enumerate(graceOfHelios, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Descent Of Divinity")
    for iv in enumerate(descentOfDivinity, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Tide of Hadaen")
    for v in enumerate(tideOfHadaen, start=1):
        print("\t", *v, sep=". ")
    print("\n - Dust Of Purification")
    for vi in enumerate(dustOfPurification, start=1):
        print("\t", *vi, sep=". ")


def albedoAbility():
    favoniusBladework_Weiss = ["Normal Attack - Perform up to 5 rapid strikes",
                               "Charged Attack - Consumes a certain amount of Stamina to unleash 2 rapid sword strikes.",
                               "Plunging Attack - Plunges from mid-air to strike the ground below, damaging opponents along the path and dealing AoE DMG upon impact."]
    abiogenesis = ["Elemental Skill",
                   "Albedo creates a Solar Isotoma using alchemy, which deals AoE Geo DMG on appearance."]
    solarIsotoma = [
        "When enemies within the Solar Isotoma zone are hit, the Solar Isotoma will generate Transient Blossoms which deal AoE Geo DMG. DMG dealt scales off Albedo's DEF.",
        "Transient Blossoms can only be generated once every 2s.",
        "When a character is located at the locus of the Solar Isotoma, the Solar Isotoma will accumulate Geo power to form a crystallized platform that lifts the character up to a certain height. Only one crystallized platform can exist at a time."]
    riteOfProgeniture = ["Elemental Burst",
                         "Under Albedo's command, Geo crystals surge and burst forth, dealing AoE Geo DMG in front of him.",
                         "If a Solar Isotoma created by Albedo himself is on the field, 7 Fatal Blossoms will be generated in the Solar Isotoma field, bursting violently into bloom and dealing AoE Geo DMG",
                         "Tecotonic Tide DMG and Fatal Blossom DMG will not generate Transient Blossoms."]
    calciteMight = ["Unlocked at Ascension 1",
                    "Transient Blossoms generated by Abiogenesis: Solar Isotoma deal 25% more DMG to enemies whose HP is below 50%."]
    homuncularNature = ["Unlocked at Ascension 4",
                        "Using Rite of Progeniture: Tectonic Tide increases the Elemental Mastery of nearby party members by 125 for 10s."]
    flashOfGenius = ["Unlocked Automatically",
                     "When Albedo crafts Weapon Ascension Materials, he has a 10% chance to receive double the product."]
    print("Skill Talents: ")
    print(" - Favonius Bladework - Weiss")
    for i in enumerate(favoniusBladework_Weiss, start=1):
        print("\t", *i, sep=". ")
    print("\n - Abiogenesis: Solar Isotoma")
    for ii in enumerate(abiogenesis, start=1):
        print("\t", *ii, sep=". ")
    print("\n\t - Solar Isotoma")
    for iii in enumerate(solarIsotoma, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Rite of Progeniture: Tectonic Tide")
    for iv in enumerate(riteOfProgeniture, start=1):
        print("\t", *iv, sep=". ")
    print("\nPassive: ")
    print(" - Calcite Might")
    for v in enumerate(calciteMight, start=1):
        print("\t", *v, sep=". ")
    print("\n - Homuncular Nature")
    for vi in enumerate(homuncularNature, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Flash of Genius (Albedo)")
    for vii in enumerate(flashOfGenius, start=1):
        print("\t", *vii, sep=". ")


def amber():
    res = input("What kind of help do you need with Amber? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return amberBuild()
    elif res == "b":
        return amberConst()
    elif res == "c":
        return amberAbility()
    else:
        error()
        return amber()


def amberBuild():
    weapon = ["elegy for the end", "the stringless"]
    altWeapon = ["sacrificial bow", "raven bow"]
    artifact = ["4x noblesse oblige", "2x crimson witch of flames, 2x noblesse oblige"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery/Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["ATK%", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["Pyro DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["CRIT DMG/CRIT Rate", "CRIT Damage/CRIT Rate, ATK%, Flat ATK, Elemental Mastery/Energy Recharge"]]
    print("Geo Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece nobless oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increases all party members' ATK by 20% for 12s. This effect cannot stack.")
    print("\t- The 2 piece set will increase your pyro damage by 15% and increase your elemental burst damage by 20%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def amberConst():
    oneArrow = ["Constellation Lv. 1",
                "Fires 2 arrows per Aimed Shot. The second arrow deals 20% of the first arrow's DMG."]
    bunnyTriggered = ["Constellation Lv. 2",
                      "Baron Bunny, new and improved! Hitting Baron Bunny's foot with a fully-charged Aimed Shot manually detonates it.",
                      "Explosion via manual detonation deals 200% additional DMG."]
    itBurns = ["Constellation Lv. 3",
               "Increases the Level of Fiery Rain by 3.",
               "Maximum upgrade level is 15."]
    notJustAnyDoll = ["Constellation Lv. 4",
                      "Decreases Explosive Puppet's CD by 20%. Adds 1 additional charge."]
    baronBunny = ["Constellation Lv. 5",
                  "Increase the Level of Explosive Puppet by 3.",
                  "Maximum upgrade level is 15."]
    wildfire = ["Constellation Lv. 6",
                "Fiery Rain increases Amber's Movement SPD by 15% and Base ATK by 15% for 10s."]

    print("Amber's Constellations:")
    print(" - One Arrow to Rule Them All")
    for i in enumerate(oneArrow, start=1):
        print("\t", *i, sep=". ")
    print("\n - Bunny Triggered")
    for ii in enumerate(bunnyTriggered, start=1):
        print("\t", *ii, sep=". ")
    print("\n - It Burns!")
    for iii in enumerate(itBurns, start=1):
        print("\t", *iii, sep=". ")
    print("\n - It's Not Just Any Doll...")
    for iv in enumerate(notJustAnyDoll, start=1):
        print("\t", *iv, sep=". ")
    print("\n - It's Baron Bunny!")
    for v in enumerate(baronBunny, start=1):
        print("\t", *v, sep=". ")
    print("\n - Wildfire")
    for vi in enumerate(wildfire, start=1):
        print("\t", *vi, sep=". ")


def amberAbility():
    sharpshooter = ["Normal Attack - Performs up to 5 consecutive shots with a bow.",
                    "Charged Attack - A fully charged flaming arrow will deal Pyro DMG.",
                    "Plunging Attack - Fires off a shower of arrows in mid-air before falling and striking the ground, dealing AoE DMG upon impact."]
    baronBunny = ["Elemental Skill",
                  "Continuously taunts the enemy, drawing their fire.",
                  "Baron Bunny's HP scales with Amber's Max HP.",
                  "When destroyed or when its timer expires, Baron Bunny explodes, dealing AoE Pyro DMG."]
    hold = ["Adjusts the throwing direction of Baron Bunny.",
            "The longer the button is held, the further the throw."]
    fieryRain = ["Elemental Burst",
                 "Fires of a shower of arrows, dealing continuous AoE Pyro DMG."]
    everyArrowFindsItsTarget = ["Unlocked at Ascension 1",
                                "Increases the CRIT Rate of Fiery Rain by 10% and widens its AoE by 30%."]
    preciseShot = ["Unlocked at Ascension 2",
                   "Aimed Shot hits on weak spots increase Base ATK by 15% for 10s."]
    glidingChampion = ["Unlocked Automatically",
                       "Decreases all party members' gliding Stamina Consumption by 20%."]
    print("Skill Talents: ")
    print(" - Sharpshooter")
    for i in enumerate(sharpshooter, start=1):
        print("\t", *i, sep=". ")
    print("\n - Baron Bunny")
    for ii in enumerate(baronBunny, start=1):
        print("\t", *ii, sep=". ")
    for iii in enumerate(hold, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Fiery Rain")
    for iv in enumerate(fieryRain, start=1):
        print("\t", *iv, sep=". ")
    print("\nPassive: ")
    print(" - Every Arrow Finds Its Target")
    for v in enumerate(everyArrowFindsItsTarget, start=1):
        print("\t", *v, sep=". ")
    print("\n - Precise Shot")
    for vi in enumerate(preciseShot, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Gliding Champion")
    for vii in enumerate(glidingChampion, start=1):
        print("\t", *vii, sep=". ")


def ayaka():
    res = input("What kind of help do you need with Ayaka? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return ayakaBuild()
    elif res == "b":
        return ayakaConst()
    elif res == "c":
        return ayakaAbility()
    else:
        error()
        return ayaka()


def ayakaBuild():
    weapon = ["mistsplitter reforged", "blackcliff longsword"]
    altWeapon = ["the black sword", "amenoma kageuchi"]
    artifact = ["4x blizzard strayer", "4x emblem of severed fate"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["ATK%", "CRIT Rate, CRIT DMG, Flat ATK, Elemental Mastery"],
                     ["Cryo DMG Bonus%", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["CRIT DMG", "CRIT Rate, Elemental Mastery, ATK%, Energy Recharge"]]
    print("Cryo DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece blizzard strayer: \n\t1. Cryo DMG Bonus +15% \n\t2. When a character attacks an opponent affected by Cryo, their CRIT Rate is increased by 20%. If the opponent is Frozen, CRIT Rate is increased by an additional 20%.")
    print(
        "\t- The 4 piece emblem of severed fate: \n\t1. Energy Recharge +20% \n\t2. Increases Elemental Burst DMG by 25% of Energy Recharge. A maximum of 75% bonus DMG can be obtained in this way.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def ayakaConst():
    snowSwept = ["Constellation Lv. 1",
                 "When Kamisato Ayaka's Normal or Charged Attacks deal Cryo DMG to opponents, it has a 50% chance of decreasing the CD of Kamisato Art: Hyouka by 0.3s. This effect can occur once every 0.1s."]
    blizzardBladeSekiNoTo = ["Constellation Lv. 2",
                             "When casting Kamisato Art: Soumetsu, unleashes 2 smaller additional Frostflake Seki no To, each dealing 20% of the original storm's DMG."]
    frostbloomKamifubuki = ["Constellation Lv. 3",
                            "Increases the Level of Kamisato Art: Soumetsu by 3.",
                            "Maximum upgrade level is 15."]
    ebbAndFlow = ["Constellation Lv. 4",
                  "Opponents damaged by Kamisato Art: Soumetsu's Frostflake Seki no To will have their DEF decreased by 30% for 6s."]
    blossomCloudIrutsuki = ["Constellation Lv. 5",
                            "Increase the Level of Kamisato Art: Hyouka by 3.",
                            "Maximum upgrade level is 15."]
    danceOfSuigetsu = ["Constellation Lv. 6",
                       """Kamisato Ayaka gains Usurahi Butou every 10s, increasing her Charged Attack DMG by 298%. 
         This buff will be cleared 0.5s after Ayaka's Charged ATK hits an opponent, after which the timer for this ability will restart."""]
    print("Ayaka's Constellations:")
    print(" - Snowswept Sakura")
    for i in enumerate(snowSwept, start=1):
        print("\t", *i, sep=". ")
    print("\n - Blizzard Blade Seki no To")
    for ii in enumerate(blizzardBladeSekiNoTo, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Frostbloom Kamifubuki")
    for iii in enumerate(frostbloomKamifubuki, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Ebb and Flow")
    for iv in enumerate(ebbAndFlow, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Blossom Cloud Irutsuki")
    for v in enumerate(blossomCloudIrutsuki, start=1):
        print("\t", *v, sep=". ")
    print("\n - Dance of Suigetsu")
    for vi in enumerate(danceOfSuigetsu, start=1):
        print("\t", *vi, sep=". ")


def ayakaAbility():
    kabuki = ["Normal Attack - Performs up to 5 rapid strikes.",
              "Charged Attack - Consumes a certain amount of Stamina to unleash a continuous stream of sword ki.",
              "Plunging Attack - Lunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    hyouka = ["Elemental Skill",
              "Summons blooming ice to launch nearby opponents, dealing AoE Cryo DMG."]
    soumetsu = [
        "Summons forth a snowstorm with flawless poise, unleashing a Frostflake Seki no To that moves forward continuously."]
    frostflakeSekiNoTo = ["Elemental Burst",
                          "A storm of whirling icy winds that slashes repeatedly at every enemy it touches, dealing Cryo DMG",
                          "The snowstorm explodes after its duration ends, dealing AoE Cryo DMG."]
    senho = ["Right Click",
             "Ayaka consumes Stamina and cloaks herself in a frozen fog that moves with her. In Senho form, she moves swiftly upon water.",
             "Ayaka unleashes frigid energy to apply Cryo on nearby opponents.",
             "Coldness condenses around Ayaka's blade, infusing her attacks with Cryo for a brief period."]
    amatsumiKunitsumiSanctification = ["Unlocked at Ascension 1",
                                       "After using Kamisato Art: Hyouka, Kamisato Ayaka's Normal and Charged attacks deal 30% increased DMG for 6s."]
    kantenSenmyouBlessing = ["Unlocked at Ascension 4",
                             "When the Cryo application at the end of Kamisato Art: Senho hits an opponent, Kamisato Ayaka gains the following effects: \nRestores 10 Stamin\nGains 18% Cryo DMG Bonus for 10s."]
    fruitsOfShinsa = ["Unlocked Automatically",
                      "When Ayaka crafts Weapon Ascension Materials, she has a 10% chance to receive double the product."]
    print("Skill Talents: ")
    print(" - Kamisato Art: Kabuki")
    for i in enumerate(kabuki, start=1):
        print("\t", *i, sep=". ")
    print("\n - Kamisato Art: Hyouka")
    for ii in enumerate(hyouka, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Kamisato Art: Soumetsu")
    for iii in enumerate(soumetsu, start=1):
        print("\t", *iii, sep=". ")
    print("\t - Frostflake Seki no To")
    for iv in enumerate(frostflakeSekiNoTo, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Kamisato Art: Senho")
    for v in enumerate(senho, start=1):
        print("\t", *v, sep=". ")
    print("\nPassive: ")
    print("\n - Amatsumi Kunitsumi Sanctification")
    for vi in enumerate(amatsumiKunitsumiSanctification, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Kanten Senmyou Blessing")
    for vii in enumerate(kantenSenmyouBlessing, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Fruits of Shinsa")
    for viii in enumerate(fruitsOfShinsa, start=1):
        print("\t", *viii, sep=". ")


def barbara():
    res = input(
        "What kind of help do you need with Barbara? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return barbaraBuild()
    elif res == "b":
        return barbaraConst()
    elif res == "c":
        return barbaraAbility()
    else:
        error()
        return barbara()


def barbaraBuild():
    weapon = ["prototype amber", "favonius codex"]
    altWeapon = ["thrilling tales of dragon slayers"]
    artifact = ["4x maiden beloved"]
    artifactStats = [["Flat ATK", "HP%, Energy Recharge, HP Flat, Elemental Mastery/DEF"],
                     ["Flat HP", "HP%, Energy Recharge, Elemental Mastery, DEF"],
                     ["HP%", "CRIT DMG, CRIT Rate, Energy Recharge, ATK%"],
                     ["HP%", "Flat HP, Energy Recharge, Elemental Mastery, DEF"],
                     ["Healing Bonus", "HP%, Flat HP, ATK%, Energy Recharge"]]
    print("Hydro Healer:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece maiden beloved: \n\t\t1. Character Healing Effectiveness +15% \n\t\t2. Using an Elemental Skill or Burst increases healing received by all party members by 20% for 10s..")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def barbaraConst():
    gleefulSongs = ["Constellation Lv. 1",
                    "Barbara regenerates 1 Energy every 10s."]
    vitalityBurst = ["Constellation Lv. 2",
                     "Decreases the CD of Let the Show Begin by 15%.",
                     "During the ability's duration, the current character gains 15% Hydro DMG Bonus."]
    starOfTomorrow = ["Constellation Lv. 3",
                      "Increases the Level of Shining Miracle by 3.",
                      "Maximum upgrade level is 15."]
    attentivenessBeMyPower = ["Constellation Lv. 4",
                              "Every enemy hit by Barbara's Charged Attack regenerates 1 Energy for her.",
                              "A maximum of 5 energy can be regenerated in this manner with any one Charged Attack."]
    thePurestCompanionship = ["Constellation Lv. 5",
                              "Increase the Level of Let the Show Begin by 3.",
                              "Maximum upgrade level is 15."]
    dedicatingEverythingToYou = ["Constellation Lv. 6",
                                 "When Barbara is not on the field, and the character in play falls she will automatically revive the character.",
                                 "Fully regenerates this characters HP by 100%.",
                                 "This effect can only occur once every 15 mins."]
    print("Barbara's Constellations:")
    print(" - Gleeful Songs")
    for i in enumerate(gleefulSongs, start=1):
        print("\t", *i, sep=". ")
    print("\n - Vitality Burst")
    for ii in enumerate(vitalityBurst, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Star of Tomorrow")
    for iii in enumerate(starOfTomorrow, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Attentiveness be My Power")
    for iv in enumerate(attentivenessBeMyPower, start=1):
        print("\t", *iv, sep=". ")
    print("\n - The Purest Companionship")
    for v in enumerate(thePurestCompanionship, start=1):
        print("\t", *v, sep=". ")
    print("\n - Dedicating Everything to You")
    for vi in enumerate(dedicatingEverythingToYou, start=1):
        print("\t", *vi, sep=". ")


def barbaraAbility():
    whisperOfWater = ["Normal Attack - Perform up to 4 water splashes attacks that deal Hydro DMG.",
                      "Charged Attack - Consumes a certain amount of Stamina to deal AoE Hydro DMG after a short casting time.",
                      "Plunging Attack - Gathering the might of Hydro, Barbara plunges towards the ground from mid-air, damaging all enemies in her path. Deals AoE Hydro DMG upon impact with the ground."]
    letTheShowBegin = ["Elemental Skill",
                       "Summons water droplets resembling musical notes that form a Melody Loop, dealing Hydro DMG to surrounding enemies and afflicting them with the Wet status."]
    melodyLoop = [
        "Barbara's Normal Attacks heal all party members and nearby allied characters for a certain amount of HP, which scales with Barbara's Max HP.",
        "Her Charged Attack generates 4 times the amount of healing.",
        "Regenerates a certain amount of the current character's HP at regular intervals.",
        "Applies the Wet status to the character and enemies who come in contact with them."]
    shiningMiracle = ["Elemental Burst",
                      "Heals friendly forces and all parties for a large amount of HP that scales with Barbara's Max HP."]
    gloriousSeason = ["Unlocked at Ascension 1",
                      "The Stamina Consumption of characters within Let the Show Begin's Melody Loop is reduced by 12%."]
    encore = ["Unlocked at Ascension 4",
              "When a character gains an Elemental Orb/Particle, the duration of Let the Show Begin's Melody Loop is extended by 1s.",
              "The maximum extension is 5s."]
    withMyWholeHeart = ["Unlocked Automatically",
                        "When a Perfect Cooking is achieved on a dish with restorative effects, there is a 12% chance to obtain double the product."]
    print("Skill Talents: ")
    print(" - Whisper of Water")
    for i in enumerate(whisperOfWater, start=1):
        print("\t", *i, sep=". ")
    print("\n - Let the Show Begin")
    for ii in enumerate(letTheShowBegin, start=1):
        print("\t", *ii, sep=". ")
    print("\n\t - Melody Loop")
    for iii in enumerate(melodyLoop, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Shining Miracle")
    for iv in enumerate(shiningMiracle, start=1):
        print("\t", *iv, sep=". ")
    print("\nPassive: ")
    print(" - Glorious Season")
    for v in enumerate(gloriousSeason, start=1):
        print("\t", *v, sep=". ")
    print("\n - Encore")
    for vi in enumerate(encore, start=1):
        print("\t", *vi, sep=". ")
    print("\n - With My Whole Heart")
    for vii in enumerate(withMyWholeHeart, start=1):
        print("\t", *vii, sep=". ")


def beidou():
    res = input("What kind of help do you need with Beidou? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return beidouBuild()
    elif res == "b":
        return beidouConst()
    elif res == "c":
        return beidouAbility()
    else:
        error()
        return beidou()


def beidouBuild():
    weapon = ["wolf's gravestone", "serpent spine"]
    altWeapon = ["luxurious sea-lord, sacrificial greatsword, favonius greatsword"]
    artifact = ["4x emblem of severed fate", "2x noblesse oblige, 2x thundering fury"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT Rate, CRIT DMG, ATK%, Energy Recharge"],
                     ["ATK%", "CRIT Rate, CRIT DMG, Elemental Mastery, Energy Recharge"],
                     ["Electro DMG Bonus%", "CRIT Rate, CRIT DMG, ATK%, Energy Recharge"],
                     ["CRIT Rate/CRIT DMG", "CRIT Rate/ CRIT DMG, ATK%, Elemental Mastery, Energy Recharge"]]
    print("Electro Sub-DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece emblem of severed fate: \n\t1. Energy Recharge +20% \n\t2. Increases Elemental Burst DMG by 25% of Energy Recharge. A maximum of 75% bonus DMG can be obtained in this way.")
    print(
        "\t- The 2 piece set will increase your electro damage by 15% and increase your elemental burst damage by 20%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def beidouConst():
    seaBeastsScourge = ["Constellation Lv. 1",
                        "When Stormbreaker is used: \n\t\t- Creates a shield that absorbs up to 16% of Beidou's Max HP for 15s. \n\t\t- This shield absorbs Electro DMG 250% more effectively."]
    turbulentSea = ["Constellation Lv. 2",
                    "Stormbreaker's arc lightning can jump 2 additional targets."]
    summonerOfStorm = ["Constellation Lv. 3",
                       "Increases the Level of Tidecaller by 3.",
                       "Maximum upgrade level is 15."]
    stunningRevenge = ["Constellation Lv. 4",
                       "Within 10s of taking DMG, Beidou's Normal Attacks gain 20% additional Electro DMG."]
    crimsonTidewalker = ["Constellation Lv. 5",
                         "Increase the Level of Stormbreaker by 3.",
                         "Maximum upgrade level is 15."]
    baneOfTheEvil = ["Constellation Lv. 6",
                     "During the duration of Stormbreaker, the Electro RES of surrounding enemies is decreased by 15%."]
    print("Beidou's Constellations:")
    print(" - Sea Beast's Scourge")
    for i in enumerate(seaBeastsScourge, start=1):
        print("\t", *i, sep=". ")
    print("\n - Upon the Turbulent Sea, the Thunder Arises")
    for ii in enumerate(turbulentSea, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Summoner of Storm")
    for iii in enumerate(summonerOfStorm, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Stunning Revenge")
    for iv in enumerate(stunningRevenge, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Crimson Tidewalker")
    for v in enumerate(crimsonTidewalker, start=1):
        print("\t", *v, sep=". ")
    print("\n - Bane of the Evil")
    for vi in enumerate(baneOfTheEvil, start=1):
        print("\t", *vi, sep=". ")


def beidouAbility():
    oceanborne = ["Normal Attack - Performs up to 5 successive strikes.",
                  "Charged Attack - Drains Stamina over time to perform continuous slashes. \n\t\t- At end of the sequence, perform a more powerful slash.",
                  "Plunging Attack - Plunges from mid-air to strike the ground, damaging enemies along the path and dealing AoE DMG upon impact."]
    pressTidecaller = ["Elemental Skill",
                       "Accumulating the power of lightning, Beidou swings her blade forward fiercely, dealing Electro DMG."]
    holdTidecaller = ["Lifts her weapon up as a shield. Max DMG absorbed scales off Beidou's Max HP.",
                      "Attacks using the energy stored within the greatsword upon release or once this ability's duration expires, dealing Electro DMG. DMG dealt scales with the number of times Beidou is attacked in the skill's duration. The greatest DMG Bonus will be attained once this effect is triggered twice.",
                      "The shield possesses the following properties: \n\t\t\t1. Has 250% Electro DMG Absorption Efficiency. \n\t\t\t2. Applies the Electro element to Beidou upon activation."]
    stormbreaker = ["Elemental Skill",
                    "Recalling her slaying of the great beast Haishan. Beidou calls upon that monstrous strength and the lightning to create a Thunderbeast's Targe around herself."]
    thunderbeastsTarget = ["Elemental Burst",
                           "When Normal and Charged Attacks hit, they create a lightning discharge that can jump between enemies, dealing Electro DMG.",
                           "Increases the character's resistance to interruption, and decreases DMG taken."]
    retribution = ["Unlocked at Ascension 1",
                   "Counterattacking with Tidecaller at the precise moment when the character is hit grants the maximum DMG Bonus."]
    lightningStorm = ["Unlocked at Ascension 4",
                      "Gain the following effects for 10s after unleashing Tidecaller with its maximum DMG Bonus: \n\t\t1. DMG dealt by Normal and Charged Attacks is increased by 15%. ATK SPD of Normal and Charged Attacks is increased by 15%. \n\t\t2. Greatly reduced delay before unleashing Charged Attacks."]
    conquerorOfTides = ["Unlocked Automatically",
                        "Decreases all party member's swimming Stamina consumption by 20%."]
    print("Skill Talents: ")
    print(" - Oceanborne")
    for i in enumerate(oceanborne, start=1):
        print("\t", *i, sep=". ")
    print("\n - Tidecaller")
    print("\t - Press:")
    for ii in enumerate(pressTidecaller, start=1):
        print("\t\t", *ii, sep=". ")
    print("\t - Hold:")
    for iii in enumerate(holdTidecaller, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Stormbreaker")
    for iv in enumerate(stormbreaker, start=1):
        print("\t", *iv, sep=". ")
    print("\t - Thunderbeast's Target")
    for v in enumerate(thunderbeastsTarget, start=1):
        print("\t\t", *v, sep=". ")
    print("\nPassive: ")
    print(" - Retribution")
    for vi in enumerate(retribution, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Lightning Storm")
    for vii in enumerate(lightningStorm, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Conqueror of Tides")
    for viii in enumerate(conquerorOfTides, start=1):
        print("\t", *viii, sep=". ")


def bennett():
    res = input(
        "What kind of help do you need with Bennett? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return bennettBuild()
    elif res == "b":
        return bennettConst()
    elif res == "c":
        return bennettAbility()
    else:
        error()
        return bennett()


def bennettBuild():
    weapon = ["skyward blade", "favonius sword"]
    altWeapon = ["sacrificial sword, festering desire"]
    artifact = ["4x noblesse oblige"]
    artifactStats = [["Flat ATK", "HP%, Energy Recharge, HP Flat, CRIT Damage/CRIT Rate"],
                     ["Flat HP", "HP%, Energy Recharge, CRIT Rate, CRIT Damage"],
                     ["HP%/Energy Recharge", "HP%/Energy Recharge, CRIT Damage, HP Flat, CRIT Rate"],
                     ["HP%", "Energy Recharge, HP Flat, CRIT Damage, CRIT Rate"],
                     ["Healing Bonus", "Energy Recharge, HP Flat, Healer, CRIT Rate/CRIT Damage"]]
    print("Pyro Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece nobless oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def bennettConst():
    grandExpectation = ["Constellation Lv. 1",
                        "Fantastic Voyage's ATK increases no longer has an HP restriction, and gains an additional 20% Base ATK."]
    impassConqueror = ["Constellation Lv. 2",
                       "When Bennett's HP falls below 70%, his Energy Recharge is increased by 30%."]
    unstoppableFervor = ["Constellation Lv. 3",
                         "Increases the Level of Passion Overload by 3.",
                         "Maximum upgrade level is 15."]
    unexpectedOdyssey = ["Constellation Lv. 4",
                         "Using a Normal Attack when executing the second attack of Passion Overload's Charge Level 1 allows an additional attack to be performed. This additional attack does 135% of the second attack's DMG."]
    trueExplorer = ["Constellation Lv. 5",
                    "Increase the Level of Fantastic Voyage by 3.",
                    "Maximum upgrade level is 15."]
    fireVenturesWithMe = ["Constellation Lv. 6",
                          "Sword, Claymore, or Polearm-wielding characters inside Fantastic Voyage's radius gain a 15% Pyro DMG Bonus. Normal and Charged Attacks now do Pyro DMG."]
    print("Bennett's Constellations:")
    print(" - Grand Expectation")
    for i in enumerate(grandExpectation, start=1):
        print("\t", *i, sep=". ")
    print("\n - Impasse Conqueror")
    for ii in enumerate(impassConqueror, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Unstoppable Fervor")
    for iii in enumerate(unstoppableFervor, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Unexpected Odyssey")
    for iv in enumerate(unexpectedOdyssey, start=1):
        print("\t", *iv, sep=". ")
    print("\n - True Explorer")
    for v in enumerate(trueExplorer, start=1):
        print("\t", *v, sep=". ")
    print("\n - Fire Ventures with Me")
    for vi in enumerate(fireVenturesWithMe, start=1):
        print("\t", *vi, sep=". ")


def bennettAbility():
    strikeOfFortune = ["Normal Attack - Perform up to 5 rapid strikes.",
                       "Charged Attack - Consumes a certain amount of Stamina to unleash 2 rapid sword swings.",
                       "Plunging Attack - Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    passionOverload = ["Elemental Skill",
                       "Bennett puts all his fire and passion for adventuring into his sword. Results may very based on how fired up he is."]
    pressPassionOverload = ["A single, swift flame strike that deals Pyro DMG."]
    holdPassionOverload = [
        "Charges up, resulting in different effects when unleashed based on the Charge Level.",
        "Level 1: Strikes twice, dealing Pyro DMG and launching enemies.",
        "Level 2: Unleashes 3 consecutive attacks that deal impressive Pyro DMG, but the last attack triggers an explosion that launches both Bennet and the enemy.",
        "Bennett takes no damage from being launched."]
    fantasticVoyage = [
        "Bennett leaps towards the enemy and performs a plunging attack, dealing Pyro DMG, creating an Inspiration Field."]
    inspirationField = ["Elemental Burst",
                        "If the health of a character in the circle is equal to or falls below 70%, their health will continuously regenerate. Regeneration scales based on Bennett's Max HP.",
                        "If the health of a character in the circle is higher than 70%, they gain an ATK Bonus that is based on Bennett's Base ATK.",
                        "Applies the Pyro element to characters within the Field."]
    rekindle = ["Unlocked at Ascension 1",
                "Decreases Passion Overload's CD by 20%."]
    fearnaught = ["Unlocked at Ascension 4",
                  "When inside the area created by Fantastic Voyage, Passion Overload takes on the following effects: \n\t\t1. CD is reduced by 50%. \n\t\t2. Bennett will not be launched by the effects of Charge Level 2."]
    itShouldBeSafe = ["Unlocked Automatically",
                      "When dispatched on an expedition in Mondstadt, time consumed is reduced by 25%."]

    print("Skill Talents: ")
    print(" - Strike of Fortune")
    for i in enumerate(strikeOfFortune, start=1):
        print("\t", *i, sep=". ")
    print("\n - Passion Overload")
    for ii in enumerate(passionOverload, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Press:")
    for iii in enumerate(pressPassionOverload, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Hold (short):")
    for iv in enumerate(holdPassionOverload, start=1):
        print("\t\t", *iv, sep=". ")
    print("\n - Fantastic Voyage")
    for v in enumerate(fantasticVoyage, start=1):
        print("\t", *v, sep=". ")
    print("\n - Inspiration Field")
    for vi in enumerate(inspirationField, start=1):
        print("\t\t", *vi, sep=". ")
    print("\nPassive: ")
    print(" - Rekindle")
    for vii in enumerate(rekindle, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Fearnaught")
    for viii in enumerate(fearnaught, start=1):
        print("\t", *viii, sep=". ")
    print("\n - It Should Be Safe...")
    for ix in enumerate(itShouldBeSafe, start=1):
        print("\t", *ix, sep=". ")


def chongyun():
    res = input(
        "What kind of help do you need with Chongyun? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return chongyunBuild()
    elif res == "b":
        return chongyunConst()
    elif res == "c":
        return chongyunAbility()
    else:
        error()
        return chongyun()


def chongyunBuild():
    weapon = ["skyward pride", "favonius greatsword"]
    altWeapon = ["prototype archaic"]
    artifact = ["4x noblesse oblige", "2x noblesse oblige, 2x blizzard strayer"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["ATK%", "CRIT Rate, CRIT DMG, Elemental Mastery, Energy Recharge"],
                     ["Cryo DMG Bonus%", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["CRIT Rate/CRIT DMG", "CRIT Rate/CRIT DMG, ATK%, Elemental Mastery, Energy Recharge"]]
    print("Cryo Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece nobless oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")
    print("\t- The 2 piece set will increase your cryo damage by 15% and increase your elemental burst damage by 20%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def chongyunConst():
    iceUnleashed = ["Constellation Lv. 1",
                    "The last attack of Chongyun's Normal Attack combo releases 3 ice blades. Each blade deals 50% of Chongyun's ATK as Cryo DMG to all enemies in its path."]
    atmosphericRevolution = ["Constellation Lv. 2",
                             "Elemental Skills and Elemental Bursts cast within the Frost Field created by Spirit Blade - Chongyun's Layered Frost have their CD time decreased by 15%."]
    cloudburst = ["Constellation Lv. 3",
                  "Increases the Level of Spirit Blade - Cloud-parting Star by 3.",
                  "Maximum upgrade level is 15."]
    frozenSkies = ["Constellation Lv. 4",
                   "Chongyun regenerates 1 Energy every time he hits an enemy affected by Cold or Frozen status effects.",
                   "This effect can only occur once every 2s."]
    theTruePath = ["Constellation Lv. 5",
                   "Increases the level of Spirit Blade - Chongyun's Layered Frost by 3.",
                   "Maximum upgrade level is 15."]
    rallyOfFourBlades = ["Constellation Lv. 6",
                         "Spirit Blade - Cloud-parting Star deals 15% more DMG to enemies with a lower percentage of their Max HP remaining than Chongyun.",
                         "This skill will also summon 1 additional spirt blade."]

    print("Chongyun's Constellations:")
    print(" - Ice Unleashed")
    for i in enumerate(iceUnleashed, start=1):
        print("\t", *i, sep=". ")
    print("\n - Atmospheric Revolution")
    for ii in enumerate(atmosphericRevolution, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Cloudburst")
    for iii in enumerate(cloudburst, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Frozen Skies")
    for iv in enumerate(frozenSkies, start=1):
        print("\t", *iv, sep=". ")
    print("\n - The True Path")
    for v in enumerate(theTruePath, start=1):
        print("\t", *v, sep=". ")
    print("\n - Rally of Four Blades")
    for vi in enumerate(rallyOfFourBlades, start=1):
        print("\t", *vi, sep=". ")


def chongyunAbility():
    demonBane = ["Normal Attack - Performs up to 4 consecutive strikes.",
                 "Charged Attack - Drains Stamina over time to perform continuous swirling attacks against all nearby enemies. At end of the sequence, perform a more powerful slash.",
                 "Plunging Attack - Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    chonghuasLayeredFrost = ["Elemental Skill",
                             "Chongyun strikes the ground with his greatsword, causing a Cryo explosion in a circular AoE in front of him that deals Cryo DMG.",
                             "After a short delay, the cold air created by the Cryo explosion will coalesce into a Chonghua Frost Field, within which all DMG done through Normal and Charged Attacks by Sword, Greatsword and Polearm-wielding characters will be converted to Cryo DMG."]
    cloudPartingStar = ["Elemental Burst",
                        "Performing the secret hand seals, Chongyun summons 3 giant spirit blades in mid-air that fall to the earth one by one after a short delay, exploding as they hit the ground.",
                        "When the spirit blades explode, they will deal AoE Cryo DMG and launch enemies."]
    steadyBreathing = ["Unlocked at Ascension 1",
                       "Sword, Claymore, or Polearm-wielding characters within the field created by Spirit Blade - Chonghua's Layered Frost have their Normal Attack SPD increased by 8%."]
    rimechaserBlade = ["Unlocked at Ascension 4",
                       "When the field created by Spirit Blade - Chonghua's Layered Frost disappears, another spirit will be summoned to strike nearby enemies, dealing 100% of Chonghua's Layered Frost's Skill DMG as AoE Cryo DMG. Enemies hit by this blade will have their Cryo RES decreased by 10% for 8s."]
    gallantJourney = ["Unlocked Automatically",
                      "When dispatched on an expedition in Liyue, time consumed is reduced by 25%."]

    print("Skill Talents: ")
    print(" - Demonbane")
    for i in enumerate(demonBane, start=1):
        print("\t", *i, sep=". ")
    print("\n - Spirit Blade - Chonghua's Layered Frost")
    for ii in enumerate(chonghuasLayeredFrost, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Spirit Blade - Cloud-Parting Star")
    for iii in enumerate(cloudPartingStar, start=1):
        print("\t", *iii, sep=". ")
    print("\nPassive: ")
    print(" - Steady Breathing:")
    for iv in enumerate(steadyBreathing, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Rimechaser Blade")
    for v in enumerate(rimechaserBlade, start=1):
        print("\t", *v, sep=". ")
    print("\n - Gallant Journey")
    for vi in enumerate(gallantJourney, start=1):
        print("\t", *vi, sep=". ")


def diluc():
    res = input("What kind of help do you need with Diluc? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return dilucBuild()
    elif res == "b":
        return dilucConst()
    elif res == "c":
        return dilucAbility()
    else:
        error()
        return diluc()


def dilucBuild():
    weapon = ["wolf's gravestone", "serpent spine"]
    altWeapon = ["skyward pride", "sacrificial greatsword"]
    artifact = ["4x crimson witch of flames"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["ATK%", "CRIT Rate, CRIT DMG, Elemental Mastery, Energy Recharge"],
                     ["Pyro DMG Bonus%", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["CRIT Rate/CRIT DMG", "CRIT Rate/CRIT DMG, ATK%, Elemental Mastery, Energy Recharge"]]
    print("Pyro DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece crimson witch of flames: \n\t1. Gain a 15% Pyro DMG Bonus \n\t2. Increases Overloaded and Burning DMG by 40%. Increases Vaporize and Melt DMG by 15%. Using an Elemental Skill increases 2-Piece Set effects by 50% for 10s. Max 3 stacks")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def dilucConst():
    conviction = ["Constellation Lv. 1",
                  "Diluc deals 15% more DMG to enemies whose HP is above 50%."]
    searingEmber = ["Constellation Lv. 2",
                    "When Diluc takes DMG, his Base ATK increases by 10% and his ATK SPD increases by 5%. Lasts for 10s.",
                    "This effect can stack up to 3 times and can only occur once every 1.5s."]
    fireAndSteel = ["Constellation Lv. 3",
                    "Increases the Level of Searing Onslaught by 3.",
                    "Maximum upgrade level is 15."]
    flowingFlame = ["Constellation Lv. 4",
                    "Casting Searing Onslaught in sequence greatly increases damage dealt.",
                    "Within 2s of using Searing Onslaught, casting the next Searing Onslaught in the combo deals 40% additional DMG. This effect lasts for the next 2s."]
    phoenix = ["Constellation Lv. 5",
               "Increases the level of Dawn by 3.",
               "Maximum upgrade level is 15."]
    flamingSword = ["Constellation Lv. 6",
                    "After casting Searing Onslaught, the next 2 Normal Attacks within the next 6s will have their DMG and ATK SPD increased by 30%.",
                    "Additionally, Searing Onslaught will not interrupt the Normal Attack combo."]

    print("Diluc's Constellations:")
    print(" - Conviction")
    for i in enumerate(conviction, start=1):
        print("\t", *i, sep=". ")
    print("\n - Searing Ember")
    for ii in enumerate(searingEmber, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Fire and Steel")
    for iii in enumerate(fireAndSteel, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Flowing Flame")
    for iv in enumerate(flowingFlame, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Phoenix, Harbinger of Dawn")
    for v in enumerate(phoenix, start=1):
        print("\t", *v, sep=". ")
    print("\n - Flaming Sword, Nemesis of Dark")
    for vi in enumerate(flamingSword, start=1):
        print("\t", *vi, sep=". ")


def dilucAbility():
    temperedSword = ["Normal Attack - Performs up to 4 consecutive strikes.",
                     "Charged Attack - Drains Stamina over time to perform continuous slashes. At end of the sequence, perform a more powerful slash.",
                     "Plunging Attack - Plunges from mid-air to strike the ground, damaging enemies along the path and dealing AoE DMG upon impact."]
    searingOnslaught = ["Elemental Skill",
                        "Performs a forward slash that deals Pyro DMG.",
                        "This skill can be used 3 times consecutively. Enters CD if not cast again within a short period."]
    dawn = ["Elemental Burst",
            "Releases intense flames to knock nearby enemies back, dealing Pyro DMG. The flames then converge into the weapon, summoning a Phoenix that flies forward and deals massive Pyro DMG to all enemies in its path. The Phoenix explodes upon reaching its destination, causing a large amount of AoE Pyro DMG.",
            "The searing flames that run down his blade cause Diluc's Normal and Charged Attacks to deal Pyro DMG for a time."]
    relentless = ["Unlocked at Ascension 1",
                  "Diluc's Charged Attack Stamina Cost is decreased by 50%, and its duration is increased by 3s."]
    blessingOfPhoenix = ["Unlocked at Ascension 4",
                         "The Pyro Enchantment provided by Dawn lasts for 4s longer.",
                         "Additionally, Diluc gains 20% Pyro DMG Bonus during the duration of this effect."]
    traditionOfTheDawnKnight = [
        "Refunds 15% of the ores used when crafting Claymore-type weapons."]

    print("Skill Talents: ")
    print(" - Tempered Sword")
    for i in enumerate(temperedSword, start=1):
        print("\t", *i, sep=". ")
    print("\n - Searing Onslaught")
    for ii in enumerate(searingOnslaught, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Dawn")
    for iii in enumerate(dawn, start=1):
        print("\t", *iii, sep=". ")
    print("\nPassive: ")
    print(" - Relentless:")
    for iv in enumerate(relentless, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Blessing of Phoenix")
    for v in enumerate(blessingOfPhoenix, start=1):
        print("\t", *v, sep=". ")
    print("\n - Tradition of the Dawn Knight")
    for vi in enumerate(traditionOfTheDawnKnight, start=1):
        print("\t", *vi, sep=". ")


def diona():
    res = input("What kind of help do you need with Diona? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return dionaBuild()
    elif res == "b":
        return dionaConst()
    elif res == "c":
        return dionaAbility()
    else:
        error()
        return diona()


def dionaBuild():
    weapon = ["sacrificial bow", "favonius warbow"]
    altWeapon = ["skyward pride", "sacrificial greatsword"]
    artifact = ["4x maiden beloved", "4x noblesse oblige"]
    artifactStats = [["Flat ATK", "HP%, Energy Recharge, HP Flat, Elemental Mastery / DEF"],
                     ["Flat HP", "HP%, Energy Recharge, Elemental Mastery, DEF"],
                     ["HP%", "CRIT DMG, CRIT Rate, Energy Recharge, ATK%"],
                     ["HP%", "Flat HP, Energy Recharge, Elemental Mastery, DEF"],
                     ["Healing Bonus/HP%", "HP%/Elemental Mastery, Flat HP, ATK%, Energy Recharge"]]
    print("Cryo Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece maiden beloved: \n\t1. Character Healing Effectiveness +15% \n\t2. Using an Elemental Skill or Burst increases healing received by all party members by 20% for 10s.")
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")
    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def dionaConst():
    aLingeringFlavor = ["Constellation Lv. 1",
                        "Regenerates 15 Energy for Diona after the effects of Signature Mix end."]
    shaken = ["Constellation Lv. 2",
              "Increases Icy Paws' DMG by 15%, and increases its shield's DMG Absorption by 15%.",
              "Additionally, when paws hit their targets, creates a shield for other nearby characters on the field with 50% of the Icy Paws shield's DMG Absorption for 5s."]
    anotherRound = ["Constellation Lv. 3",
                    "Increases the Level of Signature Mix by 3.",
                    "Maximum upgrade level is 15."]
    wineIndustrySlayer = ["Constellation Lv. 4",
                          "Within the radius of Signature Mix, Diona's charge time for aimed shots is reduced by 60%."]
    doubleShot = ["Constellation Lv. 5",
                  "Increases the level of Icy Paws by 3.",
                  "Maximum upgrade level is 15."]
    catsTailClosingTime = ["Constellation Lv. 6",
                           "Characters within Signature Mix's radius will gain the following effects based on their HP amounts: \n\t 1. Increasing Incoming Healing Bonus by 30% when HP falls below or is equal to 50%. \n\t 2. Elemental Mastery is increased by 200 when HP is above 50%."]

    print("Diona's Constellations:")
    print(" - A Lingering Flavor")
    for i in enumerate(aLingeringFlavor, start=1):
        print("\t", *i, sep=". ")
    print("\n - Shaken, Not Purred")
    for ii in enumerate(shaken, start=1):
        print("\t", *ii, sep=". ")
    print("\n - A-Another Round?")
    for iii in enumerate(anotherRound, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Wine Industry Slayer")
    for iv in enumerate(wineIndustrySlayer, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Double Shot, On The Rocks")
    for v in enumerate(doubleShot, start=1):
        print("\t", *v, sep=". ")
    print("\n - Cat's Tail Closing Time")
    for vi in enumerate(catsTailClosingTime, start=1):
        print("\t", *vi, sep=". ")


def dionaAbility():
    katzleinStyle = ["Normal Attack - Performs up to 5 consecutive shots with a bow.",
                     "Charged Attack - Perform a more precise Aimed Shot with increased DMG. While aiming, biting frost accumulates on the arrowhead. A fully charged frost arrow will deal Cryo DMG.",
                     "Plunging Attack - Fires off a shower of arrows in mid-air before falling and striking the ground, dealing AoE DMG upon impact."]
    icyPaws = ["Elemental Skill",
               "Fires an Icy Paw that deals Cryo DMG to opponents and forms a shield on hit. The shield's DMG Absorption scales based on Diona's Max HP, and its duration scales off the number of Icy Paws that hit their target."]
    pressIcyPaws = ["Rapidly fires off 2 Icy Paws."]
    holdIcyPaws = [
        "Dashes back quickly before firing five Icy Paws.",
        "The shield created by a Hold attack will gain a 75% DMG Absorption Bonus.",
        "The shield has a 250% Cryo DMG Absorption Bonus, and will cause your active character to become affected by Cryo at the point of formation for a short duration."]
    signatureMix = ["Elemental Burst",
                    "Tosses out a special cold brew that deals AoE Cryo DMG and creates a Drunken Mist in an AoE."]
    drunkenMist = ["Deals continuous Cryo DMG to opponents within the AoE.",
                   "Continuously regenerates the HP of characters within the AoE."]
    catsTailSecretMenu = ["Unlocked at Ascension 1",
                          "Characters shielded by Icy Paws have their Movement SPD increased by 10% and their Stamina",
                          "Consumption decreased by 10%."]
    drunkardsFarce = ["Unlocked at Ascension 4",
                      "Opponents who enter the AoE of Signature Mix have 10% decreased ATK for 15s."]
    complimentaryBarFood = ["Unlocked Automatically",
                            "When a Perfect Cooking is achieved on a dish with restorative effects, there is a 12% chance to obtain double the product."]

    print("Skill Talents: ")
    print(" - Katzlein Style")
    for i in enumerate(katzleinStyle, start=1):
        print("\t", *i, sep=". ")
    print("\n - Icy Paws")
    for ii in enumerate(icyPaws, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Press:")
    for iii in enumerate(pressIcyPaws, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Hold:")
    for iv in enumerate(holdIcyPaws, start=1):
        print("\t\t", *iv, sep=". ")
    print("\n - Signature Mix")
    for v in enumerate(signatureMix, start=1):
        print("\t", *v, sep=". ")
    print("\n - Drunken Mist")
    for vi in enumerate(drunkenMist, start=1):
        print("\t\t", *vi, sep=". ")
    print("\nPassive: ")
    print(" - Cat's Tail Secret Menu")
    for vii in enumerate(catsTailSecretMenu, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Drunkards' Farce")
    for viii in enumerate(drunkardsFarce, start=1):
        print("\t", *viii, sep=". ")
    print("\n - Complimentary Bar Food")
    for ix in enumerate(complimentaryBarFood, start=1):
        print("\t", *ix, sep=". ")


def eula():
    res = input("What kind of help do you need with Eula? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return eulaBuild()
    elif res == "b":
        return eulaConst()
    elif res == "c":
        return eulaAbility()
    else:
        error()
        return eula()


def eulaBuild():
    weapon = ["song of broken pines", "serpent spine"]
    altWeapon = ["wolf's gravestone", "snow-tombed starsilver"]
    artifact = ["4x pale flame", "2x pale flame, 2x bloodstained chivalry"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Energy Recharge"],
                     ["Physical DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, HP%, ATK%, Energy Recharge"]]
    print("Physical DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece pale flame: \n\t1.Physical DMG +25% \n\t2. When an Elemental Skill hits an opponent, ATK is increased by 9% for 7s. This effect stacks up to 2 times and can be triggered once every 0.3s. Once 2 stacks are reached, the 2-set effect is increased by 100%.")
    print("\t- The 2 piece set will increase your Physical DMG +50%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def eulaConst():
    tidalIllusion = ["Constellation Lv. 1",
                     "Every time Icetide Vortex's Grimheart stacks are consumed, Eula's Physical DMG is increased by 30% for 6s.",
                     "Each stack consumed will increase the duration of this effect by 6s up to a maximum of 18s."]
    ladyOfSeafoam = ["Constellation Lv. 2",
                     "Decreases the CD of Icetide Vortex's Holding Mode, rendering it identical to Tapping CD."]
    lawrencePedigree = ["Constellation Lv. 3",
                        "Increases the Level of Glacial Illumination by 3.",
                        "Maximum upgrade level is 15."]
    theObstinacyOfOnesInferiors = ["Constellation Lv. 4",
                                   "Lightfall Swords deal 25% increased DMG against opponents with less than 50% HP."]
    chivalricQuality = ["Constellation Lv. 5",
                        "Increases the Level of Icetide Vortex by 3.",
                        "Maximum upgrade level is 15."]
    nobleObligation = ["Constellation Lv. 6",
                       "Lightfall Swords created by Glacial Illumination start with 5 stacks of energy. Normal Attacks, Elemental Skills, and Elemental Bursts have a 50% chance to grant the Lightning Sword an additional stack of energy."]

    print("Eula's Constellations:")
    print(" - Tidal Illusion")
    for i in enumerate(tidalIllusion, start=1):
        print("\t", *i, sep=". ")
    print("\n - Lady of Seafoam")
    for ii in enumerate(ladyOfSeafoam, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Lawrence Pedigree")
    for iii in enumerate(lawrencePedigree, start=1):
        print("\t", *iii, sep=". ")
    print("\n - The Obstinacy of One's Inferiors")
    for iv in enumerate(theObstinacyOfOnesInferiors, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Chivalric Quality")
    for v in enumerate(chivalricQuality, start=1):
        print("\t", *v, sep=". ")
    print("\n - Noble Obligation")
    for vi in enumerate(nobleObligation, start=1):
        print("\t", *vi, sep=". ")


def eulaAbility():
    edel = ["Normal Attack - Perform up to 5 consecutive strikes.",
            "Charged Attack - Drains Stamina over time to perform continuous slashes. At the end of the sequence, perform a more powerful slash.",
            "Plunging Attack - Plunges from mid-air to strike the ground, damaging opponents along the path and dealing AoE DMG upon impact."]
    pressIcetideVortex = ["Elemental Skill",
                          "Slashes swiftly, dealing Cryo DMG. When it hits an opponent, Eula gains a stack of Grimheart that stacks up to two times. These stats can only be gained once every 0.3s."]
    grimHeartIcetideVortex = ["Increases Eula's resistance to interruption and DEF."]
    holdIcetideVortex = ["Elemental Skill",
                         "Wielding her sword, Eula consumes all the stacks of Grimheart and lashes forward, dealing AoE Cryo DMG to opponents in front of her.",
                         "If Grimheart stacks are consumed, surrounding opponents will have their Physical RES and Cryo RES decreased.",
                         "Each consumed stack of Grimheart will be converted into an Icewhirl Brand that deals Cryo DMG to nearby opponents."]
    glacialIllumination = ["Elemental Burst",
                           "Brandishes her greatsword, dealing Cryo DMG to nearby opponents and creating a Lightfall Sword that follows her around for a duration of up to 7s.",
                           "While present, the Lightfall Sword increases Eula's resistance to interruption. When Eula's own Normal Attack, Elemental Skill, and Elemental Burst deal DMG to opponents, they will charge the Lightfall Sword, which can gain an energy stack once every 0.1s.",
                           "Once its duration ends, the Lightfall Sword will descend and explode violently, dealing Physical DMG to nearby opponents.",
                           "This DMG scales on the number of energy stacks the Lightfall Sword has accumulated. If Eula leaves the field, the Lightfall Sword will immediately explode."]
    roilingRime = ["Unlocked at Ascension 1",
                   "If 2 stacks of Grimheart are consumed upon unleashing the Holding Mode of Icetide Vortex, a Shattered Lightfall Sword will be created that will explode immediately, dealing 50% of the basic Physical DMG dealt by a Lightfall Sword created by Glacial Illumination."]
    wellSpringOfWarLust = ["Unlocked at Ascension 4",
                           "When Glacial Illumination is cast, the CD of Icetide Vortex is reset and Eula gains 1 stack of Grimheart."]
    aristocraticIntrospection = ["Unlocked Automatically",
                                 "When Eula crafts Character Talent Materials, she has a 10% chance to receive double the product."]

    print("Skill Talents: ")
    print(" - Favonius Bladework - Edel")
    for i in enumerate(edel, start=1):
        print("\t", *i, sep=". ")
    print("\n - Icetide Vortex")
    print("\t - Press:")
    for ii in enumerate(pressIcetideVortex, start=1):
        print("\t\t", *ii, sep=". ")
    print("\t - Grimheart:")
    for iii in enumerate(grimHeartIcetideVortex, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Hold:")
    for iv in enumerate(holdIcetideVortex, start=1):
        print("\t\t", *iv, sep=". ")
    print("\n - Glacial Illumination")
    for v in enumerate(glacialIllumination, start=1):
        print("\t", *v, sep=". ")
    print("\nPassive: ")
    print(" - Roiling Rime")
    for vi in enumerate(roilingRime, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Wellspring of War-Lust")
    for vii in enumerate(wellSpringOfWarLust, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Aristocratic Introspection")
    for viii in enumerate(aristocraticIntrospection, start=1):
        print("\t", *viii, sep=". ")


def fischl():
    res = input("What kind of help do you need with Fischl? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return fischlBuild()
    elif res == "b":
        return fischlConst()
    elif res == "c":
        return fischlAbility()
    else:
        error()
        return fischl()


def fischlBuild():
    weapon = ["skyward harp", "elegy for the end"]
    altWeapon = ["the stringless", "favonius warbow"]
    artifact = ["4x thundersoother", "2x gladiator's finale, 2x thundering fury"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Energy Recharge"],
                     ["Electro DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Elemental Mastery, Energy Recharge"]]
    print("Electric Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece thundersoother: \n\t1.Electro RES increased by 40% \n\t2. Increases DMG against enemies affected by Electro by 35%.")
    print("\t- The 2 piece set will increase your electro damage by 15% and increase your ATK +18%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def fischlConst():
    gazeOfTheDeep = ["Constellation Lv. 1",
                     "Even when Oz is not present in combat, he can still watch over Fischl through his raven eyes. When Fischl attacks an enemy, Oz fires a joint attack, dealing 22% of ATK DMG."]
    devourerOfAllSins = ["Constellation Lv. 2",
                         "When Nightrider is used, it deals an additional 200% ATK as DMG, and its AoE is increased by 50%."]
    wingsOfNightmare = ["Constellation Lv. 3",
                        "Increases the Level of Nightrider by 3.",
                        "Maximum upgrade level is 15."]
    herPilgrimageOfBleak = ["Constellation Lv. 4",
                            "When Midnight Phatasmagoria is used, it deals 222% of ATK as Electro DMG to surrounding enemies.",
                            "When the skill duration ends, Fischl regenerates 20% of her HP."]
    againstTheFleeingLight = ["Constellation Lv. 5",
                              "Increase the Level of Midnight Phantasmagoria by 3.",
                              "Maximum upgrade level is 15."]
    evernightRaven = ["Constellation Lv. 6",
                      "Increases the duration of Oz's summoning by 2s. Additionally, Oz attacks with the current character when present, dealing 30% of Fischl's ATK as Electro DMG."]

    print("Fischl's Constellations:")
    print(" - Gaze of the Deep")
    for i in enumerate(gazeOfTheDeep, start=1):
        print("\t", *i, sep=". ")
    print("\n - Devourer of All Sins")
    for ii in enumerate(devourerOfAllSins, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Wings of Nightmare")
    for iii in enumerate(wingsOfNightmare, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Her Pilgrimage of Bleak")
    for iv in enumerate(herPilgrimageOfBleak, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Against the Fleeing Light")
    for v in enumerate(againstTheFleeingLight, start=1):
        print("\t", *v, sep=". ")
    print("\n - Evernight Raven")
    for vi in enumerate(evernightRaven, start=1):
        print("\t", *vi, sep=". ")


def fischlAbility():
    boltsOfDownfall = ["Normal Attack - Performs up to 5 consecutive shots with a bow.",
                       "Charged Attack - Perform a more precise Aimed Shot with increased DMG. While aiming, the dark lightning spirits of Immernachtreich shall heed the call of their Prinzessin and indwell the enchanted arrowhead. When fully indwelt, the Rachsuchtig Blitz shall deal immense Electro DMG.",
                       "Plunging Attack - Fires off a shower of arrows in mid-air before falling and striking the ground, dealing AoE DMG upon impact."]
    nightrider = ["Elemental Skill",
                  "Summons Oz, the night raven forged of darkness and lightning descends upon the land, dealing Electro DMG in a small AoE.",
                  "For the ability's duration, Oz will continuously attack nearby enemies with Freikugel.",
                  "Hold to adjust the location Oz will be summoned to.",
                  "\t Press again any time during the ability's duration to once again summon him to Fischl's side."]
    midnightPhantasmagoria = ["Elemental Burst",
                              "Summons Oz to spread his twin swings of twilight and defend Fischl. Has the following properties during the ability's duration: \n\t\t1. Fischl takes on Oz's form, greatly increasing her Movement Speed. \n\t\t2. Strikes nearby enemies with lightning, dealing Electro DMG to enemies she comes into contact with. Each enemy can only be struck once. \n\t\t3. Once this ability's effects end, Oz will remain on the battlefield and attack his Prinzessin's foes. If Oz is already on the field, then this will reset the duration of his presence."]
    stellarPredator = ["Unlocked at Ascension 1",
                       "When Fischl hits Oz with a fully-charged Aimed Shot, Oz brings down Thundering Retribution, dealing AoE Electro DMG equal to 152.7% of the arrow's DMG."]
    undoneBeThySinfulHex = ["Unlocked at Ascension 4",
                            "If a character triggers an Electro-related Elemental Reaction when Oz is on the field, the enemy shall be stricken with Thundering Retribution, dealing Electro DMG equal to 80% of Fischl's ATK."]
    meinHausgarten = ["Unlocked Automatically",
                      "When dispatched on an expedition in Mondstadt, time consumed is reduced by 25%."]

    print("Skill Talents: ")
    print(" - Bolts of Downfall")
    for i in enumerate(boltsOfDownfall, start=1):
        print("\t", *i, sep=". ")
    print("\n - Nightrider")
    for ii in enumerate(nightrider, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Midnight Phantasmagoria")
    for iii in enumerate(midnightPhantasmagoria, start=1):
        print("\t", *iii, sep=". ")
    print("\nPassive: ")
    print(" - Stellar Predator")
    for iv in enumerate(stellarPredator, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Undone Be Thy Sinful Hex")
    for v in enumerate(undoneBeThySinfulHex, start=1):
        print("\t", *v, sep=". ")
    print("\n - Mein Hausgarten")
    for vi in enumerate(meinHausgarten, start=1):
        print("\t", *vi, sep=". ")


def ganyu():
    res = input("What kind of help do you need with Ganyu? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return ganyuBuild()
    elif res == "b":
        return ganyuConst()
    elif res == "c":
        return ganyuAbility()
    else:
        error()
        return ganyu()


def ganyuBuild():
    weapon = ["amos' bow", "skyward harp"]
    altWeapon = ["prototype crescent", "blackcliff warbow"]
    artifact = ["4x wanerderer's troupe", "2x gladiator's finale, 2x blizzard strayer"]
    artifactStats = [["Flat ATK", "ATK%, CRIT DMG, Elemental Mastery, CRIT Rate"],
                     ["Flat HP", "ATK%, CRIT DMG, CRIT Rate, Elemental Mastery"],
                     ["ATK%", "CRIT DMG, Energy Recharge, Elemental Mastery, CRIT Rate"],
                     ["Cryo DMG Bonus%", "ATK%, CRIT DMG, CRIT Rate, Energy Recharge / Elemental Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT Rate/CRIT DMG, ATK%, Energy Recharge, Elemental Mastery"]]
    print("Cryo DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece wanderer's troupe: \n\t1. Elemental Mastery +80 \n\t2. Increases Charged Attack DMG by 35% if the character uses a Catalyst or Bow.")
    print("\t- The 2 piece set will increase your cryo damage by 15% and increase your ATK +18%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def ganyuConst():
    dewDrinker = ["Constellation Lv. 1",
                  "Taking DMG from a Charge Level 2 Frostflake Arrow Bloom decreases opponents' Cryo RES by 15% for 6s.",
                  "A hit regenerates 2 Energy for Ganyu. This effect can only occur once per Charge Level 2 Frostflake Arrow, regardless if Frostflake Arrow itself or its Bloom hit the target."]
    theAuspicious = ["Constellation Lv. 2",
                     "Trail of the Qilin gains 1 additional charge."]
    cloudStrider = ["Constellation Lv. 3",
                    "Increases the level of Celestial Shower by 3.",
                    "Maximum upgrade level is 15."]
    westwardSojourn = ["Constellation Lv. 4",
                       "Opponents standing within the AoE of Celestial Shower take increased DMG. This effect strengthens over time.",
                       "Increased DMG taken begins at 5% and increases by 5% every 3s, up to a maximum of 25%.",
                       "The effect lingers for 3s after the opponent leaves the AoE."]
    theMerciful = ["Constellation Lv. 5",
                   "Increases the level of Trail of the Qilin by 3.",
                   "Maximum upgrade level is 15."]
    theClement = ["Constellation Lv. 6",
                  "Using Trail of the Qilin causes the next Frostflake Arrow shot within 30s to not require charging."]

    print("Ganyu's Constellations:")
    print(" - Dew-Drinker")
    for i in enumerate(dewDrinker, start=1):
        print("\t", *i, sep=". ")
    print("\n - The Auspicious")
    for ii in enumerate(theAuspicious, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Cloud-Strider")
    for iii in enumerate(cloudStrider, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Westward Sojourn")
    for iv in enumerate(westwardSojourn, start=1):
        print("\t", *iv, sep=". ")
    print("\n - The Merciful")
    for v in enumerate(theMerciful, start=1):
        print("\t", *v, sep=". ")
    print("\n - The Clement")
    for vi in enumerate(theClement, start=1):
        print("\t", *vi, sep=". ")


def ganyuAbility():
    liutianArchery = ["Normal Attack - Performs up to 6 consecutive shots with a bow.",
                      "Charged Attack - Perform a more precise Aimed Shot with increased DMG. While aiming, an icy aura will accumulate on the arrowhead before the arrow is fired. Has different effects based on how long the energy has been charged: \n\t1. Charge Level 1: Fires off an icy arrow that deals Cryo DMG. \n\t2. Charge Level 2: Fires off a Frostflake Arrow that deals Cryo DMG. The Frostflake Arrow blooms after hitting its target, dealing AoE Cryo DMG.",
                      "Plunging Attack - Fires off a shower of arrows in mid-air before falling and striking the ground, dealing AoE DMG upon impact."]
    trailOfTheQilin = ["Elemental Skill",
                       "Leaving a single Ice Lotus behind, Ganyu dashes backward, shunning all impurity and dealing AoE Cryo DMG."]
    iceLotus = ["Continuously taunts surrounding opponents, attracting them to attack it.",
                "Endurance scales based on Ganyu's Max HP.",
                "Blooms profusely when destroyed or once its duration ends, dealing AoE Cryo DMG."]
    celestialShower = ["Elemental Burst",
                       "Coalesces atmospheric frost and snow to summon a Sacred Cryo Pearl that exorcises evil.",
                       "During its ability duration, the Sacred Cryo Pearl will continuously rain down shards of ice, striking opponents within an AoE and dealing Cryo DMG."]
    undividedHeart = ["Unlocked at Ascension 1",
                      "After firing a Frostflake Arrow, the CRIT Rate of subsequent Frostflake Arrows and their resulting bloom effects is increased by 20% for 5s."]
    harmonyBetweenHeavenAndEarth = ["Unlocked at Ascension 4",
                                    "Celestial Shower grants a 20% Cryo DMG Bonus to active party members in the AoE."]
    preservedForTheHunt = ["Unlocked Automatically",
                           "Refunds 15% of the ores used when crafting Bow-type weapons."]

    print("Skill Talents: ")
    print(" - Liutian Archery")
    for i in enumerate(liutianArchery, start=1):
        print("\t", *i, sep=". ")
    print("\n - Trail of the Qilin")
    for ii in enumerate(trailOfTheQilin, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Ice Lotus:")
    for iii in enumerate(iceLotus, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Celestial Shower:")
    for iv in enumerate(celestialShower, start=1):
        print("\t", *iv, sep=". ")
    print("\nPassive: ")
    print(" - Undivided Heart")
    for v in enumerate(undividedHeart, start=1):
        print("\t", *v, sep=". ")
    print("\n - Harmony between Heaven and Earth")
    for vi in enumerate(harmonyBetweenHeavenAndEarth, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Preserved for the Hunt")
    for vii in enumerate(preservedForTheHunt, start=1):
        print("\t", *vii, sep=". ")


def hutao():
    res = input("What kind of help do you need with Hu Tao? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return hutaoBuild()
    elif res == "b":
        return hutaoConst()
    elif res == "c":
        return hutaoAbility()
    else:
        error()
        return hutao()


def hutaoBuild():
    weapon = ["staff of homa", "primordial jade winged-spear"]
    altWeapon = ["deathmatch", "blackcliff pole"]
    artifact = ["4x crimson witch of flame", "4x shimenawa's reminiscence"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, HP%"],
                     ["Flat HP", "CRIT Rate, CRIT DMG, ATK%, HP%"],
                     ["HP%", "CRIT Rate, CRIT DMG, ATK%, HP Flat"],
                     ["Pyro DMG Bonus%", "CRIT Rate, CRIT DMG, ATK%, HP%"],
                     ["CRIT DMG/CRIT Rate", "CRIT Rate/CRIT DMG, ATK%, HP%, HP Flat"]]
    print("Pyro DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece crimson witch of flame: \n\t1. Gain a 15% Pyro DMG Bonus. \n\t2. Increases Overloaded and Burning DMG by 40%. Increases Vaporize and Melt DMG by 15%. Using an Elemental Skill increases 2-Piece Set effects by 50% for 10s. Max 3 stacks.")
    print(
        "\t- The 4 piece shimenawa's reminiscence: \n\t1. ATK +18% \n\t2. When casting an Elemental Skill, if the character has 15 or more Energy, they lose 15 Energy and Normal/Charged/Plunging Attack DMG is increased by 50% for 10s. This effect will not trigger again during that duration.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def hutaoConst():
    crimsonBouquet = ["Constellation Lv. 1",
                      "While in a Paramita Bouquet state activated by Guide to Afterlife, Hu Tao's Charge Attacks do not consume Stamina."]
    ominousRainfall = ["Constellation Lv. 2",
                       "Increases the Blood Blossom DMG by an amount equal to 10% of Hu Tao's Max HP at the time the effect is applied.",
                       "Additionally, Spirit Soother will also apply the Blood Blossom effect."]
    lingeringCarmine = ["Constellation Lv. 3",
                        "Increases the level of Guide to Afterlife by 3.",
                        "Maximum upgrade level is 15."]
    gardenOfEternalRest = ["Constellation Lv. 4",
                           "Upon defeating an enemy affected by a Blood Blossom that Hu Tao applied herself, all nearby allies in the party (excluding Hu Tao herself) will have their CRIT rate increased by 12% for 15s."]
    floralIncense = ["Constellation Lv. 5",
                     "Increases the level of Spirit Soother by 3.",
                     "Maximum upgrade level is 15."]
    butterflysEmbrace = ["Constellation Lv. 6",
                         "Triggers when Hu Tao's HP drops below 25%, or when she suffers a lethal strike: \n\t\t1. Hu Tao will not fall as a result of the DMG sustained.",
                         "Additionally, for the next 10s, all of her Elemental and Physical RES is increased by 200%, her CRIT Rate is increased by 100%, and her resistance to interruption is greatly increased.",
                         "This effect triggers automatically when Hu Tao has 1 HP left.",
                         "Can only occur once every 60s."]

    print("Hu Tao's Constellations:")
    print(" - Crimson Bouquet")
    for i in enumerate(crimsonBouquet, start=1):
        print("\t", *i, sep=". ")
    print("\n - Ominous Rainfall")
    for ii in enumerate(ominousRainfall, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Lingering Carmine")
    for iii in enumerate(lingeringCarmine, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Garden of Eternal Rest")
    for iv in enumerate(gardenOfEternalRest, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Floral Incense")
    for v in enumerate(floralIncense, start=1):
        print("\t", *v, sep=". ")
    print("\n - Butterfly's Embrace")
    for vi in enumerate(butterflysEmbrace, start=1):
        print("\t", *vi, sep=". ")


def hutaoAbility():
    secretSpearOfWangsheng = ["Normal Attack - Performs up to 6 consecutive spear strikes.",
                              "Charged Attack -  Consumes a certain amount of Stamina to lunge forward, dealing damage to enemies along the way.",
                              "Plunging Attack - Plunges from mid-air to strike the ground, damaging enemies along the path and dealing AoE DMG upon impact."]
    guideToAfterlife = ["Elemental Skill",
                        "Hu Tao consumes a portion of her HP to knock the surrounding enemies back and enter the Paramita Papilio state."]
    paramitaPapilio = [
        "Increases Hu Tao's ATK based on her Max HP at the time of entering this state. ATK Bonus gained this way cannot exceed 400% of Hu Tao's Base ATK.",
        "Converts attack DMG to Pyro DMG, which cannot be overridden by any other elemental infusion.",
        "Charged attacks apply the Blood Blossom effect to the enemies hit.",
        "Increases Hu Tao's resistance to interruption."]
    bloodBlossom = [
        "Enemies affected by Blood Blossom will take Pyro DMG every 4s. This DMG is considered Elemental Skill DMG.",
        "Each enemy can be affected by only one Blood Blossom effect at a time, and its duration may only be refreshed by Hu Tao herself.",
        "Paramita Papilio ends when its duration is over, or Hu Tao has left the battlefield or fallen."]
    spiritSoother = ["Elemental Burst",
                     "Commands a blazing spirit to attack, dealing Pyro DMG in a large AoE.",
                     "Upon striking the enemy, regenerates a percentage of Hu Tao's Max HP. This effect can be triggered up to 5 times, based on the number of enemies hit.",
                     "If Hu Tao's HP is below or equal to 50% when the enemy is hit, both the DMG and HP Regeneration are increased."]
    flutterBy = ["Unlocked at Ascension 1",
                 "When a Paramita Papilio state activated by Guide to Afterlife ends, all allies in the party (excluding Hu Tao herself) will have their CRIT Rate increased by 12% for 8s."]
    sanguineRouge = ["Unlocked at Ascension 4",
                     "When Hu Tao's HP is equal to or less than 50%, her Pyro DMG Bonus is increased by 33%."]
    theMoreTheMerrier = ["Unlocked Automatically",
                         "When Hu Tao cooks a dish perfectly, she has a 18% chance to receive an additional 'Suspicious' dish of the same type."]

    print("Skill Talents: ")
    print(" - Secret Spear of Wangsheng")
    for i in enumerate(secretSpearOfWangsheng, start=1):
        print("\t", *i, sep=". ")
    print("\n - Guide to Afterlife")
    for ii in enumerate(guideToAfterlife, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Paramita Papilio:")
    for iii in enumerate(paramitaPapilio, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t\t - Blood Blossom:")
    for iv in enumerate(bloodBlossom, start=1):
        print("\t\t\t", *iv, sep=". ")
    print("\n - Spirit Soother")
    for v in enumerate(spiritSoother, start=1):
        print("\t", *v, sep=". ")
    print("\nPassive: ")
    print(" - Flutter By")
    for vi in enumerate(flutterBy, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Sanguine Rouge")
    for vii in enumerate(sanguineRouge, start=1):
        print("\t", *vii, sep=". ")
    print("\n - The More the Merrier")
    for viii in enumerate(theMoreTheMerrier, start=1):
        print("\t", *viii, sep=". ")


def jean():
    res = input("What kind of help do you need with Jean? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return jeanBuild()
    elif res == "b":
        return jeanConst()
    elif res == "c":
        return jeanAbility()
    else:
        error()
        return jean()


def jeanBuild():
    weapon = ["skyward blade", "aquilla favonia"]
    altWeapon = ["favonius sword", "sacrificial sword"]
    artifact = ["4x noblesse oblige", "4x viridescent venerer"]
    artifactStats = [["Flat ATK", "ATK%, CRIT DMG, CRIT Rate, Energy Recharge"],
                     ["Flat HP", "ATK%, CRIT DMG, CRIT Rate, Energy Recharge"],
                     ["ATK%", "ATK Flat, CRIT DMG, CRIT Rate, ATK"],
                     ["Physical DMG Bonus%", "ATK%, CRIT DMG, CRIT Rate, ATK"],
                     ["CRIT Rate/CRIT DMG", "CRIT Rate/CRIT DMG, ATK%, Energy Recharge, FLAT ATK"]]
    print("Anemo Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack. ")
    print(
        "\t- The 4 piece viridescent venerer: \n\t1. Gain a 15% Anemo DMG Bonus. \n\t2. Increases Swirl DMG by 60%. Decreases opponent's Elemental RES to the element infused in the Swirl by 40% for 10s.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def jeanConst():
    spiralingTempest = ["Constellation Lv. 1",
                        "Increases the pulling speed of Gale Blade after holding for more than 1s, and increases the DMG dealt by 40%."]
    peoplesAegis = ["Constellation Lv. 2",
                    "When Jean picks up an Elemental Orb/Particle, all party members have their Movement SPD and ATK SPD increased by 15% for 15s."]
    whenTheWestWindArises = ["Constellation Lv. 3",
                             "Increases the Level of Dandelion Breeze by 3.",
                             "Maximum upgrade level is 15."]
    landsOfDandelion = ["Constellation Lv. 4",
                        "Within the Field created by Dandelion Breeze, all enemies have their Anemo RES decreased by 40%."]
    outburstingGust = ["Constellation Lv. 5",
                       "Increase the Level of Gale Blade by 3.",
                       "Maximum upgrade level is 15."]
    lionsFang = ["Constellation Lv. 6",
                 "Incoming DMG is decreased by 35% within the Field created by Dandelion Breeze. Upon leaving the Dandelion Field, this effect lasts for 3 attacks or 10s."]

    print("Jean's Constellations:")
    print(" - Spiraling Tempest")
    for i in enumerate(spiralingTempest, start=1):
        print("\t", *i, sep=". ")
    print("\n - People's Aegis")
    for ii in enumerate(peoplesAegis, start=1):
        print("\t", *ii, sep=". ")
    print("\n - When the West Wind Arises")
    for iii in enumerate(whenTheWestWindArises, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Lands of Dandelion")
    for iv in enumerate(landsOfDandelion, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Outbursting Gust")
    for v in enumerate(outburstingGust, start=1):
        print("\t", *v, sep=". ")
    print("\n - Lion's Fang, Fair Protector of Mondstadt")
    for vi in enumerate(lionsFang, start=1):
        print("\t", *vi, sep=". ")


def jeanAbility():
    favoniusBladework = ["Normal Attack - Performs up to 5 consecutive strikes.",
                         "Charged Attack -  Consumes a certain amount of Stamina to launch an enemy using the power of wind. Launched enemies will slowly fall to the ground.",
                         "Plunging Attack - Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    galeBlade = ["Elemental Skill",
                 "Focusing the might of the formless wind around her blade, Jean releases a miniature storm, launching enemies in the direction she aims at, dealing massive Anemo DMG."]
    holdGaleBlade = [
        "At the cost of continued Stamina consumption, Jean can command the whirlwind to pull surrounding enemies towards her front.",
        "Direction can be adjusted.",
        "Character is immobile during skill duration."]
    dandelionBreeze = ["Elemental Burst",
                       "Calling upon the wind's protection, Jean creates a swirling Dandelion Field, launching surrounding enemies and causing Anemo DMG.",
                       "At the same time, she instantly regenerates a large amount of HP for nearby allied units and all party members. HP restored scale off Jean's ATK."]
    dandelionField = [
        "Continuously regenerates HP for one ally and imbues them with the Anemo attribute.",
        "Deals Anemo DMG to enemies entering or exiting the field."]
    windCompanion = ["Unlocked at Ascension 1",
                     "Hits by Normal Attacks have a 50% chance to regenerate HP equal to 15% of Jean's ATK for all party members."]
    letTheWindLead = ["Unlocked at Ascension 4",
                      "Using Dandelion Breeze will regenerate 20% of its Energy."]
    guidingBreeze = ["Unlocked Automatically",
                     "When a Perfect Cooking is achieved on a dish with restorative effects, there is a 12% chance to obtain double the product."]

    print("Skill Talents: ")
    print(" - Favonius Bladework")
    for i in enumerate(favoniusBladework, start=1):
        print("\t", *i, sep=". ")
    print("\n - Gale Blade")
    for ii in enumerate(galeBlade, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Hold:")
    for iii in enumerate(holdGaleBlade, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t\t - Dandelion Breeze:")
    for iv in enumerate(dandelionBreeze, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Dandelion Field")
    for v in enumerate(dandelionField, start=1):
        print("\t\t", *v, sep=". ")
    print("\nPassive: ")
    print(" - Wind Companion")
    for vi in enumerate(windCompanion, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Let the Wind Lead")
    for vii in enumerate(letTheWindLead, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Guiding Breeze")
    for viii in enumerate(guidingBreeze, start=1):
        print("\t", *viii, sep=". ")


def kaeya():
    res = input("What kind of help do you need with Kaeya? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return kaeyaBuild()
    elif res == "b":
        return kaeyaConst()
    elif res == "c":
        return kaeyaAbility()
    else:
        error()
        return kaeya()


def kaeyaBuild():
    weapon = ["skyward blade", "primordial jade cutter"]
    altWeapon = ["favonius sword", "iron sting"]
    artifact = ["4x noblesse oblige", "2x noblesse oblige, 2x blizzard strayer"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Elemental Mastery"],
                     ["Cryo DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["CRIT Rate/CRIT DMG", "CRIT Rate/CRIT DMG, ATK%, Elemental Mastery, Flat ATK"]]
    print("Cryo Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")
    print("\t- The 2 piece set will increase your cryo damage by 15% and elemental burst damage +20%.\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def kaeyaConst():
    excellentBlood = ["Constellation Lv. 1",
                      "The CRIT Rate of Normal Attack and Charged Attack DMG against enemies affected by the Cold or Frozen status effects is increased by 15%."]
    neverEndingPerformance = ["Constellation Lv. 2",
                              "Every time Glacial Waltz defeats an enemy, its duration is increased by 2.5s, up to a maximum of 15s."]
    danceOfFrost = ["Constellation Lv. 3",
                    "Increases the Level of Frostgnaw by 3.",
                    "Maximum upgrade level is 15."]
    frozenKiss = ["Constellation Lv. 4",
                  "Triggers automatically when Kaeya's HP falls below 20%: \n\t\t1. Creates a shield that absorbs damage equal to 30% of Kaeya's Max HP. Lasts for 20s. \n\t\t2. This shield absorbs Cryo DMG with 250% efficiency. \n\t\t3. Can only occur once every 60s."]
    frostbitingEmbrace = ["Constellation Lv. 5",
                          "Increase the Level of Glacial Waltz by 3.",
                          "Maximum upgrade level is 15."]
    glacialWhirlwind = ["Constellation Lv. 6",
                        "Glacial Waltz will generate 1 additional icicle, and will regenerate 15 Energy when cast."]

    print("Kaeya's Constellations:")
    print(" - Excellent Blood")
    for i in enumerate(excellentBlood, start=1):
        print("\t", *i, sep=". ")
    print("\n - Never-Ending Performance")
    for ii in enumerate(neverEndingPerformance, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Dance of Frost")
    for iii in enumerate(danceOfFrost, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Frozen Kiss")
    for iv in enumerate(frozenKiss, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Frostbiting Embrace")
    for v in enumerate(frostbitingEmbrace, start=1):
        print("\t", *v, sep=". ")
    print("\n - Glacial Whirlwind")
    for vi in enumerate(glacialWhirlwind, start=1):
        print("\t", *vi, sep=". ")


def kaeyaAbility():
    ceremonialBladework = ["Normal Attack - Performs up to 5 consecutive strikes.",
                           "Charged Attack - Consumes a certain amount of Stamina to unleash 2 rapid sword strikes.",
                           "Plunging Attack - Plunges from mid-air to strike the ground below, damaging enemeies along the path and dealing AoE DMG upon impact."]
    frostGnaw = ["Elemental Skill",
                 "Unleashes a frigit blast, dealing Cryo DMG to enemies in front of Kaeya."]
    glacialWaltz = ["Elemental Burst",
                    "Coalescing the frost in the air, Kaeya summons 3 icicles that revolve around him.",
                    "These icicles will follow the character around and deal Cryo DMG to enemies in their path for so long as they persist."]
    coldBloodedStrike = ["Unlocked at Ascension 1",
                         "Every hit with Frostgnaw regenerates HP for Kaeya equal to 15% of ATK."]
    glacialHeart = ["Unlocked at Ascension 4",
                    "Enemies Frozen by Frostgnaw will drop additional Elemental Particles.",
                    "Frostgnaw may only produce a maximum of 2 additional Elemental Particles per use."]
    hiddenStrength = ["Unlocked Automatically",
                      "Decreases all party member's sprinting Stamina consumption by 20%."]

    print("Skill Talents: ")
    print(" - Ceremonial Bladework")
    for i in enumerate(ceremonialBladework, start=1):
        print("\t", *i, sep=". ")
    print("\n - Frostgnaw")
    for ii in enumerate(frostGnaw, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Glacial Waltz")
    for iii in enumerate(glacialWaltz, start=1):
        print("\t", *iii, sep=". ")
    print("\nPassive: ")
    print(" - Cold-Blooded Strike")
    for iv in enumerate(coldBloodedStrike, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Glacial Heart")
    for v in enumerate(glacialHeart, start=1):
        print("\t", *v, sep=". ")
    print("\n - Hidden Strength")
    for vi in enumerate(hiddenStrength, start=1):
        print("\t", *vi, sep=". ")


def kazuha():
    res = input("What kind of help do you need with Kazuha? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return kazuhaBuild()
    elif res == "b":
        return kazuhaConst()
    elif res == "c":
        return kazuhaAbility()
    else:
        error()
        return kazuha()


def kazuhaBuild():
    weapon = ["freedom-sworn", "skyward blade"]
    altWeapon = ["iron sting", "favonius sword"]
    artifact = ["4x viridescent venerer"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT Rate, CRIT DMG, ATK%, Energy Recharge"],
                     ["Elemental Mastery", "CRIT Rate, CRIT DMG, ATK%, Energy Recharge"],
                     ["Anemo DMG Bonus%/Elemental Mastery",
                      "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery / Energy Recharge"],
                     ["Elemental Mastery", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"]]
    print("Anemo Sub-DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece viridescent venerer: \n\t1. Gain a 15% Anemo DMG Bonus. \n\t2. Increases Swirl DMG by 60%. Decreases opponent's Elemental RES to the element infused in the Swirl by 40% for 10s.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def kazuhaConst():
    scarletHills = ["Constellation Lv. 1",
                    "Decreases Chihayaburu's CD by 10%.",
                    "Using Kazuha Slash resets the CD of Chihayaburu."]
    yamaarashiTailwind = ["Constellation Lv. 2",
                          "The Autumn Whirlwind field created by Kazuha Slash has the following effects: \n\t\t1. Increases Kaedehara Kazuha's own Elemental Mastery by 200. \n\t\t2. Increases the Elemental Mastery of characters within the field by 200.",
                          "The Elemental Mastery-increasing effects of this Constellation do not stack."]
    mapleMonogatari = ["Constellation Lv. 3",
                       "Increases the Level of Chihayaburu by 3.",
                       "Maximum upgrade level is 15."]
    oozoraGenpou = ["Constellation Lv. 4",
                    "When Kaedehara Kazuha's Energy is lower than 45, he obtains the following effects: \n\t\t1. Pressing or Holding Chihayaburu regenerates 3 or 4 Energy for Kaedehara Kazuha, respectively. \n\t\t2. When gliding, Kaedehara Kazuha regenerates 2 Energy per second."]
    wisdomOfBansei = ["Constellation Lv. 5",
                      "Increase the Level of Kazuha Slash by 3.",
                      "Maximum upgrade level is 15."]
    crimsonMomiji = ["Constellation Lv. 6",
                     "After using Chihayaburu or Kazuha Slash, Kaedehara Kazuha gains an Anemo Infusion for 5s. Additionally, each point of Elemental Mastery will increase the DMG dealt by Kaedehara Kazuha's Normal, Charged, and Plunging Attack by 0.2%."]

    print("Kazuha's Constellations:")
    print(" - Scarlet Hills")
    for i in enumerate(scarletHills, start=1):
        print("\t", *i, sep=". ")
    print("\n - Yamaarashi Tailwind")
    for ii in enumerate(yamaarashiTailwind, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Maple Monogatari")
    for iii in enumerate(mapleMonogatari, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Oozora Genpou")
    for iv in enumerate(oozoraGenpou, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Wisdom of Bansei")
    for v in enumerate(wisdomOfBansei, start=1):
        print("\t", *v, sep=". ")
    print("\n - Crimson Momiji")
    for vi in enumerate(crimsonMomiji, start=1):
        print("\t", *vi, sep=". ")


def kazuhaAbility():
    garyuuBladework = ["Normal Attack - Performs up to 5 rapid strikes.",
                       "Charged Attack -  Consumes a certain amount of Stamina to unleash 2 rapid sword strikes.",
                       "Plunging Attack - Plunges from mid-air to strike the ground below, damaging opponents along the path and dealing AoE DMG upon impact. If this Plunging Attack is triggered by Chihayaburu, it will be converted to Plunging Attack: Midare Ranzan.",
                       "Plunging Attack: Midare Ranzan - When a Plunging Attack is performed using the effects of the Elemental Skill Chihayaburu, Plunging Attack DMG is converted to Anemo DMG and will create a small wind tunnel via a secret blade technique that pulls in nearby objects and opponents."]
    chihayaburu = ["Elemental Skill",
                   "Unleashes a secret technique as fierce as the rushing wind that pulls objects and opponents towards Kazuha's current position before launching opponents within the AoE, dealing Anemo DMG and lifting Kazuha into the air on a rushing gust of wind."]
    pressChihayaburu = [
        "Can be used in mid-air."]
    holdChihayaburu = [
        "Charges up before unleashing greater Anemo DMG over a larger AoE than Press Mode."]
    plungeChihayaburu = [
        "Within 10s of remaining airborne after casting Chihayaburu, Kazuha can unleash a powerful Plunging Attack known as Midare Ranzan.",
        "When a Plunging Attack is performed using the effects of the Elemental Skill Chihayaburu, Plunging Attack DMG is converted to Anemo DMG. On landing, Kazuha creates a small wind tunnel via a secret blade technique that pulls in nearby objects and opponents. Midare Ranzan's DMG is considered Plunging Attack DMG."]
    kazuhaSlash = ["Elemental Burst",
                   "The signature technique of Kazuha's self-styled bladework — a single slash that strikes with the force of the first winds of autumn, dealing AoE Anemo DMG. The blade's passage will leave behind a field named 'Autumn Whirlwind' that periodically deals AoE Anemo DMG to opponents within its range."]
    elementalAbsorption = [
        "If Autumn Whirlwind comes into contact with Hydro/Pyro/Cryo/Electro, it will deal additional elemental DMG of that type. Elemental Absorption may only occur once per use."]
    soumonSwordsmanship = ["Unlocked at Ascension 1",
                           "If Chihayaburu comes into contact with Hydro/Pyro/Cryo/Electro when cast, Chihayaburu will absorb that element and if Plunging Attack: Midare Ranzan is used before the effect expires, it will deal an additional 200% ATK of the absorbed elemental type as DMG. This will be considered Plunging Attack DMG.",
                           "Elemental Absorption may only occur once per use of Chihayaburu."]
    poeticsOfFuubutsu = ["Unlocked at Ascension 4",
                         "Upon triggering a Swirl reaction, Kaedehara Kazuha will grant teammates a 0.04% Elemental DMG Bonus to their corresponding Element for every point of Elemental Mastery he has for 8s. Bonuses for different elements obtained through this method can co-exist."]
    cloudStrider = ["Unlocked Automatically",
                    "Decreases sprinting Stamina consumption for your own party members by 20%.",
                    "Not stackable with Passive Talents that provide the exact same effects."]

    print("Skill Talents: ")
    print(" - Garyuu Bladework")
    for i in enumerate(garyuuBladework, start=1):
        print("\t", *i, sep=". ")
    print("\n - Chihayaburu")
    for ii in enumerate(chihayaburu, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Press:")
    for iii in enumerate(pressChihayaburu, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Hold:")
    for iv in enumerate(holdChihayaburu, start=1):
        print("\t\t", *iv, sep=". ")
    print("\t - Plunging Attack: Midare Ranzan")
    for v in enumerate(plungeChihayaburu, start=1):
        print("\t\t", *v, sep=". ")
    print("\n - Kazuha Slash")
    for vi in enumerate(kazuhaSlash, start=1):
        print("\t", *vi, sep=". ")
    print("\t - Elemental Absorption")
    for vii in enumerate(elementalAbsorption, start=1):
        print("\t\t", *vii, sep=". ")
    print("\nPassive: ")
    print(" - Soumon Swordsmanship")
    for viii in enumerate(soumonSwordsmanship, start=1):
        print("\t", *viii, sep=". ")
    print("\n - Poetics of Fuubutsu")
    for ix in enumerate(poeticsOfFuubutsu, start=1):
        print("\t", *ix, sep=". ")
    print("\n - Cloud Strider")
    for x in enumerate(cloudStrider, start=1):
        print("\t", *x, sep=". ")


def keqing():
    res = input("What kind of help do you need with Keqing? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return keqingBuild()
    elif res == "b":
        return keqingConst()
    elif res == "c":
        return keqingAbility()
    else:
        error()
        return keqing()


def keqingBuild():
    weapon = ["mistsplitter reforged", "primordial jade cutter"]
    altWeapon = ["the black sword", "lion's roar"]
    artifact = ["4x thundersoother", "2x gladiator's finale, 2x thundering fury"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["Flat HP", " ATK%, CRIT Rate, CRIT DMG, ATK Flat"],
                     ["ATK%", "Flat ATK, CRIT Rate, CRIT DMG, Elemental Mastery"],
                     ["Electro DMG Bonus%", "ATK%, Flat ATK, CRIT Rate, CRIT DMG"],
                     ["CRIT DMG", "CRIT Rate, Flat ATK, ATK%, Elemental Mastery"]]
    print("Electro DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece thundersoother: \n\t1. Electro RES increased by 40%. \n\t2. Increases DMG against enemies affected by Electro by 35%.")
    print("\t- The 2 piece set will increase your electro damage by 15% and increase your ATK +18%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def keqingConst():
    thunderingMight = ["Constellation Lv. 1",
                       "Recasting Stellar Restoration while a Lightning Stiletto is present causes Keqing to deal 50% of her ATK as AoE Electro DMG at the start point and terminus of her Blink."]
    keenExtraction = ["Constellation Lv. 2",
                      "When Keqing's Normal and Charged Attack's hit enemies affected by Electro, they have a 50% chance of producing an Elemental Particle. This effect can only occur once every 5s."]
    foreseenReformation = ["Constellation Lv. 3",
                           "Increases the Level of Starward Sword by 3.",
                           "Maximum upgrade level is 15."]
    attunement = ["Constellation Lv. 4",
                  "For 10s after Keqing triggers an Electro-related Elemental Reaction, her ATK is increased by 25%."]
    beckoningStars = ["Constellation Lv. 5",
                      "Increase the Level of Stellar Restoration by 3.",
                      "Maximum upgrade level is 15."]
    tenaciousStar = ["Constellation Lv. 6",
                     "When initiating a Normal Attack, Charged Attack, Elemental Skill or Elemental Burst, Keqing gains a 6% Electro DMG Bonus for 8s. Effects triggered by Normal Attacks, Charged Attacks, Elemental Skills and Elemental Bursts are considered independent entities."]

    print("Keqing's Constellations:")
    print(" - Thundering Might")
    for i in enumerate(thunderingMight, start=1):
        print("\t", *i, sep=". ")
    print("\n - Keen Extraction")
    for ii in enumerate(keenExtraction, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Foreseen Reformation")
    for iii in enumerate(foreseenReformation, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Attunement")
    for iv in enumerate(attunement, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Beckoning Stars")
    for v in enumerate(beckoningStars, start=1):
        print("\t", *v, sep=". ")
    print("\n - Tenacious Star")
    for vi in enumerate(tenaciousStar, start=1):
        print("\t", *vi, sep=". ")


def keqingAbility():
    yunlaiSwordsmanship = ["Normal Attack - Performs up to 5 rapid strikes.",
                           "Charged Attack -  Consumes a certain amount of Stamina to unleash 2 rapid sword strikes.",
                           "Plunging Attack - Plunges from mid-air to strike the ground below, damaging enemeies along the path and dealing AoE DMG upon impact."]
    stellarRestoration = ["Elemental Skill",
                          "Hurls a Lightning Stiletto that annihilates her enemies like the swift thunder.",
                          "When the Stiletto hits its target, it deals Electro DMG to enemies in a small AoE, and places a Stiletto Mark on the spot hit."]
    holdStellarRestoration = [
        "Hold to adjust the direction in which the Stiletto shall be thrown.",
        "Stilettos thrown by the Hold attack mode can be suspended in mid-air, allowing Keqing to jump to them when using Stellar Restoration a second time."]
    lightningStiletto = [
        "If Keqing uses Stellar Restoration again or uses a Charged Attack while its duration lasts, it will clear the Stiletto Mark and produce different effects: \n\t\t\t\t1. If she uses Stellar Restoration again, she will blink to the location of the Mark and unleashed one slashing attack that deals AoE Electro DMG. When blinking to a Stiletto that was thrown from a Holding attack, Keqing can leap across obstructing terrain. \n\t\t\t\t2. If Keqing uses a Charged Attack, she will ignite a series of thundering cuts at the Mark's location, dealing AoE Electro DMG."]
    starwardSword = ["Elemental Burst",
                     "Keqing unleashes the power of lightning, dealing Electro DMG in an AoE.",
                     "She then blends into the shadow of her blade, striking a series of thunderclap-blows to nearby enemies simultaneous that deal multiple instance of Electro DMG. The final attack deals massive AoE Electro DMG."]
    thunderingPenance = ["Unlocked at Ascension 1",
                         "Within 5s of recasting Stellar Restoration while a Lightning Stiletto is present, Keqing's Normal and Charged Attacks are converted to Electro DMG."]
    aristocraticDignity = ["Unlocked at Ascension 4",
                           "When casting Starward Sword, Keqing's CRIT Rate is increased by 15%, and her Energy Recharge is increased by 15%. This effect lasts for 8s."]
    landsOverseer = ["Unlocked Automatically",
                     "When dispatched on an expedition in Liyue, time consumed is reduced by 25%."]

    print("Skill Talents: ")
    print(" - Yunlai Swordsmanship")
    for i in enumerate(yunlaiSwordsmanship, start=1):
        print("\t", *i, sep=". ")
    print("\n - Stellar Restoration")
    for ii in enumerate(stellarRestoration, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Hold:")
    for iii in enumerate(holdStellarRestoration, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Lightning Stiletto:")
    for iv in enumerate(lightningStiletto, start=1):
        print("\t\t", *iv, sep=". ")
    print("\n - Starward Sword")
    for v in enumerate(starwardSword, start=1):
        print("\t", *v, sep=". ")
    print("\nPassive: ")
    print(" - Thundering Penance")
    for vi in enumerate(thunderingPenance, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Aristocratic Dignity")
    for vii in enumerate(aristocraticDignity, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Land's Overseer")
    for viii in enumerate(landsOverseer, start=1):
        print("\t", *viii, sep=". ")


def klee():
    res = input("What kind of help do you need with Klee? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return kleeBuild()
    elif res == "b":
        return kleeConst()
    elif res == "c":
        return kleeAbility()
    else:
        error()
        return klee()


def kleeBuild():
    weapon = ["lost prayer to the sacred winds", "skyward atlas"]
    altWeapon = ["solar pearl", "the widsith"]
    artifact = ["4x crimson witch of flames", "2x gladiator's finale, 2x crimson witch of flames"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["Flat HP", " CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Elemental Mastery"],
                     ["Pyro DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Elemental Mastery, Flat ATK"]]
    print("Pyro DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece crimson witch of flames: \n\t1. Gain a 15% Pyro DMG Bonus \n\t2. Increases Overloaded and Burning DMG by 40%. Increases Vaporize and Melt DMG by 15%. Using an Elemental Skill increases 2-Piece Set effects by 50% for 10s. Max 3 stacks")
    print("\t- The 2 piece set will increase your pyro damage by 15% and increase your ATK +18%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def kleeConst():
    chainedReactions = ["Constellation Lv. 1",
                        "Attacks and Skills have a certain chance to summon a spark that bombards enemies, dealing DMG equal to 120% of Sparks 'n' Splash's DMG."]
    explosiveFrags = ["Constellation Lv. 2",
                      "Being hit by Jumpy Dumpty's mines decreases enemy DEF by 23% for 10s."]
    exquisiteCompound = ["Constellation Lv. 3",
                         "Increases the Level of Jumpy Dumpty by 3.",
                         "Maximum upgrade level is 15."]
    sparklyExplosion = ["Constellation Lv. 4",
                        "If Klee leaves the field during the duration of Sparks 'n' Splash, her departure triggers an explosion that deals 555% of her ATK as AoE Pyro DMG."]
    novaBurst = ["Constellation Lv. 5",
                 "Increase the Level of Sparks 'n' Splash by 3.",
                 "Maximum upgrade level is 15."]
    blazingDelight = ["Constellation Lv. 6",
                      "While under the effects of Sparks 'n' Splash, other members of the party will continuously regenerate Energy.",
                      "When Sparks 'n' Splash is used, all party members will gain 10% Pyro DMG Bonus for 25s."]

    print("Klee's Constellations:")
    print(" - Chained Reactions")
    for i in enumerate(chainedReactions, start=1):
        print("\t", *i, sep=". ")
    print("\n - Explosive Frags")
    for ii in enumerate(explosiveFrags, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Exquisite Compound")
    for iii in enumerate(exquisiteCompound, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Sparkly Explosion")
    for iv in enumerate(sparklyExplosion, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Nova Burst")
    for v in enumerate(novaBurst, start=1):
        print("\t", *v, sep=". ")
    print("\n - Blazing Delight")
    for vi in enumerate(blazingDelight, start=1):
        print("\t", *vi, sep=". ")


def kleeAbility():
    kaboom = [
        "Normal Attack - Throws things that go boom when they hit things! Perform up to 3 explosive attacks, dealing AoE Pyro DMG.",
        "Charged Attack - Consumes a certain amount of Stamina and deals Pyro DMG to enemies after a short casting time.",
        "Plunging Attack - Gathering the power of Pyro, Klee plunges towards the ground from mid-air, damaging all enemies in her path. Deals AoE Pyro DMG upon impact with the ground."]
    jumpyDumpty = ["Elemental Skill",
                   "Jumpy Dumpty is tons of boom-bang-fun!",
                   "When thrown, Jumpy Dumpty bounces thrice, igniting and dealing AoE Pyro DMG with every bounce.",
                   "On the third bounce, the bomb splits into many mines.",
                   "The mines will explode upon contact with enemies, or after a short period of time, dealing AoE Pyro DMG.",
                   "Starts with 2 charges."]
    sparksNSplash = ["Elemental Burst",
                     "Klee's Blazing Delight! For the duration of this ability, continuously summons Sparks 'n' Splash to attack nearby enemies, dealing AoE Pyro DMG."]
    poundingSurprise = ["Unlocked at Ascension 1",
                        "When Jumpy Dumpty and Normal Attacks deal DMG, Klee has a 50% chance to obtain an Explosive Spark. This Explosive Spark is consumed by the next Charged Attack, which costs no Stamina and deals 50% increased DMG."]
    sparklingBurst = ["Unlocked at Ascension 4",
                      "When a Charged Attack results in a CRIT, all party members gain 2 Elemental Energy."]
    allOfMyTreasures = ["Unlocked Automatically",
                        "Displays the location of nearby resources unique to Mondstadt on the mini-map."]

    print("Skill Talents: ")
    print(" - Kaboom!")
    for i in enumerate(kaboom, start=1):
        print("\t", *i, sep=". ")
    print("\n - Jumpy Dumpty")
    for ii in enumerate(jumpyDumpty, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Sparks 'n' Splash")
    for iii in enumerate(sparksNSplash, start=1):
        print("\t", *iii, sep=". ")
    print("\nPassive: ")
    print(" - Pounding Surprise")
    for iv in enumerate(poundingSurprise, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Sparkling Burst")
    for v in enumerate(sparklingBurst, start=1):
        print("\t", *v, sep=". ")
    print("\n - All Of My Treasures!")
    for vi in enumerate(allOfMyTreasures, start=1):
        print("\t", *vi, sep=". ")


def kokomi():
    res = input("What kind of help do you need with Kokomi? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return kokomiBuild()
    elif res == "b":
        return kokomiConst()
    elif res == "c":
        return kokomiAbility()
    else:
        error()
        return kokomi()


def kokomiBuild():
    weapon = ["everlasting moonglow", "prototype amber"]
    altWeapon = ["wine and song", "the thrilling tales of dragon slayers"]
    artifact = ["4x tenacity of the millelith"]
    artifactStats = [["Flat ATK", "HP%, Energy Recharge, HP Flat, Elemental Mastery"],
                     ["Flat HP", "HP%, Energy Recharge, Elemental Mastery, ATK%"],
                     ["HP%", "Flat HP, Energy Recharge, Elemental Mastery, ATK%"],
                     ["Hydro DMG Bonus/HP%", "Flat HP, Energy Recharge, Elemental Mastery, HP%"],
                     ["Healing Bonus/HP%", "HP% /Elemental Mastery, Flat HP, ATK%, Energy Recharge"]]
    print("Hydro Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece crimson witch of flames: \n\t1. HP +20% \n\t2. When an Elemental Skill hits an opponent, the ATK of all nearby party members is increased by 20% and their Shield Strength is increased by 30% for 3s. This effect can be triggered once every 0.5s. This effect can still be triggered even when the character who is using this artifact set is not on the field.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def kokomiConst():
    atWatersEdge = ["Constellation Lv. 1",
                    "While donning the Ceremonial Garment created by Nereid's Ascension, the final Normal Attack in Sangonomiya Kokomi's combo will unleash a swimming fish to deal 30% of her Max HP as Hydro DMG.",
                    "This DMG is not considered Normal Attack DMG."]
    theCloudsLikeWavesRippling = ["Constellation Lv. 2",
                                  "Sangonomiya Kokomi gains the following Healing Bonuses with regard to characters with 50% or less HP via the following methods: \n\t\t1. Kurage's Oath Bake-Kurage: 4.5% of Kokomi's Max HP. \n\t\t2. Nereid's Ascension Normal and Charged Attacks: 0.6% of Kokomi's Max HP."]
    theMoon = ["Constellation Lv. 3",
               "Increases the Level of Nereid's Ascension by 3.",
               "Maximum upgrade level is 15."]
    theMoonOverlooksTheWaters = ["Constellation Lv. 4",
                                 "While donning the Ceremonial Garment created by Nereid's Ascension, Sangonomiya Kokomi's Normal Attack SPD is increased by 10%, and Normal Attacks that hit opponents will restore 0.8 Energy for her.",
                                 "This effect can occur once every 0.2s."]
    allStreamsFlowToTheSea = ["Constellation Lv. 5",
                              "Increase the Level of Kurage's Oath by 3.",
                              "Maximum upgrade level is 15."]
    sangoIsshin = ["Constellation Lv. 6",
                   "While donning the Ceremonial Garment created by Nereid's Ascension, Sangonomiya Kokomi gains a 40% Hydro DMG Bonus for 4s after her Normal and Charged Attacks heal a character with 80% or more HP."]

    print("Kokomi's Constellations:")
    print(" - At Water's Edge")
    for i in enumerate(atWatersEdge, start=1):
        print("\t", *i, sep=". ")
    print("\n - The Clouds Like Waves Rippling")
    for ii in enumerate(theCloudsLikeWavesRippling, start=1):
        print("\t", *ii, sep=". ")
    print("\n - The Moon, A Ship O'er the Seas")
    for iii in enumerate(theMoon, start=1):
        print("\t", *iii, sep=". ")
    print("\n - The Moon Overlooks the Waters")
    for iv in enumerate(theMoonOverlooksTheWaters, start=1):
        print("\t", *iv, sep=". ")
    print("\n - All Streams Flow to the Sea")
    for v in enumerate(allStreamsFlowToTheSea, start=1):
        print("\t", *v, sep=". ")
    print("\n - Sango Isshin")
    for vi in enumerate(sangoIsshin, start=1):
        print("\t", *vi, sep=". ")


def kokomiAbility():
    theShapeOfWater = [
        "Normal Attack - Performs up to 3 consecutive attacks that take the form of swimming fish, dealing Hydro DMG.",
        "Charged Attack -  Consumes a certain amount of Stamina to deal AoE Hydro DMG after a short casting time.",
        "Plunging Attack - Gathering the might of Hydro, Kokomi plunges towards the ground from mid-air, damaging all opponents in her path. Deals AoE Hydro DMG upon impact with the ground."]
    kuragesOath = ["Elemental Skill",
                   "Summons a 'bake-kurage' created from water that can heal her allies.",
                   "Using this skill will apply the Wet status to Sangonomiya Kokomi."]
    bakeKurage = [
        "Deals Hydro DMG to surrounding opponents and heal nearby active characters at fixed intervals. This healing is based on Kokomi's Max HP."]
    nereidsAscension = ["Elemental Burst",
                        "The might of Watatsumi descends, dealing Hydro DMG to surrounding opponents, before robing Kokomi in a Ceremonial Garment made from the flowing waters of Sangonomiya."]
    ceremonialGarment = [
        "Sangonomiya Kokomi's Normal Attack, Charged Attack and Bake-Kurage DMG are increased based on her Max HP.",
        "When her Normal and Charged Attacks hit opponents, Kokomi will restore HP for all nearby party members, and the amount restored is based on her Max HP.",
        "Increases Sangonomiya Kokomi's resistance to interruption and allows her to move on the water's surface.",
        "These effects will be cleared once Sangonomiya Kokomi leaves the field."]
    flawlessStrategy = ["Passive",
                        "Sangonomiya Kokomi has a 25% Healing Bonus, but a 100% decrease in CRIT Rate."]
    tamanooyasCasket = ["Unlocked at Ascension 1",
                        "If Sangonomiya Kokomi's own Bake-Kurage are on the field when she uses Nereid's Ascension, the Bake-Kurage's duration will be refreshed."]
    songOfPearls = ["Unlocked at Ascension 4",
                    "While donning the Ceremonial Garment created by Nereid's Ascension, the Normal and Charged Attack DMG Bonus Sangonomiya Kokomi gains based on her Max HP will receive a further increase based on 15% of her Healing Bonus."]
    princessOfWatatsumi = ["Unlocked Automatically",
                           "Decreases swimming Stamina consumption for your own party members by 20%.",
                           "Not stackable with Passive Talents that provide the exact same effects."]

    print("Skill Talents: ")
    print(" - The Shape of Water")
    for i in enumerate(theShapeOfWater, start=1):
        print("\t", *i, sep=". ")
    print("\n - Kurage's Oath")
    for ii in enumerate(kuragesOath, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Bake-Kurage:")
    for iii in enumerate(bakeKurage, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Nereid's Ascension:")
    for iv in enumerate(nereidsAscension, start=1):
        print("\t", *iv, sep=". ")
    print("\t - Ceremonial Garment")
    for v in enumerate(ceremonialGarment, start=1):
        print("\t\t", *v, sep=". ")
    print("\n - Flawless Strategy")
    for vi in enumerate(flawlessStrategy, start=1):
        print("\t", *vi, sep=". ")
    print("\nPassive: ")
    print(" - Tamanooya's Casket")
    for vii in enumerate(tamanooyasCasket, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Song of Pearls")
    for viii in enumerate(songOfPearls, start=1):
        print("\t", *viii, sep=". ")
    print("\n - Princess of Watatsumi")
    for ix in enumerate(princessOfWatatsumi, start=1):
        print("\t", *ix, sep=". ")


def lisa():
    res = input("What kind of help do you need with Lisa? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return lisaBuild()
    elif res == "b":
        return lisaConst()
    elif res == "c":
        return lisaAbility()
    else:
        error()
        return lisa()


def lisaBuild():
    weapon = ["lost prayer to the sacred winds", "solar pearl"]
    altWeapon = ["mappa mare", "the thrilling tales of dragon slayers"]
    artifact = ["4x nobless oblige, 4x thundering fury"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Elemental Mastery"],
                     ["Electro DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Elemental Mastery, Flat ATK"]]

    print("Electro Sub-DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")
    print(
        "\t- The 4 piece thundering fury: \n\t1. Gain a 15% Electro DMG Bonus. \n\t2. Increases damage caused by Overloaded, Electro-Charged, and Superconduct DMG by 40%. Triggering such effects decreases Elemental Skill CD by 1s. Can only occur once every 0.8s.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def lisaConst():
    infiniteCircuit = ["Constellation Lv. 1",
                       "Lisa recovers 2 Energy for every opponent hit while holding Violet Arc.",
                       "A maximum of 10 Energy can be regenerated in this manner at any one time."]
    electromagneticField = ["Constellation Lv. 2",
                            "Holding Violet Arc has the following effects: \n\t\t1. Increases DEF by 25%. \n\t\t2. Increases Lisa's resistance to interruption."]
    resonantThunder = ["Constellation Lv. 3",
                       "Increases the Level of Lightning Rose by 3.",
                       "Maximum upgrade level is 15."]
    plasmaEruption = ["Constellation Lv. 4",
                      "Increases the number of lightning bolts released by Lightning Rose by 1-3."]
    electrocute = ["Constellation Lv. 5",
                   "Increase the Level of Violet Arc by 3.",
                   "Maximum upgrade level is 15."]
    pulsatingWitch = ["Constellation Lv. 6",
                      "When Lisa takes the field, she applies 3 stacks of Violet Arc's Conductive status onto nearby enemies.",
                      "This effect can only occur once every 5s."]

    print("Lisa's Constellations:")
    print(" - Infinite Circuit")
    for i in enumerate(infiniteCircuit, start=1):
        print("\t", *i, sep=". ")
    print("\n - Electromagnetic Field")
    for ii in enumerate(electromagneticField, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Resonant Thunder")
    for iii in enumerate(resonantThunder, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Plasma Eruption")
    for iv in enumerate(plasmaEruption, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Electrocute")
    for v in enumerate(electrocute, start=1):
        print("\t", *v, sep=". ")
    print("\n - Pulsating Witch")
    for vi in enumerate(pulsatingWitch, start=1):
        print("\t", *vi, sep=". ")


def lisaAbility():
    lightningTouch = [
        "Normal Attack - Perform up to 4 lightning attacks that deal Electro DMG.",
        "Charged Attack -  Consumes a certain amount of Stamina to deal AoE Electro DMG after a short casting time.",
        "Plunging Attack - Gathering the might of Hydro, Kokomi plunges towards the ground from mid-air, damaging all opponents in her path. Deals AoE Hydro DMG upon impact with the ground."]
    violetArc = ["Elemental Skill",
                 "Channels the power of lightning to sweep bothersome matters away."]
    pressVioletArc = [
        "Releases a homing Lightning Orb. On hit, it deals Electro DMG, and applies a stack of Conductive status (Max 3 stacks) to enemies in a small AoE."]
    holdVioletArc = [
        "After an extended casting time, calls down lightning from the heavens, dealing massive Electro DMG to all nearby enemies.",
        "Deals great amounts of extra damage to enemies based on the number of Conductive stacks applied to them, and clears their Conductive status."]
    lightningRose = ["Elemental Burst",
                     "Summons a Lightning Rose that unleashes powerful lightning bolts, launching surrounding enemies and dealing Electro DMG.",
                     "The Lightning Rose will continuously emit lightning to knock back enemies and deal Electro DMG for so long as it persists."]
    inducedAftershock = ["Unlocked at Ascension 1",
                         "Hits by charged Attacks apply Violet Arc's Conductive status to enemies."]
    staticElectricityField = ["Unlocked at Ascension 4",
                              "Enemies hit by Lightning Rose have their DEF decreased by 15% for 10s."]
    generalPharmaceutics = ["Unlocked Automatically",
                            "When Lisa crafts a potion, she has a 20% chance to refund a portion of the crafting materials used."]

    print("Skill Talents: ")
    print(" - Lightning Touch")
    for i in enumerate(lightningTouch, start=1):
        print("\t", *i, sep=". ")
    print("\n - Violet Arc")
    for ii in enumerate(violetArc, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Press:")
    for iii in enumerate(pressVioletArc, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Hold:")
    for iv in enumerate(holdVioletArc, start=1):
        print("\t\t", *iv, sep=". ")
    print("\t - Lightning Rose")
    for v in enumerate(lightningRose, start=1):
        print("\t", *v, sep=". ")
    print("\nPassive: ")
    print(" - Induced Aftershock")
    for vi in enumerate(inducedAftershock, start=1):
        print("\t", *vi, sep=". ")
    print(" - Static Electricity Field")
    for vii in enumerate(staticElectricityField, start=1):
        print("\t", *vii, sep=". ")
    print("\n - General Pharmaceutics")
    for viii in enumerate(generalPharmaceutics, start=1):
        print("\t", *viii, sep=". ")


def mona():
    res = input("What kind of help do you need with Mona? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return monaBuild()
    elif res == "b":
        return monaConst()
    elif res == "c":
        return monaAbility()
    else:
        error()
        return mona()


def monaBuild():
    weapon = ["skyward atlas", "the widsith"]
    altWeapon = ["favonius codex", "mappa mare"]
    artifact = ["4x nobless oblige", "4x emblem of severed fate"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["ATK%", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["Hydro DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Flat ATK, Energy Recharge"]]

    print("Hydro Sub-DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")
    print(
        "\t- The 4 piece emblem of severed fate: \n\t1. Energy Recharge +20% \n\t2. Increases Elemental Burst DMG by 25% of Energy Recharge. A maximum of 75% bonus DMG can be obtained in this way.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def monaConst():
    prophecyOfSubmersion = ["Constellation Lv. 1",
                            "The effects of Hydro-related Elemental Reactions are enhanced for 8s after a character hits an enemy affected by an Omen: \n\t\t1. Electro-Charged DMG is increased by 15%. \n\t\t2. Vaporize DMG is increased by 15%. \n\t\t3. Hydro Swirl DMG is increased by 15%. \n\t\t4. The duration for which enemies are Frozen is increased by 15%."]
    lunarChain = ["Constellation Lv. 2",
                  "When a Normal Attack hits, there is a 20% chance that it will be automatically followed by a Charged Attack.",
                  "This effect can only occur once every 5s."]
    restlessRevolution = ["Constellation Lv. 3",
                          "Increases the Level of Stellaris Phantasm by 3.",
                          "Maximum upgrade level is 15."]
    prophecyOfOblivion = ["Constellation Lv. 4",
                          "When a character attacks an enemy affected by the Omen status effect, their CRIT Rate is increased by 15%."]
    mockeryOfFortuna = ["Constellation Lv. 5",
                        "Increase the Level of Mirror Reflection of Doom by 3.",
                        "Maximum upgrade level is 15."]
    rhetoricsOfCalamitas = ["Constellation Lv. 6",
                            "Upon entering Illusory Torrent, Mona gain a 60% increase to the DMG her next Charged Attack per second of movement.",
                            "A maximum DMG Bonus of 180% can be achieved in this manner. The effect lasts for no more than 8s."]

    print("Mona's Constellations:")
    print(" - Prophecy of Submersion")
    for i in enumerate(prophecyOfSubmersion, start=1):
        print("\t", *i, sep=". ")
    print("\n - Lunar Chain")
    for ii in enumerate(lunarChain, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Restless Revolution")
    for iii in enumerate(restlessRevolution, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Prophecy of Oblivion")
    for iv in enumerate(prophecyOfOblivion, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Mockery of Fortuna")
    for v in enumerate(mockeryOfFortuna, start=1):
        print("\t", *v, sep=". ")
    print("\n - Rhetorics of Calamitas")
    for vi in enumerate(rhetoricsOfCalamitas, start=1):
        print("\t", *vi, sep=". ")


def monaAbility():
    rippleOfFate = [
        "Normal Attack - Performs up to 4 water splash attacks that deal Hydro DMG.",
        "Charged Attack -  Consumes a certain amount of Stamina and deals AoE Hydro DMG after a short casting time.",
        "Plunging Attack - Gathering the might of Hydro, Mona plunges towards the ground from mid-air, damaging all enemies in her path. Deals AoE Hydro DMG upon impact with the ground."]
    mirrorReflectionOfDoom = ["Elemental Skill",
                              "Creates an illusory Phantom of fate from coalesced waterspouts.",
                              "The Phantom has the following special properties: \n\t\t1. Continuously taunts nearby enemies, attracting their fire. \n\t\t2. Continuously deals Hydro DMG to nearby enemies. \n\t\t3. When its duration expires, the Phantom explodes, dealing AoE Hydro DMG."]
    holdMirrorReflection = ["Utilizes water currents to move backwards swiftly before conjuring a Phantom.",
                            "Only one Phantom created by Mirror Reflection of Doom can exist at any time."]
    stellarisPhantasm = ["Elemental Burst",
                         "Mona summons the sparkling waves and creates a reflection of the starry sky, applying the Illusory Bubble status to opponents in a large AoE."]
    illusoryBubble = [
        "Traps opponents inside a pocket of destiny and also makes them Wet. Renders weaker opponents immobile. When an opponent affected by Illusory Bubble sustains DMG, the following effects are produced: \n\t\t1. Applies an Omen to the opponent, which gives a DMG Bonus, also increasing the DMG of the attack that causes it. \n\t\t2. Removes the Illusory Bubble, dealing Hydro Elemental DMG in the process. The DMG Bonus does not apply to the Hydro Elemental DMG dealt in this instance."]
    omen = ["During its duration, increases DMG taken by enemies."]
    illusoryTorrent = ["Right Click", "Alternate Spirit",
                       "Mona cloaks herself within the water's flow, consuming Stamina to move rapidly.",
                       "When under the effect of Illusory Torrent, Mona can move at high speed on water.",
                       "Applies the Wet status to nearby enemies when she reappears."]
    hag = ["Unlocked at Ascension 1",
           "After she has used Illusory Torrent for 2s, if there are any enemies nearby, Mona will automatically create a Phantom.",
           "A Phantom created in this manner lasts for 2s, and its explosion DMG is equal to 50% of Mirror Reflection of Doom."]
    waterborneDestiny = ["Unlocked at Ascension 4",
                         "Increases Mona's Hydro DMG Bonus by a degree equivalent to 20% of her Energy Recharge rate."]
    principiumOfAstrology = ["Unlocked Automatically",
                             "When Mona crafts Weapon Ascension Materials, she has a 25% chance to refund a portion of the crafting materials used."]

    print("Skill Talents: ")
    print(" - Ripple of Fate")
    for i in enumerate(rippleOfFate, start=1):
        print("\t", *i, sep=". ")
    print("\n - Mirror Reflection of Doom")
    for ii in enumerate(mirrorReflectionOfDoom, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Hold:")
    for iii in enumerate(holdMirrorReflection, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Stellaris Phantasm")
    for iv in enumerate(stellarisPhantasm, start=1):
        print("\t", *iv, sep=". ")
    print("\t - Illusory Bubble")
    for v in enumerate(illusoryBubble, start=1):
        print("\t\t", *v, sep=". ")
    print("\t - Omen")
    for vi in enumerate(omen, start=1):
        print("\t\t", *vi, sep=". ")
    print("\n - Illusory Torrent")
    for vii in enumerate(illusoryTorrent, start=1):
        print("\t", *vii, sep=". ")
    print("\nPassive: ")
    print(" - Come 'n' Get Me, Hag!")
    for viii in enumerate(hag, start=1):
        print("\t", *viii, sep=". ")
    print("\n - Waterborne Destiny")
    for ix in enumerate(waterborneDestiny, start=1):
        print("\t", *ix, sep=". ")
    print("\n - Principium of Astrology")
    for x in enumerate(principiumOfAstrology, start=1):
        print("\t", *x, sep=". ")


def ningguang():
    res = input(
        "What kind of help do you need with Ningguang? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return ningguangBuild()
    elif res == "b":
        return ningguangConst()
    elif res == "c":
        return ningguangAbility()
    else:
        error()
        return ningguang()


def ningguangBuild():
    weapon = ["memory of dust", "lost prayer to the sacred winds"]
    altWeapon = ["solar pearl", "dodoco tales"]
    artifact = ["2x archaic petra, 2x gladiator's finale", "2x archaic petra, 2x noblesse oblige"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery / Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["ATK%", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["Geo DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Flat ATK, Elemental Mastery/Energy Recharge"]]

    print("Geo DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 2 piece set (archaic petra + gladiator's finale) will increase your geo damage by 15% and increase your ATK +18%\n")
    print(
        "\t- The 2 piece set (archaic petra + noblesse oblige) will increase your geo damage by 15% and increase your elemental burst DMG +20%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def ningguangConst():
    piercingFragments = ["Constellation Lv. 1",
                         "When a Normal Attack hits, it deals AoE DMG."]
    shockEffect = ["Constellation Lv. 2",
                   "When Jade Screen is shattered, its CD will reset.",
                   "Can occur once every 6s."]
    majestyBeTheArrayOfStars = ["Constellation Lv. 3",
                                "Increases the Level of Starshatter by 3.",
                                "Maximum upgrade level is 15."]
    exquisiteBeTheJade = ["Constellation Lv. 4",
                          "Jade Screen increases nearby characters' Elemental RES by 10%."]
    invincibleBeTheJadeScreen = ["Constellation Lv. 5",
                                 "Increase the Level of Jade Screen by 3.",
                                 "Maximum upgrade level is 15."]
    grandeurBeTheSevenStars = ["Constellation Lv. 6",
                               "When Starshatter is used, Ningguang gains 7 Star Jades."]

    print("Ningguang's Constellations:")
    print(" - Piercing Fragments")
    for i in enumerate(piercingFragments, start=1):
        print("\t", *i, sep=". ")
    print("\n - Shock Effect")
    for ii in enumerate(shockEffect, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Majesty be the Array of Stars")
    for iii in enumerate(majestyBeTheArrayOfStars, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Exquisite be the Jade, Outshining All Beneath")
    for iv in enumerate(exquisiteBeTheJade, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Invincible be the Jade Screen")
    for v in enumerate(invincibleBeTheJadeScreen, start=1):
        print("\t", *v, sep=". ")
    print("\n - Grandeur be the Seven Stars")
    for vi in enumerate(grandeurBeTheSevenStars, start=1):
        print("\t", *vi, sep=". ")


def ningguangAbility():
    sparklingScatter = [
        "Normal Attack - Shoots gems that deal Geo DMG. Upon hit, this grants Ningguang 1 Star Jade.",
        "Charged Attack -  Consumes a certain amount of Stamina to fire off a giant gem that deals Geo DMG. If Ningguang has any Star Jades, unleashing a Charged Attack will cause the Star Jades to be fired at the enemy as well, dealing additional DMG.",
        "Plunging Attack - Gathering the might of Geo, Ningguang plunges towards the ground from mid-air, damaging all enemies in her path. Deals AoE Geo DMG upon impact with the ground."]
    jadeScreen1 = ["Elemental Skill",
                   "Ningguang creates a Jade Screen out of gold, obsidian and her great opulence, dealing AoE Geo DMG."]
    jadeScreen2 = ["Blocks enemy projectiles.",
                   "Endurance scales based on Ningguang's Max HP.",
                   "Jade Screen is considered a Geo Construct and can be used to block certain attacks, but cannot be climbed. Only one Jade Screen may exist at any one time."]
    starshatter = ["Elemental Burst",
                   "Gathering a great number of gems, Ningguang scatters them all at once, sending homing projectiles at her enemies that deal massive Geo DMG.",
                   "If Starshatter is cast when a Jade Screen is nearby, the Jade Screen will fire additional gem projectiles at the same time."]
    backupPlan = ["Unlocked at Ascension 1",
                  "When Ningguang is in possession of Star Jades, her Charged Attack does not consume Stamina."]
    strategicReserve = ["Unlocked at Ascension 4",
                        "A character that passes through the Jade Screen will gain a 12% Geo DMG Bonus for 10s."]
    troveOfMarvelousTreasures = ["Unlocked Automatically",
                                 "Displays the location of nearby ore veins (Iron Ore, White Iron Ore, Crystal Ore, and Magical Crystal Ore) on the mini-map."]

    print("Skill Talents: ")
    print(" - Sparkling Scatter")
    for i in enumerate(sparklingScatter, start=1):
        print("\t", *i, sep=". ")
    print("\n - Jade Screen")
    for ii in enumerate(jadeScreen1, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Jade Screen:")
    for iii in enumerate(jadeScreen2, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Starshatter:")
    for iv in enumerate(starshatter, start=1):
        print("\t", *iv, sep=". ")
    print("\nPassive: ")
    print(" - Backup Plan")
    for v in enumerate(backupPlan, start=1):
        print("\t", *v, sep=". ")
    print("\n - Strategic Reserve")
    for vi in enumerate(strategicReserve, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Trove of Marvelous Treasures")
    for vii in enumerate(troveOfMarvelousTreasures, start=1):
        print("\t", *vii, sep=". ")


def noelle():
    res = input("What kind of help do you need with Noelle? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return noelleBuild()
    elif res == "b":
        return noelleConst()
    elif res == "c":
        return noelleAbility()
    else:
        error()
        return noelle()


def noelleBuild():
    weapon = ["the unforged ", "skyward pride"]
    altWeapon = ["the bell", "whiteblind"]
    artifact = ["4x maiden beloved", "2x maiden beloved, 2x retracing bolide"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, DEF%"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, DEF%"],
                     ["DEF%/ATK%", "CRIT DMG, CRIT Rate, DEF%/ATK%, Energy Recharge"],
                     ["Geo DMG Bonus%", "CRIT DMG, CRIT Rate, DEF% /ATK%, DEF%"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, DEF%, Energy Recharge"]]

    print("Geo Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece maiden beloved: \n\t1. Character Healing Effectiveness +15% \n\t2. Using an Elemental Skill or Burst increases healing received by all party members by 20% for 10s.")
    print(
        "\t- The 2 piece set will increase your character Healing Effectiveness +15% and increases Shield Strength by 35%.\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def noelleConst():
    iGotYourBack = ["Constellation Lv. 1",
                    "While Sweeping Time and Breastplate are both in effect, the chance of Breastplate's healing effects activating is increased to 100%."]
    combatMaid = ["Constellation Lv. 2",
                  "Decreases the Stamina Consumption of Noelle's Charged Attacks by 20% and increases her Charged Attack DMG by 15%."]
    invulnerableMaid = ["Constellation Lv. 3",
                        "Increases the Level of Breastplate by 3.",
                        "Maximum upgrade level is 15."]
    toBeCleaned = ["Constellation Lv. 4",
                   "When Breastplate's duration expires or it is destroyed by DMG, it will deal 400% ATK of Geo DMG to surrounding enemies."]
    favoniusSweeperMaster = ["Constellation Lv. 5",
                             "Increase the Level of Sweeping Time by 3.",
                             "Maximum upgrade level is 15."]
    mustBeSpotless = ["Constellation Lv. 6",
                      "Sweeping Time increases Noelle's ATK by an additional 50% of her DEF.",
                      "Additionally, every enemy defeated during the skill's duration adds 1s to the duration, up to 10s."]

    print("Noelle's Constellations:")
    print(" - I Got Your Back")
    for i in enumerate(iGotYourBack, start=1):
        print("\t", *i, sep=". ")
    print("\n - Combat Maid")
    for ii in enumerate(combatMaid, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Invulnerable Maid")
    for iii in enumerate(invulnerableMaid, start=1):
        print("\t", *iii, sep=". ")
    print("\n - To Be Cleaned")
    for iv in enumerate(toBeCleaned, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Favonius Sweeper Master")
    for v in enumerate(favoniusSweeperMaster, start=1):
        print("\t", *v, sep=". ")
    print("\n - Must Be Spotless")
    for vi in enumerate(mustBeSpotless, start=1):
        print("\t", *vi, sep=". ")


def noelleAbility():
    maid = ["Normal Attack - Performs up to 4 consecutive strikes.",
            "Charged Attack - Drains Stamina over time to perform continuous swirling attacks against all nearby enemies.",
            "At end of the sequence, perform a more powerful slash.",
            "Plunging Attack - Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    breastplate = ["Elemental Skill",
                   "Summons a protective stone armor, dealing Geo DMG to surrounding enemies and creating a shield. The shield's DMG Absorption scaled based on Noelle's DEF.",
                   "The shield has the following properties: \n\t\t1. When Noelle's Normal and Charged Attacks hit a target, they have a certain chance to regenerate HP for all characters, both on and off the field. \n\t\t2. Applies the Geo element to the character. \n\t\t3. Possesses 250% Absorption Efficiency against Geo DMG.",
                   "The amount of HP healed when regeneration is triggered scales based on Noelle's DEF."]
    sweepingTime = ["Elemental Burst",
                    "Gathering the strength of stone around her weapon, Noelle strikes the enemies surrounding her within a large AoE, dealing Geo DMG.",
                    "Afterwards, Noelle gains the following effects:: \n\t\t1. Larger attack AoE.. \n\t\t2. Converts attack DMG to Geo DMG.. \n\t\t3. Increased ATK that scales based on her DEF."]
    devotion = ["Unlocked at Ascension 1",
                "When Noelle is in the party but not on the field, this ability triggers automatically when the active character's HP falls below 30%: \n\t\t1. Creates a shield that lasts for 20s and absorbs DMG equal to 400% of Noelle's DEF. This effect can only occur once every 60s."]
    niceAndClean = ["Unlocked at Ascension 4",
                    "Every 4 Normal or Charged Attack hits will decrease the CD of Breastplate by 1s.",
                    "Hitting multiple enemies with a single attack is only counted as 1 hit."]
    maidsKnighthood = ["Unlocked Automatically",
                       "When a Perfect Cooking is achieved on a DEF-boosting dish, Noelle has a 12% chance to obtain double the product."]

    print("Skill Talents: ")
    print(" - Favonius Bladework - Maid")
    for i in enumerate(maid, start=1):
        print("\t", *i, sep=". ")
    print("\n - Breastplate")
    for ii in enumerate(breastplate, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Sweeping Time")
    for iii in enumerate(sweepingTime, start=1):
        print("\t", *iii, sep=". ")
    print("\nPassive: ")
    print(" - Devotion:")
    for iv in enumerate(devotion, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Nice and Clean")
    for v in enumerate(niceAndClean, start=1):
        print("\t", *v, sep=". ")
    print("\n - Maid's Knighthood")
    for vi in enumerate(maidsKnighthood, start=1):
        print("\t", *vi, sep=". ")


def qiqi():
    res = input("What kind of help do you need with Qiqi? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return qiqiBuild()
    elif res == "b":
        return qiqiConst()
    elif res == "c":
        return qiqiAbility()
    else:
        error()
        return qiqi()


def qiqiBuild():
    weapon = ["skyward blade", "sacrificial sword"]
    altWeapon = ["festering desire", "favonius sword"]
    artifact = ["4x noblesse oblige", "2x noblesse oblige, 2x blizzard strayer"]
    artifactStats = [["Flat ATK", " ATK%, CRIT DMG, Elemental Mastery, CRIT Rate"],
                     ["Flat HP", "ATK%, CRIT DMG, CRIT Rate, Elemental Mastery"],
                     ["ATK%", "CRIT DMG, Energy Recharge, Elemental Mastery, CRIT Rate"],
                     ["Cryo DMG Bonus%", "ATK%, CRIT DMG, CRIT Rate, Energy Recharge/Elemental Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Energy Recharge, Elemental Mastery"]]

    print("Cryo Healer:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")
    print("\t- The 2 piece set will increase your cryo damage by 15% and increase your elemental burst damage by 20%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def qiqiConst():
    asceticsOfFrost = ["Constellation Lv. 1",
                       "When the Herald of Frost hits an enemy marked by a Fortune-Preserving Talisman, Qiqi regenerates 2 Energy."]
    frozenToTheBone = ["Constellation Lv. 2",
                       "Qiqi's Normal and Charge Attack DMG against enemies affected by Cryo is increased by 15%."]
    ascendantPraise = ["Constellation Lv. 3",
                       "Increases the Level of Adeptus Art: Preserver of Fortune by 3.",
                       "Maximum upgrade level is 15."]
    divineSuppression = ["Constellation Lv. 4",
                         "Targets marked by the Fortune-Preserving Talisman have their ATK decreased by 20%."]
    crimsonLotusBloom = ["Constellation Lv. 5",
                         "Increase the Level of Adeptus Art: Herald of Frost by 3.",
                         "Maximum upgrade level is 15."]
    riteOfResurrection = ["Constellation Lv. 6",
                          "Using Adeptus Art: Preserve of Fortune revives all nearby fallen characters and regenerates 50% of their HP.",
                          "This effect can only occur once every 15 mins."]

    print("Qiqi's Constellations:")
    print(" - Ascetics of Frost")
    for i in enumerate(asceticsOfFrost, start=1):
        print("\t", *i, sep=". ")
    print("\n - Frozen to the Bone")
    for ii in enumerate(frozenToTheBone, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Ascendant Praise")
    for iii in enumerate(ascendantPraise, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Divine Suppression")
    for iv in enumerate(divineSuppression, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Crimson Lotus Bloom")
    for v in enumerate(crimsonLotusBloom, start=1):
        print("\t", *v, sep=". ")
    print("\n - Rite of Resurrection")
    for vi in enumerate(riteOfResurrection, start=1):
        print("\t", *vi, sep=". ")


def qiqiAbility():
    ancientSwordArt = [
        "Normal Attack - Performs up to 5 rapid strikes.",
        "Charged Attack - Consumes a certain amount of Stamina to unleash 2 rapid sword strikes.",
        "Plunging Attack - Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    heraldOfFrost1 = ["Elemental Skill",
                      "Using the Icevein Talisman, Qiqi brings forth the Herald of Frost, dealing Cryo DMG to nearby enemies."]
    heraldOfFrost2 = [
        "When Qiqi hits a target with her Normal or Charged Attacks, she regenerates HP for all party members and all nearby allied characters. Healing scales based on Qiqi's ATK.",
        "Regenerates HP for current character at regular intervals.",
        "Follows the character around, dealing Cryo DMG to enemies in its path."]
    preserverOfFortune = ["Elemental Burst",
                          "Qiqi releases the adeptus power sealed within her body, marking nearby enemies with a Fortune-Preserving Talisman that deals Cryo DMG."]
    fortunePreservingTalisman = [
        "When enemies affected by this Talisman take DMG, the character that dealt this DMG regenerates HP."]
    lifeProlongingMethods = ["Unlocked at Ascension 1",
                             "When a character under the effects of Adeptus Art: Herald of Frost triggers an Elemental Reaction, their Incoming Healing Bonus is increased by 20% for 8s."]
    aGlimpseIntoArcanum = ["Unlocked at Ascension 4",
                           "When Qiqi hits enemies with her Normal and Charged Attacks, she has a 50% chance to apply a Fortune-Preserving Talisman to them for 6s. This effect can only occur once every 30s."]
    formerLifeMemories = ["Unlocked Automatically",
                          "Displays the location of nearby resources unique to Liyue on the mini-map."]

    print("Skill Talents: ")
    print(" - Ancient Sword Art")
    for i in enumerate(ancientSwordArt, start=1):
        print("\t", *i, sep=". ")
    print("\n - Adeptus Art: Herald of Frost")
    for ii in enumerate(heraldOfFrost1, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Herald of Frost:")
    for iii in enumerate(heraldOfFrost2, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Adeptus Art: Preserver of Fortune")
    for iv in enumerate(preserverOfFortune, start=1):
        print("\t", *iv, sep=". ")
    print("\t - Fortune-Preserving Talisman")
    for v in enumerate(fortunePreservingTalisman, start=1):
        print("\t\t", *v, sep=". ")
    print("\nPassive: ")
    print(" - Life-Prolonging Methods")
    for vi in enumerate(lifeProlongingMethods, start=1):
        print("\t", *vi, sep=". ")
    print("\n - A Glimpse into Arcanum")
    for vii in enumerate(aGlimpseIntoArcanum, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Former Life Memories")
    for viii in enumerate(formerLifeMemories, start=1):
        print("\t", *viii, sep=". ")


def raiden():
    res = input(
        "What kind of help do you need with Raiden Shogun? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return raidenBuild()
    elif res == "b":
        return raidenConst()
    elif res == "c":
        return raidenAbility()
    else:
        error()
        return raiden()


def raidenBuild():
    weapon = ["engulfing lightning", "skyward spine"]
    altWeapon = ["the catch", "favonius lance"]
    artifact = ["4x thundersoother", "4x emblem of severed fate"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["Energy Recharge%", "CRIT DMG, CRIT Rate, ATK%, Element Mastery"],
                     ["ATK%/Electro DMG Bonus%", "CRIT DMG, CRIT Rate, Energy Recharge, Elemental Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Flat ATK, Energy Recharge"]]

    print("Electro Hybrid DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece thundersoother: \n\t1. Electro RES increased by 40% \n\t2. Increases DMG against enemies affected by Electro by 35%.")
    print(
        "\t- The 4 piece emblem of severed fate: \n\t1. Energy Recharge +20% \n\t2. Increases Elemental Burst DMG by 25% of Energy Recharge. A maximum of 75% bonus DMG can be obtained in this way.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def raidenConst():
    ominousInscription = ["Constellation Lv. 1",
                          "Chakra Desiderata will gather Resolve even faster. When Electro characters use their Elemental Bursts, the Resolve gained is increased by 80%. When characters of other Elemental Types use their Elemental Bursts, the Resolve gained is increased by 20%."]
    steelbreaker = ["Constellation Lv. 2",
                    "Secret Art: Musou Shinsetsu's Musou no Hitotachi and Musou Isshin attacks will ignore 60% of opponents' DEF."]
    shinkageBygones = ["Constellation Lv. 3",
                       "Increases the Level of Adeptus Art: Preserver of Fortune by 3.",
                       "Maximum upgrade level is 15."]
    pledgeOfPropriety = ["Constellation Lv. 4",
                         "When the Musou Isshin state applied by Secret Art: Musou Shinsetsu expires, all nearby party members (excluding the Raiden Shogun) gain 30% bonus ATK for 10s."]
    shogunsDescent = ["Constellation Lv. 5",
                      "Increase the Level of Transcendence: Baleful Omen by 3.",
                      "Maximum upgrade level is 15."]
    wishbearer = ["Constellation Lv. 6",
                  "While in the Musou Isshin state applied by Secret Art: Musou Shinsetsu, the Raiden Shogun's Normal, Charged, and Plunging Attacks will decrease all nearby party members' (but not including the Raiden Shogun herself) Elemental Burst CD by 1s when they hit opponents.",
                  "This effect can only occur once every 15 mins."]

    print("Raiden's Constellations:")
    print(" - Ominous Inscription")
    for i in enumerate(ominousInscription, start=1):
        print("\t", *i, sep=". ")
    print("\n - Steelbreaker")
    for ii in enumerate(steelbreaker, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Shinkage Bygones")
    for iii in enumerate(shinkageBygones, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Pledge of Propriety")
    for iv in enumerate(pledgeOfPropriety, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Shogun's Descent")
    for v in enumerate(shogunsDescent, start=1):
        print("\t", *v, sep=". ")
    print("\n - Wishbearer")
    for vi in enumerate(wishbearer, start=1):
        print("\t", *vi, sep=". ")


def raidenAbility():
    origin = [
        "Normal Attack - Performs up to 5 consecutive spear strikes.",
        "Charged Attack - Consumes a certain amount of Stamina to perform an upward slash.",
        "Plunging Attack - Plunges from mid-air to strike the ground below, damaging opponents along the path and dealing AoE DMG upon impact."]
    balefulOmen = ["Elemental Skill",
                   "The Raiden Shogun unveils a shard of her Euthymia, dealing Electro DMG to nearby opponents, and granting nearby party members the Eye of Stormy Judgment.",
                   "The Eye can initiate one coordinated attack every 0.9s per party.",
                   "Coordinated attacks generated by characters not controlled by you deal 20% of the normal DMG."]
    eyeOfStormyJudgment = [
        "When characters with this buff attack and deal DMG to opponents, the Eye will unleash a coordinated attack, dealing AoE Electro DMG at the opponent's position.",
        "Characters who gain the Eye of Stormy Judgment will have their Elemental Burst DMG increased based on the Energy Cost of the Elemental Burst during the Eye's duration."]
    musouShinsetsu = ["Elemental Burst",
                      "Gathering truths unnumbered and wishes uncounted, the Raiden Shogun unleashes the Musou no Hitotachi and deals AoE Electro DMG, using Musou Isshin in combat for a certain duration afterward. The DMG dealt by Musou no Hitotachi and Musou Isshin's attacks will be increased based on the number of Chakra Desiderata's Resolve stacks consumed when this skill is used."]
    musouIsshin = [
        "While in this state, the Raiden Shogun will wield her tachi in battle, while her Normal, Charged, and Plunging Attacks will be infused with Electro DMG, which cannot be overridden. When such attacks hit opponents, she will regenerate Energy for all nearby party members. Energy can be restored this way once every 1s, and this effect can be triggered 5 times throughout this skill's duration.",
        "While in this state, the Raiden Shogun's resistance to interruption is increased, and she is immune to Electro-Charged reaction DMG.",
        "While Musou Isshin is active, the Raiden Shogun's Normal, Charged, and Plunging Attack DMG will be considered Elemental Burst DMG.",
        "The effects of Musou Isshin will be cleared when the Raiden Shogun leaves the field."]
    chakraDesiderata = [
        "When nearby party members (excluding the Raiden Shogun herself) use their Elemental Bursts, the Raiden Shogun will build up Resolve stacks based on the Energy Cost of these Elemental Bursts.",
        "The maximum number of Resolve stacks is 60. The Resolve gained by Chakra Desiderata will be cleared 300s after the Raiden Shogun leaves the field."]
    wishesUnnumbered = ["Unlocked at Ascension 1",
                        "When nearby party members gain Elemental Orbs or Particles, Chakra Desiderata gains 2 Resolve stacks.",
                        "This effect can occur once every 3s."]
    enlightenedOne = ["Unlocked at Ascension 4",
                      "Each 1% above 100% Energy Recharge that the Raiden Shogun possesses grants her: \n\t\t1. 0.6% greater Energy restoration from Musou Isshin \n\t\t2. 0.4% Electro DMG Bonus"]
    allPreserver = ["Unlocked Automatically", "Mora expended when ascending Swords and Polearms is decreased by 50%."]

    print("Skill Talents: ")
    print(" - Origin")
    for i in enumerate(origin, start=1):
        print("\t", *i, sep=". ")
    print("\n - Transcendence: Baleful Omen")
    for ii in enumerate(balefulOmen, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Eye of Stormy Judgment")
    for iii in enumerate(eyeOfStormyJudgment, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Secret Art: Musou Shinsetsu")
    for iv in enumerate(musouShinsetsu, start=1):
        print("\t", *iv, sep=". ")
    print("\t - Musou Isshin")
    for v in enumerate(musouIsshin, start=1):
        print("\t\t", *v, sep=". ")
    print("\t - Chakra Desiderata")
    for vi in enumerate(chakraDesiderata, start=1):
        print("\t\t", *vi, sep=". ")
    print("\nPassive: ")
    print(" - Wishes Unnumbered")
    for vii in enumerate(wishesUnnumbered, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Enlightened One")
    for viii in enumerate(enlightenedOne, start=1):
        print("\t", *viii, sep=". ")
    print("\n - All-Preserver")
    for ix in enumerate(allPreserver, start=1):
        print("\t", *ix, sep=". ")


def razor():
    res = input("What kind of help do you need with Razor? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return razorBuild()
    elif res == "b":
        return razorConst()
    elif res == "c":
        return razorAbility()
    else:
        error()
        return razor()


def razorBuild():
    weapon = ["wolf's gravestone", "serpent spine"]
    altWeapon = ["snow-tombed starsilver", "prototype archaic"]
    artifact = ["4x pale flame", "4x gladiator's finale"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Energy Recharge"],
                     ["Physical DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Flat ATK, Energy Recharge"]]

    print("Physical DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece pale flame: \n\t1. Physical DMG +25% \n\t2. When an Elemental Skill hits an opponent, ATK is increased by 9% for 7s. This effect stacks up to 2 times and can be triggered once every 0.3s. Once 2 stacks are reached, the 2-set effect is increased by 100%.")
    print(
        "\t- The 4 piece gladiator's finale: \n\t1. ATK +18% \n\t2. If the wielder of this artifact set uses a Sword, Claymore or Polearm, increases their Normal Attack DMG by 35%.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def razorConst():
    wolfsInstinct = ["Constellation Lv. 1",
                     "Picking up an Elemental Orb or Particle increases Razor's DMG by 10% for 8s."]
    suppression = ["Constellation Lv. 2",
                   "Increases CRIT Rate against enemies with less than 30% HP by 10%."]
    soulCompanion = ["Constellation Lv. 3",
                     "Increases the Level of Lightning Fang by 3.",
                     "Maximum upgrade level is 15."]
    bite = ["Constellation Lv. 4",
            "When casting Claw and Thunder (Press), enemies hit will have their DEF decreased by 15% for 7s."]
    sharpenedClaws = ["Constellation Lv. 5",
                      "Increase the Level of Claw and Thunder by 3.",
                      "Maximum upgrade level is 15."]
    lupusFulguris = ["Constellation Lv. 6",
                     "Every 10s, Razor's sword charges up, causing the next Normal Attack to release lightning that deals 100% of Razor's ATK as Electro DMG.",
                     "When Razor is not using Lightning Fang, a lightning strike on an enemy will grant Razor an Electro Sigil for Claw and Thunder."]

    print("Razor's Constellations:")
    print(" - Wolf's Instinct")
    for i in enumerate(wolfsInstinct, start=1):
        print("\t", *i, sep=". ")
    print("\n - Suppression")
    for ii in enumerate(suppression, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Soul Companion")
    for iii in enumerate(soulCompanion, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Bite")
    for iv in enumerate(bite, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Sharpened Claws")
    for v in enumerate(sharpenedClaws, start=1):
        print("\t", *v, sep=". ")
    print("\n - Lupus Fulguris")
    for vi in enumerate(lupusFulguris, start=1):
        print("\t", *vi, sep=". ")


def razorAbility():
    steelFang = [
        "Normal Attack - Performs up to 4 consecutive strikes.",
        "Charged Attack - Drains Stamina over time to perform continuous swirling attacks against all nearby enemies. At end of the sequence, perform a more powerful slash.",
        "Plunging Attack - Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    clawAndThunder = [
        "Elemental Skill",
        "Hunts his prey using the techniques taught to him by his master and his Lupical."]
    pressClawAndThunder = [
        "Swings the Thunder Wolf Claw, dealing Electro DMG to enemies in front of Razor.",
        "Upon striking an enemy, Razor will gain an Electro Sigil, which increases his Energy Recharge rate.",
        "Razor can have up to 3 Electro Sigils simultaneously, and gaining a new Electro Sigil refreshes their duration."]
    holdClawAndThunder = [
        "Gathers Electro energy to unleash a lightning storm over a small AoE, causing massive Electro DMG, and clears all of Razor's Electro Sigils.",
        "Each Electro Sigil cleared in this manner will be converted into Energy for Razor."]
    lightningFang = [
        "Summons the Wolf Within which deals Electro DMG to all nearby opponents. This clears all of Razor's Electro Sigils, which will be converted into elemental energy for him.",
        "The Wolf Within will fight alongside Razor for the skill's duration."]
    theWolfWithin = [
        "Strikes alongside Razor's normal attacks, dealing Electro DMG.",
        "Raises Razor's ATK SPD and Electro RES.",
        "Causes Razor to be immune to DMG inflicted by the Electro-Charged status.",
        "Disables Razor's Charged Attacks.",
        "Increases Razor's resistance to interruption"]
    awakening = [
        "Unlocked at Ascension 1",
        "Decreases Claw and Thunder's CD by 18%.",
        "Using Lightning Fang resets the CD of Claw and Thunder."]
    hunger = [
        "Unlocked at Ascension 4",
        "When Razor's Energy is below 50%, increases Energy Recharge by 30%."]
    wolvensprint = [
        "Unlocked Automatically",
        "Decreases all party member's sprinting Stamina Consumption by 20%."]

    print("Skill Talents: ")
    print(" - Steel Fang")
    for i in enumerate(steelFang, start=1):
        print("\t", *i, sep=". ")
    print("\n - Claw and Thunder")
    for ii in enumerate(clawAndThunder, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Press:")
    for iii in enumerate(pressClawAndThunder, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Hold:")
    for iv in enumerate(holdClawAndThunder, start=1):
        print("\t\t", *iv, sep=". ")
    print("\n - Lightning Fang")
    for v in enumerate(lightningFang, start=1):
        print("\t", *v, sep=". ")
    print("\t - The Wolf Within")
    for vi in enumerate(theWolfWithin, start=1):
        print("\t\t", *vi, sep=". ")
    print("\nPassive: ")
    print(" - Awakening")
    for vii in enumerate(awakening, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Hunger")
    for viii in enumerate(hunger, start=1):
        print("\t", *viii, sep=". ")
    print("\n - Wolvensprint")
    for ix in enumerate(wolvensprint, start=1):
        print("\t", *ix, sep=". ")


def rosaria():
    res = input(
        "What kind of help do you need with Rosaria? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return rosariaBuild()
    elif res == "b":
        return rosariaConst()
    elif res == "c":
        return rosariaAbility()
    else:
        error()
        return rosaria()


def rosariaBuild():
    weapon = ["staff of homa", "engulfing lightning"]
    altWeapon = ["deathmatch", "the catch"]
    artifact = ["4x noblesse oblige", "2x noblesse oblige, 2x blizzard strayer"]
    artifactStats = [["Flat ATK", "ATK%, CRIT DMG, Elemental Mastery, CRIT Rate"],
                     ["Flat HP", "ATK%, CRIT DMG, CRIT Rate, Elemental Mastery"],
                     ["ATK%", "CRIT DMG, Energy Recharge, Elemental Mastery, CRIT Rate"],
                     ["Cryo DMG Bonus%", "ATK%, CRIT DMG, CRIT Rate, Energy Recharge / Elemental Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG, ATK%, Energy Recharge, Elemental Mastery"]]

    print("Cryo Sub-DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")
    print("\t- The 2 piece set will increase your cryo damage by 15% and increase your elemental burst damage by 20%\n")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def rosariaConst():
    unholyRevelation = [
        "Constellation Lv. 1",
        "When Rosaria deals a CRIT Hit, her ATK SPD increases by 10% and her Normal Attack DMG increases by 10% for 4s."]
    landWithoutPromise = [
        "Constellation Lv. 2",
        "The duration of the Ice Lance created by Rites of Termination is increased by 4s."]
    theWagesOfSin = [
        "Constellation Lv. 3",
        "Increases the Level of Ravaging Confession by 3.",
        "Maximum upgrade level is 15."]
    painfulGrace = [
        "Constellation Lv. 4",
        "Ravaging Confession's CRIT Hits regenerate 5 Energy for Rosaria.",
        "Can only be triggered once each time Ravaging Confession is cast."]
    lastRites = [
        "Constellation Lv. 5",
        "Increase the Level of Rites of Termination by 3.",
        "Maximum upgrade level is 15."]
    divineRetribution = [
        "Constellation Lv. 6",
        "Rites of Termination's attack decreases opponents' Physical RES by 20% for 10s."]

    print("Razor's Constellations:")
    print(" - Unholy Revelation")
    for i in enumerate(unholyRevelation, start=1):
        print("\t", *i, sep=". ")
    print("\n - Land Without Promise")
    for ii in enumerate(landWithoutPromise, start=1):
        print("\t", *ii, sep=". ")
    print("\n - The Wages of Sin")
    for iii in enumerate(theWagesOfSin, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Painful Grace")
    for iv in enumerate(painfulGrace, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Last Rites")
    for v in enumerate(lastRites, start=1):
        print("\t", *v, sep=". ")
    print("\n - Divine Retribution")
    for vi in enumerate(divineRetribution, start=1):
        print("\t", *vi, sep=". ")


def rosariaAbility():
    spearOfTheChurch = [
        "Normal Attack - Performs up to 5 consecutive spear strikes.",
        "Charged Attack - Consumes a certain amount of Stamina to lunge forward, dealing damage to enemies along the way.",
        "Plunging Attack - Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    ravagingConfession = [
        "Elemental Skill",
        "Rosaria swiftly shifts her position to appear behind her opponent, then stabs and slashes them with her polearm, dealing Cryo DMG.",
        "This ability cannot be used to travel behind opponents of a larger build."]
    ritesOfTermination = [
        "Elemental Burst",
        "Rosaria's unique take on this prayer ritual: First, she swings her weapon to slash surrounding opponents; then, she summons a frigid Ice Lance that strikes the ground. Both actions deal Cryo DMG.",
        "While active, the Ice Lance periodically releases a blast of cold air, dealing Cryo DMG to surrounding opponents."]
    reginaProbationum = [
        "Unlocked at Ascension 1",
        "When Rosaria strikes an opponent from behind using Ravaging Confession, Rosaria's CRIT Rate increases by 12% for 5s."]
    shadowSamaritan = [
        "Unlocked at Ascension 4",
        "Casting Rites of Termination increases CRIT Rate of all nearby party members (except Rosaria herself) by 15% of Rosaria's CRIT Rate for 10s.",
        "CRIT Rate Bonus gained this way cannot exceed 15%."]
    nightWalk = [
        "Unlocked Automatically",
        "At night (18:00 - 6:00), increases the Movement SPD of your own party members by 10%.",
        "Does not take effect in Domains, Trounce Domains, or Spyral Abyss. Not stackable with Passive Talents that provide the exact same effects."]

    print("Skill Talents: ")
    print(" - Spear of the Church")
    for i in enumerate(spearOfTheChurch, start=1):
        print("\t", *i, sep=". ")
    print("\n - Ravaging Confession")
    for ii in enumerate(ravagingConfession, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Rites of Termination")
    for iii in enumerate(ritesOfTermination, start=1):
        print("\t", *iii, sep=". ")
    print("\nPassive: ")
    print(" - Regina Probationum")
    for iv in enumerate(reginaProbationum, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Shadow Samaritan")
    for v in enumerate(shadowSamaritan, start=1):
        print("\t", *v, sep=". ")
    print("\n - Night Walk")
    for vi in enumerate(nightWalk, start=1):
        print("\t", *vi, sep=". ")


def sara():
    res = input("What kind of help do you need with Sara? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return saraBuild()
    elif res == "b":
        return saraConst()
    elif res == "c":
        return saraAbility()
    else:
        error()
        return sara()


def saraBuild():
    weapon = ["elegy for the end", "skyward harp"]
    altWeapon = ["alley hunter", "sacrificial bow"]
    artifact = ["4x noblesse oblige", "4x emblem of severed fate"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Energy Recharge"],
                     ["Electro DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Elemental Mastery, Energy Recharge"]]

    print("Electro Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")
    print(
        "\t- The 4 piece emblem of severed fate: \n\t1. Energy Recharge +20% \n\t2. Increases Elemental Burst DMG by 25% of Energy Recharge. A maximum of 75% bonus DMG can be obtained in this way.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def saraConst():
    crowsEye = [
        "Constellation Lv. 1",
        "When Tengu Juurai grant characters ATK Bonuses or hits opponents, the CD of Tengu Stormcall is decreased by 1s.",
        "This effect can be triggered once every 3s."]
    darkWings = [
        "Constellation Lv. 2",
        "Unleashing Tengu Stormcall will leave a weaker Crowfeather at Kujou Sara's original position that will deal 30% of its original DMG."]
    theWarWithin = [
        "Constellation Lv. 3",
        "Increases the Level of Subjugation: Koukou Sendou by 3.",
        "Maximum upgrade level is 15."]
    conclusiveProof = [
        "Constellation Lv. 4",
        "The number of Tengu Juurai: Stormcluster released by Subjugation: Koukou Sendou is increased to 6."]
    spellsinger = [
        "Constellation Lv. 5",
        "Increase the Level of Tengu Stormcall by 3.",
        "Maximum upgrade level is 15."]
    sinOfPride = [
        "Constellation Lv. 6",
        "The Electro DMG of characters who have had their ATK increased by Tengu Juurai has its Crit DMG increased by 60%."]

    print("Sara's Constellations:")
    print(" - Crow's Eye")
    for i in enumerate(crowsEye, start=1):
        print("\t", *i, sep=". ")
    print("\n - Dark Wings")
    for ii in enumerate(darkWings, start=1):
        print("\t", *ii, sep=". ")
    print("\n - The War Within")
    for iii in enumerate(theWarWithin, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Conclusive Proof")
    for iv in enumerate(conclusiveProof, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Spellsinger")
    for v in enumerate(spellsinger, start=1):
        print("\t", *v, sep=". ")
    print("\n - Sin of Pride")
    for vi in enumerate(sinOfPride, start=1):
        print("\t", *vi, sep=". ")


def saraAbility():
    tenguBowmanship = [
        "Normal Attack - Performs up to 5 consecutive shots with a bow.",
        "Charged Attack - Perform a more precise Aimed Shot with increased DMG. While aiming, crackling lightning will accumulate on the arrowhead. An arrow fully charged with the storm's might will deal Electro DMG. When in the Crowfeather Cover state, a fully-charged arrow will leave a Crowfeather behind after it hits.",
        "Plunging Attack - Fires off a shower of arrows in mid-air before falling and striking the ground, dealing AoE DMG upon impact."]
    tenguStormcall = [
        "Elemental Skill",
        "Retreats rapidly with the speed of a tengu, summoning the protection of the Crowfeather. Gains Crowfeather Cover for 18s, and when Kujou Sara fires a fully-charged Aimed Shot, Crowfeather Cover will be consumed, and will leave a Crowfeather at the target location.",
        "Crowfeathers will trigger Tengu Juurai: Ambush after a short time, dealing Electro DMG and granting the active character within its AoE an ATK Bonus based on Kujou Sara's Base ATK.",
        "The ATK Bonuses from different Tengu Juurai will not stack, and their effects and duration will be determined by the last Tengu Juurai to take effect."]
    koukouSendou = [
        "Elemental Burst",
        "Casts down Tengu Juurai: Titanbreaker, dealing AoE Electro DMG. Afterwards, Tengu Juurai: Titanbreaker spreads out into 4 consecutive bouts of Tengu Juurai: Stormcluster, dealing AoE Electro DMG.",
        "Tengu Juurai: Titanbreaker and Tengu Juurai: Stormcluster can provide the active character within their AoE with the same ATK Bonus as given by the Elemental Skill, Tengu Stormcall.",
        "The ATK Bonus provided by various kinds of Tengu Juurai will not stack, and their effects and duration will be determined by the last Tengu Juurai to take effect."]
    immovableWill = [
        "Unlocked at Ascension 1",
        "While in the Crowfeather Cover state provided by Tengu Stormcall, Aimed Shot charge times are decreased by 60%."]
    decorum = [
        "Unlocked at Ascension 4",
        "When Tengu Juurai: Ambush hits opponents, Kujou Sara will restore 1.2 Energy to all party members for every 100% Energy Recharge she has. This effect can be triggered once every 3s."]
    landSurvey = [
        "Unlocked Automatically",
        "When dispatched on an expedition in Inazuma, time consumed is reduced by 25%."]

    print("Skill Talents: ")
    print(" - Tengu Bowmanship")
    for i in enumerate(tenguBowmanship, start=1):
        print("\t", *i, sep=". ")
    print("\n - Tengu Stormcall")
    for ii in enumerate(tenguStormcall, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Subjugation: Koukou Sendou")
    for iii in enumerate(koukouSendou, start=1):
        print("\t", *iii, sep=". ")
    print("\nPassive: ")
    print(" - Immovable Will")
    for iv in enumerate(immovableWill, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Decorum")
    for v in enumerate(decorum, start=1):
        print("\t", *v, sep=". ")
    print("\n - Land Survey")
    for vi in enumerate(landSurvey, start=1):
        print("\t", *vi, sep=". ")


def sayu():
    res = input("What kind of help do you need with Sayu? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return sayuBuild()
    elif res == "b":
        return sayuConst()
    elif res == "c":
        return sayuAbility()
    else:
        error()
        return sayu()


def sayuBuild():
    weapon = ["wolf's gravestone", "skyward pride"]
    altWeapon = ["sacrificial greatsword", "katsuragikiri nagamasa"]
    artifact = ["4x viridescent venerer"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT Rate, CRIT DMG, ATK%, Energy Recharge"],
                     ["ATK%/Elemental Mastery", "CRIT Rate, CRIT DMG, ATK%/Elemental Mastery, Energy Recharge"],
                     ["Anemo DMG Bonus/Elemental Mastery",
                      "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery / Energy Recharge"],
                     ["Elemental Mastery/Healing Bonus",
                      "CRIT DMG, CRIT Rate, ATK%/Elemental Mastery, Energy Recharge"]]

    print("Anemo DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece viridescent venerer: \n\t1. Gain a 15% Anemo DMG Bonus. \n\t2. Increases Swirl DMG by 60%. Decreases opponent's Elemental RES to the element infused in the Swirl by 40% for 10s.")

    print("\n The format of the artifacts start are:")
    print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
    print(" - The recommended artifact stats:")
    for iii in enumerate(artifactStats, start=1):
        print("\t", *iii, sep=". ")


def sayuConst():
    multiTaskNoJutsu = [
        "Constellation Lv. 1",
        "The Muji-Muji Daruma created by Yoohoo Art: Mujina Flurry will ignore HP limits and can simultaneously attack nearby opponents and heal characters."]
    egressPrep = [
        "Constellation Lv. 2",
        "Yoohoo Art: Fuuin Dash gains the following effects: \n\t\t1. DMG of Fuufuu Whirlwind Kick in Tapping (mobile)/Press (PC & PlayStation) Mode increased by 3.3%. \n\t\t2. Every 0.5s in the Fuufuu Windwheel state will increase the DMG of this Fuufuu Whirlwind Kick by 3.3%. The maximum DMG increase possible through this method is 66%."]
    theBunshinCanHandleIt = [
        "Constellation Lv. 3",
        "Increases the Level of Yoohoo Art: Mujina Flurry by 3.",
        "Maximum upgrade level is 15."]
    newAndImproved = [
        "Constellation Lv. 4",
        "Sayu recovers 1.2 Energy when she triggers a Swirl reaction.",
        "This effect occurs once every 2s."]
    speedComesFirst = [
        "Constellation Lv. 5",
        "Increase the Level of Yoohoo Art: Fuuin Dash by 3.",
        "Maximum upgrade level is 15."]
    sleepOClock = [
        "Constellation Lv. 6",
        "The Muji-Muji Daruma created by Sayu's Yoohoo Art: Mujina Flurry will now also benefit from her Elemental Mastery.",
        "Each point of Sayu's Elemental Mastery will produce the following effects: \n\t\t1. Increases the damage dealt by the Muji-Muji Daruma's attacks by 0.2% ATK. A maximum of 400% ATK can be gained via this method. \n\t\t2. Increases the HP restored by the Muji-Muji Daruma by 3. A maximum of 6,000 additional HP can be restored in this manner."]

    print("Sayu's Constellations:")
    print(" - Multi-Task no Jutsu")
    for i in enumerate(multiTaskNoJutsu, start=1):
        print("\t", *i, sep=". ")
    print("\n - Egress Prep")
    for ii in enumerate(egressPrep, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Eh, the Bunshin Can Handle It")
    for iii in enumerate(theBunshinCanHandleIt, start=1):
        print("\t", *iii, sep=". ")
    print("\n - Skiving: New and Improved")
    for iv in enumerate(newAndImproved, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Speed Comes First")
    for v in enumerate(speedComesFirst, start=1):
        print("\t", *v, sep=". ")
    print("\n - Sleep O'Clock")
    for vi in enumerate(sleepOClock, start=1):
        print("\t", *vi, sep=". ")


def sayuAbility():
    shuumatsubanNinjaBlade = [
        "Normal Attack - Perform up to 4 consecutive strikes.",
        "Charged Attack - Drains Stamina over time to perfom continuous spinning attacks against all nearby opponents. At the end of the sequence, perform a more powerful slash.",
        "Plunging Attack - Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    fuuinDash = [
        "Elemental Skill",
        "The special technique of the Yoohoo Ninja Arts!",
        "Sayu curls up into a rolling Fuufuu Windwheel and smashes into opponents at high speed, dealing Anemo DMG.",
        "When the duration ends, she unleashes a Fuufuu Whirlwind Kick, dealing AoE Anemo DMG."]
    pressFuuinDash = [
        "Enters the Fuufuu Windwheel state, rolling forward a short distance before using the Fuufuu Whirlwind Kick."]
    holdFuuinDash = [
        "Rolls about continously in the Fuufuu Windwheel state, increasing Sayu's resistance to interruption while within that state.",
        "During this time, Sayu can control the direction of her roll, and can use the skill again to end her Windwheel state early and unleash a stronger version of the Fuufuu Whirlwind Kick.",
        "The Hold version of this skill can trigger Elemental Absorption. This skill has a maximum duration of 10s and enters CD once its effects end. The longer Sayu remains in her Windwheel state, the longer the CD."]
    elementalAbsorption = [
        "If Sayu comes into contact with Hydro, Pyro, Cryo and Electro while in her Windwheel state, she will deal additional elemental DMG of that type.",
        "Elemental Absorption may only occur once per use of this skill."]
    mujinaFlurry = [
        "Elemental Burst",
        "The other super special technique of the Yoohoo Ninja Arts!",
        "It summons a pair of helping hands for Sayu.",
        "Deals Anemo DMG to nearby opponents and heals all nearby party members. The amount of HP restored is based on Sayu's ATK. This skill then summons a Muji-Muji Daruma.",
        "If there are no opponents nearby, it will heal active characters nearby even if they have 70% HP or more."
    ]
    mujiMujiDaruma = [
        "At specific intervals, the Daruma will take one of several actions based on the situation around it: \n\t\t1. If the HP of nearby characters is above 70%, it will attack a nearby opponent, dealing Anemo DMG. \n\t\t2. If there are active characters with 70% or less HP nearby, it will heal the active character with the lowest percentage HP left."
    ]
    someoneMoreCapable = [
        "Unlocked at Ascension 1"
        "When Sayu triggers a Swirl reaction while active, she heals all your characters and nearby allies for 300 HP. She will also heal an additional 1.2 HP for every point of Elemental Mastery she has.",
        "This effect can be triggered once every 2s."
    ]
    noWorkToday = [
        "Unlocked at Ascension 4",
        "The Muji-Muji Daruma created by Yoohoo Art: Mujina Flurry gains the following effects: \n\t\t1. When healing a character, it will also heal characters near that healed character for 20% the amount of HP. \n\t\t2. Increases the AoE of its attack against opponents."
    ]
    silencersSecret = [
        "Unlocked Automatically",
        "When Sayu is in the party, your characters will not startle Crystalflies and certain other animals when getting near them.",
        "Check the 'Other' sub-category of the 'Living Beings/Wildlife' section in the Archive for creatures this skill works on."
    ]

    print("Skill Talents: ")
    print(" - Shuumatsuban Ninja Blade")
    for i in enumerate(shuumatsubanNinjaBlade, start=1):
        print("\t", *i, sep=". ")
    print("\n - Yoohoo Art: Fuuin Dash")
    for ii in enumerate(fuuinDash, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Press:")
    for iii in enumerate(pressFuuinDash, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Hold")
    for iv in enumerate(holdFuuinDash, start=1):
        print("\t\t", *iv, sep=". ")
    print("\t - Elemental Absorption")
    for v in enumerate(elementalAbsorption, start=1):
        print("\t\t", *v, sep=". ")
    print("\n - Yoohoo Art: Mujina Flurry")
    for vi in enumerate(mujinaFlurry, start=1):
        print("\t", *vi, sep=". ")
    print("\t - Muji-Muji Daruma")
    for vii in enumerate(mujiMujiDaruma, start=1):
        print("\t\t", *vii, sep=". ")
    print("\nPassive: ")
    print(" - Someone More Capable")
    for viii in enumerate(someoneMoreCapable, start=1):
        print("\t", *viii, sep=". ")
    print("\n - No Work Today!")
    for ix in enumerate(noWorkToday, start=1):
        print("\t", *ix, sep=". ")
    print("\n - Yoohoo Art: Silencer's Secret")
    for x in enumerate(silencersSecret, start=1):
        print("\t", *x, sep=". ")


def sucrose():
    res = input(
        "What kind of help do you need with Sucrose? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return sucroseBuild()
    elif res == "b":
        return sucroseConst()
    elif res == "c":
        return sucroseAbility()
    else:
        error()
        return sucrose()


def sucroseBuild():
    weapon = ["sacrificial fragments", "mappa mare"]
    altWeapon = ["the widsith", "the thrilling tales of dragon slayers"]
    artifact = ["4x viridescent venerer"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["Elemental Mastery/Energy Recharge",
                      "CRIT DMG, CRIT Rate, Flat ATK, Elemental Mastery/ Energy Recharge"],
                     ["Anemo DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["Elemental Mastery/Healing Bonus", "CRIT DMG, ATK%, CRIT Rate, Flat ATK"]]

    print("Anemo Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece viridescent venerer: \n\t1. Gain a 15% Anemo DMG Bonus. \n\t2. Increases Swirl DMG by 60%. Decreases opponent's Elemental RES to the element infused in the Swirl by 40% for 10s.")

    utility.artifactFormat(artifactStats)


def sucroseConst():
    const1 = ["Clustered Vacuum Field", "Constellation Lv. 1",
              "Astable Anemohypostasis Creation - 6308 gains 1 additional charge."]
    const2 = ["Beth: Unbound Form", "Constellation Lv. 2",
              "The duration of Forbidden Creation - Isomer 75 / Type II is increased by 2s."]
    const3 = ["Flawless Alchemistress", "Constellation Lv. 3",
              "Increases the Level of Astable Anemohypostasis Creation - 6308 by 3.", "Maximum upgrade level is 15."]
    const4 = ["Alchemania", "Constellation Lv. 4",
              "Every 7 Normal and Charged Attacks, Sucrose will reduce the CD of Astable Anemohypostasis Creation - 6308 by 1-7s."]
    const5 = ["Caution: Standard Flask", "Constellation Lv. 5",
              "Increase the Level of Forbidden Creation - Isomer 75 / Type II by 3.", "Maximum upgrade level is 15."]
    const6 = ["Chaotic Entropy", "Constellation Lv. 6",
              "If Forbidden Creation - Isomer 75 / Type II triggers an Elemental Absorption, all party members gain a 20% Elemental DMG Bonus for the corresponding absorbed element during its duration."]

    print("Sucrose's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def sucroseAbility():
    windSpiritCreation = [
        "Normal Attack - Performs up to 4 attacks using Wind Spirits, dealing Anemo DMG.",
        "Charged Attack - Consumes a certain amount of Stamina and deals AoE Anemo DMG after a short casting time.",
        "Plunging Attack - Calling upon the power of her Wind Spirits, Sucrose plunges towards the ground from mid-air, damaging all enemies in her path. Deals AoE Anemo DMG upon impact with the ground."]
    astableAnemohypostasis = [
        "Elemental Skill",
        "Creates a small Wind Spirit that deals Anemo DMG to enemies in an AoE, pulling them towards the location of the Wind Spirit before launching them."]
    isomer75 = [
        "Elemental Burst",
        "Sucrose hurls an unstable concoction that creates a Large Wind Spirit. While it persists, the Large Wind Spirit will continuously pull and launch nearby enemies, dealing AoE Anemo DMG."]
    elementalAbsorption = [
        "If the Wind Spirit comes into contact with Hydro / Pyro / Cryo / Electro elements, it will deal additional DMG of that type.",
        "Elemental Absorption may only occur once per use."]
    catalystConversion = ["Unlocked at Ascension 1",
                          "When Sucrose triggers a Swirl effect, characters in the party with the matching element have their Elemental Mastery increased by 50 for 8s."]
    mollisFavonius = ["Unlocked at Ascension 4",
                      "When Astable Anemohypostatis Creation - 6308 or Forbidden Creation - Isomer 75 / Type II hit an enemy, increases other party member's Elemental Mastery based on 20% of Sucrose's Elemental Mastery for 8s."]
    astableInvention = ["Unlocked Automatically",
                        "When Sucrose crafts Character and Weapon Enhancement Materials, she has a 10% to obtain double the product."]

    print("Skill Talents: ")
    print(" - Wind Spirit Creation")
    for i in enumerate(windSpiritCreation, start=1):
        print("\t", *i, sep=". ")
    print("\n - Astable Anemohypostasis Creation - 6308")
    for ii in enumerate(astableAnemohypostasis, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Forbidden Creation - Isomer 75 / Type II")
    for iii in enumerate(isomer75, start=1):
        print("\t", *iii, sep=". ")
    print("\t - Elemental Absorption")
    for iv in enumerate(elementalAbsorption, start=1):
        print("\t\t", *iv, sep=". ")
    print("\nPassive: ")
    print(" - Catalyst Conversion")
    for v in enumerate(catalystConversion, start=1):
        print("\t", *v, sep=". ")
    print("\n - Mollis Favonius")
    for vi in enumerate(mollisFavonius, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Astable Invention")
    for vii in enumerate(astableInvention, start=1):
        print("\t", *vii, sep=". ")


def tartaglia():
    res = input("What kind of help do you need with Childe? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return tartagliaBuild()
    elif res == "b":
        return tartagliaConst()
    elif res == "c":
        return tartagliaAbility()
    else:
        error()
        return tartaglia()


def tartagliaBuild():
    weapon = ["thundering pulse", "polar star"]
    altWeapon = ["the viridescent hunt", "rust"]
    artifact = ["4x heart of depth", "2x noblesse oblige, 2x heart of depth"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery / Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["ATK%", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["Hydro DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Flat ATK"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Flat ATK, Elemental Mastery/Energy Recharge"]]

    print("Hydro DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece heart of depth: \n\t1. Hydro DMG Bonus +15% \n\t2. After using Elemental Skill, increases Normal Attack and Charged Attack DMG by 30% for 15s.")
    print(
        "\t- The 2 piece set will increase your hydro damage by 15% and increase your elemental burst damage by 20%\n")

    utility.artifactFormat(artifactStats)


def tartagliaConst():
    const1 = ["Foul Legacy: Tide Withholder", "Constellation Lv. 1",
              "Decreases the CD of Foul Legacy: Raging Tide by 20%."]
    const2 = ["Foul Legacy: Understream", "Constellation Lv. 2",
              "When opponents affected by Riptide are defeated, Tartaglia regenerates 4 Elemental Energy."]
    const3 = ["Abyssal Mayhem: Vortex of Turmoil", "Constellation Lv. 3",
              "Increases the Level of Foul Legacy: Raging Tide by 3.",
              "Maximum upgrade level is 15."]
    const4 = ["Abyssal Mayhem: Hydrosprout", "Constellation Lv. 4",
              "If Tartaglia is in Foul Legacy: Raging Tide's Melee Stance, triggers Riptide Slash against opponents on the field affected by Riptide every 4s, otherwise, triggers Riptide Flash.",
              "Riptide Slashes and Riptide Flashes triggered by this Constellation effect are not subject to the time intervals that would typically apply to these two Riptide effects, nor do they have any effect on those time intervals."]
    const5 = ["Havoc: Formless Blade", "Constellation Lv. 5", "Increase the Level of Havoc: Obliteration by 3.",
              "Maximum upgrade level is 15."]
    const6 = ["Havoc: Annihilation", "Constellation Lv. 6",
              "When Havoc: Obliteration is cast in Melee Stance, the CD of Foul Legacy: Raging Tide is reset.",
              "This effect will only take place once Tartaglia returns to his Ranged Stance."]

    print("Tartaglia's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def tartagliaAbility():
    cuttingTorrent = [
        "Normal Attack - Performs up to 6 consecutive shots with a bow.",
        "Charged Attack - Perform a more precise Aimed Shot with increased DMG. While aiming, the power of Hydro will accumulate on the arrowhead. An arrow fully charged with the torrent will deal Hydro DMG and apply Riptide status.",
        "Riptide - Opponents affected by Riptide will suffer from AoE Hydro DMG effects when attacked by Tartaglia in various ways. DMG dealt in this way is considered Normal Attack DMG. \n\t\tRiptide Flash: A fully-charged Aimed Shot that hits an opponent affected by Riptide deals consecutive bouts of AoE DMG. Can occur once every 0.7s. \n\t\tRiptide Burst: Defeating an opponent affected by Riptide created a Hydro burst that inflicts the Riptide status on nearby opponents hit."
        "Plunging Attack - Fires off a shower of arrows in mid-air before falling and striking the ground, dealing AoE DMG upon impact. When Tartaglia is in Foul Legacy: Raging Tide's Melee Stance, he cannot perform a plunging attack."]
    ragingTide = [
        "Elemental Skill",
        "After 30s, or when the ability is unleashed again, this skill will end. Tartaglia will return to his Ranged Stance and this ability will enter CD. The longer Tartaglia stays in his Melee Stance, the longer the CD.",
        "If the return to a ranged stance occurs automatically after 30s, the CD is even longer."
        "Unleashes a set of weaponry made of pure water, dealing Hydro DMG to surrounding opponents and entering a Melee Stance.",
        "In this Stance, Tartaglia's Normal and Charged Attacks change as follows:"]
    normalRagingTide = [
        "Performs up to 6 consecutive Hydro strikes."
    ]
    chargedRagingTide = [
        "Consumes a certain amount of Stamina to unleash a cross slash, dealing Hydro DMG."
    ]
    riptideRagingTide = [
        "Hitting an opponent affected by Riptide with a melee attack unleashes a Riptide Slash that deals AoE Hydro DMG. DMG dealt in this way is considered Elemental Skill DMG, and can only occur once every 1.5s."
    ]
    obliteration = [
        "Elemental Burst",
        "Performs different attacks based on what stance Tartaglia is in when casting."]
    rangedStance = [
        "Swiftly fires a Hydro-imbued magic arrow, dealing AoE Hydro DMG and applying the Riptide status.",
        "Returns a portion of its Energy Cost after use."]
    meleeStance = [
        "Performs a slash with a large AoE, dealing massive Hydro DMG to all surrounding opponents, which triggers Riptide Blast."]
    riptideBlast = [
        "When the obliterating waters hit an opponent affected by Riptide, it clears their Riptide status and triggers a Hydro Explosion that deals AoE Hydro DMG.",
        "DMG dealt in this way is considered Elemental Burst DMG."]
    neverEnding = ["Unlocked at Ascension 1",
                   "Extends Riptide duration by 8s."]
    swordOfTorrents = ["Unlocked at Ascension 4",
                       "When Tartaglia is in Foul Legacy: Raging Tide's Melee Stance, or if his Normal and Charged Attacks do CRIT DMG, they will apply the Riptide status effect on the hit enemy."]
    masterOfWeaponry = ["Unlocked Automatically",
                        "Increases your own party member's Normal Attack Level by 1."]

    print("Skill Talents: ")
    print(" - Cutting Torrent")
    for i in enumerate(cuttingTorrent, start=1):
        print("\t", *i, sep=". ")
    print("\n - Foul Legacy: Raging Tide")
    for ii in enumerate(ragingTide, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Normal Attack")
    for iii in enumerate(normalRagingTide, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Charged Attack")
    for iv in enumerate(chargedRagingTide, start=1):
        print("\t\t", *iv, sep=". ")
    print("\t - Riptide Slash")
    for v in enumerate(riptideRagingTide, start=1):
        print("\t\t", *v, sep=". ")
    print("\n - Havoc: Obliteration")
    for vi in enumerate(obliteration, start=1):
        print("\t", *vi, sep=". ")
    print("\t - Ranged Stance: Flash of Havoc")
    for vii in enumerate(rangedStance, start=1):
        print("\t\t", *vii, sep=". ")
    print("\t - Melee Stance: Light Obliteration")
    for viii in enumerate(meleeStance, start=1):
        print("\t\t", *viii, sep=". ")
    print("\t - Riptide Blast")
    for ix in enumerate(riptideBlast, start=1):
        print("\t\t", *ix, sep=". ")
    print("\nPassive: ")
    print(" - Never Ending")
    for x in enumerate(neverEnding, start=1):
        print("\t", *x, sep=". ")
    print("\n - Sword of Torrents")
    for xi in enumerate(swordOfTorrents, start=1):
        print("\t", *xi, sep=". ")
    print("\n - Master of Weaponry")
    for xii in enumerate(masterOfWeaponry, start=1):
        print("\t", *xii, sep=". ")


def traveler():
    res = input(
        "Which traveler do you need help with? \n[a] Anemo Traveler \n[b] Geo Traveler \n[c] Electro Traveler \n> ")
    res.lower()
    if res == "a":
        return anemoTraveler()
    elif res == "b":
        return geoTraveler()
    elif res == "c":
        return electroTraveler()
    else:
        error()
        return traveler()


def anemoTraveler():
    res = input(
        "What kind of help do you need with Anemo Traveler? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return anemoBuild()
    elif res == "b":
        return anemoConst()
    elif res == "c":
        return anemoAbility()
    else:
        error()
        return anemoTraveler()


def anemoBuild():
    weapon = ["skyward blade", "favonius sword"]
    altWeapon = ["festering desire", "iron sting"]
    artifact = ["4x viridescent venerer"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Energy Recharge, Elemental Mastery"],
                     ["Anemo DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Elemental Mastery, Flat ATK"]]

    print("Anemo Sub-DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece viridescent venerer: \n\t1. Gain a 15% Anemo DMG Bonus. \n\t2. Increases Swirl DMG by 60%. Decreases opponent's Elemental RES to the element infused in the Swirl by 40% for 10s.")

    utility.artifactFormat(artifactStats)


def anemoConst():
    const1 = ["Raging Vortex", "Constellation Lv. 1", "Palm Vortex pulls in enemies within a 5m radius."]
    const2 = ["Uprising Whirlwind", "Constellation Lv. 2",
              "Increases Energy Recharge by 16%."]
    const3 = ["Sweeping Gust", "Constellation Lv. 3", "Increases the Level of Gust Surge by 3.",
              "Maximum upgrade level is 15."]
    const4 = ["Cherishing Breezes", "Constellation Lv. 4",
              "Reduces DMG taken while casting Palm Vortex by 10%."]
    const5 = ["Vortex Stellaris", "Constellation Lv. 5",
              "Increase the Level of Palm Vortex by 3."
              "Maximum upgrade level is 15."]
    const6 = ["Intertwined Winds", "Constellation Lv. 6",
              "Targets who take DMG from Gust Surge have their Anemo RES decreased by 20%.",
              "If an Elemental Absorption occurred, then their RES towards the corresponding Element is also decreased by 20%."]

    print("Anemo Traveler's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def anemoAbility():
    foreignIronwind = [
        "Normal Attack - Performs up to 5 consecutive strikes.",
        "Charged Attack - Consumes a certain amount of Stamina to unleash 2 rapid sword strikes.",
        "Plunging Attack -  Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    palmVortex = [
        "Elemental Skill",
        "Grasping the wind's might, you form a vortex of vacuum in your palm, causing continuous Anemo DMG to enemies in front of you.",
        "The vacuum vortex explodes when the skill duration ends, causing a greater amount of Anemo DMG over a larger area."]
    holdPalmVortex = [
        "DMG and AoE will gradually increase"
    ]
    elementalAbsorption1 = [
        "If the vortex comes in contact with Hydro/Pyro/Cryo/Electro elements, it will deal additional elemental DMG of that type.",
        "Elemental Absorption may only occur once per use."
    ]
    gustSurge = [
        "Elemental Burst",
        "Guiding the path of the wind currents, you summon a forward-moving tornado that pulls objects and opponents towards itself, dealing continuous Anemo DMG."]
    elementalAbsorption2 = [
        "If the tornado comes in contact with Hydro/Pyro/Cryo/Electro elements, it will deal additional elemental DMG of that type.",
        "Elemental Absorption may only occur once per use."]
    slittingWind = [
        "Unlocked at Ascension 1",
        "The last hit of a Normal Attack combo unleashes a wind blade, dealing 60% of ATK as Anemo DMG to all opponents in its path."]
    secondWind = [
        "Unlocked at Ascension 4",
        "Palm Vortex kills renegerate 2% HP for 5s. This effect can only occur once every 5s."]

    print("Skill Talents: ")
    print(" - Foreign Ironwind")
    for i in enumerate(foreignIronwind, start=1):
        print("\t", *i, sep=". ")
    print("\n - Palm Vortex")
    for ii in enumerate(palmVortex, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Hold")
    for iii in enumerate(holdPalmVortex, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Elemental Absorption")
    for iv in enumerate(elementalAbsorption1, start=1):
        print("\t\t", *iv, sep=". ")
    print("\n - Gust Surge")
    for v in enumerate(gustSurge, start=1):
        print("\t", *v, sep=". ")
    print("\t - Elemental Absorption")
    for vi in enumerate(elementalAbsorption2, start=1):
        print("\t\t", *vi, sep=". ")
    print("\nPassive: ")
    print("\n - Slitting Wind")
    for vii in enumerate(slittingWind, start=1):
        print("\t", *vii, sep=". ")
    print("\t - Second Wind")
    for viii in enumerate(secondWind, start=1):
        print("\t\t", *viii, sep=". ")


def geoTraveler():
    res = input(
        "What kind of help do you need with Geo Traveler? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return geoBuild()
    elif res == "b":
        return geoConst()
    elif res == "c":
        return geoAbility()
    else:
        error()
        return geoTraveler()


def geoBuild():
    weapon = ["skyward blade", "favonius sword"]
    altWeapon = ["festering desire", "iron sting"]
    artifact = ["4x archaic petra", "4x noblesse oblige"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Energy Recharge, Elemental Mastery"],
                     ["Geo DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Elemental Mastery, Flat ATK"]]

    print("Geo Sub-DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece archaic petra: \n\t1. Geo DMG Bonus +15% \n\t2. Upon obtaining an Elemental Shard created through a Crystallize Reaction, all party members gain 35% DMG Bonus for that particular element for 10s. Only one form of Elemental DMG Bonus can be gained in this manner at any one time.")
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")

    utility.artifactFormat(artifactStats)


def geoConst():
    const1 = ["Invincible Stonewall", "Constellation Lv. 1",
              "Allies within the radius of Wake of Earth have their CRIT Rate increased by 10% and have increased resistance against interruption."]
    const2 = ["Rockcore Meltdown", "Constellation Lv. 2",
              "When the meteorite created by Starfell Sword is destroyed, it will also explode, dealing additional AoE Geo DMG equal to the amount of damage dealt by Starfell Sword."]
    const3 = ["Will of the Rock", "Constellation Lv. 3", "Increases the Level of Wake of Earth by 3.",
              "Maximum upgrade level is 15."]
    const4 = ["Reaction Force", "Constellation Lv. 4",
              "The shockwave triggered by Wake of Earth regenerates 5 Energy for every enemy hit.",
              "A maximum of 25 Energy can be recovered in this manner at any one time."]
    const5 = ["Meteorite Impact", "Constellation Lv. 5",
              "Increase the Level of Starfell Sword by 3."
              "Maximum upgrade level is 15."]
    const6 = ["Everlasting Boulder", "Constellation Lv. 6",
              "The barrier created by Wake of Earth lasts 5s longer.",
              "The meteorite created by Starfell Sword lasts 10s longer."]

    print("Geo Traveler's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def geoAbility():
    foreignRockblade = [
        "Normal Attack - Performs up to 5 consecutive strikes.",
        "Charged Attack - Consumes a certain amount of Stamina to unleash 2 rapid sword strikes.",
        "Plunging Attack -  Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    starfellSword = [
        "Elemental Skill",
        "You disgorge a meteorite from the depths of the earth, dealing AoE Geo DMG.",
        "The meteorite is considered a Geo Construct, and can be climbed or used to block attacks."]
    holdStarfellSword = [
        "The skill's positioning may be adjusted."]
    wakeOfEarth = [
        "Elemental Burst",
        "Energizing the Geo elements deep underground, you set off expanding shockwaves.",
        "Launches surrounding enemies back and deals AoE Geo DMG.",
        "A stone wall is erected at the edges of the shockwave.",
        "The stone wall is considered a Geo Construct, and may be used to block attacks."]
    shatteredDarkrock = [
        "Unlocked at Ascension 1",
        "Reduces Starfell Sword's CD by 2s."]
    frenziedRockslide = [
        "Unlocked at Ascension 4",
        "The final hit of a Normal Attack combo triggers a collapse, dealing 60% of ATK as AoE Geo DMG."]

    print("Skill Talents: ")
    print(" - Foreign Rockblade")
    for i in enumerate(foreignRockblade, start=1):
        print("\t", *i, sep=". ")
    print("\n - Starfell Sword")
    for ii in enumerate(starfellSword, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Hold")
    for iii in enumerate(holdStarfellSword, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Wake of Earth")
    for iv in enumerate(wakeOfEarth, start=1):
        print("\t", *iv, sep=". ")
    print("\nPassive: ")
    print(" - Shattered Darkrock")
    for v in enumerate(shatteredDarkrock, start=1):
        print("\t", *v, sep=". ")
    print("\n - Frenzied Rockslide")
    for vi in enumerate(frenziedRockslide, start=1):
        print("\t", *vi, sep=". ")


def electroTraveler():
    res = input(
        "What kind of help do you need with Electro Traveler? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return electroBuild()
    elif res == "b":
        return electroConst()
    elif res == "c":
        return electroAbility()
    else:
        error()
        return electroTraveler()


def electroBuild():
    weapon = ["skyward blade", "primordial jate cutter"]
    altWeapon = ["sacrificial sword", "favonius sword"]
    artifact = ["4x emblem of severed fate", "4x noblesse oblige"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Energy Recharge, Elemental Mastery"],
                     ["Geo DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Elemental Mastery, Flat ATK"]]

    print("Electro Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece emblem of severed fate: \n\t1. Energy Recharge +20% \n\t2. Increases Elemental Burst DMG by 25% of Energy Recharge. A maximum of 75% bonus DMG can be obtained in this way.")
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")

    utility.artifactFormat(artifactStats)


def electroConst():
    const1 = ["Spring Thunder of Fertility", "Constellation Lv. 1",
              "The number of Abundance Amulets that can be generated using Lightning Blade is increased to 3."]
    const2 = ["Violet Vehemence", "Constellation Lv. 2",
              "When Falling Thunder created by Bellowing Thunder hits an opponent, it will decrease their Electro RES by 15% for 8s."]
    const3 = ["Distant Crackling", "Constellation Lv. 3",
              "Increases the Level of Bellowing Thunder by 3."
              "Maximum upgrade level is 15."]
    const4 = ["Fickle Cloudstrike", "Constellation Lv. 4",
              "When a character obtains Abundance Amulets generated by Lightning Blade, if this character's Energy is less than 35%, the Energy restored by the Abundance Amulets is increased by 100%."]
    const5 = ["Clamor in the Wilds", "Constellation Lv. 5",
              "Increase the Level of Lightning Blade by 3."
              "Maximum upgrade level is 15."]
    const6 = ["World-Shaker", "Constellation Lv. 6",
              "Every 2 Falling Thunder attacks triggered by Bellowing Thunder will increase the DMG dealt by the next Falling Thunder by 100%, and will restore an additional 1 Energy to the current character."]

    print("Electro Traveler's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def electroAbility():
    foreignThundershock = [
        "Normal Attack - Performs up to 5 rapid strikes.",
        "Charged Attack - Consumes a certain amount of Stamina to unleash 2 rapid sword strikes.",
        "Plunging Attack -  Plunges from mid-air to strike the ground below, damaging opponents along the path and dealing AoE DMG upon impact."]
    lightningBlade = [
        "Elemental Skill",
        "Unleashes three swift thunder shadows that deal Electro DMG to opponents and leave an Abundance Amulet behind after hitting an opponent.",
        "2 Abundance Amulets can be created initially. Using this skill will reset any Abundance Amulets that were generated."]
    abundanceAmulets = [
        "When a character is near an Abundance Amulet, they will absorb it and obtain the following effects: \n\t\t1. Restores Elemental Energy \n\t\t2. Increases Energy Recharge during the Abundance Amulet's duration."]
    bellowingThunder = [
        "Elemental Burst",
        "You call upon the protection of lightning, knocking nearby opponents back and dealing Electro DMG to them."]
    lightningShroud = [
        "When your active character's Normal or Charged Attacks hit opponents, they will call Falling Thunder forth, dealing Electro DMG.",
        "When Falling Thunder hits opponents, it will regenerate Energy for that character.",
        "One instance of Falling Thunder can be generated every 0.5s."]
    thunderflash = [
        "Unlocked at Ascension 1",
        "When another nearby character in the party obtains an Abundance Amulet created by Lightning Blade, Lightning Blade's CD is decreased by 1.5s."]
    resoundingRoar = [
        "Unlocked at Ascension 4",
        "Increases the Energy Recharge effect granted by Lightning Blade's Abundance Amulet by 10% of the Traveler's Energy Recharge."]

    print("Skill Talents: ")
    print(" - Foreign Thundershock")
    for i in enumerate(foreignThundershock, start=1):
        print("\t", *i, sep=". ")
    print("\n - Lightning Blade")
    for ii in enumerate(lightningBlade, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Abundance Amulets")
    for iii in enumerate(abundanceAmulets, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Bellowing Thunder")
    for iv in enumerate(bellowingThunder, start=1):
        print("\t", *iv, sep=". ")
    print("\t - Lightning Shroud")
    for v in enumerate(lightningShroud, start=1):
        print("\t\t", *v, sep=". ")
    print("\nPassive: ")
    print("\t - Thunderflash")
    for vi in enumerate(thunderflash, start=1):
        print("\t\t", *vi, sep=". ")
    print("\n - Resounding Roar")
    for vii in enumerate(resoundingRoar, start=1):
        print("\t", *vii, sep=". ")


def venti():
    res = input("What kind of help do you need with Venti? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return ventiBuild()
    elif res == "b":
        return ventiConst()
    elif res == "c":
        return ventiAbility()
    else:
        error()
        return venti()


def ventiBuild():
    weapon = ["skyward harp", "elegy for the end"]
    altWeapon = ["the stringless", "favonius warbow"]
    artifact = ["4x viridescent venerer", "4x noblesse oblige"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["Elemental Mastery/ATK%", "CRIT Rate, CRIT DMG, Flat ATK, Elemental Mastery/ATK"],
                     ["Anemo DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Elemental Recharge"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Elemental Mastery, Energy Recharge"]]

    print("Anemo Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece viridescent venerer: \n\t1. Gain a 15% Anemo DMG Bonus. \n\t2. Increases Swirl DMG by 60%. Decreases opponent's Elemental RES to the element infused in the Swirl by 40% for 10s.")
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")

    utility.artifactFormat(artifactStats)


def ventiConst():
    const1 = ["Splitting Gales", "Constellation Lv. 1",
              "Fires 2 additional arrows per Aimed Shot, each dealing 33% of the original arrow's DMG."]
    const2 = ["Breeze of Reminiscence", "Constellation Lv. 2",
              "Skyward Sonnet decreases enemy Anemo RES by 12% for 10s.",
              "Enemies launched by Skyward Sonnet suffer an additional 12% Anemo RES and Physical RES decrease while airborne."]
    const3 = ["Ode to Thousand Winds", "Constellation Lv. 3",
              "Increases the Level of Wind's Grand Ode by 3."
              "Maximum upgrade level is 15."]
    const4 = ["Hurricane of Freedom", "Constellation Lv. 4",
              "When Venti picks up an Elemental Orb or Particle, he receives a 25% Anemo DMG Bonus for 10s."]
    const5 = ["Concerto dal Cielo", "Constellation Lv. 5",
              "Increase the Level of Skyward Sonnet by 3."
              "Maximum upgrade level is 15."]
    const6 = ["Storm of Defiance", "Constellation Lv. 6",
              "Targets who take DMG from Wind's Grand Ode have their Anemo RES decreased by 20%.",
              "If an Elemental Absorption occurred, then their RES towards the corresponding Element is also decreased by 20%."]

    print("Venti's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def ventiAbility():
    divineMarksmanship = [
        "Normal Attack - Performs up to 6 consecutive shots with a bow.",
        "Charged Attack - Perform a more precise Aimed Shot with increased DMG. While aiming, favorable winds will accumulate on the arrowhead. A fully charged arrow will deal Anemo DMG.",
        "Plunging Attack -  Fires off a shower of arrows in mid-air before falling and striking the ground, dealing AoE DMG upon impact."]
    skywardSonnet = [
        "Elemental Skill",
        "O wind upon which all hymns and songs fly, bear these earth-walkers up into the sky!",
        "Enemies hit by Skyward Sonnet will fall to the ground slowly."]
    pressSkywardSonnet = [
        "Summons a Wind Domain at the enemy's location, dealing AoE Anemo DMG and launching enemies into the air."]
    holdSkywardSonnet = [
        "Summons an even larger Wind Domain with Venti as the epicenter, dealing AoE Anemo DMG and launching affected enemies into the air.",
        "After unleashing the Hold version of this ability, Venti rides the wind into the air."]
    windsGrandOde = [
        "Elemental Burst",
        "Fires off an arrow made of countless coalesced winds, creating a huge Stormeye that sucks in objects and enemies along its path, dealing continuous Anemo DMG."]
    elementalAbsorption = [
        "If the Stormeye comes into contact with Hydro/Pyro/Cryo/Electro elements, it will deal additional elemental DMG of that type.",
        "Elemental Absorption may only occur once per use."]
    embraceOfWinds = [
        "Unlocked at Ascension 1",
        "Holding Skyward Sonnet creates an upcurrent that lasts for 20s."]
    stormeye = [
        "Unlocked at Ascnesion 4",
        "Regenerates 15 Energy for Venti after the effects of Wind's Grand Ode end.",
        "If an Elemental Absorption occurred, this also restores 15 Energy to all characters of that corresponding element."]
    windrider = [
        "Unlocked Automatically",
        "Decreases all party member's gliding Stamina Consumption by 20%."]

    print("Skill Talents: ")
    print(" - Divine Marksmanship")
    for i in enumerate(divineMarksmanship, start=1):
        print("\t", *i, sep=". ")
    print("\n - Skyward Sonnet")
    for ii in enumerate(skywardSonnet, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Press")
    for iii in enumerate(pressSkywardSonnet, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Hold")
    for iv in enumerate(holdSkywardSonnet, start=1):
        print("\t\t", *iv, sep=". ")
    print("\n - Wind's Grand Ode")
    for v in enumerate(windsGrandOde, start=1):
        print("\t", *v, sep=". ")
    print("\t - Elemental Absorption")
    for vi in enumerate(elementalAbsorption, start=1):
        print("\t\t", *vi, sep=". ")
    print("\nPassive: ")
    print("\n - Embrace of Winds")
    for vii in enumerate(embraceOfWinds, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Stormeye")
    for viii in enumerate(stormeye, start=1):
        print("\t", *viii, sep=". ")
    print("\n - windrider")
    for ix in enumerate(windrider, start=1):
        print("\t", *ix, sep=". ")


def xiangling():
    res = input(
        "What kind of help do you need with Xiangling? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return xianglingBuild()
    elif res == "b":
        return xianglingConst()
    elif res == "c":
        return xianglingAbility()
    else:
        error()
        return xiangling()


def xianglingBuild():
    weapon = ["engulfing lightning", "skyward spine"]
    altWeapon = ["the catch", "prototype starglitter"]
    artifact = ["4x viridescent venerer", "4x noblesse oblige"]
    artifactStats = [["Flat ATK", "CRIT Rate, CRIT DMG, ATK%, Elemental Mastery"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Elemental Mastery"],
                     ["Elemental Mastery/ATK%", "CRIT Rate, CRIT DMG, Flat ATK, Elemental Mastery/ATK"],
                     ["Anemo DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Elemental Recharge"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Elemental Mastery, Energy Recharge"]]

    print("Anemo Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece crimson witch of flames: \n\t1. Gain a 15% Pyro DMG Bonus. \n\t2. Increases Overloaded and Burning DMG by 40%. Increases Vaporize and Melt DMG by 15%. Using an Elemental Skill increases 2-Piece Set effects by 50% for 10s. Max 3 stacks.")
    print(
        "\t- The 4 piece emblem of severed fate: \n\t1. Energy Recharge +20% \n\t2. Increases Elemental Burst DMG by 25% of Energy Recharge. A maximum of 75% bonus DMG can be obtained in this way.")

    utility.artifactFormat(artifactStats)


def xianglingConst():
    const1 = ["Crispy Outside, Tender Inside", "Constellation Lv. 1",
              "Enemies hit by Guoba's attacks have their Pyro RES reduced by 15% for 6s."]
    const2 = ["Oil Meets Fire", "Constellation Lv. 2",
              "The last attack in a Normal Attack sequence applies the Implode status onto the enemy for 2s. An explosion will occur once this duration ends, dealing 75% of Xiangling's ATK as AoE Pyro DMG."]
    const3 = ["Deepfry", "Constellation Lv. 3",
              "Increases the Level of Pyronado by 3."
              "Maximum upgrade level is 15."]
    const4 = ["Slowbake", "Constellation Lv. 4",
              "Pyronado's duration is increased by 40%."]
    const5 = ["Guoba Mad", "Constellation Lv. 5",
              "Increase the Level of Guoba Attack by 3."
              "Maximum upgrade level is 15."]
    const6 = ["Condensed Pyronado", "Constellation Lv. 6",
              "For the duration of Pyronado, all party members receive a 15% Pyro DMG Bonus."]

    print("Venti's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def xianglingAbility():
    doughFu = [
        "Normal Attack - Performs up to 5 consecutive spear strikes.",
        "Charged Attack - Consumes a certain amount of Stamina to lunge forward, dealing damage to enemies along the way.",
        "Plunging Attack -  Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    guobaAttack = [
        "Elemental Skill",
        "Summons Guoba the Panda. Guoba continuously breathes fire, dealing AoE Pyro DMG."]
    pyronado = [
        "Elemental Burst",
        "Displaying her mastery over both fire and polearms, Xiangling sends a Pyronado whirling around her.",
        "The Pyronado will move with your character for so long as the ability persists, dealing Pyro DMG to all enemies in its path."]
    crossfire = [
        "Unlocked at Ascension 1",
        "Increases the flame range of Guoba by 20%."]
    superHot = [
        "Unlocked at Ascnesion 4",
        "When Guoba Attack's effect ends, Guoba leaves a chili pepper on the spot where it disappeared. Picking up a chili pepper increases ATK by 10% for 10s."]
    chefDeCuisine = [
        "Unlocked Automatically",
        "When Xiangling cooks an ATK-boosting dish perfectly, she has a 12% chance to receive double the product."]

    print("Skill Talents: ")
    print(" - Dough-Fu")
    for i in enumerate(doughFu, start=1):
        print("\t", *i, sep=". ")
    print("\n - Guoba Attack")
    for ii in enumerate(guobaAttack, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Pyronado")
    for iii in enumerate(pyronado, start=1):
        print("\t", *iii, sep=". ")
    print("\nPassive: ")
    print(" - Crossfire")
    for iv in enumerate(crossfire, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Beware, It's Super Hot!")
    for v in enumerate(superHot, start=1):
        print("\t", *v, sep=". ")
    print("\n - Chef de Cuisine")
    for vi in enumerate(chefDeCuisine, start=1):
        print("\t", *vi, sep=". ")


def xiao():
    res = input("What kind of help do you need with Xiao? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return xiaoBuild()
    elif res == "b":
        return xiaoConst()
    elif res == "c":
        return xiaoAbility()
    else:
        error()
        return xiao()


def xiaoBuild():
    weapon = ["primordial jade winged-spear", "staff of homa"]
    altWeapon = ["blackcliff pole", "deathmatch"]
    artifact = ["2x gladiator's finale, 2x viridescent venerer", "2x shimenawa's reminiscence, 2x viridescent venerer"]
    artifactStats = [["Flat ATK", "CRIT DMG, ATK%, CRIT Rate, Elemental Mastery/Energy Recharge"],
                     ["Flat HP", "CRIT DMG. ATK%, CRIT Rate, Energy Recharge/Flat ATK"],
                     ["ATK%", "CRIT DMG, CRIT Rate. Elemental Mastery/Flat ATK, Energy Recharge"],
                     ["Anemo DMG Bonus%", "CRIT DMG, ATK%, CRIT Rate, Flat ATK"],
                     ["CRIT DMG", "ATK%, CRIT Rate, Flat ATK/Elemental Mastery, Energy Recharge"]]

    print("Anemo DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 2 piece set (viridescent venerer + gladiator's finale) will increase your anemo damage by 15% and increase your ATK +18%\n")
    print(
        "\t- The 2 piece set (viridescent venerer + shimenawa's reminiscence) will increase your anemo damage by 15% and increase your ATK +18%\n")

    utility.artifactFormat(artifactStats)


def xiaoConst():
    const1 = ["Dissolution Eon - Destroyer of Worlds", "Constellation Lv. 1",
              "Increases Lemniscatic Wind Cycling's charges by 1."]
    const2 = ["Annihilation Eon - Blossom of Kaleidos", "Constellation Lv. 2",
              "When in party but not on the field, Xiao's Energy Recharge is increased by 25%."]
    const3 = ["Conqueror of Evil: Wrath Deity", "Constellation Lv. 3",
              "Increases the Level of Lemniscatic Wind Cycling by 3."
              "Maximum upgrade level is 15."]
    const4 = ["Transcension - Extinction of Suffering", "Constellation Lv. 4",
              "When Xiao's HP falls below 50%, he gains a 100% DEF Bonus."]
    const5 = ["Evolution Eon - Origin of Ignorance", "Constellation Lv. 5",
              "Increase the Level of Bane of All Evil by 3."
              "Maximum upgrade level is 15."]
    const6 = ["Conqueror of Evil: Guardian Yaksha", "Constellation Lv. 6",
              "While under the effects of Bane of All Evil, hitting at least 2 opponents with Xiao's Plunging Attack will immediately grant him 1 charge of Lemniscatic Wind Cycling and for the next 1s, he may use Lemniscatic Wind Cycling while ignoring its CD."]

    print("Xiao's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def xiaoAbility():
    whirlwindThrust = [
        "Normal Attack - Performs up to 6 consecutive spear strikes.",
        "Charged Attack - Consumes a certain amount of Stamina to perform an upward thrust.",
        "Plunging Attack -  Plunges from mid-air to strike the ground from below, damaging opponents along the path and dealing AoE DMG upon impact. Xiao does not take DMG from performing Plunging Attacks."]
    lemniscaticWindCycling = [
        "Elemental Skill",
        "Xiao lunges forward, dealing Anemo DMG to opponents in his path.",
        "\tCan be used in mid - air.",
        "\tStarts with 2 charges.",
        "\tGenerates 3 elemental particles when hits at least 1 target."]
    baneOfAllEvil = [
        "Elemental Burst",
        "Xiao dons the Yaksha Mask that set gods and demons trembling millennia ago.",
        "In this state, Xiao will continuously lose HP.",
        "The effects of this skill end when Xiao leaves the field."]
    yakshasMask = [
        "Greatly increases Xiao's jumping ability.",
        "Increases his attack AoE and attack DMG.",
        "Converts attack DMG into Anemo DMG, which cannot be overriden by any other elemental infusion."]
    tamerOfDemons = [
        "Unlocked at Ascension 1",
        "While under the effects of Bane of All Evil, all DMG dealt by Xiao increases by 5%. DMG increases by a further 5% for every 3s the ability persists. The maximum DMG Bonus is 25%."]
    heavenFall = [
        "Unlocked at Ascension 4",
        "Using Lemniscatic Wind Cycling increases the DMG of subsequent uses of Lemniscatic Wind Cycling by 15%. This effect lasts for 7s, and has a maximum of 3 stacks. Gaining a new stack refreshes the effect's duration."]
    gravityDefier = [
        "Unlocked Automatically",
        "Decreases climbing Stamina consumption for your own party members by 20%.",
        "Not stackable with Passive Talents that provide the exact same effects."]

    print("Skill Talents: ")
    print(" - Whirlwind Thrust")
    for i in enumerate(whirlwindThrust, start=1):
        print("\t", *i, sep=". ")
    print("\n - Lemniscatic Wind Cycling")
    for ii in enumerate(lemniscaticWindCycling, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Bane of All Evil")
    for iii in enumerate(baneOfAllEvil, start=1):
        print("\t", *iii, sep=". ")
    print("\t - Yaksha's Mask")
    for iv in enumerate(yakshasMask, start=1):
        print("\t\t", *iv, sep=". ")
    print("\nPassive: ")
    print("\n - Conqueror of Evil: Tamer of Demons")
    for v in enumerate(tamerOfDemons, start=1):
        print("\t", *v, sep=". ")
    print("\n - Dissolution Eon: Heaven Fall")
    for vi in enumerate(heavenFall, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Transcension: Gravity Defier")
    for vii in enumerate(gravityDefier, start=1):
        print("\t", *vii, sep=". ")


def xingqiu():
    res = input(
        "What kind of help do you need with Xingqiu? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return xingqiuBuild()
    elif res == "b":
        return xingqiuConst()
    elif res == "c":
        return xingqiuAbility()
    else:
        error()
        return xingqiu()


def xingqiuBuild():
    weapon = ["skyward blade", "sacrificial sword"]
    altWeapon = ["favonius sword", "festering desire"]
    artifact = ["4x emblem of severed fate", "4x noblesse oblige"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Energy Recharge"],
                     ["Hydro DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Flat ATK, Energy Recharge"]]

    print("Anemo DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece noblesse oblige: \n\t1. Elemental Burst DMG +20% \n\t2. Using an Elemental Burst increase all party members' ATK by 20% for 12s. This effect cannot stack.")
    print(
        "\t- The 4 piece emblem of severed fate: \n\t1. Energy Recharge +20% \n\t2. Increases Elemental Burst DMG by 25% of Energy Recharge. A maximum of 75% bonus DMG can be obtained in this way.")

    utility.artifactFormat(artifactStats)


def xingqiuConst():
    const1 = ["The Scent Remained", "Constellation Lv. 1",
              "Increases the maximum number of Rain Swords by 1."]
    const2 = ["Rainbow Upon the Azure Sky", "Constellation Lv. 2",
              "Extends the duration of Guhua Sword - Raincutter by 3s.",
              "Decreases the Hydro RES of enemies hit by sword rain attacks by 15% for 4s."]
    const3 = ["Weaver of Verses", "Constellation Lv. 3",
              "Increases the Level of Guhua Sword - Raincutter by 3.",
              "Maximum upgrade level is 15."]
    const4 = ["Evilsoother", "Constellation Lv. 4",
              "Throughout the duration of Guhua Sword: Raincutter, the DMG dealt by Guhua Sword: Fatal Rainscreen is increased by 50%."]
    const5 = ["Embrace of Rain", "Constellation Lv. 5",
              "Increase the Level of Guhua Sword - Fatal Rainscreen by 3.",
              "Maximum upgrade level is 15."]
    const6 = ["Hence, Call Them My Own Verses", "Constellation Lv. 6",
              "Activating 2 of Guhua Sword - Raincutter's sword rain attacks greatly increases the DMG of the third.",
              "Xingqiu regenerates 3 Energy when sword rain attacks hit enemies."]

    print("Xingqiu's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def xingqiuAbility():
    guhuaStyle = [
        "Normal Attack - Performs up to 5 rapid strikes.",
        "Charged Attack - Consumes a certain amount of Stamina to unleash 2 rapid sword strikes.",
        "Plunging Attack -  Plunges from mid-aur to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    fatalRainscreen1 = [
        "Elemental Skill",
        "Xingqiu performs twin strikes with his sword, dealing Hydro DMG. At the same time, this ability creates the maximum number of Rain Swords, which will orbit the character."]
    fatalRainscreen2 = [
        "20% of Xingqiu's Hydro DMG Bonus will be converted to additional DMG Reduction for the Rain Swords.",
        "The maximum amount of additional DMG Reduction that can be gained this way is 24%.",
        "The initial maximum number of Rain Swords is 3.",
        "Using this ability applies the Wet status onto the character."]
    propertyFatalRainscreen = [
        "When a character takes DMG, the Rain Sword will shatter, reducing the amount of DMG taken.",
        "Increases the character's resistance to interruption."]
    raincutter = [
        "Initiate Rainbow Bladework and fight using an illusory sword rain, while creating the maximum number of Rain Swords."]
    rainbowBladework = [
        "Normal Attacks will trigger consecutive sword rain attacks, dealing Hydro DMG.",
        "Rain Swords will remain at the maximum number throughout the ability's duration.",
        "These effects carry over to other characters."]
    hydropathic = [
        "Unlocked at Ascension 1",
        "When a Rain Sword is shattered or when its duration expires, it regenerates the current character's HP based on 6% of Xingqiu's Max HP."]
    bladesAmidstRaindrops = [
        "Unlocked at Ascension 4",
        "Xingqiu gains a 20% Hydro DMG Bonus."]
    flashOfGenius = [
        "Unlocked Automatically",
        "When Xingqiu crafts Character Talent Materials, he has a 25% chance to refund a portion of the crafting materials used."]

    print("Skill Talents: ")
    print(" - Guhua Style")
    for i in enumerate(guhuaStyle, start=1):
        print("\t", *i, sep=". ")
    print("\n - Guhua Sword: Fatal Rainscreen")
    for ii in enumerate(fatalRainscreen1, start=1):
        print("\t", *ii, sep=". ")
    print("\t - The Rain Swords have the following properties:")
    for iii in enumerate(propertyFatalRainscreen, start=1):
        print("\t\t", *iii, sep=". ")
    for iv in enumerate(fatalRainscreen2, start=1):
        print("\t", *iv, sep=". ")
    print("\n - Guhua Sword: Raincutter")
    for v in enumerate(raincutter, start=1):
        print("\t", *v, sep=". ")
    print("\t - Rainbow Bladework")
    for vi in enumerate(rainbowBladework, start=1):
        print("\t\t", *vi, sep=". ")
    print("\nPassive: ")
    print(" - Hydropathic")
    for vii in enumerate(hydropathic, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Blades Amidst Raindrops")
    for viii in enumerate(bladesAmidstRaindrops, start=1):
        print("\t", *viii, sep=". ")
    print("\n - Flash of Genius")
    for ix in enumerate(flashOfGenius, start=1):
        print("\t", *ix, sep=". ")


def xinyan():
    res = input("What kind of help do you need with Xinyan? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return xinyanBuild()
    elif res == "b":
        return xinyanConst()
    elif res == "c":
        return xinyanAbility()
    else:
        error()
        return xinyan()


def xinyanBuild():
    weapon = ["wolf's gravestone", "skyward pride"]
    altWeapon = ["prototype aminus", "sacrificial greatsword"]
    artifact = ["4x gladiator's finale", "4x noblesse oblige"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Energy Recharge"],
                     ["Physical DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Energy Recharge, DEF%"]]

    print("Physical DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece gladiator's finale: \n\t1. ATK +18% \n\t2. If the wielder of this artifact set uses a Sword, Claymore or Polearm, increases their Normal Attack DMG by 35%.")
    print(
        "\t- The 2 piece set will increase your physical damage by 25% and increase your ATK +18%\n")

    utility.artifactFormat(artifactStats)


def xinyanConst():
    const1 = ["Fatal Acceleration", "Constellation Lv. 1",
              "Upon scoring a CRIT hit, increases ATK SPD of Xinyan's Normal and Charged Attacks by 12% for 5s.",
              "Can only occur once every 5s."]
    const2 = ["Impromptu Opening", "Constellation Lv. 2",
              "Riff Revolution Physical DMG has its Crit rate increased by 100%, and will form a shield at Shield Level 3: Rave when cast."]
    const3 = ["Double-Stop", "Constellation Lv. 3",
              "Increases the Level of Sweeping Fervor by 3.",
              "Maximum upgrade level is 15."]
    const4 = ["Wildfire Rhythm", "Constellation Lv. 4",
              "Sweeping Fervor's swing DMG decrease opponents Physical RES by 15% for 12s."]
    const5 = ["Screamin' for an Encore", "Constellation Lv. 5",
              "Increases the Level of Riff Revolution by 3.",
              "Maximum upgrade level is 15."]
    const6 = ["Rockin' in a Flaming World", "Constellation Lv. 6",
              "Decrease the stamina consumption of Xinyan Charged Attacks by 30%. Additionally, Xinyan Charged Attack gain an ATK bonus equal to 50% of her DEF."]

    print("Xinyan's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def xinyanAbility():
    danceOnFire = [
        "Normal Attack - Performs up to 4 consecutive strikes.",
        "Charged Attack - Drains Stamina over time to perform continuous spinning attacks against all nearby enemies. At the end of the sequence, perform a more powerful slash.",
        "Plunging Attack -  Plunges from mid-air to strike the ground, damaging enemies along the path and dealing AoE DMG upon impact."]
    sweepingFervor1 = [
        "Elemental Skill",
        "Xinyan brandishes her instrument, dealing Pyro DMG on nearby enemies, forming a shield made out of her audience's passion.",
        "The shield's DMG Absorption scales based on Xinyan's DEF and on the number of enemies hit."]
    propertySweepingFervor1 = [
        "Hitting 0-1 enemies grants Shield Level 1: Ad Lib.",
        "Hitting 2 enemies grants Shield Level 2: Lead-In.",
        "Hitting 3 or more enemies grants Shield Level 3: Rave, which will also deal intermittent Pyro DMG to nearby enemies."]
    propertySweepingFervor2 = [
        "When unleashed, it infuses Xinyan with Pyro.",
        "It has 250% DMG Absorption effectiveness against Pyro DMG."]
    riffRevolution = [
        "Elemental Burst",
        "Strumming rapidly, Xinyan launches nearby enemies and deals Physical DMG to them, hyping up the crowd. The sheer intensity of the atmosphere will cause explosions that deal Pyro DMG to nearby enemies."]
    theShowGoesOn = [
        "Unlocked at Ascension 1",
        "Decreases the number of enemies Sweeping Fervor must hit to trigger each level of shielding.",
        "\t Shield Level 2: Lead-In requirement reduced to 1 enemy hit.",
        "\t Shield Level 3: Rave requirement reduced to 2 enemies hit or more."]
    rockNRoll = [
        "Unlocked at Ascension 4",
        "Characters shielded by Sweeping Fervor deal 15% increased Physical DMG."]
    aRadRecipe = [
        "Unlocked Automatically",
        "When a Perfect Cooking is achieved on an DEF-boosting dish, Xinyan has a 12% chance to obtain double the product."]

    print("Skill Talents: ")
    print(" - Dance on Fire")
    for i in enumerate(danceOnFire, start=1):
        print("\t", *i, sep=". ")
    print("\n - Sweeping Fervor")
    for ii in enumerate(sweepingFervor1, start=1):
        print("\t", *ii, sep=". ")
    for iii in enumerate(propertySweepingFervor1, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - The shield has the following special properties:")
    for iv in enumerate(propertySweepingFervor2, start=1):
        print("\t\t", *iv, sep=". ")
    print("\n - Riff Revolution")
    for v in enumerate(riffRevolution, start=1):
        print("\t", *v, sep=". ")
    print("\nPassive: ")
    print("\t - 'The Show Goes On, Even Without an Audience...'")
    for vi in enumerate(theShowGoesOn, start=1):
        print("\t\t", *vi, sep=". ")
    print("\n - '...Now That's Rock 'N' Roll!'")
    for vii in enumerate(rockNRoll, start=1):
        print("\t", *vii, sep=". ")
    print("\n - A Rad Recipe")
    for viii in enumerate(aRadRecipe, start=1):
        print("\t", *viii, sep=". ")


def yanfei():
    res = input("What kind of help do you need with Yanfei? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return yanfeiBuild()
    elif res == "b":
        return yanfeiConst()
    elif res == "c":
        return yanfeiAbility()
    else:
        error()
        return yanfei()


def yanfeiBuild():
    weapon = ["lost prayer to the sacred winds", "skyward atlas"]
    altWeapon = ["the widsith", "solar pearl"]
    artifact = ["4x crimson witch of flames"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Energy Mastery"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Energy Mastery"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Energy Mastery/ATK%"],
                     ["Pyro DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Energy Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Energy Mastery, Flat ATK"]]

    print("Pyro DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece crimson witch of flames: \n\t1. Gain a 15% Pyro DMG Bonus. \n\t2. Increases Overloaded and Burning DMG by 40%. Increases Vaporize and Melt DMG by 15%. Using an Elemental Skill increases 2-Piece Set effects by 50% for 10s. Max 3 stacks.")

    utility.artifactFormat(artifactStats)


def yanfeiConst():
    const1 = ["The Law Knows No Kindness", "Constellation Lv. 1",
              "When Yanfei uses her Charged Attacks,each existing Scarlet Seal additionally reduces the stamina cost of this Charged Attack by 10% and increases resistance against interruption during its release."]
    const2 = ["Right of Final Interpretation", "Constellation Lv. 2",
              "Increases Yanfei's Charged Attack CRIT rate by 20% against enemies below 50% HP."]
    const3 = ["Samadhi Fire-Forged", "Constellation Lv. 3",
              "Increases the Level of Signed Edict by 3.",
              "Maximum upgrade level is 15."]
    const4 = ["Supreme Amnesty", "Constellation Lv. 4",
              "When Done Deal is used: \n\t\tCreates a shield which absorbes upto 45% of Yanfei's Max HP for 15s. This shield absorbes Pyro DMG 250% more efficiently."]
    const5 = ["Abiding Affidavit", "Constellation Lv. 5",
              "Increases the Level of Done Deal by 3.",
              "Maximum upgrade level is 15."]
    const6 = ["Extra Clause", "Constellation Lv. 6",
              "Increases the maximum number of Scarlet Seals by 1."]

    print("Yanfei's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def yanfeiAbility():
    sealOfApproval = [
        "Normal Attack - Shoots fireballs that deal up to three counts of Pyro DMG. When Yanfei's Normal Attacks hit enemies, they will grant her a single Scarlet Seal. Yanfei may possess a maximum of 3 Scarlet Seals, and each time this effect is triggered, the duration of currently possessed Scarlet Seals will refresh. Each Scarlet Seal will decrease Yanfei's Stamina consumption and will disappear when she leaves the field.",
        "Charged Attack - Consumes Stamina and all Scarlet Seals before dealing AoE Pyro DMG to the opponents after a short casting time. This Charged Attack's AoE and DMG will increase according to the amount of Scarlet Seals consumed.",
        "Plunging Attack -  Gathering the power of Pyro, Yanfei plunges towards the ground from mid-air, damaging all opponents in her path. Deals AoE Pyro DMG upon impact with the ground."]
    signedEdict = [
        "Elemental Skill",
        "Summons blistering flames that deal AoE Pyro DMG.",
        "If this attack hits an enemy, Yanfei is granted the maximum number of Scarlet Seals."]
    doneDeal = [
        "Elemental Burst",
        "Triggers a spray of intense flames that rush at nearby opponents, dealing AoE Pyro DMG, granting Yanfei the maximum number of Scarlet Seals, and applying Brilliance to her."]
    brilliance = [
        "Perodically grants Yanfei a Scarlet Seal. Increases the DMG of her Charged Attacks. The Brilliance effect stops when Yanfei leaves the field or dies."]
    proviso = [
        "Unlocked at Ascension 1",
        "When Yanfei consumes Scarlet Seals by using a Charged Attack, each Scarlet Seal will increase Yanfei's Pyro DMG Bonus by 5%. This effect lasts for 6s. When a Charged Attack is used again during the effect's duration, it will dispel the previous effect."]
    blazingEye = [
        "Unlocked at Ascension 4",
        "When Yanfei's Charged Attack deals a CRIT Hit to opponents, she will deal an additional instance of AoE Pyro DMG equal to 80% of her ATK. This DMG counts as Charged Attack DMG."]
    encyclopedicExpertise = [
        "Unlocked Automatically",
        "Displays the location of nearby resources unique to Liyue on the mini-map."]

    print("Skill Talents: ")
    print(" - Seal of Approval")
    for i in enumerate(sealOfApproval, start=1):
        print("\t", *i, sep=". ")
    print("\n - Signed Edict")
    for ii in enumerate(signedEdict, start=1):
        print("\t", *ii, sep=". ")
    print("\n - Done Deal")
    for iii in enumerate(doneDeal, start=1):
        print("\t", *iii, sep=". ")
    print("\t - Brilliance")
    for iv in enumerate(brilliance, start=1):
        print("\t\t", *iv, sep=". ")
    print("\nPassive: ")
    print(" - Proviso")
    for v in enumerate(proviso, start=1):
        print("\t", *v, sep=". ")
    print("\n - Blazing Eye")
    for vi in enumerate(blazingEye, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Encyclopedic Expertise")
    for vii in enumerate(encyclopedicExpertise, start=1):
        print("\t", *vii, sep=". ")


def yoimiya():
    res = input(
        "What kind of help do you need with Yoimiya? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return yoimiyaBuild()
    elif res == "b":
        return yoimiyaConst()
    elif res == "c":
        return yoimiyaAbility()
    else:
        error()
        return yoimiya()


def yoimiyaBuild():
    weapon = ["thundering pulse", "amos bow"]
    altWeapon = ["rust", "hamayumi"]
    artifact = ["4x shimenawa's reminiscence", "2x crimson witch of flames, 2x gladiator's finale"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, ATK%, Energy Mastery"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, ATK%, Energy Mastery"],
                     ["ATK%", "CRIT DMG, CRIT Rate, Flat ATK, Energy Mastery"],
                     ["Pyro DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Energy Mastery"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, ATK%, Energy Mastery, Flat ATK"]]

    print("Pyro DPS:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece shimenawa's reminiscence: \n\t1. ATK +18% \n\t2. When casting an Elemental Skill, if the character has 15 or more Energy, they lose 15 Energy and Normal/Charged/Plunging Attack DMG is increased by 50% for 10s.")
    print(
        "\t- The 2 piece set will increase your pyro damage by 15% and increase your ATK +18%\n")

    utility.artifactFormat(artifactStats)


def yoimiyaConst():
    const1 = ["Agate Ryuukin", "Constellation Lv. 1",
              "The Auros Blaze created by Ryuukin Saxifrage lasts for an extra 4s.",
              "Additionally, when an opponent affected by Aurous Blaze is defeated within its duration, Yoimiya's ATK is increased by 20% for 20s."]
    const2 = ["A Procession of Bonfires", "Constellation Lv. 2",
              "When Yoimiya's Pyro DMG scores a CRIT Hit, Yoimiya will gain a 25% Pyro DMG Bonus for 6s.",
              "This effect can be triggered even when Yoimiya is not the active character."]
    const3 = ["Trickster's Flare", "Constellation Lv. 3",
              "Increases the Level of Niwabi Fire-Dance by 3.",
              "Maximum upgrade level is 15."]
    const4 = ["Pyrotechnic Professional", "Constellation Lv. 4",
              "When Yoimiya's own Aurous Blaze triggers an explosion, Niwabi Fire-Dance's CD is decreased by 1.2."]
    const5 = ["A Summer Festival's Eve", "Constellation Lv. 5",
              "Increases the Level of Ryuukin Saxifrage by 3.",
              "Maximum upgrade level is 15."]
    const6 = ["Naganohara Meteor Swarm", "Constellation Lv. 6",
              "During Niwabi Fire-Dance, Yoimiya's Normal Attacks have a 50% chance of firing an extra Kindling Arrow that deals 60% of its original DMG. This DMG is considered Normal Attack DMG."]

    print("Yoimiya's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def yoimiyaAbility():
    fireworkFlareUp = [
        "Normal Attack - Perform up to 5 consecutive shots with a bow.",
        "Charged Attack - Perform a more precise Aimed Shot with increased DMG. While aiming, flames will accumulate on the arrowhead before being fired off as an attack. Has different effects based on how long the energy has been charged: \n\t\t1. Charge Level 1: Fires off a flaming arrow that deals Pyro DMG. \n\t\t2. Charge Level 2: Generates a maxmimum of 3 Kindling Arrows based on time spent charging, releasing them as part of this Aimed Shot. Kindling Arrows will home in on nearby opponents, dealing Pyro DMG on hit.",
        "Plunging Attack -  Fires off a shower of arrows in mid-air before falling and striking the ground, dealing AoE DMG upon impact."]
    niwabiFireDance = [
        "Elemental Skill",
        "Yoimiya waves a sparkler and causes a ring of saltpeter to surround her."]
    niwabiEnshou = [
        "During this time, arrows fired by Yoimiya's Normal Attack will be Blazing Arrows, and their DMG will be increased and converted to Pyro DMG. during this time, Normal Attack: Firework Flare-Up will not generate Kindling Arrows at Charge Level 2.',"
        "This effect will deactivate when Yoimiya leaves the field."]
    ryuukinSaxifrage = [
        "Elemental Burst",
        "Yoimiya leaps into the air along with her original creation, the 'Ryuukin Saxifrage,' and fires forth blazing rockets bursting with surprises that deal AoE Pyro DMG and mark one of the hit opponents with Aurous Blaze."]
    aurousBlaze = [
        "All Normal/Charged/Plunging Attacks, Elemental Skills, and Elemental Bursts by any party member other than Yoimiya that hit an opponent marked by Aurous Blaze will trigger an explosion, dealing AoE Pyro DMG.",
        "When an opponent affected by Aurous Blaze is defeated before its duration expires, the effect will pass on to another nearby opponent, who will inherit the remaining duration.",
        "One Aurous Blaze explosion can be triggered every 2s. When Yoimiya is down, Aurous Blaze effects created through her skills will be deactivated."]
    troubleMaker = [
        "Unlocked at Ascension 1",
        "During Niwabi Fire-Dance, shots from Yoimiya's Normal Attack will increase her Pyro DMG Bonus by 2% on hit. This effect lasts for 3s and can have a maximum of 10 stacks."]
    summerNightsDawn = [
        "Unlocked at Ascension 4",
        "Using Ryuukin Saxifrage causes nearby party members (not including Yoimiya) to gain a 10% ATK increase for 15s. Additionally, a further ATK Bonus will be added on based on the number of 'Tricks of the Trouble-Maker' stacks Yoimiya possesses when using Ryuukin Saxifrage. Each stack increases this ATK Bonus by 1%."]
    blazingMatch = [
        "Unlocked Automatically",
        "When Yoimiya crafts Decoration, Ornament, and Landscape-type Furnishings, she has a 100% chance to refund a portion of the materials used."]

    print("Skill Talents: ")
    print(" - Firework Flare-Up")
    for i in enumerate(fireworkFlareUp, start=1):
        print("\t", *i, sep=". ")
    print("\n - Niwabi Fire-Dance")
    for ii in enumerate(niwabiFireDance, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Niwabi Enshou")
    for iii in enumerate(niwabiEnshou, start=1):
        print("\t\t", *iii, sep=". ")
    print("\n - Ryuukin Saxifrage")
    for iv in enumerate(ryuukinSaxifrage, start=1):
        print("\t", *iv, sep=". ")
    print("\t - Aurous Blaze")
    for v in enumerate(aurousBlaze, start=1):
        print("\t\t", *v, sep=". ")
    print("\nPassive: ")
    print(" - Tricks of the Trouble-Maker")
    for vi in enumerate(troubleMaker, start=1):
        print("\t", *vi, sep=". ")
    print("\n - Summer Night's Dawn")
    for vii in enumerate(summerNightsDawn, start=1):
        print("\t", *vii, sep=". ")
    print("\n - Blazing Match")
    for viii in enumerate(blazingMatch, start=1):
        print("\t", *viii, sep=". ")


def zhongli():
    res = input(
        "What kind of help do you need with Zhongli? \n[a] General Build \n[b] Constellation \n[c] Ability \n> ")
    res.lower()
    if res == "a":
        return zhongliBuild()
    elif res == "b":
        return zhongliConst()
    elif res == "c":
        return zhongliAbility()
    else:
        error()
        return zhongli()


def zhongliBuild():
    weapon = ["staff of homa", "primordial jade winged-spear"]
    altWeapon = ["deathmatch", "prototype starglitter"]
    artifact = ["4x tenacity of the millelith", "4x archaic petra"]
    artifactStats = [["Flat ATK", "CRIT DMG, CRIT Rate, HP%, Energy Recharge"],
                     ["Flat HP", "CRIT DMG, CRIT Rate, HP%, Energy Recharge"],
                     ["HP%", "CRIT DMG, CRIT Rate, Energy Recharge, ATK%"],
                     ["Geo DMG Bonus%", "CRIT DMG, CRIT Rate, ATK%, Energy Recharge"],
                     ["CRIT DMG/CRIT Rate", "CRIT DMG/CRIT Rate, HP%, ATK%, Energy Recharge"]]

    print("Geo Support:")
    utility.weaponDetails(weapon, altWeapon)

    print("\n - The recommended combination of artifacts are", artifact)
    print(
        "\t- The 4 piece tenacity of the millelith: \n\t1. HP +20% \n\t2. When an Elemental Skill hits an opponent, the ATK of all nearby party members is increased by 20% and their Shield Strength is increased by 30% for 3s. This effect can be triggered once every 0.5s. This effect can still be triggered even when the character who is using this artifact set is not on the field.")
    print(
        "\t- The 4 piece archaic petra: \n\t1. Gain a 15% Geo DMG Bonus. \n\t2. Upon obtaining an Elemental Shard created through a Crystallize Reaction, all party members gain a 35% DMG Bonus for that particular element for 10s. Only one form of Elemental DMG Bonus can be gained in this manner at any one time.")

    utility.artifactFormat(artifactStats)


def zhongliConst():
    const1 = ["Rock, the Backbone of Earth", "Constellation Lv. 1",
              "Increases the maximum number of Stone Steles created by Dominus Lapidis that may exist simultaneously to 2."]
    const2 = ["Stone, the Cradle of Jade", "Constellation Lv. 2",
              "Planet Befall grants nearby characters on the field a Jade Shield when it descends."]
    const3 = ["Jade, Shimmering through Darkness", "Constellation Lv. 3",
              "Jade, Shimmering through Darkness",
              "Maximum upgrade level is 15."]
    const4 = ["Topaz, Unbreakable and Fearless", "Constellation Lv. 4",
              "Increases Planet Befall's AoE by 20% and increases the duration of Planet Befall's Petrification effect by 2s."]
    const5 = ["Lazuli, Herald of the Order", "Constellation Lv. 5",
              "Increase the Level of Planet Befall by 3.",
              "Maximum upgrade level is 15."]
    const6 = ["Chrysos, Bounty of Dominator", "Constellation Lv. 6",
              "When the Jade Shield takes DMG, 40% of that incoming DMG is converted to HP for the current character. A single instance of regeneration cannot exceed 8% of that character's Max HP."]

    print("Zhongli's Constellations")
    utility.constellationDetails(const1, const2, const3, const4, const5, const6)


def zhongliAbility():
    rainOfStone = [
        "Normal Attack - Performs up to 6 consecutive spear strikes.",
        "Charged Attack - Consumes a certain amount of Stamina to lunge forward, causing stone spears to fall along his path.",
        "Plunging Attack -  Plunges from mid-air to strike the ground below, damaging enemies along the path and dealing AoE DMG upon impact."]
    dominusLapidis = ["Elemental Skill"]
    pressDominusLapidis = [
        "Commands the omnipresent power of the earth to solidify into a Stone Stele, standing 30 seconds, dealing AoE Geo DMG at the creation."]
    holdDominusLapidis = [
        "Causes nearby Geo energy to explode, causing the following effects: \n\t\t1. If their maximum number hasn't been reached, creates a Stone Stele. \n\t\t2. Creates a shield of jade. The shield's DMG Absorption scales based on Zhongli's Max HP. Possesses 150% DMG Absorption against all Elemental and Physical DMG. \n\t\t3. Deals AoE Geo DMG. \n\t\t4. If there are nearby targets with the Geo element, it will drain a large amount of Geo element from a maximum of 2 such targets. This effect does not cause DMG."]
    stoneStele = [
        "When created, deals AoE Geo DMG. Additionally, every 2 seconds, it will resonate with other nearby Geo Constructs, dealing Geo DMG to surrounding opponents. Stele creation and Resonance generate 0.5 elemental particles.",
        "The Stone Stele is considered a Geo Construct that can both be climbed and used to block attacks.",
        "Only one Stele created by Zhongli himself may initially exist at any one time."]
    jadeShield = [
        "Possesses 150% DMG Absorption against all Elemental and Physical DMG.",
        "Characters protected by the Jade Shield will decrease the Elemental RES and Physical RES of opponents in a small AoE by 20%. This effect cannot be stacked."]
    planetBefall = [
        "Elemental Burst"
        "Brings a falling meteor down to earth, dealing massive Geo DMG to opponents caught in its AoE and applying the Petrification status to them."]
    petrification = [
        "Opponents affected by the Petrification status cannot move."]
    resonantWaves = [
        "Unlocked at Ascension 1",
        "When the Jade Shield takes DMG, it will Fortify: \n\t\t1. Fortified characters have 5% increased Shield Strength.",
        "Can stack up to 5 times, and lasts until the Jade Shield dissapears."]
    dominanceOfEarth = [
        "Unlocked at Ascension 4",
        "Zhongli deals bonus DMG based on his Max HP: \n\t\t1. Normal Attack, Charged Attack, and Plunging Attack DMG is increased by 1.39% of Max HP. \n\t\t2. Dominus Lapidis Stone Stele, resonance, and hold DMG is increased by 1.9% of Max HP. \n\t\t3. Planet Befall deals additional DMG equal to 33% of Zhongli's Max HP."]
    arcanumOfCrystal = [
        "Unlocked Automatically",
        "Refunds 15% of the ores used when crafting Polearm-type weapons."]

    print("Skill Talents: ")
    print(" - Rain of Stone")
    for i in enumerate(rainOfStone, start=1):
        print("\t", *i, sep=". ")
    print("\n - Dominus Lapidis")
    for ii in enumerate(dominusLapidis, start=1):
        print("\t", *ii, sep=". ")
    print("\t - Press")
    for iii in enumerate(pressDominusLapidis, start=1):
        print("\t\t", *iii, sep=". ")
    print("\t - Hold")
    for iv in enumerate(holdDominusLapidis, start=1):
        print("\t\t", *iv, sep=". ")
    print("\t - Stone Stele")
    for v in enumerate(stoneStele, start=1):
        print("\t\t", *v, sep=". ")
    print("\t - Jade Shield")
    for vi in enumerate(jadeShield, start=1):
        print("\t\t", *vi, sep=". ")
    print("\n - Planet Befall")
    for vii in enumerate(planetBefall, start=1):
        print("\t", *vii, sep=". ")
    print("\t - Petrification")
    for viii in enumerate(petrification, start=1):
        print("\t\t", *viii, sep=". ")
    print("\nPassive: ")
    print(" - Resonant Waves")
    for ix in enumerate(resonantWaves, start=1):
        print("\t", *ix, sep=". ")
    print("\n - Dominance of Earth")
    for x in enumerate(dominanceOfEarth, start=1):
        print("\t", *x, sep=". ")
    print("\n - Arcanum of Crystal")
    for xi in enumerate(arcanumOfCrystal, start=1):
        print("\t", *xi, sep=". ")


def rerolling():
    rerollOrder = ["Create an account", "Choose and name your character", "Complete the tutorial", "Defeat Stormterror",
                   "Enter the Knights of Favonius' headquarters (Unlock Wishes upon ending the scene)",
                   "Receive the 10 Acquaint Fates from the pre-registration campaign in your Mailbox",
                   "Choose a banner and pull ※If you get the character you want you're finished",
                   "To reroll, exit the game from the main menu",
                   "Log out of your account at the title screen and return to step number 1"]
    print("Rerolling: ")
    for i in enumerate(rerollOrder, start=1):
        print("\t", *i, sep=". ")

    print("""\n※Note!※
Genshin Impact is a game that was not intentionally made for rerolling so there is no method of deleting an account unless personally contacting a mihoyo staff member on the request to delete your own account.""")


def ending():
    res = input(
        "\nIs there anything else you want to go over again? \n[a] Farming \n[b] Character \n[c] Rerolling \n[d] End \n> ")
    if res == "a":
        return farming()
    elif res == "b":
        return character()
    elif res == "c":
        return rerolling()
    elif res == "d":
        print("Thank you for using BOT_Paimon! See you next time~✧☆✧")
        exit()
    else:
        error()
        return ending()


welcome()
question()
while True:
    ending()
