import os
import random

"""Generate Simulation"""
NUMBER_OF_TIME_STEPS_WITH_CAR_GENERATION = 50
DET_POS = 40


def gen_sim(folder, p_west_east, p_east_west, p_north_south, p_south_north, N=NUMBER_OF_TIME_STEPS_WITH_CAR_GENERATION,
            round=2):
    os.makedirs(f'data/{folder}', exist_ok=True)
    # Specify routes taken by vehicles
    with open(f'data/{folder}/cross.rou.xml', "w+") as routes:
        print("""<routes>
            <vType id="typeWE" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="15" guiShape="passenger"/>
            <vType id="typeNS" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="15" guiShape="passenger"/>
            <route id="right" edges="51o 1i 2o 52i" />
            <route id="left" edges="52o 2i 1o 51i" />
            <route id="down" edges="54o 4i 3o 53i" />
            <route id="up" edges="53o 3i 4o 54i" />""", file=routes)
        vehNr = 0
        for i in range(N):
            if random.uniform(0, 1) < p_west_east:
                print('    <vehicle id="right_%i" type="typeWE" route="right" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < p_east_west:
                print('    <vehicle id="left_%i" type="typeWE" route="left" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < p_north_south:
                print('    <vehicle id="down_%i" type="typeNS" route="down" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < p_south_north:
                print('    <vehicle id="up_%i" type="typeNS" route="up" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
        print("</routes>", file=routes)
    with open(f'data/{folder}/cross.sumocfg', "w+") as cfg:
        print("""<?xml version="1.0" encoding="UTF-8"?>
            <configuration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/sumoConfiguration.xsd">
            <input>
                <net-file value="cross.net.xml"/>
                <route-files value="cross.rou.xml"/>
                <additional-files value="cross.det.xml"/>
                <gui-settings-file value="cross.settings.xml"/>
            </input>
            <time>
                <begin value="0"/>
            </time>
            <report>
                <verbose value="true"/>
                <no-step-log value="true"/>
            </report>
            </configuration>""", file=cfg)
    traff_states = """
                <tlLogic id="0" type="static" programID="0" offset="0">
                    <phase duration="300" state="GrGr"/>
                    <phase duration="6" state="yryr"/>
                    <phase duration="300" state="rGrG"/>
                    <phase duration="6" state="ryry"/>
                </tlLogic>
                """
    if round == 2:
        traff_states = """
                     <tlLogic id="0" type="static" programID="0" offset="0">
                        <phase duration="300" state="Grrr"/>
                        <phase duration="6" state="yrrr"/>
                        <phase duration="300" state="rGrr"/>
                        <phase duration="6" state="ryrr"/>
                        <phase duration="300" state="rrGr"/>
                        <phase duration="6" state="rryr"/>
                        <phase duration="300" state="rrrG"/>
                        <phase duration="6" state="rrry"/>
                    </tlLogic>
                """
    if round not in [1, 2]:
        print(f"ROUND {round} does not exist")
        raise ValueError

    with open(f'data/{folder}/cross.net.xml', "w+") as net:
        print("""<?xml version="1.0" encoding="UTF-8"?>
            <!-- generated on Thu Mar 26 16:23:52 2015 by SUMO netconvert Version dev-SVN-r18156I
            This data file and the accompanying materials
            are made available under the terms of the Eclipse Public License v2.0
            which accompanies this distribution, and is available at
            http://www.eclipse.org/legal/epl-v20.html
            SPDX-License-Identifier: EPL-2.0
            <configuration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/netconvertConfiguration.xsd">
                <input>
                    <node-files value="./complex/tutorial/traci_tls/data/cross.nod.xml"/>
                    <edge-files value="./complex/tutorial/traci_tls/data/cross.edg.xml"/>
                    <connection-files value="./complex/tutorial/traci_tls/data/cross.con.xml"/>
                </input>
                <output>
                    <output-file value="./complex/tutorial/traci_tls/data/cross.net.xml"/>
                </output>
                <report>
                    <verbose value="true"/>
                </report>
            </configuration>
            -->
            <net version="0.13" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/net_file.xsd">
                <location netOffset="510.00,510.00" convBoundary="0.00,0.00,1020.00,1020.00" origBoundary="-510.00,-510.00,510.00,510.00" projParameter="!"/>
                <edge id=":0_0" function="internal">
                    <lane id=":0_0_0" index="0" speed="15.28" length="9.50" shape="508.35,514.75 508.35,505.25"/>
                </edge>
                <edge id=":0_1" function="internal">
                    <lane id=":0_1_0" index="0" speed="15.28" length="9.50" shape="514.75,511.65 505.25,511.65"/>
                </edge>
                <edge id=":0_2" function="internal">
                    <lane id=":0_2_0" index="0" speed="15.28" length="9.50" shape="511.65,505.25 511.65,514.75"/>
                </edge>
                <edge id=":0_3" function="internal">
                    <lane id=":0_3_0" index="0" speed="15.28" length="9.50" shape="505.25,508.35 514.75,508.35"/>
                </edge>
                <edge id=":1_0" function="internal">
                    <lane id=":1_0_0" index="0" speed="15.28" length="0.10" shape="10.00,511.65 10.00,511.65"/>
                </edge>
                <edge id=":1_1" function="internal">
                    <lane id=":1_1_0" index="0" speed="15.28" length="2.41" shape="10.00,511.65 8.76,510.82 8.35,510.00"/>
                </edge>
                <edge id=":1_4" function="internal">
                    <lane id=":1_4_0" index="0" speed="15.28" length="2.41" shape="8.35,510.00 8.76,509.18 10.00,508.35"/>
                </edge>
                <edge id=":1_2" function="internal">
                    <lane id=":1_2_0" index="0" speed="15.28" length="0.10" shape="10.00,508.35 10.00,508.35"/>
                </edge>
                <edge id=":1_3" function="internal">
                    <lane id=":1_3_0" index="0" speed="15.28" length="2.41" shape="10.00,508.35 11.24,509.18 11.65,510.00"/>
                </edge>
                <edge id=":1_5" function="internal">
                    <lane id=":1_5_0" index="0" speed="15.28" length="2.41" shape="11.65,510.00 11.24,510.82 10.00,511.65"/>
                </edge>
                <edge id=":2_0" function="internal">
                    <lane id=":2_0_0" index="0" speed="15.28" length="0.10" shape="1010.00,511.65 1010.00,511.65"/>
                </edge>
                <edge id=":2_1" function="internal">
                    <lane id=":2_1_0" index="0" speed="15.28" length="2.41" shape="1010.00,511.65 1008.76,510.82 1008.35,510.00"/>
                </edge>
                <edge id=":2_4" function="internal">
                    <lane id=":2_4_0" index="0" speed="15.28" length="2.41" shape="1008.35,510.00 1008.76,509.18 1010.00,508.35"/>
                </edge>
                <edge id=":2_2" function="internal">
                    <lane id=":2_2_0" index="0" speed="15.28" length="0.10" shape="1010.00,508.35 1010.00,508.35"/>
                </edge>
                <edge id=":2_3" function="internal">
                    <lane id=":2_3_0" index="0" speed="15.28" length="2.41" shape="1010.00,508.35 1011.24,509.18 1011.65,510.00"/>
                </edge>
                <edge id=":2_5" function="internal">
                    <lane id=":2_5_0" index="0" speed="15.28" length="2.41" shape="1011.65,510.00 1011.24,510.82 1010.00,511.65"/>
                </edge>
                <edge id=":3_0" function="internal">
                    <lane id=":3_0_0" index="0" speed="15.28" length="0.10" shape="508.35,10.00 508.35,10.00"/>
                </edge>
                <edge id=":3_1" function="internal">
                    <lane id=":3_1_0" index="0" speed="15.28" length="2.41" shape="508.35,10.00 509.18,8.76 510.00,8.35"/>
                </edge>
                <edge id=":3_4" function="internal">
                    <lane id=":3_4_0" index="0" speed="15.28" length="2.41" shape="510.00,8.35 510.82,8.76 511.65,10.00"/>
                </edge>
                <edge id=":3_2" function="internal">
                    <lane id=":3_2_0" index="0" speed="15.28" length="0.10" shape="511.65,10.00 511.65,10.00"/>
                </edge>
                <edge id=":3_3" function="internal">
                    <lane id=":3_3_0" index="0" speed="15.28" length="2.41" shape="511.65,10.00 510.82,11.24 510.00,11.65"/>
                </edge>
                <edge id=":3_5" function="internal">
                    <lane id=":3_5_0" index="0" speed="15.28" length="2.41" shape="510.00,11.65 509.18,11.24 508.35,10.00"/>
                </edge>
                <edge id=":4_0" function="internal">
                    <lane id=":4_0_0" index="0" speed="15.28" length="0.10" shape="508.35,1010.00 508.35,1010.00"/>
                </edge>
                <edge id=":4_1" function="internal">
                    <lane id=":4_1_0" index="0" speed="15.28" length="2.41" shape="508.35,1010.00 509.18,1008.76 510.00,1008.35"/>
                </edge>
                <edge id=":4_4" function="internal">
                    <lane id=":4_4_0" index="0" speed="15.28" length="2.41" shape="510.00,1008.35 510.82,1008.76 511.65,1010.00"/>
                </edge>
                <edge id=":4_2" function="internal">
                    <lane id=":4_2_0" index="0" speed="15.28" length="0.10" shape="511.65,1010.00 511.65,1010.00"/>
                </edge>
                <edge id=":4_3" function="internal">
                    <lane id=":4_3_0" index="0" speed="15.28" length="2.41" shape="511.65,1010.00 510.82,1011.24 510.00,1011.65"/>
                </edge>
                <edge id=":4_5" function="internal">
                    <lane id=":4_5_0" index="0" speed="15.28" length="2.41" shape="510.00,1011.65 509.18,1011.24 508.35,1010.00"/>
                </edge>
                <edge id=":51_0" function="internal">
                    <lane id=":51_0_0" index="0" speed="15.28" length="4.82" shape="0.00,511.65 -1.24,510.82 -1.65,510.00 -1.24,509.18 0.00,508.35"/>
                </edge>
                <edge id=":52_0" function="internal">
                    <lane id=":52_0_0" index="0" speed="15.28" length="4.82" shape="1020.00,508.35 1021.24,509.18 1021.65,510.00 1021.24,510.82 1020.00,511.65"/>
                </edge>
                <edge id=":53_0" function="internal">
                    <lane id=":53_0_0" index="0" speed="15.28" length="4.82" shape="508.35,0.00 509.18,-1.24 510.00,-1.65 510.82,-1.24 511.65,0.00"/>
                </edge>
                <edge id=":54_0" function="internal">
                    <lane id=":54_0_0" index="0" speed="15.28" length="4.82" shape="511.65,1020.00 510.82,1021.24 510.00,1021.65 509.18,1021.24 508.35,1020.00"/>
                </edge>
                <edge id="1i" from="1" to="0" priority="78">
                    <lane id="1i_0" index="0" speed="19.44" length="495.25" shape="10.00,508.35 505.25,508.35"/>
                </edge>
                <edge id="1o" from="0" to="1" priority="46">
                    <lane id="1o_0" index="0" speed="11.11" length="495.25" shape="505.25,511.65 10.00,511.65"/>
                </edge>
                <edge id="2i" from="2" to="0" priority="78">
                    <lane id="2i_0" index="0" speed="19.44" length="495.25" shape="1010.00,511.65 514.75,511.65"/>
                </edge>
                <edge id="2o" from="0" to="2" priority="46">
                    <lane id="2o_0" index="0" speed="11.11" length="495.25" shape="514.75,508.35 1010.00,508.35"/>
                </edge>
                <edge id="3i" from="3" to="0" priority="78">
                    <lane id="3i_0" index="0" speed="19.44" length="495.25" shape="511.65,10.00 511.65,505.25"/>
                </edge>
                <edge id="3o" from="0" to="3" priority="46">
                    <lane id="3o_0" index="0" speed="11.11" length="495.25" shape="508.35,505.25 508.35,10.00"/>
                </edge>
                <edge id="4i" from="4" to="0" priority="78">
                    <lane id="4i_0" index="0" speed="19.44" length="495.25" shape="508.35,1010.00 508.35,514.75"/>
                </edge>
                <edge id="4o" from="0" to="4" priority="46">
                    <lane id="4o_0" index="0" speed="11.11" length="495.25" shape="511.65,514.75 511.65,1010.00"/>
                </edge>
                <edge id="51i" from="1" to="51" priority="78">
                    <lane id="51i_0" index="0" speed="19.44" length="10.00" shape="10.00,511.65 0.00,511.65"/>
                </edge>
                <edge id="51o" from="51" to="1" priority="46">
                    <lane id="51o_0" index="0" speed="11.11" length="10.00" shape="0.00,508.35 10.00,508.35"/>
                </edge>
                <edge id="52i" from="2" to="52" priority="78">
                    <lane id="52i_0" index="0" speed="19.44" length="10.00" shape="1010.00,508.35 1020.00,508.35"/>
                </edge>
                <edge id="52o" from="52" to="2" priority="46">
                    <lane id="52o_0" index="0" speed="11.11" length="10.00" shape="1020.00,511.65 1010.00,511.65"/>
                </edge>
                <edge id="53i" from="3" to="53" priority="78">
                    <lane id="53i_0" index="0" speed="19.44" length="10.00" shape="508.35,10.00 508.35,0.00"/>
                </edge>
                <edge id="53o" from="53" to="3" priority="46">
                    <lane id="53o_0" index="0" speed="11.11" length="10.00" shape="511.65,0.00 511.65,10.00"/>
                </edge>
                <edge id="54i" from="4" to="54" priority="78">
                    <lane id="54i_0" index="0" speed="19.44" length="10.00" shape="511.65,1010.00 511.65,1020.00"/>
                </edge>
                <edge id="54o" from="54" to="4" priority="46">
                    <lane id="54o_0" index="0" speed="11.11" length="10.00" shape="508.35,1020.00 508.35,1010.00"/>
                </edge>
                """ + traff_states +
              """
                <junction id="0" type="traffic_light" x="510.00" y="510.00" incLanes="4i_0 2i_0 3i_0 1i_0" intLanes=":0_0_0 :0_1_0 :0_2_0 :0_3_0" shape="506.75,514.75 513.25,514.75 514.75,513.25 514.75,506.75 513.25,505.25 506.75,505.25 505.25,506.75 505.25,513.25">
                    <request index="0" response="0000" foes="1010" cont="0"/>
                    <request index="1" response="0101" foes="0101" cont="0"/>
                    <request index="2" response="0000" foes="1010" cont="0"/>
                    <request index="3" response="0101" foes="0101" cont="0"/>
                </junction>
                <junction id="1" type="priority" x="10.00" y="510.00" incLanes="1o_0 51o_0" intLanes=":1_0_0 :1_4_0 :1_2_0 :1_5_0" shape="10.00,513.25 10.00,506.75 10.00,513.25">
                    <request index="0" response="0000" foes="1000" cont="0"/>
                    <request index="1" response="0100" foes="0100" cont="1"/>
                    <request index="2" response="0000" foes="0010" cont="0"/>
                    <request index="3" response="0001" foes="0001" cont="1"/>
                </junction>
                <junction id="2" type="priority" x="1010.00" y="510.00" incLanes="52o_0 2o_0" intLanes=":2_0_0 :2_4_0 :2_2_0 :2_5_0" shape="1010.00,513.25 1010.00,506.75 1010.00,513.25">
                    <request index="0" response="0000" foes="1000" cont="0"/>
                    <request index="1" response="0100" foes="0100" cont="1"/>
                    <request index="2" response="0000" foes="0010" cont="0"/>
                    <request index="3" response="0001" foes="0001" cont="1"/>
                </junction>
                <junction id="3" type="priority" x="510.00" y="10.00" incLanes="3o_0 53o_0" intLanes=":3_0_0 :3_4_0 :3_2_0 :3_5_0" shape="506.75,10.00 513.25,10.00 506.75,10.00">
                    <request index="0" response="0000" foes="1000" cont="0"/>
                    <request index="1" response="0100" foes="0100" cont="1"/>
                    <request index="2" response="0000" foes="0010" cont="0"/>
                    <request index="3" response="0001" foes="0001" cont="1"/>
                </junction>
                <junction id="4" type="priority" x="510.00" y="1010.00" incLanes="54o_0 4o_0" intLanes=":4_0_0 :4_4_0 :4_2_0 :4_5_0" shape="506.75,1010.00 513.25,1010.00 506.75,1010.00">
                    <request index="0" response="0000" foes="1000" cont="0"/>
                    <request index="1" response="0100" foes="0100" cont="1"/>
                    <request index="2" response="0000" foes="0010" cont="0"/>
                    <request index="3" response="0001" foes="0001" cont="1"/>
                </junction>
                <junction id="51" type="priority" x="0.00" y="510.00" incLanes="51i_0" intLanes=":51_0_0" shape="-0.00,509.95 -0.00,506.75 0.00,513.25 0.00,510.05">
                    <request index="0" response="0" foes="0" cont="0"/>
                </junction>
                <junction id="52" type="priority" x="1020.00" y="510.00" incLanes="52i_0" intLanes=":52_0_0" shape="1020.00,510.05 1020.00,513.25 1020.00,506.75 1020.00,509.95">
                    <request index="0" response="0" foes="0" cont="0"/>
                </junction>
                <junction id="53" type="priority" x="510.00" y="0.00" incLanes="53i_0" intLanes=":53_0_0" shape="510.05,-0.00 513.25,-0.00 506.75,0.00 509.95,0.00">
                    <request index="0" response="0" foes="0" cont="0"/>
                </junction>
                <junction id="54" type="priority" x="510.00" y="1020.00" incLanes="54i_0" intLanes=":54_0_0" shape="509.95,1020.00 506.75,1020.00 513.25,1020.00 510.05,1020.00">
                    <request index="0" response="0" foes="0" cont="0"/>
                </junction>
                <junction id=":1_4_0" type="internal" x="8.35" y="510.00" incLanes=":1_1_0 51o_0" intLanes=":1_2_0"/>
                <junction id=":1_5_0" type="internal" x="11.65" y="510.00" incLanes=":1_3_0 1o_0" intLanes=":1_0_0"/>
                <junction id=":2_4_0" type="internal" x="1008.35" y="510.00" incLanes=":2_1_0 2o_0" intLanes=":2_2_0"/>
                <junction id=":2_5_0" type="internal" x="1011.65" y="510.00" incLanes=":2_3_0 52o_0" intLanes=":2_0_0"/>
                <junction id=":3_4_0" type="internal" x="510.00" y="8.35" incLanes=":3_1_0 53o_0" intLanes=":3_2_0"/>
                <junction id=":3_5_0" type="internal" x="510.00" y="11.65" incLanes=":3_3_0 3o_0" intLanes=":3_0_0"/>
                <junction id=":4_4_0" type="internal" x="510.00" y="1008.35" incLanes=":4_1_0 4o_0" intLanes=":4_2_0"/>
                <junction id=":4_5_0" type="internal" x="510.00" y="1011.65" incLanes=":4_3_0 54o_0" intLanes=":4_0_0"/>
                <connection from="1i" to="2o" fromLane="0" toLane="0" via=":0_3_0" tl="0" linkIndex="3" dir="s" state="o"/>
                <connection from="1o" to="51i" fromLane="0" toLane="0" via=":1_0_0" dir="s" state="M"/>
                <connection from="1o" to="1i" fromLane="0" toLane="0" via=":1_1_0" dir="t" state="m"/>
                <connection from="2i" to="1o" fromLane="0" toLane="0" via=":0_1_0" tl="0" linkIndex="1" dir="s" state="o"/>
                <connection from="2o" to="52i" fromLane="0" toLane="0" via=":2_2_0" dir="s" state="M"/>
                <connection from="2o" to="2i" fromLane="0" toLane="0" via=":2_3_0" dir="t" state="m"/>
                <connection from="3i" to="4o" fromLane="0" toLane="0" via=":0_2_0" tl="0" linkIndex="2" dir="s" state="o"/>
                <connection from="3o" to="53i" fromLane="0" toLane="0" via=":3_0_0" dir="s" state="M"/>
                <connection from="3o" to="3i" fromLane="0" toLane="0" via=":3_1_0" dir="t" state="m"/>
                <connection from="4i" to="3o" fromLane="0" toLane="0" via=":0_0_0" tl="0" linkIndex="0" dir="s" state="o"/>
                <connection from="4o" to="54i" fromLane="0" toLane="0" via=":4_2_0" dir="s" state="M"/>
                <connection from="4o" to="4i" fromLane="0" toLane="0" via=":4_3_0" dir="t" state="m"/>
                <connection from="51i" to="51o" fromLane="0" toLane="0" via=":51_0_0" dir="t" state="M"/>
                <connection from="51o" to="1i" fromLane="0" toLane="0" via=":1_2_0" dir="s" state="M"/>
                <connection from="51o" to="51i" fromLane="0" toLane="0" via=":1_3_0" dir="t" state="m"/>
                <connection from="52i" to="52o" fromLane="0" toLane="0" via=":52_0_0" dir="t" state="M"/>
                <connection from="52o" to="2i" fromLane="0" toLane="0" via=":2_0_0" dir="s" state="M"/>
                <connection from="52o" to="52i" fromLane="0" toLane="0" via=":2_1_0" dir="t" state="m"/>
                <connection from="53i" to="53o" fromLane="0" toLane="0" via=":53_0_0" dir="t" state="M"/>
                <connection from="53o" to="3i" fromLane="0" toLane="0" via=":3_2_0" dir="s" state="M"/>
                <connection from="53o" to="53i" fromLane="0" toLane="0" via=":3_3_0" dir="t" state="m"/>
                <connection from="54i" to="54o" fromLane="0" toLane="0" via=":54_0_0" dir="t" state="M"/>
                <connection from="54o" to="4i" fromLane="0" toLane="0" via=":4_0_0" dir="s" state="M"/>
                <connection from="54o" to="54i" fromLane="0" toLane="0" via=":4_1_0" dir="t" state="m"/>
                <connection from=":0_0" to="3o" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":0_1" to="1o" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":0_2" to="4o" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":0_3" to="2o" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":1_0" to="51i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":1_1" to="1i" fromLane="0" toLane="0" via=":1_4_0" dir="s" state="m"/>
                <connection from=":1_4" to="1i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":1_2" to="1i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":1_3" to="51i" fromLane="0" toLane="0" via=":1_5_0" dir="s" state="m"/>
                <connection from=":1_5" to="51i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":2_0" to="2i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":2_1" to="52i" fromLane="0" toLane="0" via=":2_4_0" dir="s" state="m"/>
                <connection from=":2_4" to="52i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":2_2" to="52i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":2_3" to="2i" fromLane="0" toLane="0" via=":2_5_0" dir="s" state="m"/>
                <connection from=":2_5" to="2i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":3_0" to="53i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":3_1" to="3i" fromLane="0" toLane="0" via=":3_4_0" dir="s" state="m"/>
                <connection from=":3_4" to="3i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":3_2" to="3i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":3_3" to="53i" fromLane="0" toLane="0" via=":3_5_0" dir="s" state="m"/>
                <connection from=":3_5" to="53i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":4_0" to="4i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":4_1" to="54i" fromLane="0" toLane="0" via=":4_4_0" dir="s" state="m"/>
                <connection from=":4_4" to="54i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":4_2" to="54i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":4_3" to="4i" fromLane="0" toLane="0" via=":4_5_0" dir="s" state="m"/>
                <connection from=":4_5" to="4i" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":51_0" to="51o" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":52_0" to="52o" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":53_0" to="53o" fromLane="0" toLane="0" dir="s" state="M"/>
                <connection from=":54_0" to="54o" fromLane="0" toLane="0" dir="s" state="M"/>
            </net>""", file=net)
    with open(f'data/{folder}/cross.det.xml', "w+") as det:
        print("""<additional>
            <e1Detector id="0" lane="4i_0" pos="-5" freq="30" file="cross.out" friendlyPos="x"/>
            <e1Detector id="1" lane="3i_0" pos="-5" freq="30" file="cross2.out" friendlyPos="x"/>
            <e1Detector id="2" lane="2i_0" pos="-5" freq="30" file="cross3.out" friendlyPos="x"/>
            <e1Detector id="3" lane="1i_0" pos="-5" freq="30" file="cross4.out" friendlyPos="x"/>
            <e1Detector id="4" lane="4i_0" pos="-""" + str(DET_POS) + "\"" + """ freq="30" file="cross.out" friendlyPos="x"/>
            <e1Detector id="5" lane="3i_0" pos="-""" + str(DET_POS) + "\"" + """ freq="30" file="cross.out" friendlyPos="x"/>
            <e1Detector id="6" lane="2i_0" pos="-""" + str(DET_POS) + "\"" + """ freq="30" file="cross.out" friendlyPos="x"/>
            <e1Detector id="7" lane="1i_0" pos="-""" + str(DET_POS) + "\"" + """ freq="30" file="cross.out" friendlyPos="x"/>
            </additional>""", file=det)
    with open(f'data/{folder}/cross.settings.xml', "w+") as settings_file:
        print("""<viewsettings>
            <viewport y="500" x="500" zoom="600"/>
            <delay value="120"/>
            </viewsettings>""", file=settings_file)
    with open(f'data/{folder}/vehicles.txt', "w+") as veh:
        print(vehNr, file=veh)
    return vehNr