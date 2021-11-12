class utility:
    def weaponDetails(weapon, altWeapon):
        print(" - The best weapons are:")
        for i in enumerate(weapon, start=1):
            print("\t", *i, sep=". ")
        print(" - The alternative to the weapons are:")
        for ii in enumerate(altWeapon, start=1):
            print("\t", *ii, sep=". ")

    def constellationDetails(const1, const2, const3, const4, const5, const6):
        print(" - " + const1[0])
        for i in enumerate(const1[1:], start=1):
            print("\t", *i, sep=". ")
        print("\n - " + const2[0])
        for ii in enumerate(const2[1:], start=1):
            print("\t", *ii, sep=". ")
        print("\n - " + const3[0])
        for iii in enumerate(const3[1:], start=1):
            print("\t", *iii, sep=". ")
        print("\n - " + const4[0])
        for iv in enumerate(const4[1:], start=1):
            print("\t", *iv, sep=". ")
        print("\n - " + const5[0])
        for v in enumerate(const5[1:], start=1):
            print("\t", *v, sep=". ")
        print("\n - " + const6[0])
        for vi in enumerate(const6[1:], start=1):
            print("\t", *vi, sep=". ")

    def artifactFormat(artifactStats):
        print("\n The format of the artifacts start are:")
        print(" ['Main stat', 'Sub Stat1, SubStat2, SubStat3, SubStat4']")
        print(" - The recommended artifact stats:")
        for iii in enumerate(artifactStats, start=1):
            print("\t", *iii, sep=". ")