import copy
from operator import pos
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    oomp_mode = "project"
    #oomp_mode = "oobb"

    test = False
    #test = True

    if typ == "all":
        #no overwrite
        
        filter = ""; save_type = "all"; navigation = True; overwrite = False; modes = ["3dpr"]; oomp_run = True; test = False
        #default
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
        #default
        #filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        options = []

        # standard circle ones
        if True:        
        #if True:
            thicknesses = [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,70,80,90,100]
            diams = [20,14]
            flange_extras = [6,12,18,20,0]
            flange_depths = [0,3,6]
            screw_diams = ["m4_screw_wood", "m3_screw_wood", "m3_5_screw_wood", "m5_screw_wood"]

            

            for thickness in thicknesses:
                for diam in diams:
                    for flange_extra in flange_extras:
                        for flange_depth in flange_depths:
                            for screw_diameter in screw_diams:
                                option = {}
                                option["thickness"] = thickness
                                option["diam"] = diam
                                option["flange_extra"] = flange_extra
                                option["flange_depth"] = flange_depth
                                option["screw_diameter"] = screw_diameter
                                options.append(option)
            #m6 wood screw ones
        if True:
            if True:
                thicknesses = [120,130,140]
                diams = [20,14]
                flange_extras = [0,6,12]
                flange_depths = [0,3,6]
                screw_diams = ["m6_screw_wood"]

                
                for thickness in thicknesses:
                    for diam in diams:
                        for flange_extra in flange_extras:
                            for flange_depth in flange_depths:
                                for screw_diameter in screw_diams:
                                    option = {}
                                    option["thickness"] = thickness
                                    option["diam"] = diam
                                    option["flange_extra"] = flange_extra
                                    option["flange_depth"] = flange_depth
                                    option["screw_diameter"] = screw_diameter
                                    options.append(option)

            option = {}
            option["thickness"] = 12
            option["diam"] = 5
            option["flange_extra"] = 5
            option["flange_depth"] = 5
            option["screw_diameter"] = "m3_screw_wood"
            options.append(option)

            option = {}
            option["thickness"] = 30
            option["diam"] = 14
            option["flange_extra"] = 6
            option["flange_depth"] = 6
            option["screw_diameter"] = "m4_screw_wood"
            options.append(option)

            #screws in screwtite box
            thicknesses = [15,20,30,40,50,60,70,90]
            diams = [8,10,14]
            flange_extras = [6]
            flange_depths = [0,3]
            screw_diams = ["m4_screw_wood"]

            

            for thickness in thicknesses:
                for diam in diams:
                    for flange_extra in flange_extras:
                        for flange_depth in flange_depths:
                            for screw_diameter in screw_diams:
                                option = {}
                                option["thickness"] = thickness
                                option["diam"] = diam
                                option["flange_extra"] = flange_extra
                                option["flange_depth"] = flange_depth
                                option["screw_diameter"] = screw_diameter
                                options.append(option)


            # pegs
            for option in options:
                thickness = option["thickness"]
                diam = option["diam"]
                flange_extra = option["flange_extra"]
                screw_diameter = option["screw_diameter"]
                if "flange_depth" in option:
                    flange_depth = option["flange_depth"]
                
                
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["thickness"] = thickness               
                p3["radius"] = diam/2        
                p3["flange_extra"] = flange_extra
                p3["flange_depth"] = flange_depth
                p3["screw_diameter"] = screw_diameter
                p3["extra"] = f"flange_{diam}_flange_extra_{flange_extra}_flange_depth_{flange_depth}_screw_dameter_{screw_diameter}"        
                part["kwargs"] = p3
                part["name"] = f"peg"
                
                parts.append(part)


            #sockets 
            
            diams = copy.deepcopy(diams)
            flange_extras = copy.deepcopy(flange_extras)

            for diam in diams:
                for flange_extra in flange_extras:
                    for flange_depth in flange_depths:
                        for screw_diameter in screw_diams:
                            option = {}
                            option["thickness"] = 6
                            option["diam"] = diam
                            option["flange_extra"] = flange_extra
                            option["width"] = 3
                            option["height"] = 3
                            options.append(option)



            for option in options:
                thickness = option["thickness"]
                diam = option["diam"]
                flange_extra = option["flange_extra"]                
                
                part = copy.deepcopy(part_default)
                p3 = copy.deepcopy(kwargs)
                p3["thickness"] = thickness               
                p3["radius"] = diam/2        
                p3["flange_extra"] = flange_extra
                p3["flange_depth"] = flange_depth
                p3["screw_diameter"] = screw_diameter
                p3["extra"] = f"flange_{diam}_flange_extra_{flange_extra}" 
                p3["width"] = option.get("width", 1)
                p3["height"] = option.get("height", 1)
                part["kwargs"] = p3
                part["name"] = f"socket"
                       
                parts.append(part)

# multi hole ones
        #if False:
        if True:

            pegs = []
            
            flange_extras = [15,0,30,100,50]

            peg = {}            
            peg["diam"] = 20
            peg["flange_extra"] = 15
            peg["flange_depth"] = 6
            peg["screw_diameter"] = "m3_screw_wood"
            thicknesses = [15,30,40]
            
            for thickness in thicknesses:
                peg = copy.deepcopy(peg)
                peg["thickness"] = thickness
                pegs.append(peg)


            peg = copy.deepcopy(peg)
            peg["thickness"] = 80
            peg["screw_diameter"] = "m5_screw_wood"
            pegs.append(peg)

            peg = copy.deepcopy(peg)
            peg["thickness"] = 130
            peg["screw_diameter"] = "m6_screw_wood"                     
            peg["diam"] = 25
            pegs.append(peg)
            
            peg = copy.deepcopy(peg)
            peg["thickness"] = 0
            peg["screw_diameter"] = "m6_screw_wood"                     
            peg["diam"] = 25
            pegs.append(peg)

            
            peg = copy.deepcopy(peg)
            peg["thickness"] = 175
            peg["screw_diameter"] = "m6_screw_wood"                     
            peg["diam"] = 25
            pegs.append(peg)

            peg = copy.deepcopy(peg)
            peg["thickness"] = 25
            peg["screw_diameter"] = "m6_screw_wood"                     
            peg["diam"] = 25
            pegs.append(peg)

            peg = copy.deepcopy(peg)
            peg["thickness"] = 50
            peg["screw_diameter"] = "m6_screw_wood"                     
            peg["diam"] = 25
            pegs.append(peg)

            peg = copy.deepcopy(peg)
            peg["thickness"] = 75
            peg["screw_diameter"] = "m6_screw_wood"                     
            peg["diam"] = 25
            pegs.append(peg)


            for peg in pegs:
                for flange_extra in flange_extras:
                    thickness = peg["thickness"]
                    diam = peg["diam"]
                    #flange_extra = peg["flange_extra"]
                    flange_extra = flange_extra
                    flange_depth = peg["flange_depth"]
                    screw_diameter = peg["screw_diameter"]
                    part = copy.deepcopy(part_default)
                    p3 = copy.deepcopy(kwargs)
                    
                    p3["thickness"] = thickness               
                    p3["radius"] = diam/2        
                    p3["flange_extra"] = flange_extra
                    p3["flange_depth"] = flange_depth
                    p3["screw_diameter"] = screw_diameter
                    multi_hole = 3
                    p3["multi_hole"] = multi_hole                        
                    p3["extra"] = f"_flange_{diam}_flange_extra_{flange_extra}_flange_depth_{flange_depth}_screw_dameter_{screw_diameter}_multi_hole_{multi_hole}"        
                    part["kwargs"] = p3
                    part["name"] = f"peg"
                    
                    parts.append(part)

            
            diams = [20]
            screw_diams = ["m3_screw_wood", "m4_screw_wood", "m5_screw_wood"]

            for diam in diams:
                for screw_diam in screw_diams:
                    thickness = 9
                    diam = diam
                    screw_diameter = screw_diam
                    part = copy.deepcopy(part_default)
                    p3 = copy.deepcopy(kwargs)                    
                    p3["thickness"] = thickness               
                    p3["radius"] = diam/2        
                    p3["screw_diameter"] = screw_diameter
                    multi_hole = 3
                    p3["multi_hole"] = multi_hole                        
                    p3["extra"] = f"flange_{diam}__screw_dameter_{screw_diameter}_multi_hole_{multi_hole}"        
                    part["kwargs"] = p3
                    part["name"] = f"label_holder"
                    
                    parts.append(part)



        
        # flat ones
        #if False:
        if True:
            thicknesses = [15]
            diams = [20]
            flange_extras = [6]
            flange_depths = [3]
            flat_lengths = [10]

            for thickness in thicknesses:
                for diam in diams:
                    for flange_extra in flange_extras:
                        for flange_depth in flange_depths:                        
                            for flat_length in flat_lengths:                                
                                part = copy.deepcopy(part_default)
                                p3 = copy.deepcopy(kwargs)
                                p3["thickness"] = thickness               
                                p3["radius"] = diam/2        
                                
                                p3["flat_length"] = flat_length
                                p3["flange_extra"] = flange_extra
                                p3["flange_depth"] = flange_depth        
                                p3["extra"] = f"flange_{diam}_flange_extra_{flange_extra}_flange_depth_{flange_depth}_flat_length_{flat_length}_depth_{thickness}"        
                                part["kwargs"] = p3
                                part["name"] = f"peg"
                                
                                parts.append(part)
        
        #cap
        
        if True:
            diameters = [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
            depths = [3, 6]
            extra_diameters = [12,6,2]
            for diameter in diameters:
                for depth in depths:
                    for extra_diameter in extra_diameters:
                        part = copy.deepcopy(part_default)
                        p3 = copy.deepcopy(kwargs)
                        p3["thickness"] = depth               
                        p3["diameter"] = diameter
                        p3["extra_diameter"] = extra_diameter
                        p3["extra"] = f"{extra_diameter}_extra_diameter"
                        part["kwargs"] = p3
                        part["name"] = f"cap"                        
                        parts.append(part)

    

        kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        #sort.append("width")
        #sort.append("height")
        sort.append("thickness")
        sort.append("radius")
        sort.append("diameter")
        sort.append("screw_diameter")
        sort.append("flange_extra")
        sort.append("flange_depth")
        #extra_diameter
        sort.append("extra_diameter")
        
        scad_help.generate_navigation(sort = sort)


def get_base(thing, **kwargs):
    name = kwargs.get("type", "default")
    if "label_holder" in name:
        get_label_holder(thing, **kwargs)
    if "socket" in name:
        get_socket(thing, **kwargs)
    else:
        depth = kwargs.get("thickness", 4)
        radius = kwargs.get("radius", 10)
        prepare_print = kwargs.get("prepare_print", False)
        screw_diameter = kwargs.get("screw_diameter", "m4_screw_wood")
        #
        flange_extra = kwargs.get("flange_extra", 0)
        flange_depth = kwargs.get("flange_depth", 0)
        flat_length = kwargs.get("flat_length", 0)
        multi_hole = kwargs.get("multi_hole", 1)



        pos = kwargs.get("pos", [0, 0, 0])
        #pos = copy.deepcopy(pos)
        #pos[2] += -20

        #add cylinder
        if flat_length == 0:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "p"
            p3["shape"] = f"oobb_cylinder"    
            p3["depth"] = depth
            p3["radius"] = radius
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            p3["pos"] = pos1
            p3["zz"] = "top"
            oobb_base.append_full(thing,**p3)
            #add flange if flange extra is set
            if flange_extra > 0:            
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"oobb_cylinder"    
                p3["depth"] = flange_depth
                p3["radius"] = radius + flange_extra/2
                #p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                p3["pos"] = pos1
                p3["zz"] = "top"
                oobb_base.append_full(thing,**p3)
        else:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "p"
            p3["shape"] = f"rounded_rectangle"    
            wid = radius*2 + flat_length
            hei = radius*2
            dep = depth
            size = [wid, hei, dep]
            p3["size"] = size
            p3["radius"] = radius        
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            pos1[2] += -dep
            p3["pos"] = pos1
            p3["zz"] = "top"
            oobb_base.append_full(thing,**p3)
            #add flange if flange extra is set
            if flange_extra > 0:            
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"rounded_rectangle"    
                wid = radius*2 + flat_length + flange_extra
                hei = radius*2 + flange_extra
                dep = flange_depth
                size = [wid, hei, dep]
                p3["size"] = size
                #p3["radius"] = radius + flange_extra/2            
                #p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                pos1[2] += -dep
                p3["pos"] = pos1            
                oobb_base.append_full(thing,**p3)


        #add holes
        if True:
            if multi_hole == 1:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_screw_countersunk"    
                p3["depth"] = depth
                p3["radius_name"] = screw_diameter
                p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                p3["pos"] = pos1
                oobb_base.append_full(thing,**p3)
            if multi_hole == 3:
                
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_screw_countersunk"    
                p3["depth"] = depth
                p3["radius_name"] = screw_diameter
                p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                
                import math          
                if radius == 12.5:
                    shift = 8
                else:
                    shift = 6
                
                pos11 = copy.deepcopy(pos1)
                angle = 0
                pos11[0] += math.cos(math.radians(angle))*shift
                pos11[1] += math.sin(math.radians(angle))*shift
                pos12 = copy.deepcopy(pos1)
                angle = 120
                pos12[0] += math.cos(math.radians(angle))*shift
                pos12[1] += math.sin(math.radians(angle))*shift
                pos13 = copy.deepcopy(pos1)
                angle = 240
                pos13[0] += math.cos(math.radians(angle))*shift
                pos13[1] += math.sin(math.radians(angle))*shift
                

                poss = []
                poss.append(pos11)
                poss.append(pos12)
                poss.append(pos13)


                p3["pos"] = poss
                oobb_base.append_full(thing,**p3)


        if prepare_print:
            #put into a rotation object
            components_second = copy.deepcopy(thing["components"])
            return_value_2 = {}
            return_value_2["type"]  = "rotation"
            return_value_2["typetype"]  = "p"
            pos1 = copy.deepcopy(pos)
            pos1[0] += 50
            return_value_2["pos"] = pos1
            return_value_2["rot"] = [180,0,0]
            return_value_2["objects"] = components_second
            
            thing["components"].append(return_value_2)

        
            #add slice # top
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_slice"
            #p3["m"] = "#"
            oobb_base.append_full(thing,**p3)

def get_peg(thing, **kwargs):
    if True:
        depth = kwargs.get("thickness", 4)
        radius = kwargs.get("radius", 10)
        prepare_print = kwargs.get("prepare_print", False)
        screw_diameter = kwargs.get("screw_diameter", "m4_screw_wood")
        #
        flange_extra = kwargs.get("flange_extra", 0)
        flange_depth = kwargs.get("flange_depth", 0)
        flat_length = kwargs.get("flat_length", 0)
        multi_hole = kwargs.get("multi_hole", 1)



        pos = kwargs.get("pos", [0, 0, 0])
        #pos = copy.deepcopy(pos)
        #pos[2] += -20

        #add cylinder
        if flat_length == 0:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "p"
            p3["shape"] = f"oobb_cylinder"    
            p3["depth"] = depth
            p3["radius"] = radius
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            p3["pos"] = pos1
            p3["zz"] = "top"
            oobb_base.append_full(thing,**p3)
            #add flange if flange extra is set
            if flange_extra > 0:            
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"oobb_cylinder"    
                p3["depth"] = flange_depth
                p3["radius"] = radius + flange_extra/2
                #p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                p3["pos"] = pos1
                p3["zz"] = "top"
                oobb_base.append_full(thing,**p3)
        else:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "p"
            p3["shape"] = f"rounded_rectangle"    
            wid = radius*2 + flat_length
            hei = radius*2
            dep = depth
            size = [wid, hei, dep]
            p3["size"] = size
            p3["radius"] = radius        
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            pos1[2] += -dep
            p3["pos"] = pos1
            p3["zz"] = "top"
            oobb_base.append_full(thing,**p3)
            #add flange if flange extra is set
            if flange_extra > 0:            
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "p"
                p3["shape"] = f"rounded_rectangle"    
                wid = radius*2 + flat_length + flange_extra
                hei = radius*2 + flange_extra
                dep = flange_depth
                size = [wid, hei, dep]
                p3["size"] = size
                #p3["radius"] = radius + flange_extra/2            
                #p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                pos1[2] += -dep
                p3["pos"] = pos1            
                oobb_base.append_full(thing,**p3)


        #add holes
        if True:
            if multi_hole == 1:
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_screw_countersunk"    
                p3["depth"] = depth
                p3["radius_name"] = screw_diameter
                p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                p3["pos"] = pos1
                oobb_base.append_full(thing,**p3)
            if multi_hole == 3:
                
                p3 = copy.deepcopy(kwargs)
                p3["type"] = "n"
                p3["shape"] = f"oobb_screw_countersunk"    
                p3["depth"] = depth
                p3["radius_name"] = screw_diameter
                p3["m"] = "#"
                pos1 = copy.deepcopy(pos)         
                
                import math          
                if radius == 12.5:
                    shift = 8
                else:
                    shift = 6
                
                pos11 = copy.deepcopy(pos1)
                angle = 0
                pos11[0] += math.cos(math.radians(angle))*shift
                pos11[1] += math.sin(math.radians(angle))*shift
                pos12 = copy.deepcopy(pos1)
                angle = 120
                pos12[0] += math.cos(math.radians(angle))*shift
                pos12[1] += math.sin(math.radians(angle))*shift
                pos13 = copy.deepcopy(pos1)
                angle = 240
                pos13[0] += math.cos(math.radians(angle))*shift
                pos13[1] += math.sin(math.radians(angle))*shift
                

                poss = []
                poss.append(pos11)
                poss.append(pos12)
                poss.append(pos13)


                p3["pos"] = poss
                oobb_base.append_full(thing,**p3)


        if prepare_print:
            #put into a rotation object
            components_second = copy.deepcopy(thing["components"])
            return_value_2 = {}
            return_value_2["type"]  = "rotation"
            return_value_2["typetype"]  = "p"
            pos1 = copy.deepcopy(pos)
            pos1[0] += 50
            return_value_2["pos"] = pos1
            return_value_2["rot"] = [180,0,0]
            return_value_2["objects"] = components_second
            
            thing["components"].append(return_value_2)

        
            #add slice # top
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_slice"
            #p3["m"] = "#"
            oobb_base.append_full(thing,**p3)

def get_cap(thing, **kwargs):
    depth = kwargs.get("thickness", 4)
    diameter = kwargs.get("diameter", 20)
    extra_diameter = kwargs.get("extra_diameter", 6)
    extra_depth = 1
    clearance = 0.2

    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])

    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"    
    p3["depth"] = depth + extra_depth
    p3["radius"] = (diameter+extra_diameter)/2
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    p3["zz"] = "top"
    oobb_base.append_full(thing,**p3)

    #hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_cylinder"    
    p3["depth"] = depth
    p3["radius"] = (diameter+clearance)/2
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    p3["zz"] = "top"
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_label_holder(thing, **kwargs):

    depth = kwargs.get("thickness", 4)
    radius = kwargs.get("radius", 10)
    kwargs.pop("radius","")
    prepare_print = kwargs.get("prepare_print", False)
    screw_diameter = kwargs.get("screw_diameter", "m4_screw_wood")
    #
    flange_extra = kwargs.get("flange_extra", 0)
    flange_depth = kwargs.get("flange_depth", 0)
    flat_length = kwargs.get("flat_length", 0)
    multi_hole = kwargs.get("multi_hole", 1)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add cylinder    
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"    
        p3["depth"] = 3
        p3["radius"] = radius + 5
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += -(depth - 3)
        p3["pos"] = pos1
        p3["zz"] = "top"
        oobb_base.append_full(thing,**p3)

        p4 = copy.deepcopy(p3)
        p4["type"] = "n"
        p4["radius"] = radius
        p4["depth"] = 100
        pos1 = copy.deepcopy(pos)
        pos1[2] += -depth + 100 + 3
        p4["pos"] = pos1
        #p4["m"] = "#"
        oobb_base.append_full(thing,**p4)
    
    
    #add plate
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_plate"    
        p3["width"] = 1
        hei = 3
        p3["height"] = hei
        p3["depth"] = depth
        #p3["include"] = "hole"
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[1] += radius + (hei-2)/2*15
        p3["pos"] = pos1
        p3["zz"] = "top"
        oobb_base.append_full(thing,**p3)

        p4 = copy.deepcopy(p3)
        p4["type"] = "n"
        p4["shape"] = f"oobb_holes"
        p4["holes"] = "single"
        p4["location"] = []
        p4["location"].append([1,3])
        p4["location"].append([1,2])
        oobb_base.append_full(thing,**p4)

        p5 = copy.deepcopy(p4)
        p5["radius_name"] = "m3"
        p5["location"] = []
        p5["location"].append([1,2.5])
        #p5["m"] = "#"
        oobb_base.append_full(thing,**p5)


        #add extra plate to 1.5 it with no holes
        p4 = copy.deepcopy(p3)
        p4["width"] = 1.5
        p4["include"] = ""
        oobb_base.append_full(thing,**p4)

    #add joiner
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_plate"    
        p3["width"] = 1.5
        hei = 3
        p3["height"] = hei
        p3["depth"] = 3
        
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[1] += 15/2
        pos1[2] += -depth + 3
        p3["pos"] = pos1
        p3["zz"] = "top"
        #oobb_base.append_full(thing,**p3)

    #add hole and nut cutout
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_hole_new"    
        p3["radius_name"] = "m6"
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[1] += radius + 15/2 + 15
        p3["pos"] = pos1        
        oobb_base.append_full(thing,**p3)

        p4 = copy.deepcopy(p3)
        p4["shape"] = f"oobb_nut"
        p4["overhang"] = True
        pos1 = copy.deepcopy(p4["pos"])
        pos1[2] += -depth
        p4["zz"] = "bottom"
        p4["pos"] = pos1
        oobb_base.append_full(thing,**p4)

    #add holes
    if True:
        if multi_hole == 1:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_hole"    
            p3["depth"] = depth
            p3["radius_name"] = screw_diameter
            p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)
        if multi_hole == 3:
            
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_screw_countersunk"    
            p3["depth"] = depth + 50
            p3["radius_name"] = screw_diameter
            p3["zz"] = "top"
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)
            pos1[2] += -depth + 50 
            
            import math          
            shift = 6
            pos11 = copy.deepcopy(pos1)
            angle = 0
            pos11[0] += math.cos(math.radians(angle))*shift
            pos11[1] += math.sin(math.radians(angle))*shift
            pos12 = copy.deepcopy(pos1)
            angle = 120
            pos12[0] += math.cos(math.radians(angle))*shift
            pos12[1] += math.sin(math.radians(angle))*shift
            pos13 = copy.deepcopy(pos1)
            angle = 240
            pos13[0] += math.cos(math.radians(angle))*shift
            pos13[1] += math.sin(math.radians(angle))*shift
            

            poss = []
            poss.append(pos11)
            poss.append(pos12)
            poss.append(pos13)


            p3["pos"] = poss
            oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_socket(thing, **kwargs):
    name = kwargs.get("type", "default")
    if True:    
        depth = kwargs.get("thickness", 4)
        radius = kwargs.get("radius", 10)
        prepare_print = kwargs.get("prepare_print", False)        
        #
        flange_extra = kwargs.get("flange_extra", 0)
        flange_depth = kwargs.get("flange_depth", 0)
        flat_length = kwargs.get("flat_length", 0)
        multi_hole = kwargs.get("multi_hole", 1)
        width = kwargs.get("width", 1)
        height = kwargs.get("height", 1)
        clearance = kwargs.get("clearance", 1)


        pos = kwargs.get("pos", [0, 0, 0])
        #pos = copy.deepcopy(pos)
        #pos[2] += -20

        shift_up = (radius + flange_extra/2 + 1) - 7

        # add plate
        if True:
            p3 = copy.deepcopy(kwargs)
            p3.pop("radius","")
            p3["type"] = "p"
            p3["shape"] = f"oobb_plate"    
            p3["width"] = width
            p3["height"] = height
            p3["depth"] = depth
            #p3["m"] = "#"
            poss = []
            pos1 = copy.deepcopy(pos)   
            poss.append(pos1)
            pos1 = copy.deepcopy(pos)
            pos1[0] += -shift_up - 3
            poss.append(pos1)
            p3["pos"] = poss
            oobb_base.append_full(thing,**p3)      
            
            p4 = copy.deepcopy(p3)
            p4["type"] = "p"
            p4["shape"] = f"oobb_holes"
            p4["both_holes"] = True
            p4["holes"] = "bottom"
            pos1 = copy.deepcopy(pos)
            p4["pos"] = pos1
            oobb_base.append_full(thing,**p4)
            
    #add cutout
    if True:
        
        #slot
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"rounded_rectangle"
        rad = radius + clearance/2
        p3["radius"] = rad
        hei = rad*2
        wid = rad*2 + 15/2
        dep = depth
        size = [wid, hei, dep]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[2] += 0
        pos1[0] += -15/2 - shift_up
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        #hole
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cylinder"
        rad = radius + clearance/2 + flange_extra/2
        p3["radius"] = rad
        p3["depth"] = depth
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth/2
        pos1[0] += -shift_up        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

        


        if prepare_print:
            #put into a rotation object
            components_second = copy.deepcopy(thing["components"])
            return_value_2 = {}
            return_value_2["type"]  = "rotation"
            return_value_2["typetype"]  = "p"
            pos1 = copy.deepcopy(pos)
            pos1[0] += 50
            return_value_2["pos"] = pos1
            return_value_2["rot"] = [180,0,0]
            return_value_2["objects"] = components_second
            
            thing["components"].append(return_value_2)

        
            #add slice # top
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_slice"
            #p3["m"] = "#"
            oobb_base.append_full(thing,**p3)
    
if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)